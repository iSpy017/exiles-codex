#!/usr/bin/env python3
"""Parse a poe2db crawl dump into compact mod data for the app.

Input:  a dump folder (pages/*.html.gz + manifest.tsv) or zip parts made by
        `poe2db_crawl.py --pack-only`.
Output: data/mods/<page>.json  one file per item-class page that embeds ModsView data
        data/mods/index.json   list of classes with counts + source URL + crawl date

Only extracted fields are written (paraphrase-free structured data with a link back
to the poe2db page). Raw HTML is never copied into the repo.

Usage:
    python tools/build_data.py <dump_dir_or_zip> [more zips...] [--out data/mods]
"""
import argparse, gzip, html, json, re, sys, zipfile
from pathlib import Path

MODSVIEW = re.compile(r"new ModsView\((\{.*?\})\);\s*\}\);", re.S)
TAG = re.compile(r'data-tag="([^"]+)"')
KIND = {"1": "prefix", "2": "suffix", "3": "implicit", "5": "corrupted"}
GROUP_LABEL = {
    "normal": "Base", "corrupted": "Corrupted", "desecrated": "Desecrated", "essence": "Essence",
    "perfect_essence": "Perfect essence", "corruption_upgrade": "Corruption upgrade",
    "breach_otherworldly": "Breach (otherworldly)", "breach_minion": "Breach (minion)",
    "breach_caster": "Breach (caster)", "socketable": "Socketable", "bonded": "Bonded",
}


def text(s):
    s = re.sub(r"<[^>]+>", "", str(s or ""))
    return re.sub(r"\s+", " ", html.unescape(s)).replace("—", "–").strip()


def parse_page(raw, url, fetched):
    m = MODSVIEW.search(raw)
    if not m:
        return None
    try:
        d = json.loads(m.group(1))
    except json.JSONDecodeError:
        return None
    base = d.get("baseitem") or {}
    title = text(base.get("link_name")) or base.get("href") or url.rsplit("/", 1)[-1]
    mods = []
    for group, rows in d.items():
        if not isinstance(rows, list) or not rows or not isinstance(rows[0], dict) or "str" not in rows[0]:
            continue
        for r in rows:
            mods.append({
                "g": group,
                "n": text(r.get("Name")),
                "lvl": int(r["Level"]) if str(r.get("Level", "")).isdigit() else None,
                "k": KIND.get(str(r.get("ModGenerationTypeID")), "other"),
                "fam": (r.get("ModFamilyList") or [""])[0],
                "w": int(r["DropChance"]) if str(r.get("DropChance", "")).isdigit() else None,
                "t": text(r.get("str")),
                "tags": sorted(set(TAG.findall(" ".join(r.get("mod_no") or [])))),
            })
    if not mods:
        return None
    # tier = rank by mod level within (group, kind, family, stat line); higher = better (PoE2 numbering)
    fams, sigs = {}, {}
    for x in mods:
        sig = (x["g"], x["k"], x["fam"], re.sub(r"[+\-]?\d+(\.\d+)?", "#", x["t"]))
        x["s"] = sigs.setdefault(sig, len(sigs))
        fams.setdefault(sig, []).append(x)
    for lst in fams.values():
        lst.sort(key=lambda x: (x["lvl"] or 0))
        for i, x in enumerate(lst, 1):
            x["tier"] = i
            x["tiers"] = len(lst)
    return {"title": title, "url": url, "fetched": fetched, "mods": mods}


def iter_pages(sources):
    """Yield (filename, raw_html) from dump dirs or zip parts."""
    for src in sources:
        p = Path(src)
        if p.is_dir():
            for f in sorted((p / "pages").glob("*.html.gz")):
                yield f.name, gzip.decompress(f.read_bytes()).decode("utf-8", "replace")
        elif p.suffix == ".zip":
            with zipfile.ZipFile(p) as z:
                for n in z.namelist():
                    if n.endswith(".html.gz"):
                        yield n.split("/")[-1], gzip.decompress(z.read(n)).decode("utf-8", "replace")


def load_manifest(sources):
    man = {}
    for src in sources:
        p = Path(src)
        txt = None
        if p.is_dir() and (p / "manifest.tsv").exists():
            txt = (p / "manifest.tsv").read_text(encoding="utf-8")
        elif p.suffix == ".zip":
            with zipfile.ZipFile(p) as z:
                if "manifest.tsv" in z.namelist():
                    txt = z.read("manifest.tsv").decode("utf-8")
        for line in (txt or "").splitlines()[1:]:
            c = line.split("\t")
            if len(c) >= 5 and c[1]:
                man[c[1]] = (c[0], c[4])
    return man


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sources", nargs="+")
    ap.add_argument("--out", default="data/mods")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    man = load_manifest(a.sources)
    index, seen = [], 0
    for fname, raw in iter_pages(a.sources):
        seen += 1
        url, fetched = man.get(fname, ("https://poe2db.tw/us/" + fname.replace(".html.gz", ""), ""))
        page = parse_page(raw, url, fetched)
        if not page:
            continue
        key = re.sub(r"[^A-Za-z0-9_-]+", "_", fname.replace(".html.gz", ""))
        (out / f"{key}.json").write_text(json.dumps(page, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        groups = sorted({m["g"] for m in page["mods"]})
        index.append({"key": key, "title": page["title"], "url": url, "fetched": fetched,
                      "count": len(page["mods"]), "groups": groups})
    index.sort(key=lambda x: x["title"].lower())
    (out / "index.json").write_text(json.dumps({"groupLabels": GROUP_LABEL, "classes": index},
                                               ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"pages scanned={seen} item-class pages={len(index)} mods={sum(i['count'] for i in index)}")


if __name__ == "__main__":
    sys.exit(main())
