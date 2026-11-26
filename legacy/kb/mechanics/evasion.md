# Evasion

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## What evasion does
- Claim: Evasion Rating gives a chance to avoid enemy hits entirely; the chance depends on the attacker's accuracy.
- Version: 0.5.5.9
- Volatility: stable
- Source: game keywords "Evasion", tier 2; [poe2wiki Evasion rating](https://www.poe2wiki.net/wiki/Evasion_rating), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Formula and cap
- Claim: Chance to evade = (1 − (Accuracy × 1.25) ÷ (Accuracy + Evasion × 0.3)) × 100. Capped at 95% (attacker always has ≥5% to hit).
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Evasion](https://mobalytics.gg/poe-2/guides/evasion), tier 3; [poe2wiki Evasion rating](https://www.poe2wiki.net/wiki/Evasion_rating) (95% cap), tier 2; retrieved 2026-11-17
- Confidence: confirmed (cap); single-source (formula)
- Notes: same formula as [[mechanics/accuracy]] seen from the defender's side.

## Entropy (not pure RNG)
- Claim: Evasion uses a deterministic counter: each attack adds its hit chance to a running total, so a hit is guaranteed after a set number of evades. Streaks of bad luck can't happen.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Evasion Rating](https://poe2wiki.net/wiki/Evasion_Rating), tier 2; [Mobalytics Evasion](https://mobalytics.gg/poe-2/guides/evasion), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Weaknesses
- Claim: Heavily stunned players can't evade. Boss attacks with a red flash bypass evasion (deflection still works on them).
- Version: 0.5.5.9 / 0.5.x
- Volatility: may-change
- Source: game keywords "Player Heavy Stun", tier 2; [poe2wiki Deflection](https://www.poe2wiki.net/wiki/Deflection) ("unlike evasion, deflection works against red-flash attacks"), tier 2; retrieved 2026-11-17
- Confidence: single-source each
- Notes: evasion only stops hits, not DoT — [INFERRED] from definition.

## Distance and evasion
- Claim: Accuracy falls with distance (no penalty within 2 m, up to 90% less beyond 9 m), so evasion is effectively stronger against ranged attackers. A unique keystone-style mod gives enemies an accuracy penalty against you by distance and caps your evade chance at 50%.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Accuracy", tier 2; [poe2wiki Evasion rating](https://www.poe2wiki.net/wiki/Evasion_rating) (unique mod text), tier 2; retrieved 2026-11-17
- Confidence: single-source each
- Notes: unique's name not visible in the snippet — find in uniques.json.

## Evasion feeds Deflection
- Most deflection rating comes as "% of Evasion Rating" → [[mechanics/deflection]].
