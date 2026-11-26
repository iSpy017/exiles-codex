#!/usr/bin/env python3
"""Build site/kb.json (search app) + site/index.jsonl (one line per entry, for Claude/grep) from the repo KB.
Reads kb/**/*.md (frontmatter + '@' meta lines), sources.yaml, conflicts.yaml, CHANGELOG.md. Nothing here is hand-edited."""
import glob, json, re, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kbschema import parse_meta, slug as kslug, DATE_RE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
SECTION_NAMES = {"mechanics": "Mechanics", "gems": "Gems", "classes": "Classes", "items": "Items", "crafting": "Crafting",
                 "economy": "Economy", "campaign": "Campaign", "endgame": "Endgame", "builds": "Builds", "strategy": "Strategy", "": "Library"}

src = open(os.path.join(ROOT, "sources.yaml"), encoding="utf-8").read()
SRC = {m.group(1): (m.group(2), m.group(3), m.group(4)) for m in
       re.finditer(r'id: (S\d{3}), title: "((?:[^"\\]|\\.)*)", url: "((?:[^"\\]|\\.)*)", tier: "([^"]*)"', src)}

def slug(s):
    s = re.sub(r"[`*_\[\]()]", "", s.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:80]

def expand(md):
    """[S012] -> markdown link; poe2db:Page -> link. Keeps the stored file compact, the app readable."""
    md = re.sub(r"\[(S\d{3})\]", lambda m: f"[{m.group(1)}]({SRC[m.group(1)][1]})" if m.group(1) in SRC else m.group(0), md)
    return re.sub(r"(?<![\w/])poe2db:([^\s«,;)/]+)", lambda m: f"[PoE2DB {m.group(1).replace('_', ' ')}](https://poe2db.tw/us/{m.group(1)})", md)

def strip_md(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s); s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)
    return re.sub(r"[`*]", "", s)

def tiers(text):
    t = [int(x) for x in re.findall(r"tier\s*(\d)", text)] + [int(SRC[s][2]) for s in re.findall(r"\[(S\d{3})\]", text) if s in SRC and SRC[s][2].isdigit()]
    if "poe2db:" in text: t.append(2)
    return min(t) if t else None

out_docs, entries, items, jl, tracker = [], [], [], [], []
for f in sorted(glob.glob(os.path.join(ROOT, "kb", "**", "*.md"), recursive=True)):
    rel = os.path.relpath(f, os.path.join(ROOT, "kb")).replace(os.sep, "/")
    raw = open(f, encoding="utf-8").read()
    fm, body = (raw[4:].split("\n---\n", 1) if raw.startswith("---\n") else ("", raw))
    g = lambda k: (re.search(rf"^{k}: (.*)$", fm, re.M) or [None, ""])[1].strip().strip('"')
    title, status, defaults = g("title") or rel, g("status"), dict(x.split("=", 1) for x in g("defaults").split() if "=" in x)
    section = rel.split("/")[0] if "/" in rel else ""
    md = expand(f"# {title}\n" + body.rstrip() + "\n")
    lines = body.split("\n")
    first = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
    head = lines[:first]
    out_docs.append({"path": rel, "title": title, "section": section, "sectionName": SECTION_NAMES.get(section, section.title()),
                     "md": md, "status": status, "version": defaults.get("v", ""), "dates": sorted(set(DATE_RE.findall("\n".join(head))))})
    tracker.append({"topic": g("tracker_topic") or title, "doc": "kb/" + rel, "status": g("tracker_note") or status})
    intro = strip_md(expand(" ".join(l for l in head if l.strip())))
    if intro:
        entries.append({"doc": rel, "heading": title, "anchor": "", "text": intro[:600], "vol": defaults.get("vol", ""), "conf": "",
                        "version": defaults.get("v", ""), "dates": [], "tier": None, "intro": True})
    idx = [i for i, l in enumerate(lines) if l.startswith("## ")] + [len(lines)]
    for a, b in zip(idx, idx[1:]):
        heading, sec = lines[a][3:].strip(), lines[a + 1:b]
        meta = next((parse_meta(l) for l in sec if l.startswith("@ ")), None) or {}
        txt = [l for l in sec if not l.startswith("@ ")]
        blob = "\n".join(txt)
        text = strip_md(expand(" ".join(l.strip() for l in txt if l.strip())))
        clean = lambda v: "" if v in (None, "?") else v
        dates = sorted(set(DATE_RE.findall(blob)) | ({meta["date"]} if meta.get("date") else set()))
        e = {"doc": rel, "heading": heading, "anchor": slug(heading), "text": text[:1500],
             "vol": clean(meta.get("vol")) or defaults.get("vol", ""), "conf": clean(meta.get("conf")),
             "version": clean(meta.get("v")) or defaults.get("v", ""), "dates": dates, "tier": tiers(blob)}
        entries.append(e)
        jl.append({"id": f"{rel[:-3]}#{kslug(heading)}", "v": e["version"], "vol": e["vol"], "conf": e["conf"], "date": meta.get("date", ""),
                   "tier": e["tier"], "fill": meta.get("fill", ""), "missing": meta.get("missing", ""),
                   "src": sorted(set(re.findall(r"\[(S\d{3})\]", blob)) | set("poe2db:" + p for p in re.findall(r"poe2db:([^\s«,;)/]+)", blob))),
                   "text": text[:240]})
        claim = next((l for l in txt if l.strip() and not l.lstrip().startswith(("- ", "|", "<!--"))), "")
        if rel.startswith("items/uniques-") and rel in ("items/uniques-armour.md", "items/uniques-other.md"):
            cls = re.sub(r"\s*uniques.*$", "", heading, flags=re.I)
            for name in claim.rstrip(".").split(", "):
                if name.strip(): items.append({"name": name.strip(), "kind": "Unique · " + cls, "doc": rel, "anchor": slug(heading)})
        if rel == "gems/lineage-supports.md" and heading.startswith("Full list"):
            for l in txt:
                if "·" in l and not l.startswith("-"):
                    for name in l.split("·"):
                        name = re.sub(r"\(.*$", "", name).strip()
                        if name: items.append({"name": name, "kind": "Lineage support", "doc": rel, "anchor": slug(heading)})
        if rel == "classes/passive-tree.md" and heading.startswith("Keystones"):
            for l in txt:
                if "·" in l and not l.startswith("-"):
                    for name in l.split("·"):
                        if name.strip(): items.append({"name": name.strip(), "kind": "Keystone", "doc": rel, "anchor": slug(heading)})
        if rel == "mechanics/charms.md" and heading.startswith("Charm bases"):
            for l in txt:
                mm = re.match(r"^\|\s*([A-Z][a-z]+)\s*\|\s*\d", l)
                if mm: items.append({"name": mm.group(1) + " Charm", "kind": "Charm base", "doc": rel, "anchor": slug(heading)})

changes = []
cl = open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8").read()
for blk in re.split(r"\n## ", "\n" + cl)[1:]:
    h, _, body = blk.partition("\n"); d = DATE_RE.search(h)
    refs = sorted(set(re.findall(r"\b(mechanics|gems|classes|items|crafting|economy|campaign|endgame|builds|strategy)/([a-z0-9.\-]+)", body)))
    changes.append({"date": d.group(0) if d else "", "title": h.strip(), "bullets": [strip_md(l[2:]) for l in body.split("\n") if l.startswith("- ")],
                    "refs": [f"{a}/{b.rstrip('.')}" for a, b in refs]})
changes.sort(key=lambda c: c["date"], reverse=True)

os.makedirs(OUT, exist_ok=True)
built = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
json.dump({"built": built, "docs": out_docs, "entries": entries, "items": items, "changes": changes, "tracker": tracker},
          open(os.path.join(OUT, "kb.json"), "w", encoding="utf-8"), ensure_ascii=False)
with open(os.path.join(OUT, "index.jsonl"), "w", encoding="utf-8") as fh:
    for r in jl: fh.write(json.dumps(r, ensure_ascii=False) + "\n")
cov = {}
for t in tracker: k = (t["status"].split() or ["?"])[0].strip("(;"); cov[k] = cov.get(k, 0) + 1
json.dump({"built": built, "by_status": cov, "topics": tracker}, open(os.path.join(OUT, "coverage.json"), "w", encoding="utf-8"), ensure_ascii=False)
print(f"docs={len(out_docs)} entries={len(entries)} index={len(jl)} items={len(items)} changes={len(changes)} coverage={cov}")

# coverage.html: static coverage page (replaces the old claude.ai dashboard artifact)
import html as H
rows = sorted(tracker, key=lambda t: (t["doc"].split("/")[1] if t["doc"].count("/") > 1 else "", t["status"], t["doc"]))
col = {"done": "#2e7d32", "partial": "#b26a00", "todo": "#9e9e9e", "needs-1.0-check": "#1565c0", "retired": "#6d4c41"}
by_area = {}
for t in rows:
    a = t["doc"].split("/")[1] if t["doc"].count("/") > 1 else "other"; s = (t["status"].split() or ["?"])[0].strip("(;")
    by_area.setdefault(a, {}).setdefault(s, 0); by_area[a][s] += 1
page = ["<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>KB coverage</title>",
        "<style>body{font:14px system-ui,sans-serif;max-width:1100px;margin:24px auto;padding:0 12px;color:#222}table{border-collapse:collapse;width:100%}td,th{border-bottom:1px solid #ddd;padding:4px 6px;text-align:left;vertical-align:top}.s{font-weight:600}input{padding:6px;width:100%;margin:8px 0}</style>",
        f"<h1>KB coverage</h1><p>Built {built} from <code>kb/</code> frontmatter · " + " · ".join(f"<b style='color:{col.get(k, '#000')}'>{k}</b> {v}" for k, v in sorted(cov.items())) + " · <a href='./'>search app</a></p>",
        "<table><tr><th>Area</th>" + "".join(f"<th>{k}</th>" for k in ("done", "partial", "needs-1.0-check", "todo")) + "</tr>"]
for a, d in sorted(by_area.items()):
    page.append(f"<tr><td>{H.escape(a)}</td>" + "".join(f"<td>{d.get(k, '')}</td>" for k in ("done", "partial", "needs-1.0-check", "todo")) + "</tr>")
page.append("</table><input id=q placeholder='filter topics…' oninput=\"for(const r of document.querySelectorAll('#t tr.r'))r.style.display=r.textContent.toLowerCase().includes(this.value.toLowerCase())?'':'none'\">")
page.append("<table id=t><tr><th>Topic</th><th>Doc</th><th>Status</th></tr>")
for t in rows:
    s = (t["status"].split() or ["?"])[0].strip("(;")
    page.append(f"<tr class=r><td>{H.escape(t['topic'])}</td><td><code>{H.escape(t['doc'])}</code></td><td class=s style='color:{col.get(s, '#000')}'>{H.escape(t['status'])}</td></tr>")
page.append("</table>")
open(os.path.join(OUT, "coverage.html"), "w", encoding="utf-8").write("\n".join(page))
