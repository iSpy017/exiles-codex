"""Step 3: convert legacy/ Project docs into the repo KB format (dry run writes to OUT only).
Usage: python3 -I convert.py <legacy_dir> <out_dir>
"""
import sys, re, json, pathlib, collections, hashlib
sys.path.insert(0, str(pathlib.Path(__file__).parent)); sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / 'tools'))
from kbschema import *

LEG = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2])
FIELD_RE = re.compile(r'^\s*[-*] \*{0,2}(Claim|Version|Volatility|Sources?|Confidence|Notes)\*{0,2}:\s?(.*)$')
INLINE_RE = re.compile(r'\s*[|·,]?\s*\*{0,2}(Version|Volatility|Sources?|Confidence)\*{0,2}:\s*')
CONTROL = {'kb/00-index.md', 'kb/00-index-2.md', 'kb/01-coverage-tracker.md', 'kb/02-sources.md',
           'kb/03-changelog.md', 'kb/03-changelog-2.md', 'kb/04-conflicts.md', 'kb/04-conflicts-2.md'}
NO_MERGE = re.compile(r'campaign/(act-\d|boss-data-acts-)')
rep = collections.defaultdict(list); stats = collections.Counter()
MAN = {m['path']: m['created_at'][:10] for m in json.load(open(LEG / 'MANIFEST.json'))['docs']}
LINK_FIX = {'mechanics/ailments': 'mechanics/ailments-overview'}  # verified: target exists, only plausible match

# ---------- source registry
registry = {}  # url -> dict
PH = []
def reg(url, title='', tier='', checked='', use='', reach=''):
    url = url.rstrip('.,;')
    r = registry.get(url)
    if not r:
        r = registry[url] = dict(id=None, title=title, url=url, tier=tier, last_checked=checked, use=use, reachable=reach)
    else:
        r['title'] = r['title'] or title; r['tier'] = r['tier'] or tier
        if checked and checked > (r['last_checked'] or ''): r['last_checked'] = checked
    return r

src_md = (LEG / 'kb/02-sources.md').read_text(encoding='utf-8')
reg_rows = 0
for l in src_md.splitlines():
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) >= 6 and URL_RE.match(c[1] or ''):
        for u in URL_RE.findall(c[1]):
            reg(u, re.sub(r'\*', '', c[0]), c[2], (DATE_RE.findall(c[5]) or [''])[-1], c[3], c[4]); reg_rows += 1
reg_preserved = [l for l in src_md.splitlines() if l.strip() and not (l.startswith('|') and URL_RE.search(l))]

def shorten_sources(text, date):
    """[Title](url) -> [Sxxx] / poe2db:Page ; registers each source. Returns new text."""
    def sub(m):
        title, url = m.group(1), m.group(2)
        p = POE2DB_RE.match(url)
        if p and re.fullmatch(r"[\w%'.:-]+", p.group(1)) and p.group(0) == url.rstrip('.,;'):
            reg(url, title, '2', date)['short'] = True; stats['src_poe2db'] += 1
            return f'poe2db:{p.group(1)}' + ('' if title.lower().replace(' ', '_') in ('poe2db_' + p.group(1).lower(), p.group(1).lower()) else f' «{title}»')
        r = reg(url, title, '', date); stats['src_registry'] += 1
        PH.append(r['url']); return f'{title} \u27e6{len(PH) - 1}\u27e7'  # placeholder resolved after ids assigned
    return MDLINK_RE.sub(sub, text)

# ---------- tracker -> status per doc
status_of = {}
for l in (LEG / 'kb/01-coverage-tracker.md').read_text(encoding='utf-8').splitlines():
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) >= 3 and ('.md' in c[1] or c[1] == '—'):
        st = norm_enum(c[2], STATUS) or ('needs-1.0-check' if c[2].startswith('needs-1.0') else None)
        for d in re.findall(r'[\w./-]+\.md', c[1]):
            d = d if d.startswith('kb/') or '/' not in d else 'kb/' + d
            status_of.setdefault(d, (st or 'partial', c[0], c[2]))
        if c[1] == '—' or not re.findall(r'[\w./-]+\.md', c[1]):
            pass
todo_topics = []
for l in (LEG / 'kb/01-coverage-tracker.md').read_text(encoding='utf-8').splitlines():
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) >= 3 and c[2].startswith('todo'):
        m = re.findall(r'([\w-]+/[\w.-]+\.md)', c[1])
        todo_topics.append((c[0], ('kb/' + m[0]) if m and '<' not in c[1] else None, c[2]))

# ---------- families to merge
docs = sorted(p.relative_to(LEG).as_posix() for p in LEG.rglob('*') if p.is_file() and p.name != 'MANIFEST.json')
fam = {}
for d in docs:
    if not d.startswith('kb/') or d in CONTROL or d.startswith('kb/tools/'): continue
    m = re.match(r'(.*?)-(\d+)\.md$', d)
    base = d
    if m and not NO_MERGE.search(d):
        cand = m.group(1) + '.md'
        if cand in docs or 'uniques-mods-' in d:
            base = cand
    fam.setdefault(base, []).append(d)
for b in fam:
    fam[b].sort(key=lambda d: int(re.search(r'-(\d+)\.md$', d).group(1)) if re.search(r'-(\d+)\.md$', d) and d != b else 0)

# ---------- doc parse/convert
def preamble_defaults(pre):
    d = {}
    for l in pre:
        for m in re.finditer(r'(Version|Volatility|Confidence|Status):\s*(.+?)(?=\.\s|\.$|[|·;]|$)', l):
            d.setdefault(m.group(1), m.group(2).strip())
        for k, rx in (('Volatility', r'(?i)\bvolatility[:\s]+(stable|may-change|volatile)\b'), ('Version', r'(?i)\bversion[:\s]+(1\.0|0\.5\.5\.9|0\.5\.5|0\.5\.x|0\.5)\b'), ('Confidence', r'(?i)\bconfidence[:\s]+(confirmed|single-source)\b')):
            mm = re.search(rx, l)
            if mm: d.setdefault(k, mm.group(1).lower())
        ds = DATE_RE.findall(l)
        if ds: d['_date'] = max(ds + [d.get('_date', '')])
        if 'Source' not in d and l.lstrip().startswith('Source'):
            d['Source'] = l.split(':', 1)[1].strip() if ':' in l else ''
    return d

def split_inline(field, value):
    """'0.5.x | Volatility: may-change | Confidence: x' -> {Version:'0.5.x', Volatility:..., ...}"""
    out = {}; parts = INLINE_RE.split(value)
    out[field] = parts[0].strip().strip('|·').strip()
    for i in range(1, len(parts) - 1, 2):
        k = 'Source' if parts[i].startswith('Source') else parts[i]
        out.setdefault(k, parts[i + 1].strip().strip('|·').strip())
    return out

def convert_section(head, lines, dflt, doc):
    fields, order, cur, pre, tail = {}, [], None, [], []
    for l in lines:
        m = FIELD_RE.match(l)
        if m:
            k = 'Source' if m.group(1).startswith('Source') else m.group(1)
            for kk, vv in split_inline(k, m.group(2)).items():
                if kk in fields: fields[kk] += ' ' + vv
                else: fields[kk] = vv; order.append(kk)
            cur = k
        elif cur:
            fields.setdefault(cur + '+', []).append(l)
        else:
            pre.append(l)
    if not any(k in fields for k in ('Claim', 'Version', 'Source', 'Confidence')):
        return None
    stats['entries'] += 1
    date = max(DATE_RE.findall(' '.join([fields.get('Source', '')] + fields.get('Source+', []))) or [''])
    blob = '\n'.join(lines)
    for k, rx in (('Volatility', r'(?i)\bvolatility[:\s]+(stable|may-change|volatile)\b'), ('Version', r'(?i)\bversion[:\s]+(1\.0|0\.5\.5\.9|0\.5\.5|0\.5\.x)\b')):
        if k not in fields:
            mm = re.search(rx, blob)
            if mm: fields[k + '_stated'] = mm.group(1).lower()
    meta, filled, missing, keep_raw = {}, [], [], {}
    for k, key, fn in [('Version', 'v', norm_version), ('Volatility', 'vol', lambda s: norm_enum(s, VOL)), ('Confidence', 'conf', lambda s: norm_enum(s, CONF))]:
        raw = fields.get(k, '')
        val = fn(raw) if raw else None
        if not raw and fields.get(k + '_stated'): val = fn(fields[k + '_stated']); stats[f'stated_{key}'] += 1
        if raw and val is None: stats[f'unmapped_{key}'] += 1; rep['unmapped'].append((doc, head, k, raw[:60]))
        if raw and (val is None or raw.strip().rstrip('.') != val): keep_raw[key] = raw
        if not raw and not val:
            dv = fn(dflt.get(k, '')) if dflt.get(k) else None
            if not dv and k == 'Version' and dflt.get('_tnote'): dv = norm_version(dflt['_tnote'].split('(', 1)[-1])
            if not dv and k == 'Volatility' and re.search(r'\bvolatile\b', dflt.get('_tnote', '')): dv = 'volatile'
            if dv: val = dv; filled.append(key); stats[f'filled_{key}'] += 1
            else: missing.append(key); stats[f'missing_{key}'] += 1
        meta[key] = val or '?'
    if 'Source' not in fields:
        if dflt.get('Source'): filled.append('src'); stats['filled_src'] += 1
        else: missing.append('src'); stats['missing_src'] += 1
    if not date: date = dflt.get('_date', '')
    if not date and meta.get('vol') == 'volatile' and dflt.get('_written'): date = dflt['_written']; filled.append('date'); stats['filled_date'] += 1
    m = f"@ v={meta['v']} vol={meta['vol']} conf={meta['conf']}" + (f' date={date}' if date else '') + \
        (f" fill={','.join(filled)}" if filled else '') + (f" missing={','.join(missing)}" if missing else '')
    o = [f'## {head}', m]
    o += [l for l in pre if l.strip()] if any(l.strip() for l in pre) else []
    if 'Claim' in fields: o.append(fields['Claim']); o += fields.get('Claim+', [])
    else: stats['no_claim'] += 1
    for k, lab in [('Version', None), ('Volatility', None), ('Confidence', None)]:
        o += fields.get(k + '+', [])
    if 'Source' in fields: o.append('- src: ' + shorten_sources(fields['Source'], date)); o += [shorten_sources(x, date) for x in fields.get('Source+', [])]
    for key, raw in keep_raw.items(): o.append(f'- {key}: {raw}')
    if 'Notes' in fields: o.append('- notes: ' + fields['Notes']); o += fields.get('Notes+', [])
    return o

SPECIAL = {'00-index': 'index', '00-index-2': 'index', '01-coverage-tracker': 'coverage', '02-sources': 'sources', '03-changelog': 'changelog', '03-changelog-2': 'changelog', '04-conflicts': 'conflicts', '04-conflicts-2': 'conflicts'}
def fix_links(l):
    def sub(m):
        t = m.group(1).strip().removesuffix('.md'); k = t.removeprefix('kb/')
        if k in SPECIAL: return '[[' + SPECIAL[k]
        if k in LINK_FIX: return '[[' + LINK_FIX[k]
        if k.startswith('tools/'): return '[[notes/' + k
        for b, parts in fam.items():
            if 'kb/' + k + '.md' in parts and len(parts) > 1: return '[[' + b[3:-3]
        return m.group(0)
    return re.sub(r'\[\[([^\]|#]+)', sub, l)

def convert_doc(paths):
    out_lines, merged_title, dflt_all, n_entries = [], None, {}, 0
    for part_i, p in enumerate(paths):
        text = (LEG / p).read_text(encoding='utf-8'); lines = text.splitlines()
        title = next((l[2:].strip() for l in lines if l.startswith('# ')), pathlib.Path(p).stem)
        secs, cur = [], ('(pre)', [])
        for l in lines:
            if l.startswith('## '): secs.append(cur); cur = (l[3:].strip(), [])
            elif l.startswith('# ') and cur[0] == '(pre)' and not cur[1]: continue
            else: cur[1].append(l)
        secs.append(cur)
        pre = secs[0][1]; dflt = preamble_defaults(pre)
        if part_i == 0: merged_title = title; dflt_all = dflt
        else: out_lines += ['', f'<!-- merged from {p} -->'] + ([f'Part title: {title}'] if title != merged_title else [])
        out_lines += [shorten_sources(l, '') if MDLINK_RE.search(l) and l.lstrip().startswith('Source') else l for l in pre]
        for h, body in secs[1:]:
            st = status_of.get(p) or next((status_of[q] for q in paths if q in status_of), None)
            c = convert_section(h, body, {**dflt_all, **dflt, '_tnote': st[2] if st else '', '_written': MAN.get(p, '')}, p)
            if c: out_lines += c + ['']; n_entries += 1
            else: out_lines += [f'## {h}'] + body; stats['prose_sections'] += 1
    return merged_title, dflt_all, out_lines, n_entries

# ---------- run
OUT.mkdir(parents=True, exist_ok=True)
docrows = []
for base, parts in sorted(fam.items()):
    title, dflt, lines, ne = convert_doc(parts)
    st = next((status_of[p] for p in parts if p in status_of), None)
    fm = ['---', f'title: {title}', f"status: {st[0] if st else 'partial'}" + ('' if st else '  # not in tracker')]
    if st: fm.append(f'tracker_topic: "{st[1]}"'); fm.append(f'tracker_note: "{st[2].replace(chr(34), chr(39))}"')
    dv = {k: f(dflt.get(K, '')) for k, K, f in [('v', 'Version', norm_version), ('vol', 'Volatility', lambda s: norm_enum(s, VOL)), ('conf', 'Confidence', lambda s: norm_enum(s, CONF))] if dflt.get(K)}
    if any(dv.values()): fm.append('defaults: ' + ' '.join(f'{k}={v}' for k, v in dv.items() if v))
    if len(parts) > 1: fm.append('merged_from: [' + ', '.join(pathlib.Path(p).name for p in parts) + ']')
    fm.append('---')
    target = OUT / base
    target.parent.mkdir(parents=True, exist_ok=True)
    docrows.append(dict(target=base, parts=len(parts), entries=ne, status=st[0] if st else 'partial*', lines=lines, fm=fm))

# assign source ids (stable order: registry table first, then first-seen)
for i, r in enumerate(sorted(registry.values(), key=lambda r: (0 if r['use'] else 1, r['url'])), 1):
    r['id'] = f'S{i:03d}'
def resolve(l):
    return re.sub('\u27e6(\\d+)\u27e7', lambda m: f"[{registry[PH[int(m.group(1))]]['id']}]", l)
for d in docrows:
    body = [fix_links(resolve(l)) for l in d['lines']]
    txt = '\n'.join(d['fm'] + body).rstrip() + '\n'
    (OUT / d['target']).write_text(txt, encoding='utf-8'); d['chars'] = len(txt)

# todo stubs (fixes broken links to planned docs)
for topic, path, note in todo_topics:
    if path and not (OUT / path).exists() and path not in fam:
        (OUT / path).parent.mkdir(parents=True, exist_ok=True)
        (OUT / path).write_text(f'---\ntitle: {topic}\nstatus: todo\ntracker_note: "{note}"\n---\n# {topic}\n\nNot researched yet.\n', encoding='utf-8')
        rep['stubs'].append(path)
# planned docs referenced by links but missing from tracker paths
for name in ['kb/strategy/skip-route.md', 'kb/strategy/farm-ranking.md', 'kb/endgame/conquerors-league.md']:
    if not (OUT / name).exists():
        (OUT / name).write_text(f'---\ntitle: {pathlib.Path(name).stem}\nstatus: todo\n---\n# {pathlib.Path(name).stem}\n\nNot researched yet.\n', encoding='utf-8'); rep['stubs'].append(name)

# sources.yaml
def y(s): return '"' + str(s).replace('\\', '\\\\').replace('"', '\\"') + '"'
sy = ['# Source registry. Entries cite [Sxxx]; PoE2DB pages are cited as poe2db:<Page> (crawl date: see S-poe2db).',
      'poe2db_crawl: 2026-11-23', 'tiers: {1: official, 2: data refs, 3: guide sites, 4: economy data, 5: community leads}', 'notes: |'] + \
     ['  ' + l for l in reg_preserved] + ['sources:']
for r in sorted(registry.values(), key=lambda r: r['id']):
    if r.get('short'): continue
    sy.append(f"  - {{id: {r['id']}, title: {y(r['title'])}, url: {y(r['url'])}, tier: {y(r['tier'])}, last_checked: {y(r['last_checked'])}" +
              (f", use: {y(r['use'])}, reachable: {y(r['reachable'])}" if r['use'] else '') + '}')
(OUT / 'sources.yaml').write_text('\n'.join(sy) + '\n', encoding='utf-8')

# conflicts.yaml
cy, cid = ['# Unresolved and resolved source conflicts. Never settled silently: both claims kept.', 'conflicts:'], 0
for f in ['kb/04-conflicts.md', 'kb/04-conflicts-2.md']:
    t = (LEG / f).read_text(encoding='utf-8')
    for blk in re.split(r'\n(?=## )', t)[1:]:
        h, *body = blk.split('\n'); cid += 1
        if h.strip() == '## <topic>': cid -= 1; continue
        st = next((l.split(':', 1)[1].strip() for l in body if l.startswith('- Status:')), '')
        cy.append(f'  - id: C{cid:03d}\n    topic: {y(h[3:].strip())}\n    from: {f}\n    status: {"open" if st.lower().startswith("open") else "resolved" if st.lower().startswith("resolved") else "other"}\n    text: |')
        cy += ['      ' + l for l in body if l.strip()]
(OUT / 'conflicts.yaml').write_text('\n'.join(cy) + '\n', encoding='utf-8')
stats['conflicts'] = cid
# changelog: concatenate history verbatim
(OUT / 'CHANGELOG.md').write_text('# Changelog\n\nFrom 2026-11-27 on: see git log. History below is the pre-migration changelog, verbatim.\n\n' +
                                  (LEG / 'kb/03-changelog.md').read_text(encoding='utf-8') + '\n\n' + (LEG / 'kb/03-changelog-2.md').read_text(encoding='utf-8'), encoding='utf-8')
# passthrough non-kb files byte-exact
PASS = {'claude/': 'notes/', 'kb/tools/': 'notes/tools/'}
for d in docs:
    if d.startswith('kb/') and not d.startswith('kb/tools/'): continue
    tgt = next((v + d[len(k):] for k, v in PASS.items() if d.startswith(k)), 'notes/' + d)
    if d.endswith('.csv'): tgt = 'data/prices/' + pathlib.Path(d).name
    (OUT / tgt).parent.mkdir(parents=True, exist_ok=True); (OUT / tgt).write_bytes((LEG / d).read_bytes()); rep['pass'].append(f'{d} → {tgt}')

# ---------- lossless checks (numbers, urls, INFERRED, words) per family
def toks(s, rx): return collections.Counter(rx.findall(s))
NUM = re.compile(r'(?<![\w.])\d+(?:[.,]\d+)*%?'); WORD = re.compile(r"[A-Za-z][A-Za-z'’-]{2,}")
LABELS = {'Claim', 'Version', 'Volatility', 'Source', 'Sources', 'Confidence', 'Notes'}
ids = {r['id']: r for r in registry.values()}
loss = []
for base, parts in fam.items():
    src = '\n'.join((LEG / p).read_text(encoding='utf-8') for p in parts)
    dst = (OUT / base).read_text(encoding='utf-8'); dst = (re.search(r'^title: (.*)$', dst, re.M).group(1) + '\n' + dst.split('\n---\n', 1)[1]) if dst.startswith('---') else dst
    dst_exp = re.sub(r'\[(S\d{3})\]', lambda m: ids[m.group(1)]['url'], dst)
    dst_exp = re.sub(r'poe2db:([^\s«,;)]+)', lambda m: 'PoE2DB https://poe2db.tw/us/' + m.group(1) + ' ' + m.group(1).replace('_', ' '), dst_exp)
    srcn = MDLINK_RE.sub(lambda m: m.group(1) + ' ' + m.group(2), src)
    srcn = re.sub(r'\[\[[^\]]*\]\]', ' ', srcn); dst_exp = re.sub(r'\[\[[^\]]*\]\]', ' ', dst_exp)
    miss_num = toks(srcn, NUM) - toks(dst_exp, NUM)
    miss_url = {u.rstrip('.,;') for u in URL_RE.findall(src)} - {u.rstrip('.,;') for u in URL_RE.findall(dst_exp)}
    inf = src.count('[INFERRED]') - dst.count('[INFERRED]')
    ws, wd = toks(srcn.lower(), WORD), toks(dst_exp.lower(), WORD)
    for l in LABELS: ws.pop(l.lower(), None)
    miss_w = ws - wd; cov = 1 - sum(miss_w.values()) / max(sum(ws.values()), 1)
    if miss_num or miss_url or inf or cov < 0.995:
        loss.append(dict(doc=base, missing_numbers=dict(miss_num.most_common(6)), missing_urls=list(miss_url)[:3], inferred_delta=inf, word_cov=round(cov, 4), missing_words=dict(miss_w.most_common(6))))

# ---------- report
before = sum(len((LEG / d).read_text(encoding='utf-8')) for d in docs)
after = sum(len(p.read_text(encoding='utf-8')) for p in OUT.rglob('*') if p.is_file() and p.suffix in ('.md', '.yaml', '.csv', '.py', '.filter', '.build'))
R = ['# Conversion dry run — legacy → repo KB', '',
     f'Docs in: {len(docs)} · topic families out: {len(fam)} (merged {sum(1 for p in fam.values() if len(p) > 1)} families from {sum(len(p) for p in fam.values() if len(p) > 1)} part-docs) · todo stubs: {len(rep["stubs"])} · passthrough files: {len(rep["pass"])}',
     f'Entries converted: {stats["entries"]} · prose sections kept as-is: {stats["prose_sections"]} · conflicts → conflicts.yaml: {stats["conflicts"]} · sources in registry: {sum(1 for r in registry.values() if not r.get("short"))} (+{sum(1 for r in registry.values() if r.get("short"))} PoE2DB pages as poe2db:<Page>)',
     f'Chars: {before:,} → {after:,} ({after / before - 1:+.1%}); est tokens {round(before / 2.79):,} → {round(after / 2.79):,}  (control docs become generated, not counted again)', '',
     '## Fill-in of missing metadata (derivable only, from doc header)',
     ' · '.join(f'{k}: {v}' for k, v in sorted(stats.items()) if k.startswith(('filled', 'missing', 'unmapped', 'no_claim'))), '',
     '## Lossless check (numbers, URLs, [INFERRED], words ≥99.5%)',
     f'Families failing: {len(loss)} of {len(fam)}']
for x in loss[:25]: R.append(f"- {x['doc']}: cov {x['word_cov']} · nums {x['missing_numbers']} · urls {x['missing_urls']} · inf Δ{x['inferred_delta']} · words {x['missing_words']}")
R += ['', '## Merged families'] + [f"- {b} ← {len(p)} parts" for b, p in sorted(fam.items()) if len(p) > 1]
R += ['', '## Todo stubs'] + [f'- {s}' for s in rep['stubs']]
R += ['', '## Passthrough (byte-exact)'] + [f'- {s}' for s in rep['pass']]
R += ['', '## Unmapped labels (kept raw)'] + [f'- {d} «{h[:40]}» {k}: {v}' for d, h, k, v in rep['unmapped'][:30]] + ([f'- … {len(rep["unmapped"]) - 30} more'] if len(rep['unmapped']) > 30 else [])
(OUT / '_REPORT.md').write_text('\n'.join(R) + '\n', encoding='utf-8')
json.dump(loss, open(OUT / '_loss.json', 'w'), indent=1)
print('\n'.join(R[:14])); print('loss sample:', loss[:6])
