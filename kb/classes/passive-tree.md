# Passive Tree (attributes, keystones, notables)

Version: game data 0.5.5.9 (researched 2026-11-17). 1.0 overhauls the tree (hundreds of new stats, jewel sockets moved into clusters, 18 → 60 sockets) — treat everything here as pre-1.0 baseline.

## Points
- Claim: One passive point per character level, plus some from quests. Ascendancy points are separate (2 per trial step, max 8). Weapon-set points convert existing points — see [[classes/weapon-set-points]].
- Version: 0.5.x
- Source: [poe2wiki Passive Skill Points](https://www.poe2wiki.net/wiki/Passive_Skill_Points), tier 2; [poe2wiki Passive tree](https://poe2wiki.net/wiki/Passive_tree), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: game data has quest-reward nodes granting passive points ("Passive Point(s)") and a Sorceress node granting 4 — quest point totals → [[campaign/permanent-rewards]].

## Tree size (0.5.5.9, placed nodes on the main tree)
- ~4,480 placed nodes · 984 notables · 33 keystones · 18 jewel sockets.
- Source: [RePoE poe2 passive_skill_trees/Default.json](https://github.com/repoe-fork/poe2), tier 2, retrieved 2026-11-17
- Confidence: single-source (game data); 18 sockets matches the reveal notes' "18 → 60" (claude/reveal-notes-and-price-findings.md).

## Node types
- Claim: Travel nodes, small passives, notables, keystones. Attribute travel nodes give +5 to an attribute you choose and can be switched for gold without refunding nodes behind them.
- Version: 0.5.x
- Source: [poe2wiki Passive skill tree](https://poe2wiki.net/wiki/Passive_skill_tree), [poe2wiki Passive tree](https://poe2wiki.net/wiki/Passive_tree), [poe2wiki Respec](https://poe2wiki.net/wiki/Respec), tier 2, retrieved 2026-11-17
- Confidence: confirmed (+5, switchable); switch cost conflict → kb/04-conflicts.md "Attribute node switch cost"

## Keystones in 0.5.5.9 (33)
Ancestral Bond · Avatar of Fire · Blackflame Covenant · Blood Magic · Bulwark · Chaos Inoculation · Conduit · Crimson Assault · Dance with Death · Eldritch Battery · Elemental Equilibrium · Eternal Youth · Giant's Blood · Glancing Blows · Heartstopper · Hollow Palm Technique · Iron Reflexes · Lord of the Wilds · Mind Over Matter · Necromantic Talisman · Oasis · Pain Attunement · Primal Hunger · Resolute Technique · Resonance · Ritual Cadence · Scarred Faith · Trusted Kinship · Unwavering Stance · Vaal Pact · Whispers of Doom · Wildsurge Incantation · Zealot's Oath
- Source: RePoE Default.json (is_keystone), tier 2, retrieved 2026-11-17. single-source.
- Already documented effects: Ancestral Bond ([[mechanics/totems]]), Bulwark + Unwavering Stance ([[mechanics/dodge-roll]]), Zealot's Oath ([[mechanics/recovery]]), Vaal Pact blocks life flasks ([[mechanics/flasks]]), Resolute Technique can't crit ([[mechanics/crit]]), Elemental Equilibrium, Primal Hunger (game keywords). Others: pull stats from Default.json on demand.
- Notes: keystones and jewel sockets can't be weapon-set-specific.

## Not yet sourced
- Notable list by region; jewel socket radius rules; 1.0 tree (rebuild after launch from new game data).
