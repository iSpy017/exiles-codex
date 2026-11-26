# Ailments Overview & Buildup Thresholds

Version: game data 0.5.5.9 unless noted (researched 2026-11-17). Re-check at 1.0.
Primary source: [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2) — the in-game keyword definitions extracted from game files (tier 2). Cited below as "game keywords".

## The seven ailments
- Claim: Ailments are Bleeding, Ignite, Chill, Freeze, Shock, Electrocute and Poison.
- Damaging: Bleeding, Ignite, Poison. Non-damaging: Chill, Freeze, Shock, Electrocute.
- Elemental: Ignite, Chill, Freeze, Shock, Electrocute. Lightning ailments: Shock, Electrocute.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Ailments", "Damaging Ailments", "Non-Damaging Ailments", "Elemental Ailments", "Lightning Ailments", tier 2; [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; [poe2wiki Elemental Ailments](https://www.poe2wiki.net/wiki/Elemental_Ailments), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Three ways ailments get applied
- Claim: (1) Chance-based from damage: Ignite (via Flammability) and Shock — chance grows with damage dealt relative to the target's ailment threshold. (2) Buildup: Freeze and Electrocute fill a meter; the ailment lands at 100%. (3) Explicit chance only: Bleeding and Poison — damage never creates chance, you need a stated source of bleed/poison chance; damage only sets their magnitude. Chill needs no chance: cold hits chill automatically if big enough.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Flammability", "Shock", "Freeze", "Electrocution", "Bleeding", "Poison", "Chill", tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments) (buildup applies at 100%), tier 3 (updated 2026-02-23); retrieved 2026-11-17
- Confidence: confirmed

## Elemental ailment threshold (players)
- Claim: A player's elemental ailment threshold defaults to half their maximum life. Higher threshold = elemental hits less likely to ailment you and less Freeze/Electrocute buildup taken.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Elemental Ailment Threshold", tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Mobalytics says threshold can be raised by tree points, an Act 3 permanent-buff quest, items and skills → verify in [[campaign/permanent-rewards]].

## Primed for Freeze / Electrocute
- Claim: An enemy is "Primed" (a state some effects key off) once its Freeze or Electrocute buildup reaches: Normal 40%, Magic 50%, Rare 60%, Unique 70%.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Primed for Freeze", "Primed for Electrocution", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: monster Freeze/Electrocute thresholds themselves (how much buildup = 100%) not found yet.

## "Ailment Application" modifiers
- Claim: Modifiers to Ailment Application boost Bleeding, Poison and Shock chance, and Flammability, Freeze and Electrocute buildup.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Ailment Application", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Chill is not on the list.

## Making other damage types contribute
- Claim: "X damage contributes to [ailment]" adds that type into the ailment's calculation. For chance/buildup ailments this lets the new type inflict it; for Bleed/Poison (magnitude-only) you still need a bleed/poison chance source.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Damage Contributing to Ailments", tier 2; [poe2wiki Poisons](https://www.poe2wiki.net/wiki/Poisons), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Magnitude modifiers
- Claim: An ailment's magnitude = the size of its effect. Magnitude modifiers come from whoever applies it and multiply with "effect on target" modifiers.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Buff/Debuff Magnitude", tier 2; [poe2wiki Ignite](https://poe2wiki.net/wiki/Ignite), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Stacking: strongest wins
- Claim: Unless stated otherwise, same-type debuffs don't stack — only the strongest applies. Weaker copies stay on the target and take over when the strongest expires (confirmed for Ignite and Poison).
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Poisonous](https://www.poe2wiki.net/wiki/Poisonous), tier 2; [Mobalytics Ignite](https://mobalytics.gg/poe-2/guides/ignite), tier 3; [Mobalytics Poison](https://mobalytics.gg/poe-2/guides/poison), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Poison has a raisable stack limit — see [[mechanics/poison]].

## Spreading ailments
- Claim: Spreading copies an ailment (same source) onto another target; it can keep spreading but never back to a target it already hit, and never to/from the original inflicter.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Spreading Ailments", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Per-ailment docs
[[mechanics/ignite]] · [[mechanics/chill-freeze]] · [[mechanics/shock-electrocute]] · [[mechanics/poison]] · [[mechanics/bleed]] · [[mechanics/exposure-penetration]]
