# Block (and Parry)

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## What block does
- Claim: A blocked hit deals no damage — but you still take its stun. You can't block while stunned or frozen. Some boss skills can't be blocked; they glow red with an audio cue on wind-up.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Block", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Since 0.3 block works against all hits (spells too). Source: Sportskeeda 0.3 patch coverage, tier 5 — [INFERRED] still true; verify in 0.3.0 patch notes.

## Passive (chance) vs active (guaranteed) block
- Claim: "Chance to Block" counts only chance-based modifiers. Guaranteed block — e.g. raising your shield — isn't part of block chance.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Chance to Block", tier 2; [Mobalytics Block](https://mobalytics.gg/poe-2/guides/block), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Block chance math and caps
- Claim: Base block comes from the shield (or other source); "increased block chance" multiplies it (e.g. 26% base × 1.5 = 39%). Block rounds to the nearest integer. Default max block is 50%; raisable by rare mods; hard cap 90%. "Overcapped block" = amount above your max.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Block](https://mobalytics.gg/poe-2/guides/block), tier 3; [poe2wiki Block](https://www.poe2wiki.net/wiki/Block) (50% cap, rounding), tier 2; game keywords "Overcapped Block Chance", tier 2; retrieved 2026-11-17
- Confidence: confirmed (50% cap); single-source (90% hard cap, rounding)
- Notes: Mobalytics says Warbringer's Turtle Charm sets max block to 75% but blocked hits still deal 20% — verify in ascendancies.json. Max block was cut from 75% to 50% in 0.3 (Sportskeeda, tier 5).

## Raising a shield = heavy-stun risk
- Claim: Players normally can't be heavy stunned, but they build heavy-stun buildup while raising a shield, parrying with a buckler, or riding a mount. Heavily stunned players can't block, deflect or evade.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Player Heavy Stun", "Heavy Stun", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: → [[mechanics/stun]]

## Parry
- Claim: Parry is a skill from bucklers, targes and dual-wielded swords: block a hit and counter, inflicting "Parried" on the enemy (takes 50% more attack damage for 2 s). Buckler parry blocks damage from enemies within 1 m and projectiles from within 1.5 m.
- Version: 0.5.x
- Volatility: may-change
- Source: game keywords "Parry", tier 2; [poe2wiki Blocked](https://www.poe2wiki.net/wiki/Blocked), [poe2wiki Evasion rating](https://www.poe2wiki.net/wiki/Evasion_rating) (parry skill text), tier 2; retrieved 2026-11-17
- Confidence: confirmed (definition); single-source (numbers)
