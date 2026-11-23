# Exposure & Penetration

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Exposure
- Claim: Exposure is a debuff that lowers an enemy's total elemental resistance(s): −20% for 4 s by default (some sources override both). It can push resistance below 0.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Exposure", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Example source with different values: Incinerate applies stacking fire exposure, 6% per stack at max stages ([poe2wiki Burn](https://poe2wiki.net/wiki/Burn), tier 2).

## Exposure vs monster rarity
- Claim: Exposure is weaker on tougher enemies: 15% less effect on Magic, 30% less on Rare, 50% less on Unique.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Exposure", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: So default −20% becomes −10% on bosses — [INFERRED] arithmetic.

## Penetration
- Claim: Penetration makes your hits treat the target's resistance as lower by the stated amount, but by default not below 0%. It only affects hits, so it does nothing for ailment damage (ignite, poison, bleed).
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Resistance Penetration", "Ignite", "Poison", tier 2; [poe2wiki Poisons](https://www.poe2wiki.net/wiki/Poisons), tier 2; [poe2wiki Damage over Time](https://www.poe2wiki.net/wiki/Damage_over_Time), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Practical split
- Claim: [INFERRED] DoT/ailment builds want exposure, curses and other true resistance reduction (these lower the enemy's stat for all damage); pure hit builds can use penetration but it stops at 0% resistance.
- Reason: follows directly from the two definitions above.

## Related: Elemental Weakness
- Claim: Elemental Weakness is a curse lowering elemental resistances by 30% for 20 s unless specified otherwise.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Elemental Weakness", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Curse vs exposure stacking not yet sourced → [[mechanics/resistances]] (batch 3).
