#!/usr/bin/env python3
"""For every poe2db:<Page> the KB cites, extract that page's table rows from the crawl corpus into data/poe2db/<Page>.tsv,
and write data/poe2db/_refs.csv (page, in_crawl, rows, cited_by). Lets Claude/scripts query the cited data instead of copying it.
Usage: python tools/gen_poe2db_refs.py <corpus_dir> <crawl_date> [repo_root=.]"""
import sys, re, csv, pathlib, urllib.parse, collections

C = pathlib.Path(sys.argv[1]); CRAWL = sys.argv[2]; R = pathlib.Path(sys.argv[3] if len(sys.argv) > 3 else '.')
idx = {}
for l in (C / '_index.tsv').read_text(encoding='utf-8').splitlines()[1:]:
    u, f, *_ = l.split('\t'); idx[urllib.parse.unquote(u)[21:]] = f
cited = collections.defaultdict(set)
for p in (R / 'kb').rglob('*.md'):
    for pg in re.findall(r'(?<![\w/])poe2db:([^\s«,;)/\]]+)', p.read_text(encoding='utf-8')):
        cited[pg.rstrip('.')].add(p.relative_to(R / 'kb').as_posix()[:-3])
out = R / 'data' / 'poe2db'; out.mkdir(parents=True, exist_ok=True)
refs, total = [], 0
for pg in sorted(cited):
    key = urllib.parse.unquote(pg); f = idx.get(key) or idx.get(key.replace('_2C_', ',_').replace('_28', '(').replace('_29', ')'))
    rows = []
    if f:
        rows = [l for l in (C / f).read_text(encoding='utf-8').split('\n')[4:] if ' | ' in l]
        if rows:
            (out / (re.sub(r'[^\w.-]', '_', pg) + '.tsv')).write_text(f'# https://poe2db.tw/us/{pg} · crawl {CRAWL} · CC BY-NC-SA 3.0\n' + '\n'.join(r.replace(' | ', '\t') for r in rows) + '\n', encoding='utf-8')
    total += len(rows)
    refs.append(dict(page=pg, in_crawl=bool(f), rows=len(rows), cited_by=';'.join(sorted(cited[pg]))))
with open(out / '_refs.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=['page', 'in_crawl', 'rows', 'cited_by']); w.writeheader(); w.writerows(refs)
print(f'cited pages={len(refs)} in_crawl={sum(r["in_crawl"] for r in refs)} not_in_crawl={[r["page"] for r in refs if not r["in_crawl"]][:10]} table_rows={total}')
