# Stun & Heavy Stun

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2. Second source for most entries: [PoE2DB Keywords](https://poe2db.tw/us/Keywords) (same game text) — counted as one source.

## Two kinds of stun
- Claim: Light stun: any hit can cause it; interrupts for a fraction of a second. Heavy stun: happens when the target's stun bar fills; lasts several seconds; the target can't act and counts as Immobilised; harder to heavy stun again for a short time after.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Stun", "Light Stun", "Heavy Stun", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Light stun chance (vs monsters)
- Claim: Chance scales with damage relative to the target's max life — 100% base at a hit equal to their max life. Under 15% counts as 0%.
- Version: 0.5.5.9
- Source: game keywords "Light Stun", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Stunning players
- Claim: Your stun threshold = your max life. A hit ≥ threshold always stuns you; chance falls linearly for smaller hits; under 10% counts as 0%. Players and minions normally can't be heavy stunned, except while raising a shield, parrying with a buckler, or riding a mount; the bar only empties when not doing those. Heavily stunned players can't block, deflect or evade.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Player Stun Threshold", "Player Heavy Stun", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Blocked hits still apply stun ([[mechanics/block]]). "Unwavering Stance" = can't be light stunned, but no dodge roll or sprint. Stun recovery mods speed recovery.

## Damage-type bonuses to stun
- Claim: Player physical damage and player melee damage each give 50% more light-stun chance and heavy-stun buildup, multiplying together (phys melee ≈ 2.25×). Monster physical gives 100% more and monster melee 33% more, also multiplicative. Cold hits build Freeze, not heavy stun.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Stun", "Heavy Stun", "Light Stun", tier 2; [PoE2DB Keywords](https://poe2db.tw/us/Keywords) (cold), tier 2; retrieved 2026-11-17
- Confidence: single-source (game data); 2.25× is [INFERRED] arithmetic

## Primed for Stun, Crushing Blows, Daze
- Claim: Enemies are Primed for Stun at 40% heavy-stun buildup (Normal), 50% (Magic), 60% (Rare), 70% (Unique). Crushing Blows heavy-stun Primed enemies outright. Daze (chance on hit from some skills) lasts 8 s and makes the enemy take 50% more stun buildup.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Primed for Stun", "Crushing Blows", "Daze", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Monster mods
- Claim: "Stun Resistant" = 250% increased stun threshold; "Stuns" = 100% increased stun buildup; "Increased Stun Threshold" monster mod text says it can't be stunned.
- Version: 0.5.5.9
- Source: game keywords (monster modifier entries), tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Not yet sourced
- Monster stun-threshold values; heavy-stun duration in seconds; post-heavy-stun immunity length; boss stun rules.
