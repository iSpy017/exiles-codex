"""Step 0 profiling of the frozen legacy KB (INF791 §2.5 EDA, §2.2 cleaning, §2.3 IQR, dedupe).
Usage: python3 -I profile_kb.py <legacy_dir> <out_dir>
Writes: profile.md (human report), docs.csv, entries.csv, dupes.csv, issues.csv
"""
import sys, re, os, json, pathlib, collections, statistics
import pandas as pd

root = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
CONTROL = re.compile(r'kb/0\d-')
FIELDS = ['Claim', 'Version', 'Volatility', 'Source', 'Confidence', 'Notes']
FIELD_RE = re.compile(r'\*{0,2}(Claim|Version|Volatility|Sources?|Confidence|Notes)\*{0,2}:\s*')
DATE_RE = re.compile(r'20\d\d-\d\d-\d\d')
URL_RE = re.compile(r'https?://[^\s)\]>|]+')
TIER_RE = re.compile(r'tier\s*([1-5])', re.I)
LINK_RE = re.compile(r'\[\[([^\]|#]+)')
PRICE_RE = re.compile(r'\b\d[\d.,]*\s*(div|divine|ex|exalt|chaos)s?\b', re.I)
INF_RE = re.compile(r'\[INFERRED\]\s*[:\-—–]?\s*(\S.{0,3})?')

def split_fields(line):
    """Return {field: value} from one line, handling inline 'Version: x | Volatility: y · ...'."""
    res = {}
    ms = list(FIELD_RE.finditer(line))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(line)
        v = line[m.end():end].strip().strip('|·,;').strip()
        k = 'Source' if m.group(1).startswith('Source') else m.group(1)
        res.setdefault(k, v)
    return res

def norm_version(v):
    v = v.lower()
    if not v: return 'MISSING'
    if v.startswith('1.0'): return '1.0'
    for k in ['0.5.5.9', '0.5.5', '0.5.x', '0.5.0', '0.5']:
        if v.startswith(k): return k
    if re.match(r'0\.[0-4]', v): return '<0.5'
    return 'OTHER'

def first_word(v):
    v = v.lower().strip()
    if not v: return 'MISSING'
    if v.startswith('[inferred'): return 'inferred'
    return re.split(r'[\s(;,—–]', v)[0].strip('*')

docs, entries, issues = [], [], []
man = {m['path']: m['est_tokens'] for m in json.load(open(root / 'MANIFEST.json'))['docs']}
all_paths = {}
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name != 'MANIFEST.json':
        rel = p.relative_to(root).as_posix(); all_paths[rel] = p
stems = collections.defaultdict(list)
for rel in all_paths:
    stems[pathlib.PurePosixPath(rel).stem].append(rel)
    stems[re.sub(r'^kb/', '', rel).rsplit('.', 1)[0]].append(rel)

table_rows = collections.defaultdict(set)
for rel, p in all_paths.items():
    text = p.read_text(encoding='utf-8', errors='replace')
    lines = text.splitlines()
    tbl = [l for l in lines if l.lstrip().startswith('|') and not re.match(r'^\s*\|[\s:\-|]+\|\s*$', l)]
    tbl_chars = sum(len(l) for l in tbl)
    # sections by ## heading
    secs, cur = [], {'h': '(preamble)', 'lines': []}
    for l in lines:
        if l.startswith('## '):
            secs.append(cur); cur = {'h': l[3:].strip(), 'lines': []}
        else:
            cur['lines'].append(l)
    secs.append(cur)
    n_entry = 0
    for s in secs:
        f = {}
        for l in s['lines']:
            for k, v in split_fields(l).items():
                f.setdefault(k, v)
        if 'Claim' not in f and 'Version' not in f:
            continue
        n_entry += 1
        body = '\n'.join(s['lines'])
        src = f.get('Source', '')
        e = dict(doc=rel, heading=s['h'][:90],
                 has_claim='Claim' in f, has_version='Version' in f, has_volatility='Volatility' in f,
                 has_source='Source' in f, has_confidence='Confidence' in f, has_notes='Notes' in f,
                 version_raw=f.get('Version', '')[:50], version=norm_version(f.get('Version', '')),
                 volatility=first_word(f.get('Volatility', '')), confidence=first_word(f.get('Confidence', '')),
                 src_url=bool(URL_RE.search(src)) or 'poe2db' in src.lower(), src_tier=(TIER_RE.search(src).group(1) if TIER_RE.search(src) else ''),
                 src_date=bool(DATE_RE.search(src)), chars=len(body),
                 inferred=body.count('[INFERRED]'),
                 price_no_date=bool(PRICE_RE.search(body)) and not DATE_RE.search(body),
                 claim=f.get('Claim', ''))
        entries.append(e)
    # links
    for t in set(LINK_RE.findall(text)):
        t2 = t.strip().removesuffix('.md')
        if not (stems.get(t2) or stems.get(pathlib.PurePosixPath(t2).name)):
            issues.append(dict(doc=rel, kind='broken_link', detail=t2))
    for m in INF_RE.finditer(text):
        if not m.group(1):
            issues.append(dict(doc=rel, kind='inferred_no_reason', detail=text[max(0, m.start() - 60):m.start()].replace('\n', ' ')[-60:]))
    if not CONTROL.search(rel):
        for l in tbl:
            k = re.sub(r'\s+', ' ', l.strip().lower())
            if len(k) > 25: table_rows[k].add(rel)
    docs.append(dict(doc=rel, folder=rel.rsplit('/', 1)[0] if '/' in rel else '.', chars=len(text), est_tokens=man.get(rel, 0),
                     sections=len(secs) - 1, entries=n_entry, table_rows=len(tbl), table_share=round(tbl_chars / max(len(text), 1), 2),
                     inferred=text.count('[INFERRED]'), urls=len(URL_RE.findall(text)), split_part=bool(re.search(r'-\d+\.md$', rel)),
                     control=bool(CONTROL.search(rel))))

D = pd.DataFrame(docs); E = pd.DataFrame(entries); I = pd.DataFrame(issues, columns=['doc', 'kind', 'detail'])
# IQR outliers on doc size (skewed -> IQR, §2.3)
q1, q3 = D.chars.quantile([.25, .75]); iqr = q3 - q1; hi = q3 + 1.5 * iqr
D['size_outlier'] = D.chars > hi
D['table_copy'] = (D.table_share >= 0.5) & ~D.control
# exact duplicate table rows across docs
dup_rows = [(k, sorted(v)) for k, v in table_rows.items() if len(v) > 1]
# near-duplicate claims across docs (TF-IDF cosine)
near = []
if len(E):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    c = E[E.claim.str.len() > 40].reset_index(drop=True)
    fam = lambda d: re.sub(r'-\d+$', '', d.rsplit('.', 1)[0])
    tc = dict(zip(D.doc, D.table_copy))
    X = TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True).fit_transform(c.claim)
    S = cosine_similarity(X)
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            if S[i, j] >= 0.75 and fam(c.doc[i]) != fam(c.doc[j]) and not (tc.get(c.doc[i]) or tc.get(c.doc[j])):
                near.append(dict(sim=round(S[i, j], 2), doc_a=c.doc[i], head_a=c.heading[i], doc_b=c.doc[j], head_b=c.heading[j]))
N = pd.DataFrame(near).sort_values('sim', ascending=False) if near else pd.DataFrame(columns=['sim', 'doc_a', 'head_a', 'doc_b', 'head_b'])

D.to_csv(out / 'docs.csv', index=False); E.drop(columns='claim').to_csv(out / 'entries.csv', index=False)
N.to_csv(out / 'near_dupes.csv', index=False); I.to_csv(out / 'issues.csv', index=False)
pd.DataFrame([dict(row=k[:160], n_docs=len(v), docs=';'.join(v)) for k, v in dup_rows]).to_csv(out / 'dup_table_rows.csv', index=False)

# ---- report
nonctl = D[~D.control]
def vc(s): return ', '.join(f'{k} {v}' for k, v in s.value_counts().items())
R = []
R.append('# KB profile — legacy freeze 2026-11-26\n')
R.append(f'Docs {len(D)} ({D.control.sum()} control) · chars {D.chars.sum():,} · tokens {D.est_tokens.sum():,} (claude.ai count) · entries {len(E)} · table rows {D.table_rows.sum():,}\n')
R.append('## Doc size (IQR, §2.3)')
R.append(f'median {int(D.chars.median()):,} chars · Q1 {int(q1):,} · Q3 {int(q3):,} · outlier > {int(hi):,} → {D.size_outlier.sum()} docs: ' + ', '.join(D[D.size_outlier].sort_values('chars', ascending=False).doc.head(12)))
R.append(f'\nsplit part-docs (-N.md): {D.split_part.sum()} · table-copy docs (≥50% table chars): {D.table_copy.sum()} holding {D[D.table_copy].chars.sum() / D.chars.sum():.0%} of all chars')
R.append('\nBy folder (docs / chars / entries / table rows):')
g = D.groupby('folder').agg(docs=('doc', 'count'), chars=('chars', 'sum'), entries=('entries', 'sum'), rows=('table_rows', 'sum')).sort_values('chars', ascending=False)
R.append('| folder | docs | chars | entries | table rows |\n|---|---|---|---|---|')
for f, r in g.iterrows(): R.append(f'| {f} | {r.docs} | {r.chars:,} | {r.entries} | {r.rows} |')
R.append(f'\nNon-control docs with 0 structured entries: {(nonctl.entries == 0).sum()}')
if len(E):
    R.append('\n## Entry completeness (§2.2 missing values)')
    for f in ['claim', 'version', 'volatility', 'source', 'confidence', 'notes']:
        m = (~E['has_' + f]).sum(); R.append(f'- {f}: missing {m} ({m / len(E):.0%})')
    R.append(f'- source without URL/PoE2DB ref: {(~E.src_url & E.has_source).sum()} · without tier: {(E.src_tier == "").sum()} · without date: {(~E.src_date).sum()}')
    R.append(f'- price numbers with no date in entry: {E.price_no_date.sum()}')
    R.append('\n## Label consistency (§2.2 inconsistent data)')
    R.append('- version (normalised): ' + vc(E.version))
    R.append(f'- distinct raw version strings: {E.version_raw.nunique()}')
    R.append('- volatility: ' + vc(E.volatility))
    R.append('- confidence (first word): ' + vc(E.confidence))
    R.append('- source tier: ' + vc(E.src_tier.replace('', 'none')))
R.append('\n## Integrity')
R.append('- ' + (vc(I.kind) if len(I) else 'no issues'))
R.append(f'- exact duplicate table rows across docs: {len(dup_rows)}')
R.append(f'- near-duplicate claims across docs (TF-IDF cosine ≥0.75): {len(N)}')
if len(N):
    R.append('\nTop near-dupes:')
    for _, r in N.head(8).iterrows(): R.append(f'- {r.sim} · {r.doc_a} «{r.head_a[:40]}» ↔ {r.doc_b} «{r.head_b[:40]}»')
(out / 'profile.md').write_text('\n'.join(R), encoding='utf-8')
print('\n'.join(R))
