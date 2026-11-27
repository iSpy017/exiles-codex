#!/usr/bin/env python3
"""Unique sources / leagues from Path of Building PoE2 (hand-maintained data, tier 2) -> data/unique_sources.csv,
and add a pob_source column to data/uniques.csv where names match.
Usage: python tools/gen_pob_uniques.py <pob_repo_dir> <pob_commit_or_date> [repo_root=.]"""
import sys, re, csv, pathlib

P = pathlib.Path(sys.argv[1]) / 'src' / 'Data' / 'Uniques'; REF = sys.argv[2]; R = pathlib.Path(sys.argv[3] if len(sys.argv) > 3 else '.')
rows = []
for f in sorted(P.glob('*.lua')):
    t = f.read_text(encoding='utf-8', errors='replace')
    for blk in re.findall(r'\[\[\n(.*?)\]\]', t, re.S):
        L = [l.strip() for l in blk.strip().split('\n') if l.strip()]
        if len(L) < 2: continue
        get = lambda k: next((l.split(':', 1)[1].strip() for l in L if l.startswith(k + ':')), '')
        src = re.sub(r'(\w+)\{([^}]*)\}', r'\2', get('Source'))  # unique{Xesht} -> Xesht
        rows.append(dict(name=L[0], base=L[1], file=f.stem, source=src, league=get('League'),
                         variants=sum(l.startswith('Variant:') for l in L), pob=REF))
out = R / 'data'; out.mkdir(exist_ok=True)
with open(out / 'unique_sources.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
by = {r['name']: r for r in rows}
u = list(csv.DictReader(open(out / 'uniques.csv', encoding='utf-8')))
for x in u:
    m = by.get(x['name']); x['pob_source'] = m['source'] if m else ''; x['pob_league'] = m['league'] if m else ''
with open(out / 'uniques.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=list(u[0])); w.writeheader(); w.writerows(u)
print(f"pob uniques={len(rows)} with source={sum(bool(r['source']) for r in rows)} · matched to uniques.csv={sum(1 for x in u if x['name'] in by)}/{len(u)} · with source={sum(bool(x['pob_source']) for x in u)}")
