---
title: Accuracy
status: done
tracker_topic: "Accuracy"
tracker_note: "done (0.5.x; recheck 1.0; 1 conflict)"
---

Version note: researched 2026-11-17 against 0.5.x sources (live 0.5.5; game-data export 0.5.5.9). Re-check at 1.0.
Access note: poe2wiki claims come from search-engine snippets (direct fetch blocked).

## Who uses accuracy
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Accuracy only matters for attacks; spells ignore it entirely. It's checked against the defender's evasion.

- src: RePoE poe2 keywords.json "Accuracy" [S002], tier 2 game data; Mobalytics Mechanics [S078], tier 3; poe2db:Keywords, tier 2; retrieved 2026-11-17

## Chance-to-hit formula
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Chance to hit = (Accuracy × 1.25 × 100) ÷ (Accuracy + Evasion × 0.3).
- src: Mobalytics Accuracy [S050], tier 3; same formula in Mobalytics Evasion [S066], tier 3; retrieved 2026-11-17
- conf: single-source (one site, two pages; poe2wiki formula image not readable via snippet — verify)
- notes: the formula itself tops out at 125%; see caps below.


## Hit chance floor and ceiling
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Chance to hit can't go below 5% (evade can't exceed 95%). It normally caps at 100%; Amazon's "Critical Strike" notable lets it exceed 100%, and the formula's hard ceiling is 150%.
- src: poe2wiki Accurate [S599], poe2wiki Evasion Rating [S615], tier 2; Mobalytics Evasion [S066], tier 3; retrieved 2026-11-17
- conf: confirmed for 5%/95%; single-source for 150% ceiling
- notes: [INFERRED] "150%" conflicts with the 1.25× formula ceiling of 125% unless the Amazon node adds its own multiplier — check the node text in ascendancies.json. Amazon overcap reportedly converts into base crit (Reddit, tier 5, unverified).


## Distance penalty (new in PoE2)
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Player attacks lose accuracy with distance from the damage origin to the target: no penalty within 2 m, rising to 90% less accuracy for targets beyond 9 m. Mainly hurts ranged/projectile attacks.
- src: RePoE poe2 keywords.json "Accuracy" [S002], tier 2 game data; poe2wiki Accuracy [S598], tier 2; Mobalytics Accuracy [S050], tier 3; retrieved 2026-11-17
- conf: confirmed for 2 m / 90%; max distance 9 m per game data (wiki said 12 m) — see kb/04-conflicts.md (resolved by game data)
- notes: Deadeye has a node that removes the distance penalty (GGG forum player thread, tier 5 — verify in [[classes/index]]).


## Dexterity → accuracy
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Each point of Dexterity gives +8 Accuracy Rating; Dex gives nothing else unless stated.

- src: RePoE poe2 keywords.json "Dexterity" [S002], tier 2 game data; poe2db:Keywords, tier 2; retrieved 2026-11-17

## Evasion is deterministic (entropy)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Evasion uses an entropy counter rather than pure RNG: each attack adds its hit chance to a running total, guaranteeing a hit after a set number of evades.
- src: poe2wiki Evasion Rating [S615], tier 2; Mobalytics Evasion [S066], tier 3; retrieved 2026-11-17
- notes: full detail belongs in [[mechanics/evasion]] (batch 3).
