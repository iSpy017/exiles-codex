#!/usr/bin/env python3
"""Exalt-style odds from PoE2DB spawn weights (data/mods/<class>.json).
Chance that one 'add a random mod' click (Exalted Orb, Greater/Perfect Exalted) hits a target mod family (optionally a minimum tier),
plus expected clicks and cost.

  python tools/craftodds.py Amulets --ilvl 82 --target IncreasedLife --min-tier 8 --have FireResistance,ColdResistance --open prefix,suffix --orb greater --price 0.7
  python tools/craftodds.py Amulets --list            # families + tiers on this class

Rules used (KB): mod level <= item level; a family already on the item can't roll again; Greater/Perfect = minimum mod level 35/50,
but a family whose tiers are all below the minimum keeps its highest ilvl-allowed tier ([[crafting/currency-index]]).
Assumption [INFERRED]: one mod is drawn from all eligible prefixes+suffixes in proportion to weight (standard weighted roll)."""
import sys, json, argparse, pathlib, collections

ap = argparse.ArgumentParser()
ap.add_argument('item_class'); ap.add_argument('--ilvl', type=int, default=82)
ap.add_argument('--target'); ap.add_argument('--min-tier', type=int, default=1)
ap.add_argument('--have', default='', help='comma list of families already on the item')
ap.add_argument('--open', default='prefix,suffix', help='which affix kinds still have room')
ap.add_argument('--orb', choices=['normal', 'greater', 'perfect'], default='normal')
ap.add_argument('--price', type=float, help='cost of one orb (any unit)')
ap.add_argument('--undo-price', type=float, default=0, help='cost to undo a miss (e.g. annul), for the retry-loop cost')
ap.add_argument('--slots', type=int, default=1, help='open slots you will fill with this orb (misses stay on the item)')
ap.add_argument('--list', action='store_true'); ap.add_argument('--root', default='.')
a = ap.parse_args()

f = pathlib.Path(a.root) / 'data' / 'mods' / f'{a.item_class}.json'
if not f.exists():
    sys.exit('no such class; options: ' + ', '.join(sorted(p.stem for p in f.parent.glob('*.json'))))
d = json.load(open(f, encoding='utf-8'))
mods = [m for m in d['mods'] if m['g'] == 'normal' and m['k'] in ('prefix', 'suffix') and m['w'] > 0]
if a.list:
    by = collections.defaultdict(list)
    for m in mods: by[(m['k'], m['fam'])].append(m)
    for (k, fam), ms in sorted(by.items()):
        ms.sort(key=lambda m: m['lvl'])
        print(f"{k:6} {fam:40} tiers={len(ms):2} lvls={ms[0]['lvl']}-{ms[-1]['lvl']} w={ms[0]['w']}  e.g. {ms[-1]['t'][:60]}")
    sys.exit()

minlvl = {'normal': 0, 'greater': 35, 'perfect': 50}[a.orb]
have = {x for x in a.have.split(',') if x}; open_ = set(a.open.split(','))
pool = []
fams = collections.defaultdict(list)
for m in mods:
    if m['k'] in open_ and m['fam'] not in have and m['lvl'] <= a.ilvl: fams[m['fam']].append(m)
for fam, ms in fams.items():
    keep = [m for m in ms if m['lvl'] >= minlvl]
    pool += keep if keep else [max(ms, key=lambda m: m['lvl'])]
tot = sum(m['w'] for m in pool)
hit = [m for m in pool if m['fam'] == a.target and m['tier'] >= a.min_tier] if a.target else []
p = sum(m['w'] for m in hit) / tot if tot else 0
print(f"{d['title']} ilvl {a.ilvl} · orb={a.orb} (min mod level {minlvl}) · open={','.join(sorted(open_))} · pool {len(pool)} mods, weight {tot}")
print(f"source: {d['url']} (PoE2DB spawn weights, fetched {d['fetched'][:10]})")
if a.target:
    for m in sorted(hit, key=lambda m: m['tier']): print(f"  T{m['tier']}/{m['tiers']} lvl {m['lvl']} w {m['w']}: {m['t']}")
    print(f"P(hit per click) = {p:.2%}")
    if p:
        print(f"P(>=1 hit filling {a.slots} open slot(s)) ~ {1 - (1 - p) ** a.slots:.2%}  [INFERRED: ignores the pool shrinking as slots fill]")
        if a.price:
            per = a.price + a.undo_price
            print(f"retry loop (undo each miss): {1 / p:.1f} attempts x {per:g} ~ {per / p:.2f} per hit  [undo can hit the wrong mod; treat as a floor]")
