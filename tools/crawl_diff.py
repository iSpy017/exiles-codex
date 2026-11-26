#!/usr/bin/env python3
"""1.0 refresh worklist = data drift between two PoE2DB crawls (INF791 §11 step 10: monitor for drift).
Compares the pages the KB cites (text, table rows) and every unique, then lists the KB entries that cite a changed page.
Usage: python tools/crawl_diff.py <old_corpus> <new_corpus> [repo_root=.] > refresh-worklist.md"""
import sys, re, pathlib, hashlib, urllib.parse, collections

A, B = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]); R = pathlib.Path(sys.argv[3] if len(sys.argv) > 3 else '.')
def load_idx(c):
    d = {}
    for l in (c / '_index.tsv').read_text(encoding='utf-8').splitlines()[1:]:
        u, f, *_ = l.split('\t'); d[urllib.parse.unquote(u)[21:]] = f
    return d
ia, ib = load_idx(A), load_idx(B)
def body(c, idx, pg):
    key = urllib.parse.unquote(pg); f = idx.get(key) or idx.get(key.replace('_2C_', ',_').replace('_28', '(').replace('_29', ')'))
    return None if not f else '\n'.join((c / f).read_text(encoding='utf-8').split('\n')[4:])
def digest(t): return hashlib.sha1(t.encode()).hexdigest() if t is not None else None

# entries citing each page
cites = collections.defaultdict(list)
for p in sorted((R / 'kb').rglob('*.md')):
    rel = p.relative_to(R / 'kb').as_posix()[:-3]
    for sec in re.split(r'\n(?=## )', p.read_text(encoding='utf-8')):
        h = sec.split('\n', 1)[0].lstrip('# ').strip(); h = '(intro)' if h.startswith('---') else h
        for pg in set(re.findall(r'(?<![\w/])poe2db:([^\s«,;)/\]]+)', sec)):
            cites[pg.rstrip('.')].append(f'{rel}#{h[:60]}')

changed, removed = [], []
for pg in sorted(cites):
    ta, tb = body(A, ia, pg), body(B, ib, pg)
    if tb is None: removed.append(pg)
    elif digest(ta) != digest(tb):
        ra = {l for l in (ta or '').split('\n') if ' | ' in l}; rb = {l for l in tb.split('\n') if ' | ' in l}
        changed.append((pg, len(rb - ra), len(ra - rb)))
new_pages = sorted(set(ib) - set(ia))
print(f'# 1.0 refresh worklist\n\nOld crawl: {A} · new crawl: {B}\n\nCited pages: {len(cites)} · changed: {len(changed)} · gone: {len(removed)} · new pages in crawl: {len(new_pages)}\n')
print('## KB entries citing a changed page (re-check each, then update v= and date=)')
for pg, add, rem in changed:
    print(f'- poe2db:{pg} (+{add}/−{rem} table rows): ' + '; '.join(cites[pg][:8]) + (' …' if len(cites[pg]) > 8 else ''))
print('\n## Cited pages missing from the new crawl (retired or renamed?)')
for pg in removed: print(f'- poe2db:{pg}: ' + '; '.join(cites[pg][:8]))
print('\n## New pages (candidates for new topics; first 200)')
for pg in new_pages[:200]: print(f'- {pg}')
