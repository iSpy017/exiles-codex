"""KB lint. Usage: python lint.py <repo_root> [--all]
Errors fail the build (exit 1). Warnings are the fix queue. Prints counts + first items only (quiet by design)."""
import sys, re, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kbschema import *
try:
    import yaml
except ImportError:
    yaml = None

root = pathlib.Path(sys.argv[1]); show_all = '--all' in sys.argv
err, warn = collections.defaultdict(list), collections.defaultdict(list)
kb = root / 'kb'
docs = {p.relative_to(kb).as_posix()[:-3]: p for p in kb.rglob('*.md')}
names = collections.defaultdict(list)
for d in docs: names[pathlib.PurePosixPath(d).name].append(d)

src_ids = set()
if (root / 'sources.yaml').exists():
    t = (root / 'sources.yaml').read_text(encoding='utf-8')
    src_ids = set(re.findall(r'id: (S\d{3})', t))
    if yaml:
        try: yaml.safe_load(t)
        except Exception as e: err['sources.yaml invalid YAML'].append(str(e)[:120])
else:
    err['missing file'].append('sources.yaml')
if (root / 'conflicts.yaml').exists():
    t = (root / 'conflicts.yaml').read_text(encoding='utf-8'); ids = re.findall(r'id: (C\d{3})', t)
    if len(ids) != len(set(ids)): err['duplicate conflict id'].append('conflicts.yaml')
    if yaml:
        try: yaml.safe_load(t)
        except Exception as e: err['conflicts.yaml invalid YAML'].append(str(e)[:120])

refs = {}
if (root / 'data/poe2db/_refs.csv').exists():
    import csv
    refs = {r['page']: r['in_crawl'] == 'True' for r in csv.DictReader(open(root / 'data/poe2db/_refs.csv', encoding='utf-8'))}
n_entries = 0
for d, p in sorted(docs.items()):
    t = p.read_text(encoding='utf-8')
    if not t.startswith('---\n'): err['no frontmatter'].append(d); continue
    fm, body = t[4:].split('\n---\n', 1)
    st = re.search(r'^status: ([\w.-]+)', fm, re.M)
    if not re.search(r'^title: \S', fm, re.M): err['frontmatter: no title'].append(d)
    if not st or st.group(1) not in STATUS: err['frontmatter: bad status'].append(f'{d}: {st.group(1) if st else None}')
    for sec in re.split(r'\n(?=## )', body):
        h = sec.split('\n', 1)[0]
        meta = next((parse_meta(l) for l in sec.split('\n') if l.startswith('@ ')), None)
        if meta is None: continue
        n_entries += 1; loc = f'{d} «{h[3:43]}»'
        if meta.get('v') not in VERS: warn['entry: version unknown'].append(loc)
        if meta.get('vol') not in VOL: warn['entry: volatility unknown'].append(loc)
        if meta.get('conf') not in CONF: warn['entry: confidence unknown'].append(loc)
        if 'src' in meta.get('missing', ''): warn['entry: no source'].append(loc)
        if meta.get('vol') == 'volatile' and not meta.get('date'): err['volatile entry without date'].append(loc)
        if PRICE_RE.search(sec) and not DATE_RE.search(sec) and 'date' not in meta: err['price without date'].append(loc)
    for s in set(re.findall(r'\[(S\d{3})\]', body)):
        if s not in src_ids: err['unknown source id'].append(f'{d}: {s}')
    if refs:
        for pg in set(re.findall(r'(?<![\w/])poe2db:([^\s«,;)/\]]+)', body)):
            pg = pg.rstrip('.')
            if pg not in refs: warn['poe2db ref not indexed (run tools/gen_poe2db_refs.py)'].append(f'{d}: {pg}')
            elif not refs[pg]: err['poe2db ref not in crawl'].append(f'{d}: {pg}')
    for l in set(LINK_RE.findall(body)):
        l2 = l.strip().removesuffix('.md').removeprefix('kb/')
        if l2 in ('index', 'coverage', 'sources', 'conflicts', 'changelog') or (root / (l2 + '.md')).exists(): continue
        if l2 not in docs and not names.get(pathlib.PurePosixPath(l2).name): err['broken [[link]]'].append(f'{d} → {l2}')
    for m in re.finditer(r'\[INFERRED\]:\s*$', body, re.M): err['[INFERRED]: with empty reason'].append(f'{d}: …{body[max(0, m.start() - 50):m.start()]!r}')
    for m in INF_NOREASON_RE.finditer(body): warn['[INFERRED] tag at line end (check reason nearby)'].append(f'{d}: …{body[max(0, m.start() - 50):m.start()]!r}')

print(f'lint: {len(docs)} docs, {n_entries} entries, {sum(map(len, err.values()))} errors, {sum(map(len, warn.values()))} warnings')
for lab, dd in (('ERROR', err), ('warn', warn)):
    for k, v in sorted(dd.items()):
        print(f'{lab} {k}: {len(v)}')
        for x in (v if show_all else v[:3]): print('   ', x)
sys.exit(1 if err else 0)
