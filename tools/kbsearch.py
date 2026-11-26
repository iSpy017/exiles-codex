#!/usr/bin/env python3
"""BM25 search over KB entries (the retrieval path Claude uses: search -> read only the matching section).
Usage: python tools/kbsearch.py "query" [-k 5] [--show]   (--show prints the matching sections)
Tokenising follows INF791 §6.1: lowercase, light stemming, NO stopword removal of negations (not/no/cannot)."""
import sys, re, math, pathlib, collections, argparse

STOP = set('a an the of to in on for and or is are be by with as at from that this it its into per how what when which who does do did i my me much can should'.split())  # negations kept on purpose
def stem(w):
    for suf in ('ing', 'ed', 'es', 's'):
        if len(w) > 4 and w.endswith(suf): return w[: -len(suf)]
    return w
def toks(s): return [stem(w) for w in re.findall(r"[a-z0-9][a-z0-9'.%+-]*", s.lower().replace('’', "'")) if w not in STOP]

def load(root):
    secs = []
    for p in sorted((root / 'kb').rglob('*.md')):
        rel = p.relative_to(root / 'kb').as_posix()[:-3]; t = p.read_text(encoding='utf-8')
        title = (re.search(r'^title: (.*)$', t, re.M) or [None, rel])[1]
        parts = re.split(r'\n(?=## )', t.split('\n---\n', 1)[-1])
        for i, s in enumerate(parts):
            h = s.split('\n', 1)[0][3:].strip() if s.startswith('## ') else '(intro)'
            secs.append(dict(id=f'{rel}#{h}', doc=rel, title=title, head=h, text=s,
                             tf=collections.Counter(toks(f'{title} {h} {h} {rel.replace("/", " ").replace("-", " ")} {s}'))))
    return secs

def search(secs, q, k=5, k1=1.4, b=0.6):
    N = len(secs); avg = sum(sum(s['tf'].values()) for s in secs) / N
    df = collections.Counter(w for s in secs for w in s['tf'])
    qt = toks(q); res = []
    for s in secs:
        L = sum(s['tf'].values()); sc = 0.0
        for w in qt:
            f = s['tf'].get(w, 0)
            if f: sc += math.log(1 + (N - df[w] + .5) / (df[w] + .5)) * f * (k1 + 1) / (f + k1 * (1 - b + b * L / avg))
        if sc: res.append((sc, s))
    return [s for _, s in sorted(res, key=lambda x: -x[0])[:k]]

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('q'); ap.add_argument('-k', type=int, default=5); ap.add_argument('--show', action='store_true'); ap.add_argument('--root', default='.')
    a = ap.parse_args(); secs = load(pathlib.Path(a.root))
    for s in search(secs, a.q, a.k):
        print(f"{s['id']}  ({len(s['text'])} chars)")
        if a.show: print(s['text'].strip() + '\n')
