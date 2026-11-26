---
title: Exposure & Penetration
status: done
tracker_topic: "Exposure & penetration"
tracker_note: "done (0.5.5.9; recheck 1.0)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Exposure
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Exposure is a debuff that lowers an enemy's total elemental resistance(s): −20% for 4 s by default (some sources override both). It can push resistance below 0.
- src: game keywords "Exposure", tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: Example source with different values: Incinerate applies stacking fire exposure, 6% per stack at max stages ([poe2wiki Burn](https://poe2wiki.net/wiki/Burn), tier 2).


## Exposure vs monster rarity
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Exposure is weaker on tougher enemies: 15% less effect on Magic, 30% less on Rare, 50% less on Unique.
- src: game keywords "Exposure", tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: So default −20% becomes −10% on bosses — [INFERRED] arithmetic.


## Penetration
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Penetration makes your hits treat the target's resistance as lower by the stated amount, but by default not below 0%. It only affects hits, so it does nothing for ailment damage (ignite, poison, bleed).

- src: game keywords "Resistance Penetration", "Ignite", "Poison", tier 2; poe2wiki Poisons [S715], tier 2; poe2wiki Damage over Time [S685], tier 2; retrieved 2026-11-17

## Practical split
@ v=0.5.5.9 vol=? conf=? date=2026-11-17 fill=v missing=vol,conf,src
[INFERRED] DoT/ailment builds want exposure, curses and other true resistance reduction (these lower the enemy's stat for all damage); pure hit builds can use penetration but it stops at 0% resistance.
- Reason: follows directly from the two definitions above.


## Related: Elemental Weakness
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Elemental Weakness is a curse lowering elemental resistances by 30% for 20 s unless specified otherwise.
- src: game keywords "Elemental Weakness", tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: Curse vs exposure stacking not yet sourced → [[mechanics/resistances]] (batch 3).
