---
title: Damage Types & Conversion
status: done
tracker_topic: "Damage types & conversion"
tracker_note: "done (0.5.x; recheck 1.0)"
---

Version note: all entries researched 2026-11-17 against 0.5.x sources (live league 0.5.5). Re-check at 1.0.
Access note: poe2wiki pages are blocked to direct fetch (Anubis); poe2wiki claims below come from search-engine snippets of those pages.

## The five damage types
@ v=0.5.x vol=stable conf=single-source date=2026-11-17
Five types: Physical, Fire, Cold, Lightning, Chaos. Fire, Cold, Lightning are the elemental types.

- src: poe2db:Keywords, tier 2, retrieved 2026-11-17
- conf: single-source (consistent with every other page read)

## How each type is mitigated / special behaviour
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Physical is reduced by Armour (the only type that is), the others by their matching resistance. Chaos is the rarest type and strips double its value from Energy Shield. Fire hits build Flammability (→ Ignite); Cold hits apply Chill and build Freeze but cannot build Heavy Stun; Lightning hits can Shock.
- src: poe2db:Keywords, tier 2, retrieved 2026-11-17
- notes: details per ailment in batch 2 docs; armour/res in [[mechanics/armour]], [[mechanics/resistances]]


## Conversion: two-step order
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Conversion happens in two steps: conversion built into the skill (skill gem, item- or ascendancy-granted skill) first, then every other source (gear, tree, global effects) applies to what's left.

- src: poe2db:Damage_conversion, tier 2; poe2wiki Conversion [S678], tier 2; both retrieved 2026-11-17

## Converted damage scales only as its final type
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Once converted, damage scales with modifiers for its new type only; the original type's modifiers no longer apply (e.g. phys→fire is not boosted by increased physical damage). This is a change from PoE1.

- src: poe2wiki Damage conversion [S610], tier 2; PoE2DB Damage Conversion [S107], tier 2; retrieved 2026-11-17

## Any type → any type, no loops
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Damage can convert from any type to any other with no fixed order (PoE1 had a strict order). All conversion is applied at once, so damage can't convert twice and loops are impossible.

- src: poe2wiki Overconversion [S626], tier 2; Mobalytics Damage Conversion [S060], tier 3; retrieved 2026-11-17

## Overconversion
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
If either step adds up to more than 100% of a type, it's scaled down proportionally to 100%.

- src: poe2wiki Overconversion [S626], tier 2, retrieved 2026-11-17

## When conversion is calculated
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Conversion is applied after flat added damage is combined with base damage, but before any increased/more modifiers.
- src: poe2wiki Damage conversion [S610], tier 2; Mobalytics Damage Conversion [S060], tier 3; retrieved 2026-11-17 poe2wiki Conversion [S678], single-source.
- notes: exception — weapon-local conversion on some weapons applies before the weapon's own local mods (quality, added phys, % phys), so those local mods don't boost the converted portion.


## "Gain as extra"
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
"Gain X% of [type] as extra [type]" adds new damage while leaving the original intact (regular conversion removes it). It follows the same two-step process. Gained damage scales with the new type's modifiers only.

- src: poe2wiki Overconversion [S626], tier 2; poe2wiki Conversion [S607], tier 2; retrieved 2026-11-17
- conf: single-source (one wiki, two pages)

## Hits only
@ v=0.5.x vol=stable conf=confirmed date=2026-11-17
Conversion and gain only affect hits; damage over time can't be converted or gained.
- src: poe2db:Damage_conversion, tier 2; poe2wiki Damage conversion [S610], tier 2; Mobalytics [S060], tier 3; retrieved 2026-11-17
- notes: see [[mechanics/hits-vs-dot]]


## Non-damage conversion
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Stat conversion (e.g. evasion → armour) works the same way: the converted part scales with the new stat's modifiers only.
- src: poe2wiki Conversion (Gains) [S618], tier 2, retrieved 2026-11-17
