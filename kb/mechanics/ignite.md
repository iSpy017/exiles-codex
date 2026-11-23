# Ignite & Flammability

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Basics
- Claim: Ignite deals fire damage over time for 4 s by default.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Ignite", tier 2; [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Ignite damage
- Claim: Base ignite = 20% of the hit's fire damage per second. Uses the hit's final damage, but not the target's damage-taken modifiers against that hit. After that, your damage modifiers don't change it. Things that lower the enemy's mitigation (e.g. Shock) do raise ignite damage taken; hit-only effects (e.g. penetration) don't.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Ignite", tier 2; [Mobalytics Ignite](https://mobalytics.gg/poe-2/guides/ignite), tier 3; retrieved 2026-11-17
- Confidence: confirmed (20%); single-source on the modifier rules (game data)
- Notes: Over 4 s, base ignite ≈ 80% of the hit's fire damage — [INFERRED] simple arithmetic, ignoring duration/magnitude mods.

## Chance to ignite comes from Flammability
- Claim: Fire hits apply Flammability, a debuff giving chance to ignite: 1% ignite chance per 5% of the target's ailment threshold dealt as fire. A hit's own Flammability is applied before its ignite roll. Flammability stacks up to 100% chance; each instance lasts 8 s on its own timer. "Increased chance to inflict ailments" increases Flammability magnitude.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Flammability", tier 2; [poe2wiki Ignite](https://poe2wiki.net/wiki/Ignite), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: So 100% ignite chance from one hit needs fire damage ≥ 5× the target's threshold, [INFERRED] from the 1%-per-5% rule.

## Non-hit ignites (Ignited Ground)
- Claim: Effects that ignite without hitting (e.g. Ignited Ground) add Flammability but don't roll; they ignite once total Flammability reaches 50%. Ignited Ground lasts 4 s, radius 2 m by default.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Flammability", "Ignited Ground", tier 2; [poe2wiki Ignite](https://poe2wiki.net/wiki/Ignite), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Stacking
- Claim: Ignites don't stack: all stay on the target, only the highest-damage one deals damage; the next takes over when it expires.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Ignite](https://mobalytics.gg/poe-2/guides/ignite), tier 3; [poe2wiki Poisonous](https://www.poe2wiki.net/wiki/Poisonous) (general debuff rule), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Aggravated Ignite
- Claim: Aggravated ignite deals 100% extra damage and stays aggravated until it expires; each ignite is aggravated independently.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Aggravated Ignite", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Compounding Ignite (skill-specific)
- Claim: On skills with Compounding Ignite, re-igniting a target already ignited by the same skill use removes the old ignite and multiplies the new one's magnitude by the number compounded. Doesn't work when reflected or from ignited Oil Ground.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Compounding Ignite", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
