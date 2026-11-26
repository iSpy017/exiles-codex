# Deflection

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Exists? Yes — added in 0.3
- Claim: Deflection is a real PoE2 defence, added in patch 0.3 (The Third Edict).
- Version: 0.3+ (still in 0.5.5.9)
- Volatility: may-change
- Source: game keywords "Deflect", tier 2; [poe2wiki Deflection](https://www.poe2wiki.net/wiki/Deflection) (version history from 0.3.0), tier 2; Sportskeeda deflection guide, tier 5; retrieved 2026-11-17
- Confidence: confirmed

## What it does
- Claim: Deflection Rating gives a chance to deflect a hit; a deflected hit has 40% of its damage prevented. Chance depends on the attacker's accuracy. It's rolled separately from (in addition to) evasion.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Deflect", tier 2; [PoE2DB Deflect](https://poe2db.tw/Deflect), tier 2; [Mobalytics Deflection](https://mobalytics.gg/poe-2/guides/deflection), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: some items add to the 40%, e.g. a rune "Prevent +3% of Damage from Deflected Hits" ([PoE2DB Deflect](https://poe2db.tw/us/Deflect)).

## Works on red-flash boss attacks
- Claim: Unlike evasion, deflection works against boss attacks with a red flash.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Deflection](https://www.poe2wiki.net/wiki/Deflection), tier 2, retrieved 2026-11-17
- Confidence: single-source

## Formula and cap
- Claim: Mobalytics: chance to deflect = 150 × (1 − A ÷ (A + 0.12 × D)), A = attacker accuracy, D = deflection rating, capped at 95%. poe2wiki: no minimum or maximum deflect chance.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Deflection](https://mobalytics.gg/poe-2/guides/deflection), tier 3; [poe2wiki Deflection](https://www.poe2wiki.net/wiki/Deflection), tier 2; retrieved 2026-11-17
- Confidence: conflict on the cap → kb/04-conflicts.md "Deflection cap"

## Where it comes from
- Claim: Mostly converted from evasion: mods like "Gain Deflection Rating equal to X% of Evasion Rating" on Dex gear, uniques and passives. This applies after your evasion scaling, so it rewards heavy evasion investment.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Deflection](https://mobalytics.gg/poe-2/guides/deflection), tier 3; [poe2wiki Deflection](https://www.poe2wiki.net/wiki/Deflection), [PoE2DB Deflect](https://poe2db.tw/Deflect) (example items), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Heavily stunned players can't deflect (game keywords "Player Heavy Stun").
