---
title: Hits vs Damage over Time
status: done
tracker_topic: "Hits vs damage over time"
tracker_note: "done (0.5.x; recheck 1.0)"
---

Version note: researched 2026-11-17 against 0.5.x sources (live 0.5.5; game data 0.5.5.9). Re-check at 1.0.
Access note: poe2wiki claims come from search-engine snippets (direct fetch blocked).

## Definitions
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
A hit is any damage that isn't damage over time. DoT is damage dealt gradually over a duration rather than at once.

- src: PoE2DB Hit Damage [S109], tier 2; poe2wiki Damage over time [S611], tier 2; RePoE poe2 keywords.json "Hit Damage" [S002], tier 2 game data; retrieved 2026-11-17

## What doesn't apply to DoT
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
DoT is not a hit, so hit-only bonuses and defences skip it. Resistances still reduce DoT; armour and penetration don't.
- src: poe2wiki Damage over Time [S685], tier 2; game keywords "Resistance Penetration" (penetration doesn't affect ailments), tier 2; retrieved 2026-11-17
- notes: also no conversion/gain ([[mechanics/damage-types-conversion]]), and DoT can't crit ([[mechanics/crit]]).


## Damaging ailments
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
The damaging ailments are Bleeding, Ignite and Poison.

- src: poe2db:Keywords, tier 2; game keywords "Damaging Ailments", tier 2; retrieved 2026-11-17

## Ailment damage is locked in at the hit
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
A damaging ailment takes its damage from the hit that applied it (the hit's final damage for ignite; pre-mitigation damage for bleed/poison). After that, your damage modifiers don't apply to it. So bigger hits = bigger ailments.
- src: game keywords "Hit Damage", "Ignite", "Poison", "Bleeding", tier 2; poe2wiki Poisons [S715], tier 2; Mobalytics Ailments [S052], tier 3; retrieved 2026-11-17
- notes: Enemy-side mitigation changes (e.g. Shock) still raise ailment damage taken. Conflict with poe2wiki "Ailment" page resolved by game data — see kb/04-conflicts.md.


## Poison and bleed bypass Energy Shield
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Poison and Bleeding damage skip Energy Shield.

- src: game keywords "Poison", "Bleeding", tier 2; poe2wiki Poisons [S715], tier 2; Mobalytics Ailments [S052], tier 3; retrieved 2026-11-17

## Per-ailment detail
Moved to batch-2 docs: [[mechanics/ailments-overview]] · [[mechanics/ignite]] · [[mechanics/poison]] · [[mechanics/bleed]] · [[mechanics/chill-freeze]] · [[mechanics/shock-electrocute]] · [[mechanics/exposure-penetration]]
