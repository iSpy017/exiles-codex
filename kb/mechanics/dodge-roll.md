---
title: Dodge Roll & Sprint
status: done
tracker_topic: "Dodge roll"
tracker_note: "done (0.5.x; recheck 1.0)"
defaults: v=0.5.x
---

Version: 0.5.x (researched 2026-11-17). Re-check at 1.0. No dodge-roll keyword in game data; sources are poe2wiki, poe2db community wiki, Mobalytics.

## Basics
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Every character has a dodge roll on its own keybind (spacebar default), no gem, no cooldown, no cost. It cancels almost any animation except another roll.

- src: poe2wiki Dodge roll [S613], poe2wiki Dodged [S688], tier 2; PoE2DB Dodge Roll [S113] (community wiki section), tier 2; Mobalytics Dodge Roll [S062], tier 3; retrieved 2026-11-17

## What it avoids
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
The first half of the roll avoids projectiles and non-AoE (melee/strike) attacks. It does NOT avoid AoE or ground effects. PoE2DB's wiki phrases this as "no invulnerability" but the same avoidance window — practical effect is identical.

- src: poe2wiki Dodged [S688], tier 2; poe2db:Dodge_Roll, tier 2; retrieved 2026-11-17

## Speed / distance
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Not faster than running; roll speed scales with movement speed. Distance roughly 3.7 m.

- src: PoE2DB Dodge Roll [S113], tier 2 (speed); 3.7 m from tier-5 sources only
- conf: single-source (speed); [INFERRED] 3.7 m — verify

## Keystones that change it
@ v=0.5.x vol=may-change conf=? date=2026-11-17 fill=vol missing=conf,src
- Unwavering Stance: can't be light stunned, but no dodge roll or sprint. (game keywords; [poe2wiki Dodge roll](https://poe2wiki.net/wiki/Dodge_roll) also says it doubles stun threshold)
- Bulwark: rolls no longer avoid damage, instead you take 30% less hit damage while rolling. ([poe2wiki Dodge roll](https://poe2wiki.net/wiki/Dodge_roll); [PoE2DB Dodge Roll](https://poe2db.tw/us/Dodge_Roll) for the 30%)

- v: 0.5.x, confidence confirmed (both named in 2 sources)

## Sprint
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Hold the roll key after a roll to sprint: 50% increased movement speed, but getting hit can knock you down. Any skill use ends it. A settings toggle can make the key toggle sprint. Pathfinder's Running Assault prevents knockdown. No roll = no sprint (e.g. with Blink active).
- src: poe2wiki Sprint [S725], tier 2; Mobalytics Sprinting [S089], tier 3; retrieved 2026-11-17
- v: 0.5.x (sprint added 0.3.1)
- conf: confirmed (50%, knockdown); single-source (Running Assault)
- notes: sprint is the skip-route travel tool between packs → [[strategy/skip-route]].
