#!/usr/bin/env python3
"""Parse raw KB batch dumps into kb.json for the search app."""
import glob, json, re, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "kb.json")
SKIP = {"kb/02-sources.md"}

docs = {}
for f in sorted(glob.glob(os.path.join(ROOT, "kb", "**", "*.md"), recursive=True)):
    rel = os.path.relpath(f, ROOT).replace(os.sep, "/")
    if rel in SKIP or rel.startswith("kb/tools/"):
        continue
    docs[rel] = open(f, encoding="utf-8").read().rstrip() + "\n"

SECTION_NAMES = {
    "mechanics": "Mechanics", "gems": "Gems", "classes": "Classes", "items": "Items",
    "crafting": "Crafting", "economy": "Economy", "campaign": "Campaign",
    "builds": "Builds", "strategy": "Strategy", "": "Library",
}

def slug(s):
    s = re.sub(r"[`*_\[\]()]", "", s.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:80]

DATE_RE = re.compile(r"20\d\d-\d\d-\d\d")
TIER_RE = re.compile(r"tier\s*(\d)")
FIELD_RE = re.compile(r"^\s*-\s*(Claim|Version|Volatility|Source|Confidence|Notes)\s*(?:\(([^)]*)\))?:\s*(.*)$", re.I)

def strip_md(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)
    s = re.sub(r"[`*]", "", s)
    return s

def parse_fields(lines):
    """Pull Version/Volatility/Confidence/Source from entry lines (incl. inline 'Version: x · Volatility: y')."""
    f = {}
    blob = "\n".join(lines)
    for key in ("Version", "Volatility", "Confidence"):
        m = re.search(r"%s:\s*([^\n·|]+)" % key, blob)
        if m:
            f[key.lower()] = m.group(1).strip().rstrip(".")
    m = re.search(r"Source:\s*(.+)", blob)
    if m:
        f["source"] = m.group(1).strip()
    tiers = [int(t) for t in TIER_RE.findall(blob)]
    if tiers:
        f["tier"] = min(tiers)
    dates = sorted(set(DATE_RE.findall(blob)))
    if dates:
        f["dates"] = dates
    return f

def vol_class(v):
    v = (v or "").lower()
    if "volatile" in v: return "volatile"
    if "retired" in v: return "retired"
    if "may-change" in v or "may change" in v: return "may-change"
    if "stable" in v: return "stable"
    return ""

def conf_class(c):
    c = (c or "").lower()
    if "conflict" in c: return "conflict"
    if c.startswith("[inferred]") or c.startswith("inferred"): return "inferred"
    if "confirmed" in c: return "confirmed"
    if "single" in c: return "single-source"
    if "inferred" in c: return "inferred"
    return ""

out_docs, entries, items = [], [], []
for path, md in sorted(docs.items()):
    rel = path[3:] if path.startswith("kb/") else path
    section = rel.split("/")[0] if "/" in rel else ""
    lines = md.split("\n")
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), rel)
    # doc-level header text (before first ##)
    first_h2 = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
    head_lines = lines[1:first_h2]
    head_fields = parse_fields(head_lines)
    if not head_fields.get("volatility") and re.search(r"\bvolatile\b", "\n".join(head_lines), re.I):
        head_fields["volatility"] = "volatile"
    status = ""
    m = re.search(r"Status:\s*([^.—\n]+)", "\n".join(head_lines))
    if m: status = m.group(1).strip()
    out_docs.append({
        "path": rel, "title": title, "section": section,
        "sectionName": SECTION_NAMES.get(section, section.title()),
        "md": md, "status": status,
        "version": head_fields.get("version", ""),
        "dates": head_fields.get("dates", []),
    })
    # intro pseudo-entry
    intro = strip_md(" ".join(l for l in head_lines if l.strip()))
    if intro:
        entries.append({"doc": rel, "heading": title, "anchor": "", "text": intro[:600],
                        "vol": vol_class(head_fields.get("volatility")), "conf": "",
                        "version": head_fields.get("version", ""), "dates": head_fields.get("dates", []),
                        "tier": head_fields.get("tier"), "intro": True})
    # each ## section
    idx = [i for i, l in enumerate(lines) if l.startswith("## ")] + [len(lines)]
    for a, b in zip(idx, idx[1:]):
        heading = lines[a][3:].strip()
        body = lines[a+1:b]
        f = parse_fields(body)
        if not f.get("volatility"):
            f["volatility"] = head_fields.get("volatility", "")
        if not f.get("version"):
            f["version"] = head_fields.get("version", "")
        if not f.get("dates"):
            f["dates"] = head_fields.get("dates", [])
        text = strip_md(" ".join(l.strip() for l in body if l.strip()))
        anchor = slug(heading)
        entries.append({
            "doc": rel, "heading": heading, "anchor": anchor, "text": text[:1500],
            "vol": vol_class(f.get("volatility")), "conf": conf_class(f.get("confidence")),
            "version": f.get("version", ""), "dates": f.get("dates", []), "tier": f.get("tier"),
        })
        # unique-name lists -> individual searchable items
        if rel.startswith("items/uniques-") and rel != "items/uniques-index.md":
            cls = re.sub(r"\s*uniques.*$", "", heading, flags=re.I)
            for l in body:
                mm = re.match(r"^\s*-\s*Claim:\s*(.+)$", l)
                if mm:
                    for name in mm.group(1).rstrip(".").split(", "):
                        items.append({"name": name.strip(), "kind": "Unique · " + cls, "doc": rel, "anchor": anchor})
        # lineage gems
        if rel == "gems/lineage-supports.md" and heading.startswith("Full list"):
            for l in body:
                if "·" in l and not l.startswith("-"):
                    for name in l.split("·"):
                        name = re.sub(r"\(.*$", "", name).strip()
                        if name: items.append({"name": name, "kind": "Lineage support", "doc": rel, "anchor": anchor})
        # keystones
        if rel == "classes/passive-tree.md" and heading.startswith("Keystones"):
            for l in body:
                if "·" in l and not l.startswith("-"):
                    for name in l.split("·"):
                        if name.strip(): items.append({"name": name.strip(), "kind": "Keystone", "doc": rel, "anchor": anchor})
        # charm table rows
        if rel == "mechanics/charms.md" and heading.startswith("Charm bases"):
            for l in body:
                mm = re.match(r"^\|\s*([A-Z][a-z]+)\s*\|\s*\d", l)
                if mm: items.append({"name": mm.group(1) + " Charm", "kind": "Charm base", "doc": rel, "anchor": anchor})

# changelog
changes = []
cl = docs.get("kb/03-changelog.md", "")
for blk in re.split(r"\n## ", "\n" + cl)[1:]:
    head, _, body = blk.partition("\n")
    d = DATE_RE.search(head)
    bullets = [strip_md(l[2:]) for l in body.split("\n") if l.startswith("- ")]
    refs = sorted(set(re.findall(r"\b(mechanics|gems|classes|items|crafting|economy|campaign|builds|strategy)/([a-z0-9.\-]+)", body)))
    changes.append({"date": d.group(0) if d else "", "title": head.strip(), "bullets": bullets,
                    "refs": [f"{a}/{b.rstrip('.')}" for a, b in refs]})

# needs-1.0-check / todo from tracker
tracker = []
for l in docs.get("kb/01-coverage-tracker.md", "").split("\n"):
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    if len(cells) >= 3 and cells[0] not in ("Topic", "---") and not cells[0].startswith("-") and l.startswith("|"):
        tracker.append({"topic": cells[0], "doc": cells[1], "status": cells[2]})

import datetime
os.makedirs(os.path.dirname(OUT), exist_ok=True)
data = {"built": sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat(), "docs": out_docs, "entries": entries,
        "items": items, "changes": changes, "tracker": tracker}
json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
print(f"docs={len(out_docs)} entries={len(entries)} items={len(items)} changes={len(changes)} tracker={len(tracker)} bytes={os.path.getsize(OUT)}")
