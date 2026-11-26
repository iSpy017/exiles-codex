---
title: Evasion
status: done
tracker_topic: "Evasion"
tracker_note: "done (0.5.5.9; recheck 1.0)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## What evasion does
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Evasion Rating gives a chance to avoid enemy hits entirely; the chance depends on the attacker's accuracy.

- src: game keywords "Evasion", tier 2; poe2wiki Evasion rating [S693], tier 2; retrieved 2026-11-17

## Formula and cap
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Chance to evade = (1 − (Accuracy × 1.25) ÷ (Accuracy + Evasion × 0.3)) × 100. Capped at 95% (attacker always has ≥5% to hit).
- src: Mobalytics Evasion [S066], tier 3; poe2wiki Evasion rating [S693] (95% cap), tier 2; retrieved 2026-11-17
- conf: confirmed (cap); single-source (formula)
- notes: same formula as [[mechanics/accuracy]] seen from the defender's side.


## Entropy (not pure RNG)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Evasion uses a deterministic counter: each attack adds its hit chance to a running total, so a hit is guaranteed after a set number of evades. Streaks of bad luck can't happen.

- src: poe2wiki Evasion Rating [S615], tier 2; Mobalytics Evasion [S066], tier 3; retrieved 2026-11-17

## Weaknesses
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Heavily stunned players can't evade. Boss attacks with a red flash bypass evasion (deflection still works on them).
- src: game keywords "Player Heavy Stun", tier 2; poe2wiki Deflection [S686] ("unlike evasion, deflection works against red-flash attacks"), tier 2; retrieved 2026-11-17
- v: 0.5.5.9 / 0.5.x
- conf: single-source each
- notes: evasion only stops hits, not DoT — [INFERRED] from definition.


## Distance and evasion
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Accuracy falls with distance (no penalty within 2 m, up to 90% less beyond 9 m), so evasion is effectively stronger against ranged attackers. A unique keystone-style mod gives enemies an accuracy penalty against you by distance and caps your evade chance at 50%.
- src: game keywords "Accuracy", tier 2; poe2wiki Evasion rating [S693] (unique mod text), tier 2; retrieved 2026-11-17
- conf: single-source each
- notes: unique's name not visible in the snippet — find in uniques.json.


## Evasion feeds Deflection
- Most deflection rating comes as "% of Evasion Rating" → [[mechanics/deflection]].
