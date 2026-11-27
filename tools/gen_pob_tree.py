#!/usr/bin/env python3
"""Passive tree nodes from Path of Building PoE2 TreeData -> data/passive_tree_<ver>.csv (one row per node).
Usage: python tools/gen_pob_tree.py <pob_repo_dir> <tree_version e.g. 0_5> <ref> [repo_root=.]"""
import sys, json, csv, pathlib

P, VER, REF = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3]; R = pathlib.Path(sys.argv[4] if len(sys.argv) > 4 else '.')
t = json.load(open(P / 'src' / 'TreeData' / VER / 'tree.json', encoding='utf-8'))
rows = []
for nid, v in t['nodes'].items():
    if v.get('isOnlyImage'): continue
    kind = ('keystone' if v.get('isKeystone') else 'notable' if v.get('isNotable') else 'jewel_socket' if v.get('isJewelSocket')
            else 'attribute' if v.get('isAttribute') else 'ascendancy_start' if v.get('isAscendancyStart') else 'small')
    rows.append(dict(id=nid, name=v.get('name', ''), kind=kind, ascendancy=v.get('ascendancyName', ''),
                     stats=' / '.join(v.get('stats', [])), options=len(v.get('options', []) or []), links=len(v.get('connections', [])),
                     tree=VER, ref=REF))
out = R / 'data' / f'passive_tree_{VER}.csv'
with open(out, 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
main = [r for r in rows if not r['ascendancy']]
c = lambda k, s: sum(1 for r in s if r['kind'] == k)
print(f"nodes={len(rows)} main: notables={c('notable', main)} keystones={c('keystone', main)} jewel_sockets={c('jewel_socket', main)} attribute={c('attribute', main)} · ascendancy nodes={len(rows) - len(main)} ({len({r['ascendancy'] for r in rows if r['ascendancy']})} ascendancies)")
