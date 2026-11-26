#!/usr/bin/env python3
"""Generate data/uniques.csv + data/unique_mods.csv from a PoE2DB text corpus (crawl).
Usage: python tools/gen_uniques.py <corpus_dir> <crawl_date> [out_dir=data]
One row per unique / per unique mod. Game-data text, linked back to the PoE2DB page (CC BY-NC-SA 3.0)."""
import sys, re, csv, os, pathlib, urllib.parse

C = pathlib.Path(sys.argv[1]); CRAWL = sys.argv[2]; OUT = pathlib.Path(sys.argv[3] if len(sys.argv) > 3 else 'data')
idx = {}
for l in (C / '_index.tsv').read_text(encoding='utf-8').splitlines()[1:]:
    u, f, *_ = l.split('\t'); idx[urllib.parse.unquote(u)] = f

def read(name):
    f = idx.get('https://poe2db.tw/us/' + name)
    return (C / f).read_text(encoding='utf-8') if f else None

def join(lines):
    s = ' '.join(x.strip() for x in lines if x.strip())
    s = re.sub(r'\(\s*', '(', s); s = re.sub(r'\s*\)', ')', s); s = re.sub(r'\s*—\s*', '–', s)
    s = re.sub(r'\s+([,%:])', r'\1', s); s = re.sub(r'(\d)\s+%', r'\1%', s)
    return re.sub(r'\s+', ' ', s).strip()

# list page: name, base, category. A list line is a unique if its own page's header line is "<name> Unique".
L = (C / 'Unique_item.txt').read_text(encoding='utf-8').split('\n')[4:]
def pname(n): return re.sub(r"['’]", '', n).replace(' ', '_')
def is_unique(n):
    t = read(pname(n))
    if not t: return False
    hs = t.split('\n')[4:7]
    return any(h in (n, n + ' Unique') for h in hs) and 'GenerationType | Unique' in t
cat, rows, seen = None, [], set()
for i, l in enumerate(L):
    m = re.match(r'(.*) Uniques? /(\d+)$', l)
    if m:
        cat = m.group(1); continue
    if l and len(l) < 60 and l not in seen and is_unique(l):
        seen.add(l); rows.append(dict(category=cat, name=l, base=L[i + 1] if i + 1 < len(L) else ''))
# pages that are uniques but not on the list page (e.g. Deferred / unlisted):
# header "X Unique", or header "X" twice followed by a base type seen on the list page plus unique-generation mods
bases = {r['base'] for r in rows if r['base']}
for u, f in idx.items():
    if not u.startswith('https://poe2db.tw/us/') or '/' in u[21:]: continue
    t = (C / f).read_text(encoding='utf-8', errors='replace'); hs = t.split('\n')[4:8]
    nm = next((h[:-7] for h in hs if h.endswith(' Unique') and pname(h[:-7]) == u[21:]), None)
    if not nm and len(hs) >= 3 and hs[0] == hs[1] and hs[2] in bases and 'GenerationType | Unique' in t and pname(hs[0]) == u[21:]:
        nm = hs[0]
    if nm and nm not in seen:
        seen.add(nm); rows.append(dict(category='Unlisted', name=nm, base=''))
uni, mods, missing = [], [], []
for r in rows:
    page = pname(r['name'])
    t = read(page); url = 'https://poe2db.tw/us/' + urllib.parse.quote(page, safe="_,'()-")
    if t is None:
        missing.append(r['name']); continue
    lines = t.split('\n')[4:]
    req = next((int(m.group(1)) for x in lines[:80] for m in [re.match(r'Level (\d+)$', x)] if m), '')
    rel = next((lines[k + 1].replace('Version ', '') for k, x in enumerate(lines) if x == 'Release Version' and k + 1 < len(lines)), '')
    flags = ';'.join(sorted({f for f in ('Drop disabled', 'Corrupted', 'Foulborn') if any(f in x for x in lines)}))
    # mod blocks: display text lines, then Family | ... ; Stats | ...
    try: start = lines.index('BaseType') + 2
    except ValueError: start = 0
    buf, n = [], 0
    k = start
    while k < len(lines):
        x = lines[k]
        if x.startswith('Family |'):
            blk = {}
            while k < len(lines) and ' | ' in lines[k]:
                a, b = lines[k].split(' | ', 1); blk[a.strip()] = b.strip(); k += 1
            n += 1
            mods.append(dict(unique=r['name'], n=n, text=join(buf), family=blk.get('Family', ''), generation=blk.get('GenerationType', ''),
                             stats=blk.get('Stats', ''), tags=blk.get('Craft Tags', ''), page=url))
            buf = []; continue
        buf.append(x); k += 1
    uni.append(dict(category=r['category'], name=r['name'], base=r['base'], req_level=req, release=rel, flags=flags, n_mods=n,
                    page=url, crawl=CRAWL))

OUT.mkdir(parents=True, exist_ok=True)
for fn, data in (('uniques.csv', uni), ('unique_mods.csv', mods)):
    with open(OUT / fn, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(data[0].keys())); w.writeheader(); w.writerows(data)
print(f'uniques={len(uni)} mods={len(mods)} no_page={len(missing)} by_category=' +
      str({c: sum(1 for u in uni if u["category"] == c) for c in dict.fromkeys(u["category"] for u in uni)}) + (f' missing={missing[:8]}' if missing else ''))
