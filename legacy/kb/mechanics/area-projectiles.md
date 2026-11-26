# Area of Effect & Projectiles

Status: partial — area-vs-radius maths still lacks a tier 1–2 statement (poe2wiki "Area of effect" page has no mechanics text, checked 2026-11-25). Re-check at 1.0.

## Area of effect definition
- Claim: An AoE skill affects every target inside its area instead of picking targets. If the area starts from a target the skill hit, that target's size is added to the radius. Dodge roll gives no avoidance against AoE.
- Version: 0.5.x
- Volatility: stable
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; [poe2wiki Area of effect](https://www.poe2wiki.net/wiki/Area_of_effect), tier 2, rev 109096, read via built-in browser 2026-11-25
- Confidence: confirmed

## AoE modifiers scale area, not radius
- Claim: "% increased Area of Effect" scales the area, so radius grows with the square root: radius × √(1 + inc). +40% area on a 2 m radius ≈ 2.37 m; +90% on 2 m ≈ 2.76 m.
- Version: 0.5.x
- Volatility: may-change
- Source: GGG forum player threads ([3674502](https://pathofexile.com/forum/view-thread/3674502), [3653958](https://webcdn.pathofexile.com/forum/view-thread/3653958), [3672838](https://www.pathofexile.com/forum/view-thread/3672838)), tier 5; [Switchblade Gaming Titan guide](https://www.switchbladegaming.com/path-of-exile-2/warrior-titan-build/), tier 5; retrieved 2026-11-17 / 2026-11-25
- Confidence: [INFERRED]: several independent players measured tooltip radius growing ~√ of the bonus (e.g. 2.3 m × √1.15 ≈ 2.46 → shown 2.5); same rule as PoE1. No tier 1–2 statement.
- Notes: flat "+X metres to radius" lines are separate from % area ([INFERRED] added to base radius before % area, as in PoE1).

## Presence radius
- Claim: Your Presence is a 4 m radius around you by default, where many auras etc. apply. Only Presence Area modifiers change it; normal skill-area modifiers don't.
- Version: 0.5.5.9
- Volatility: may-change
- Source: [RePoE poe2 keywords.json "Presence"](https://github.com/repoe-fork/poe2), tier 2 game data; [Mobalytics Presence](https://mobalytics.gg/poe-2/guides/presence), tier 3; retrieved 2026-11-17
- Confidence: confirmed (poe2wiki said 6 m — see kb/04-conflicts.md, resolved by game data)

## "Nearby"
- Claim: "Nearby" is not a keyword; it just means a circular area, always paired with a stated distance in metres.
- Version: 0.5.x
- Volatility: stable
- Source: [poe2wiki Distance](https://poe2wiki.net/wiki/Distance), tier 2, retrieved 2026-11-17
- Confidence: single-source

## Projectile definition & volleys
- Claim: A projectile is a moving attack or spell that usually hits on contact. From one volley fired together, only one projectile can hit each target unless stated otherwise. Projectiles fired in sequence can each hit the same target.
- Version: 0.5.x
- Volatility: stable
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; [poe2wiki Chains](https://www.poe2wiki.net/wiki/Chains), [poe2wiki Projectile behaviour](https://www.poe2wiki.net/wiki/Projectile_behaviour), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Behaviour order: Split → Pierce → Fork → Chain (→ Return)
- Claim: Only one behaviour happens per collision, in priority order Split, Pierce, Fork, Chain. A projectile that pierces everything never forks or chains. Terrain can't be pierced, so a piercing projectile can still chain off terrain.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Projectile](https://poe2wiki.net/wiki/Projectile), [poe2wiki Projectiles](https://poe2wiki.net/wiki/Projectiles), [poe2wiki Chained](https://www.poe2wiki.net/wiki/Chained), tier 2; [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Return position after Chain taken from PoE2DB's Return definition; [INFERRED] lowest priority as in PoE1.

## Individual behaviours
- Split: fires copies toward several targets within 6 m after the first hit. Source: [poe2wiki Projectile](https://poe2wiki.net/wiki/Projectile). single-source.
- Pierce: passes through and keeps damaging. "X% chance to Pierce" = one guaranteed pierce per 100% plus a chance for the remainder (250% = 2 pierces + 50% for a third). Source: [poe2wiki Pierce](https://www.poe2wiki.net/wiki/Pierce). single-source.
- Fork: splits into two the first time it hits an enemy (and doesn't pierce it). Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), [poe2wiki Fork](https://www.poe2wiki.net/wiki/Fork). confirmed.
- Chain: redirects to a new target after hitting. Projectiles chain up to 6 m, other effects 4 m; no target twice in one chain. Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords). single-source.
- Return: comes back to the shooter after finishing travel or its last target. Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords). single-source.
- Version 0.5.x, volatility may-change.
