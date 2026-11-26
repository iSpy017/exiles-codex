---
title: Attack, Cast & Skill Speed
status: partial
tracker_topic: "Attack & cast speed"
tracker_note: "partial (use-time formula, frame cap, dual wield added 2026-11-25; weapon base rates by class missing; 1 conflict)"
---

Status: partial — use-time formula and dual-wield rules added 2026-11-25; weapon base rates by class and reload specifics still missing. Re-check at 1.0.

## Attacks use the weapon; spells use the skill
@ v=0.5.x vol=stable conf=confirmed date=2026-11-17
An attack's base damage, attack speed and crit come from the equipped weapon unless the skill says otherwise. Spells have their own base damage, cast time and crit, and ignore weapon stats.

- src: poe2wiki Attack [S668], tier 2; poe2db:Keywords, tier 2; retrieved 2026-11-17

## Skill speed stacks additively with attack/cast speed
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-25
"Skill Speed" affects every skill and adds together with the narrower variants (attack speed incl. crossbow reload, cast speed, trap throw speed, totem placement, warcry speed, reload speed) into one total. E.g. 6% inc cast + 5% inc skill = 11% for spells.

- src: poe2wiki Skill speed [S669], tier 2, rev 130082, read via built-in browser 2026-11-25; Mobalytics Skill Speed [S087], tier 3, 2026-11-17

## Use-time formula
@ v=0.5.x vol=stable conf=single-source date=2026-11-25
Final use time = base use time ÷ (1 + total skill speed%) + any flat time penalty. E.g. 0.8 s base (1.25/s) with 40% inc → 1.75/s → 0.57 s.

- src: poe2wiki Skill speed, tier 2, 2026-11-25

## Fixed use-time penalties can't be sped up
@ v=0.5.x vol=may-change conf=single-source date=2026-11-25
Some skills carry a flat penalty (e.g. Whirling Assault "+1 second to Total Attack Time"). It's added after speed modifiers, so speed stats don't shrink it.

- src: poe2wiki Skill speed, tier 2, 2026-11-17 and 2026-11-25

## Server-frame cap
@ v=0.5.x vol=may-change conf=single-source date=2026-11-25
Non-channelled actions happen at most once per 33 ms server frame (~30.3/s). Faster use times lose DPS even though the tooltip still counts them.

- src: poe2wiki Skill speed, tier 2, 2026-11-25

## Action speed is different
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-25
Action speed is a separate multiplier from skill speed and is what slows (e.g. chill) reduce.

- src: poe2wiki Skill speed, tier 2, 2026-11-25; Mobalytics Skill Speed explained [S093], tier 3, 2026-11-17

## Local weapon attack speed
@ v=0.5.x vol=stable conf=single-source date=2026-11-25
"% increased Attack Speed" on a weapon modifies that weapon's base attack speed and is multiplicative with global attack speed.

- src: poe2wiki Modifier [S705], tier 2, rev 135639, 2026-11-25
- conf: single-source; see [[mechanics/damage-calculation]] for other local mods.

## Dual wielding
@ v=0.5.x vol=may-change conf=single-source date=2026-11-25
Dual wielding = a martial weapon in each hand, both the same item class. Caster weapons, spears and flails can't be dual wielded, which leaves maces, swords, axes and daggers. Two empty hands don't count. No inherent bonus (unlike PoE1's 10% more attack speed). Two one-handed swords grant Parry only if a sword is in the off-hand. Two-handed axes/maces/swords can be dual wielded with Giant's Blood or The Bringer of Rain.
- src: poe2wiki Dual wielding [S690], tier 2, rev 135854, 2026-11-25
- vol: may-change (1.0 adds Duelist)
- notes: an older revision snippet ([poe2wiki Dual wield](https://poe2wiki.net/wiki/Dual_wield)) only says "same item class"; the newer list may exclude claws because no claws are dual-wieldable in 0.5 — [INFERRED], check at 1.0.


## Dual-wield hits: alternate or combined
@ v=0.5.x vol=may-change conf=single-source date=2026-11-25
The skill decides: it alternates hands, or uses both for one combined hit. In a combined hit each hand rolls separately and the damage is summed; one hand critting makes the whole hit a crit. If one weapon can't be used by the skill, only the compatible one is used.

- src: poe2wiki Dual wielding, tier 2, 2026-11-25
- conf: single-source; conflicts with a PoB-PoE2 pull request saying "double hits when dual wielding" skills make two separate hits — see [[conflicts]].

## Onslaught
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Onslaught grants 20% increased Skill Speed.

- src: poe2db:Keywords, tier 2, retrieved 2026-11-17

## Still to source
- Weapon base attack rates by class; dual-wield attack rate when the two weapons differ; reload speed specifics; warcry speed specifics.
