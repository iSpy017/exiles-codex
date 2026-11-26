---
title: Deflection
status: done
tracker_topic: "Deflection (exists, since 0.3)"
tracker_note: "done (0.5.x; cap conflict open)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Exists? Yes — added in 0.3
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Deflection is a real PoE2 defence, added in patch 0.3 (The Third Edict).

- src: game keywords "Deflect", tier 2; poe2wiki Deflection [S686] (version history from 0.3.0), tier 2; Sportskeeda deflection guide, tier 5; retrieved 2026-11-17
- v: 0.3+ (still in 0.5.5.9)

## What it does
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Deflection Rating gives a chance to deflect a hit; a deflected hit has 40% of its damage prevented. Chance depends on the attacker's accuracy. It's rolled separately from (in addition to) evasion.
- src: game keywords "Deflect", tier 2; PoE2DB Deflect [S108], tier 2; Mobalytics Deflection [S061], tier 3; retrieved 2026-11-17
- notes: some items add to the 40%, e.g. a rune "Prevent +3% of Damage from Deflected Hits" ([PoE2DB Deflect](https://poe2db.tw/us/Deflect)).


## Works on red-flash boss attacks
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Unlike evasion, deflection works against boss attacks with a red flash.

- src: poe2wiki Deflection [S686], tier 2, retrieved 2026-11-17

## Formula and cap
@ v=0.5.x vol=may-change conf=conflict date=2026-11-17
Mobalytics: chance to deflect = 150 × (1 − A ÷ (A + 0.12 × D)), A = attacker accuracy, D = deflection rating, capped at 95%. poe2wiki: no minimum or maximum deflect chance.

- src: Mobalytics Deflection [S061], tier 3; poe2wiki Deflection [S686], tier 2; retrieved 2026-11-17
- conf: conflict on the cap → kb/04-conflicts.md "Deflection cap"

## Where it comes from
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Mostly converted from evasion: mods like "Gain Deflection Rating equal to X% of Evasion Rating" on Dex gear, uniques and passives. This applies after your evasion scaling, so it rewards heavy evasion investment.
- src: Mobalytics Deflection [S061], tier 3; poe2wiki Deflection [S686], PoE2DB Deflect [S108] (example items), tier 2; retrieved 2026-11-17
- notes: Heavily stunned players can't deflect (game keywords "Player Heavy Stun").
