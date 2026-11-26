---
title: Skill Combos & Interactions (meta, trigger, energy, marks, curses, infusions)
status: done
tracker_topic: "Skill combos & interactions"
tracker_note: "done (0.5.5.9 game data only)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2. Mostly single-source (game data) — second-source checks happen in the gems batch.

## Triggered skills
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
A triggered skill fires instantly (no attack/cast time) and usually targets whatever caused the trigger. Triggering doesn't count as "using" the skill. If two different trigger methods apply to one skill, the skill is disabled. Channelled skills can't be triggered.

- src: game keywords "Triggered Skills", tier 2, retrieved 2026-11-17

## Meta gems & Energy
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Meta gems are skill gems you socket other gems into; they use/trigger/apply those gems. Skill and support gems can go in interchangeably; most need at least one skill gem; meta gems can't go inside other meta gems. Many meta skills build their own Energy counter and spend it to trigger socketed skills, scaled by the triggered skill's use time. For energy maths, "total use time" modifiers count double. Triggered skills' direct effects can't generate energy (no loops).
- src: game keywords "Meta Gems", "Energy", tier 2, retrieved 2026-11-17
- notes: meta gems also reserve spirit ([[mechanics/spirit-reservation]]). Full meta/trigger gem list → [[gems/meta-trigger]].


## Persistent, Herald, Link, Aura
@ v=0.5.5.9 vol=? conf=? date=2026-11-17 fill=v missing=vol,conf
- Persistent skills: toggled in the Skills Panel, usually reserve spirit.
- Heralds: persistent buffs with on-kill effects.
- Link skills: buff an ally you're linked to while within range.
- Auras: buff allies / debuff enemies in a radius (often your 4 m Presence).
- src: game keywords, tier 2. single-source.


## Combo
@ v=0.5.5.9 vol=? conf=? date=2026-11-17 fill=v missing=vol,conf
Some skills count Combo, gained when you Strike enemies (melee hits with weapon/body — slams don't count). It decays without hits, only builds with the weapon its skill is bound to, and is lost on weapon swap.
- src: game keywords "Combo", "Strike", tier 2. single-source.


## Marks and curses
@ v=0.5.5.9 vol=? conf=? date=2026-11-17 fill=v missing=vol,conf
- Marks: single-target debuffs. You can mark several enemies, but each enemy holds one mark. Marks Activate on a condition, do something extra, then are consumed. "Marked for Death" = 50% increased damage taken.
- Curses: one curse per target by default. Weaker on tougher enemies: 15% less effect on Magic, 30% on Rare, 50% on Unique (same scaling as Exposure).
- src: game keywords "Mark", "Activating Marks", "Marked for Death", "Curses", tier 2. single-source.


## Infusions & remnants
@ v=0.5.5.9 vol=? conf=? date=2026-11-17 fill=v missing=vol,conf
- Remnants: objects your skills leave behind; walk over to collect a bonus; they expire.
- Elemental Infusions: some skills drop infusion remnants; picking one up gives the infusion for 20 s or until another skill consumes it. Max 3 of each element by default. Skills that repeat must consume one per repeat. Verisium Infusion can stand in for any element (used last).
- src: game keywords "Remnants", "Elemental Infusions", "Verisium Infusion", tier 2. single-source.


## Other rules worth knowing
@ v=0.5.5.9 vol=may-change conf=? date=2026-11-17 missing=conf
- Sustained skills roll crit on every hit, not once per use.
- Cooldown Recovery Rate only affects skill cooldowns (100% increased = half the cooldown).
- Elemental Surges: consumed by non-melee projectile attacks to add a Surging Blast at the end of flight; max 6 of each per weapon, 15 s, weapon-specific; split/forked projectiles don't benefit.
- Aftershocks: repeat area damage after an attack's impact; only attack damage can cause them.
- src: game keywords "Sustained Skills", "Cooldown Recovery Rate", "Elemental Surges", "Aftershocks", tier 2. single-source.
- Version 0.5.5.9, volatility may-change for all.
