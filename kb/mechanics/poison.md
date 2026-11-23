# Poison

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Basics
- Claim: Poison deals chaos damage over time, 2 s default, and bypasses Energy Shield.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Poison", tier 2; [poe2wiki Poisons](https://www.poe2wiki.net/wiki/Poisons), tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Needs an explicit poison chance
- Claim: Damage never creates poison chance — you need a stated source of poison chance. Physical and chaos hit damage then set its strength.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Poison", tier 2; [poe2wiki Poisons](https://www.poe2wiki.net/wiki/Poisons), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Poison damage
- Claim: Base poison = 20% of the hit's pre-mitigation physical + chaos damage, per second. Your damage modifiers don't change it afterwards. Enemy mitigation reducers (e.g. Shock) increase it; hit-only effects (e.g. penetration) don't.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Poison", tier 2; [poe2wiki Ailment](https://poe2wiki.net/wiki/Ailment), tier 2; [Mobalytics Poison](https://mobalytics.gg/poe-2/guides/poison), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Mobalytics' general ailments page lists only "Physical" in the base — its poison page says phys+chaos, matching game data; treated as an omission, not a conflict.

## Stack limit
- Claim: Default limit is 1 active poison per target. All poisons stay with their own timers, but only the highest-damage ones up to your stack limit deal damage. The limit also governs poisons from your minions/other sources. Raised by e.g. the Escalating Poison support and passive notables (named in Mobalytics: Stacking Toxins, Building Toxins).
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Poisons](https://www.poe2wiki.net/wiki/Poisons), tier 2; [Mobalytics Poison](https://mobalytics.gg/poe-2/guides/poison), tier 3; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; retrieved 2026-11-17
- Confidence: confirmed (limit 1 + highest-first); named sources single-source (verify names in skill_gems.json / passive tree)
- Notes: big change from PoE1 where poisons stacked freely.
