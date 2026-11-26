# Accuracy

Version note: researched 2026-11-17 against 0.5.x sources (live 0.5.5; game-data export 0.5.5.9). Re-check at 1.0.
Access note: poe2wiki claims come from search-engine snippets (direct fetch blocked).

## Who uses accuracy
- Claim: Accuracy only matters for attacks; spells ignore it entirely. It's checked against the defender's evasion.
- Version: 0.5.5.9
- Volatility: stable
- Source: [RePoE poe2 keywords.json "Accuracy"](https://github.com/repoe-fork/poe2), tier 2 game data; [Mobalytics Mechanics](https://mobalytics.gg/poe-2/guides/mechanics), tier 3; [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Chance-to-hit formula
- Claim: Chance to hit = (Accuracy × 1.25 × 100) ÷ (Accuracy + Evasion × 0.3).
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Accuracy](https://mobalytics.gg/poe-2/guides/accuracy), tier 3; same formula in [Mobalytics Evasion](https://mobalytics.gg/poe-2/guides/evasion), tier 3; retrieved 2026-11-17
- Confidence: single-source (one site, two pages; poe2wiki formula image not readable via snippet — verify)
- Notes: the formula itself tops out at 125%; see caps below.

## Hit chance floor and ceiling
- Claim: Chance to hit can't go below 5% (evade can't exceed 95%). It normally caps at 100%; Amazon's "Critical Strike" notable lets it exceed 100%, and the formula's hard ceiling is 150%.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Accurate](https://poe2wiki.net/wiki/Accurate), [poe2wiki Evasion Rating](https://poe2wiki.net/wiki/Evasion_Rating), tier 2; [Mobalytics Evasion](https://mobalytics.gg/poe-2/guides/evasion), tier 3; retrieved 2026-11-17
- Confidence: confirmed for 5%/95%; single-source for 150% ceiling
- Notes: [INFERRED] "150%" conflicts with the 1.25× formula ceiling of 125% unless the Amazon node adds its own multiplier — check the node text in ascendancies.json. Amazon overcap reportedly converts into base crit (Reddit, tier 5, unverified).

## Distance penalty (new in PoE2)
- Claim: Player attacks lose accuracy with distance from the damage origin to the target: no penalty within 2 m, rising to 90% less accuracy for targets beyond 9 m. Mainly hurts ranged/projectile attacks.
- Version: 0.5.5.9
- Volatility: may-change
- Source: [RePoE poe2 keywords.json "Accuracy"](https://github.com/repoe-fork/poe2), tier 2 game data; [poe2wiki Accuracy](https://poe2wiki.net/wiki/Accuracy), tier 2; [Mobalytics Accuracy](https://mobalytics.gg/poe-2/guides/accuracy), tier 3; retrieved 2026-11-17
- Confidence: confirmed for 2 m / 90%; max distance 9 m per game data (wiki said 12 m) — see kb/04-conflicts.md (resolved by game data)
- Notes: Deadeye has a node that removes the distance penalty (GGG forum player thread, tier 5 — verify in [[classes/index]]).

## Dexterity → accuracy
- Claim: Each point of Dexterity gives +8 Accuracy Rating; Dex gives nothing else unless stated.
- Version: 0.5.5.9
- Volatility: may-change
- Source: [RePoE poe2 keywords.json "Dexterity"](https://github.com/repoe-fork/poe2), tier 2 game data; [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Evasion is deterministic (entropy)
- Claim: Evasion uses an entropy counter rather than pure RNG: each attack adds its hit chance to a running total, guaranteeing a hit after a set number of evades.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Evasion Rating](https://poe2wiki.net/wiki/Evasion_Rating), tier 2; [Mobalytics Evasion](https://mobalytics.gg/poe-2/guides/evasion), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: full detail belongs in [[mechanics/evasion]] (batch 3).
