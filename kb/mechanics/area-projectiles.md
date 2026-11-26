---
title: Area of Effect & Projectiles
status: partial
tracker_topic: "Area of effect & projectiles"
tracker_note: "partial (area-vs-radius √ rule still tier 5 only; poe2wiki AoE page has no mechanics text; PoE2DB corpus has none either)"
---

Status: partial — area-vs-radius maths still lacks a tier 1–2 statement (poe2wiki "Area of effect" page has no mechanics text, checked 2026-11-25). Re-check at 1.0.

## Area of effect definition
@ v=0.5.x vol=stable conf=confirmed date=2026-11-25
An AoE skill affects every target inside its area instead of picking targets. If the area starts from a target the skill hit, that target's size is added to the radius. Dodge roll gives no avoidance against AoE.

- src: poe2db:Keywords, tier 2; poe2wiki Area of effect [S665], tier 2, rev 109096, read via built-in browser 2026-11-25

## AoE modifiers scale area, not radius
@ v=0.5.x vol=may-change conf=inferred date=2026-11-25
"% increased Area of Effect" scales the area, so radius grows with the square root: radius × √(1 + inc). +40% area on a 2 m radius ≈ 2.37 m; +90% on 2 m ≈ 2.76 m.
- src: GGG forum player threads (3674502 [S103], 3653958 [S653], 3672838 [S657]), tier 5; Switchblade Gaming Titan guide [S737], tier 5; retrieved 2026-11-17 / 2026-11-25
- conf: [INFERRED]: several independent players measured tooltip radius growing ~√ of the bonus (e.g. 2.3 m × √1.15 ≈ 2.46 → shown 2.5); same rule as PoE1. No tier 1–2 statement.
- notes: flat "+X metres to radius" lines are separate from % area ([INFERRED] added to base radius before % area, as in PoE1).


## Presence radius
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Your Presence is a 4 m radius around you by default, where many auras etc. apply. Only Presence Area modifiers change it; normal skill-area modifiers don't.

- src: RePoE poe2 keywords.json "Presence" [S002], tier 2 game data; Mobalytics Presence [S081], tier 3; retrieved 2026-11-17
- conf: confirmed (poe2wiki said 6 m — see kb/04-conflicts.md, resolved by game data)

## "Nearby"
@ v=0.5.x vol=stable conf=single-source date=2026-11-17
"Nearby" is not a keyword; it just means a circular area, always paired with a stated distance in metres.

- src: poe2wiki Distance [S612], tier 2, retrieved 2026-11-17

## Projectile definition & volleys
@ v=0.5.x vol=stable conf=confirmed date=2026-11-17
A projectile is a moving attack or spell that usually hits on contact. From one volley fired together, only one projectile can hit each target unless stated otherwise. Projectiles fired in sequence can each hit the same target.

- src: poe2db:Keywords, tier 2; poe2wiki Chains [S676], poe2wiki Projectile behaviour [S716], tier 2; retrieved 2026-11-17

## Behaviour order: Split → Pierce → Fork → Chain (→ Return)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Only one behaviour happens per collision, in priority order Split, Pierce, Fork, Chain. A projectile that pierces everything never forks or chains. Terrain can't be pierced, so a piercing projectile can still chain off terrain.
- src: poe2wiki Projectile [S629], poe2wiki Projectiles [S630], poe2wiki Chained [S675], tier 2; poe2db:Keywords, tier 2; retrieved 2026-11-17
- notes: Return position after Chain taken from PoE2DB's Return definition; [INFERRED] lowest priority as in PoE1.


## Individual behaviours
- Split: fires copies toward several targets within 6 m after the first hit. Source: [poe2wiki Projectile](https://poe2wiki.net/wiki/Projectile). single-source.
- Pierce: passes through and keeps damaging. "X% chance to Pierce" = one guaranteed pierce per 100% plus a chance for the remainder (250% = 2 pierces + 50% for a third). Source: [poe2wiki Pierce](https://www.poe2wiki.net/wiki/Pierce). single-source.
- Fork: splits into two the first time it hits an enemy (and doesn't pierce it). Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), [poe2wiki Fork](https://www.poe2wiki.net/wiki/Fork). confirmed.
- Chain: redirects to a new target after hitting. Projectiles chain up to 6 m, other effects 4 m; no target twice in one chain. Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords). single-source.
- Return: comes back to the shooter after finishing travel or its last target. Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords). single-source.
- Version 0.5.x, volatility may-change.
