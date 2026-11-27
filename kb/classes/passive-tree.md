---
title: Passive Tree (attributes, keystones, notables)
status: needs-1.0-check
tracker_topic: "Passive tree: attributes, keystones, notables"
tracker_note: "needs-1.0-check (0.5.5.9 baseline; tree overhauled in 1.0; jewel sockets move into clusters)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 (researched 2026-11-17). 1.0 overhauls the tree (hundreds of new stats, jewel sockets moved into clusters, 18 → 60 sockets) — treat everything here as pre-1.0 baseline.

## Points
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17 fill=vol
One passive point per character level, plus some from quests. Ascendancy points are separate (2 per trial step, max 8). Weapon-set points convert existing points — see [[classes/weapon-set-points]].
- src: poe2wiki Passive Skill Points [S709], tier 2; poe2wiki Passive tree [S628], tier 2; retrieved 2026-11-17
- notes: game data has quest-reward nodes granting passive points ("Passive Point(s)") and a Sorceress node granting 4 — quest point totals → [[campaign/permanent-rewards]].


## Tree size (0.5.5.9, placed nodes on the main tree)
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-27 fill=v,vol
- ~4,480 placed nodes · 984 notables · 33 keystones · 18 jewel sockets.

- src: RePoE poe2 passive_skill_trees/Default.json [S002], tier 2, retrieved 2026-11-17; Path of Building PoE2 [S739] TreeData 0_5/tree.json (commit 601768b), tier 2, retrieved 2026-11-27 → data/passive_tree_0_5.csv
- conf: confirmed — PoB's 0.5 tree gives the same 984 notables, 33 keystones and 18 jewel sockets on the main tree (PoB counts 4,546 nodes incl. 431 ascendancy nodes; node totals depend on what is counted); 18 sockets matches the reveal notes' "18 → 60" (claude/reveal-notes-and-price-findings.md).

## Node types
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17 fill=vol
Travel nodes, small passives, notables, keystones. Attribute travel nodes give +5 to an attribute you choose and can be switched for gold without refunding nodes behind them.

- src: poe2wiki Passive skill tree [S627], poe2wiki Passive tree [S628], poe2wiki Respec [S633], tier 2, retrieved 2026-11-17
- conf: confirmed (+5, switchable); switch cost conflict → kb/04-conflicts.md "Attribute node switch cost"

## Keystones in 0.5.5.9 (33)
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17 fill=v,vol
Ancestral Bond · Avatar of Fire · Blackflame Covenant · Blood Magic · Bulwark · Chaos Inoculation · Conduit · Crimson Assault · Dance with Death · Eldritch Battery · Elemental Equilibrium · Eternal Youth · Giant's Blood · Glancing Blows · Heartstopper · Hollow Palm Technique · Iron Reflexes · Lord of the Wilds · Mind Over Matter · Necromantic Talisman · Oasis · Pain Attunement · Primal Hunger · Resolute Technique · Resonance · Ritual Cadence · Scarred Faith · Trusted Kinship · Unwavering Stance · Vaal Pact · Whispers of Doom · Wildsurge Incantation · Zealot's Oath
- src: RePoE Default.json (is_keystone), tier 2, retrieved 2026-11-17. single-source.
- Already documented effects: Ancestral Bond ([[mechanics/totems]]), Bulwark + Unwavering Stance ([[mechanics/dodge-roll]]), Zealot's Oath ([[mechanics/recovery]]), Vaal Pact blocks life flasks ([[mechanics/flasks]]), Resolute Technique can't crit ([[mechanics/crit]]), Elemental Equilibrium, Primal Hunger (game keywords). Others: pull stats from Default.json on demand.
- notes: keystones and jewel sockets can't be weapon-set-specific.


## Not yet sourced
- Notable list by region; jewel socket radius rules; 1.0 tree (rebuild after launch from new game data).
