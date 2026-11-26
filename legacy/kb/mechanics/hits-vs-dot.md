# Hits vs Damage over Time

Version note: researched 2026-11-17 against 0.5.x sources (live 0.5.5; game data 0.5.5.9). Re-check at 1.0.
Access note: poe2wiki claims come from search-engine snippets (direct fetch blocked).

## Definitions
- Claim: A hit is any damage that isn't damage over time. DoT is damage dealt gradually over a duration rather than at once.
- Version: 0.5.5.9
- Volatility: stable
- Source: [PoE2DB Hit Damage](https://poe2db.tw/Hit_Damage), tier 2; [poe2wiki Damage over time](https://poe2wiki.net/wiki/Damage_over_time), tier 2; [RePoE poe2 keywords.json "Hit Damage"](https://github.com/repoe-fork/poe2), tier 2 game data; retrieved 2026-11-17
- Confidence: confirmed

## What doesn't apply to DoT
- Claim: DoT is not a hit, so hit-only bonuses and defences skip it. Resistances still reduce DoT; armour and penetration don't.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Damage over Time](https://www.poe2wiki.net/wiki/Damage_over_Time), tier 2; game keywords "Resistance Penetration" (penetration doesn't affect ailments), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: also no conversion/gain ([[mechanics/damage-types-conversion]]), and DoT can't crit ([[mechanics/crit]]).

## Damaging ailments
- Claim: The damaging ailments are Bleeding, Ignite and Poison.
- Version: 0.5.5.9
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; game keywords "Damaging Ailments", tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Ailment damage is locked in at the hit
- Claim: A damaging ailment takes its damage from the hit that applied it (the hit's final damage for ignite; pre-mitigation damage for bleed/poison). After that, your damage modifiers don't apply to it. So bigger hits = bigger ailments.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Hit Damage", "Ignite", "Poison", "Bleeding", tier 2; [poe2wiki Poisons](https://www.poe2wiki.net/wiki/Poisons), tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Enemy-side mitigation changes (e.g. Shock) still raise ailment damage taken. Conflict with poe2wiki "Ailment" page resolved by game data — see kb/04-conflicts.md.

## Poison and bleed bypass Energy Shield
- Claim: Poison and Bleeding damage skip Energy Shield.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Poison", "Bleeding", tier 2; [poe2wiki Poisons](https://www.poe2wiki.net/wiki/Poisons), tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Per-ailment detail
Moved to batch-2 docs: [[mechanics/ailments-overview]] · [[mechanics/ignite]] · [[mechanics/poison]] · [[mechanics/bleed]] · [[mechanics/chill-freeze]] · [[mechanics/shock-electrocute]] · [[mechanics/exposure-penetration]]
