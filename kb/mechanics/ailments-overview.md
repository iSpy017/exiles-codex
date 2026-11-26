---
title: Ailments Overview & Buildup Thresholds
status: done
tracker_topic: "Ailments overview + buildup thresholds"
tracker_note: "done (0.5.5.9; recheck 1.0)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 unless noted (researched 2026-11-17). Re-check at 1.0.
Primary source: [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2) — the in-game keyword definitions extracted from game files (tier 2). Cited below as "game keywords".

## The seven ailments
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Ailments are Bleeding, Ignite, Chill, Freeze, Shock, Electrocute and Poison.
- Damaging: Bleeding, Ignite, Poison. Non-damaging: Chill, Freeze, Shock, Electrocute.
- Elemental: Ignite, Chill, Freeze, Shock, Electrocute. Lightning ailments: Shock, Electrocute.

- src: game keywords "Ailments", "Damaging Ailments", "Non-Damaging Ailments", "Elemental Ailments", "Lightning Ailments", tier 2; poe2db:Keywords, tier 2; poe2wiki Elemental Ailments [S691], tier 2; retrieved 2026-11-17

## Three ways ailments get applied
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
(1) Chance-based from damage: Ignite (via Flammability) and Shock — chance grows with damage dealt relative to the target's ailment threshold. (2) Buildup: Freeze and Electrocute fill a meter; the ailment lands at 100%. (3) Explicit chance only: Bleeding and Poison — damage never creates chance, you need a stated source of bleed/poison chance; damage only sets their magnitude. Chill needs no chance: cold hits chill automatically if big enough.

- src: game keywords "Flammability", "Shock", "Freeze", "Electrocution", "Bleeding", "Poison", "Chill", tier 2; Mobalytics Ailments [S052] (buildup applies at 100%), tier 3 (updated 2026-02-23); retrieved 2026-11-17

## Elemental ailment threshold (players)
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
A player's elemental ailment threshold defaults to half their maximum life. Higher threshold = elemental hits less likely to ailment you and less Freeze/Electrocute buildup taken.
- src: game keywords "Elemental Ailment Threshold", tier 2; Mobalytics Ailments [S052], tier 3; retrieved 2026-11-17
- notes: Mobalytics says threshold can be raised by tree points, an Act 3 permanent-buff quest, items and skills → verify in [[campaign/permanent-rewards]].


## Primed for Freeze / Electrocute
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
An enemy is "Primed" (a state some effects key off) once its Freeze or Electrocute buildup reaches: Normal 40%, Magic 50%, Rare 60%, Unique 70%.
- src: game keywords "Primed for Freeze", "Primed for Electrocution", tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: monster Freeze/Electrocute thresholds themselves (how much buildup = 100%) not found yet.


## "Ailment Application" modifiers
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Modifiers to Ailment Application boost Bleeding, Poison and Shock chance, and Flammability, Freeze and Electrocute buildup.
- src: game keywords "Ailment Application", tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: Chill is not on the list.


## Making other damage types contribute
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
"X damage contributes to [ailment]" adds that type into the ailment's calculation. For chance/buildup ailments this lets the new type inflict it; for Bleed/Poison (magnitude-only) you still need a bleed/poison chance source.

- src: game keywords "Damage Contributing to Ailments", tier 2; poe2wiki Poisons [S715], tier 2; retrieved 2026-11-17

## Magnitude modifiers
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
An ailment's magnitude = the size of its effect. Magnitude modifiers come from whoever applies it and multiply with "effect on target" modifiers.

- src: game keywords "Buff/Debuff Magnitude", tier 2; poe2wiki Ignite [S622], tier 2; retrieved 2026-11-17

## Stacking: strongest wins
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Unless stated otherwise, same-type debuffs don't stack — only the strongest applies. Weaker copies stay on the target and take over when the strongest expires (confirmed for Ignite and Poison).
- src: poe2wiki Poisonous [S714], tier 2; Mobalytics Ignite [S072], tier 3; Mobalytics Poison [S080], tier 3; retrieved 2026-11-17
- notes: Poison has a raisable stack limit — see [[mechanics/poison]].


## Spreading ailments
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Spreading copies an ailment (same source) onto another target; it can keep spreading but never back to a target it already hit, and never to/from the original inflicter.

- src: game keywords "Spreading Ailments", tier 2, retrieved 2026-11-17
- conf: single-source (game data)

## Per-ailment docs
[[mechanics/ignite]] · [[mechanics/chill-freeze]] · [[mechanics/shock-electrocute]] · [[mechanics/poison]] · [[mechanics/bleed]] · [[mechanics/exposure-penetration]]
