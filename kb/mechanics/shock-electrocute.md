# Shock & Electrocute

Version: game data 0.5.5.9 (researched 2026-11-17; threshold note added batch 17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Shock
- Claim: Shocked targets take 20% increased damage. Lasts 4 s on players, 8 s on non-players by default.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Shock", tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Shock chance
- Claim: Lightning hit damage gives shock chance: 1% per 4% of the target's ailment threshold dealt. Rolled per hit (no Flammability-style stacking debuff).
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Shock", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Per-hit roll vs stacking: [INFERRED] from absence of a shock-chance debuff keyword. Shock raises ailment damage taken too ([[mechanics/ignite]], [[mechanics/poison]], [[mechanics/bleed]]).

## Shocked Ground
- Claim: Shocked Ground shocks anyone standing on it; 6 s default.
- Version: 0.5.5.9
- Source: game keywords "Shocked Ground", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Electrocute
- Claim: Electrocute interrupts the target and stops it acting; 5 s default. Buildup-based; only lightning damage from specific skills/effects builds it — ordinary lightning doesn't.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Electrocution", "Electrocute Threshold", tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments) (applies at 100% buildup), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Primed for Electrocution
- Claim: Primed at 40% buildup (Normal), 50% (Magic), 60% (Rare), 70% (Unique).
- Version: 0.5.5.9
- Source: game keywords "Primed for Electrocution", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Monster thresholds (batch 17)
- Claim: Same as freeze: most monsters' ailment threshold ≈ their max life; Unique bosses and some Rares have lower relative thresholds. No numeric table is published. Poison/bleed chance does not use the threshold at all (static chance).
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Chill](https://mobalytics.gg/poe-2/guides/chill), [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; [poe2wiki Contributes](https://poe2wiki.net/wiki/Contributes), tier 2 (snippet); retrieved 2026-11-17
- Confidence: confirmed (2+ sources)
- Notes: poe2wiki Ailment says the exact magnitude formula is unknown. See [[mechanics/chill-freeze]].

## Still not sourced
- Which skills/supports enable electrocute buildup (list from skill_gems.json — next gems pass); shock max-magnitude modifiers; numeric monster thresholds.
