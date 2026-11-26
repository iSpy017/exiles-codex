#!/usr/bin/env python3
"""Step 5 retrieval test (INF791 §1 metrics, §3.5 split). Same BM25 on both sides, different storage:
  OLD = legacy Project docs, retrieve whole docs, read whole doc (models project_search -> project_read)
  NEW = repo KB, retrieve sections, read only the section (models kbsearch -> read lines)
A hit = a retrieved unit is from a gold doc AND contains the answer string. Gold labels were written before running.
Usage: python migration/retrieval_eval.py <repo_root> <legacy_dir>"""
import sys, re, pathlib, collections, statistics
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / 'tools'))
from kbsearch import load, search, toks

R, LEG = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
CPT = 2.79  # chars per token, claude.ai's own count for this KB (1,163,940 chars / 417,914 tokens)
# (split, question, gold docs (any), answer string that must be in the unit)
Q = [
 ('dev', 'how long does ignite last and how much damage does it do', ['mechanics/ignite'], '20%'),
 ('dev', 'what is the resistance hard cap', ['mechanics/resistances'], '90%'),
 ('dev', 'what character level do I need for a level 10 gem', ['gems/gem-levels'], '36'),
 ('dev', 'does penetration work on damage over time', ['mechanics/exposure-penetration', 'mechanics/hits-vs-dot'], 'penetration'),
 ('dev', 'how many support sockets can a skill gem have', ['gems/socketing-limits'], '5'),
 ('dev', 'how do I get ascendancy points', ['classes/ascendancy-trials'], '8'),
 ('dev', 'how much gold does a respec cost', ['classes/respec'], 'gold'),
 ('dev', 'is gold tradeable between players', ['economy/gold'], "can't be traded"),
 ('dev', 'what waystone tier is area level 80', ['endgame/waystones', 'items/item-level'], '80'),
 ('dev', 'late league uncut spirit gem level 8 price spike', ['strategy/league-lifecycle-pricing'], 'L8'),
 ('test', 'evasion chance cap', ['mechanics/evasion'], '95%'),
 ('test', 'maximum block chance', ['mechanics/block'], '90%'),
 ('test', 'how does the currency exchange order book work', ['economy/currency-exchange'], 'order'),
 ('test', 'what does a gemcutter prism do', ['gems/quality', 'items/quality', 'crafting/currency-index'], '5%'),
 ('test', 'armour damage reduction formula', ['mechanics/armour'], 'armour'),
 ('test', 'Xesht breachstone boss', ['endgame/breach'], 'Xesht'),
 ('test', 'ritual reroll and defer rewards', ['endgame/ritual'], 'defer'),
 ('test', 'perfect essence removes a mod and adds one', ['crafting/essences', 'crafting/essence-table-high'], 'Perfect'),
 ('test', 'omens that change exalted orb outcome', ['crafting/omens'], 'Exalt'),
 ('test', 'desecration well of souls choose one of three mods', ['crafting/desecration'], 'Well of Souls'),
 ('test', 'expedition logbooks', ['endgame/expedition'], 'Logbook'),
 ('test', 'storm shaman tornado flame wall', ['builds/storm-shaman', 'builds/storm-shaman-levelling', 'builds/storm-shaman-pivot'], 'Tornado'),
 ('test', 'the 5 div T15 test before investing', ['strategy/league-start-framework', 'builds/budget-tiers'], 'T15'),
 ('test', 'unique monster life multiplier boss', ['mechanics/monster-life'], '29'),
 ('test', 'freeze buildup threshold on monsters', ['mechanics/chill-freeze', 'mechanics/ailments-overview'], 'threshold'),
 ('test', 'life leech cap and recoup duration', ['mechanics/recovery'], 'recoup'),
 ('test', 'how many charm slots', ['mechanics/charms'], 'slot'),
 ('test', 'how many zones and bosses in act 5 and 6', ['campaign/act-5', 'campaign/act-6', 'strategy/official-1.0-reveal'], '24'),
 ('test', 'thunderstorm drench enemy level cap', ['gems/elemental-caster-gems'], 'Drench'),
 ('test', 'when does crit chance leave the passive tree in 1.0', ['mechanics/crit', 'strategy/dev-statements-1.0-balance'], 'crit'),
]

# OLD units: legacy docs (control docs excluded, like the Project search would surface them anyway)
old = []
for p in sorted((LEG / 'kb').rglob('*.md')):
    rel = p.relative_to(LEG / 'kb').as_posix()[:-3]
    if rel.startswith(('0', 'tools/')): continue
    t = p.read_text(encoding='utf-8')
    old.append(dict(id=rel, doc=re.sub(r'-\d+$', '', rel) if 'uniques-mods' in rel or (LEG / 'kb' / (re.sub(r'-\d+$', '', rel) + '.md')).exists() else rel,
                    title=rel, head='', text=t, tf=collections.Counter(toks(rel.replace('/', ' ').replace('-', ' ') + ' ' + t))))
new = load(R)

def run(units, q, gold, ans, k):
    hits = search(units, q, k); toks_read, found, rel = 0, None, 0
    for i, u in enumerate(hits):
        good = u['doc'] in gold and ans.lower() in u['text'].lower()
        rel += good
        if found is None: toks_read += len(u['text']) / CPT
        if good and found is None: found = i + 1
    return found, toks_read, rel, len(hits)

out = ['# Retrieval test — old Project docs vs repo KB', '', 'Same BM25 ranking both sides; OLD reads whole docs, NEW reads one section. Hit = unit from a gold doc containing the answer string.',
       'OLD models project_search → project_read (approximation: the real Project search is a RAG snippet index, not BM25).', '']
for split in ('dev', 'test'):
    qs = [x for x in Q if x[0] == split]
    out.append(f'## {split} ({len(qs)} questions)')
    out.append('| store | recall@1 | recall@3 | recall@5 | precision@5 | F1@5 | MRR | median tokens read to answer | mean tokens |')
    out.append('|---|---|---|---|---|---|---|---|---|')
    for name, units in (('OLD docs', old), ('NEW sections', new)):
        f1s, f3s, f5s, prec, mrr, tk = [], [], [], [], [], []
        for _, q, gold, ans in qs:
            found, t, rel, n = run(units, q, gold, ans, 5)
            f1s.append(found == 1); f3s.append(bool(found and found <= 3)); f5s.append(bool(found)); prec.append(rel / 5); mrr.append(1 / found if found else 0); tk.append(t)
        r5, p5 = sum(f5s) / len(qs), statistics.mean(prec)
        out.append(f'| {name} | {sum(f1s) / len(qs):.2f} | {sum(f3s) / len(qs):.2f} | {r5:.2f} | {p5:.2f} | {2 * r5 * p5 / (r5 + p5) if r5 + p5 else 0:.2f} | {statistics.mean(mrr):.2f} | {statistics.median(tk):,.0f} | {statistics.mean(tk):,.0f} |')
    out.append('')
out.append('## Per test question (rank of first hit, tokens read: OLD → NEW)')
for split, q, gold, ans in Q:
    if split != 'test': continue
    a, b = run(old, q, gold, ans, 5), run(new, q, gold, ans, 5)
    out.append(f'- {q}: {a[0] or "miss"} / {a[1]:,.0f} → {b[0] or "miss"} / {b[1]:,.0f}')
print('\n'.join(out))
