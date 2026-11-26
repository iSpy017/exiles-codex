#!/usr/bin/env python3
"""Paraphrase check: flag 9-word runs a KB doc shares with the PoE2DB crawl text (copied wording).
Usage: python tools/copycheck.py <corpus_dir> [kb paths...]   (default: all kb/**/*.md)
Ignores table rows (game stat data) and quoted text. Prints doc: phrase, one line per merged run."""
import sys, re, pathlib
C = pathlib.Path(sys.argv[1]); N = 9
files = [pathlib.Path(p) for p in sys.argv[2:]] or sorted(pathlib.Path('kb').rglob('*.md'))
def words(t): return re.findall(r"[a-z0-9%']+", t.lower())
corp = set()
for p in C.glob('*.txt'):
    w = words('\n'.join(l for l in p.read_text(encoding='utf-8', errors='replace').split('\n')[4:] if ' | ' not in l))
    corp.update(' '.join(w[i:i + N]) for i in range(len(w) - N + 1))
total = 0
for f in files:
    t = f.read_text(encoding='utf-8')
    t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith(('|', '- src:', '@ ', 'title:', 'tracker_')))
    t = re.sub(r'"[^"\n]{0,200}"|“[^”\n]{0,200}”|https?://\S+|poe2db:\S+', ' ', t)
    w = words(t); hit = [i for i in range(len(w) - N + 1) if ' '.join(w[i:i + N]) in corp]
    runs, cur = [], None
    for i in hit:
        if cur and i <= cur[1] + 1: cur[1] = i
        else: cur = [i, i]; runs.append(cur)
    for a, b in runs:
        total += 1; print(f"{f}: {' '.join(w[a:b + N])}")
print(f'copycheck: {total} copied run(s)', file=sys.stderr)
