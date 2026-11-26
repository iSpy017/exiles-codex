---
title: Meta & Trigger Gems
status: done
tracker_topic: "Meta & trigger gems"
tracker_note: "done (0.5.5.9; sources of tier-0 metas partial)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0. Mechanics → [[mechanics/skill-interactions]].

## Rules recap
- Meta gems hold other skill/support gems and use or trigger them; can't nest; usually reserve spirit; energy-based ones trigger by the socketed skill's use time. Two trigger methods on one skill disables it. (game keywords, see skill-interactions)

## Meta gems in game data (tag "meta"; [DNT]/unused entries removed)
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Engravable (tier = min uncut level):
- Tier 3: Pounce
- Tier 7: Ferocious Roar, Spell Totem
- Tier 8: Barrier Invocation, Blasphemy, Cast on Minion Death, Elemental Invocation, Mirage Archer
- Tier 9: Hand of Chayula
- Tier 11: Mortar Cannon
- Tier 13: Ancestral Warrior Totem
- Tier 14: Cast on Critical, Cast on Dodge, Cast on Elemental Ailment, Feral Invocation, Reaper's Invocation
Not engravable (tier 0 — granted by items/ascendancies/other sources): Animus Splinters, Called Shots, Cast on Block, Cast on Charm Use, Cast on Death, Cast on Freeze, Cast on Ignite, Cast on Melee Kill, Cast on Melee Stun, Cast on Shock, Cast when Damage Taken, Cast when Stunned, Cast while Channelling, Curse on Block, Demon Magus, Fire Spell on Hit, Hollow Form, Hydra Familiar, Mirage Deadeye, Spellslinger, Spirit Vessel, Summon Companion, Thundergod's Wrath
- src: RePoE poe2 skill_gems.json [S002] (tags + crafting_level), tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: tier-0 sources not yet mapped (e.g. Mirage Deadeye → Deadeye ascendancy, Demon Magus → Infernalist per launch brief; Spirit Vessel granted by a unique per [PoE2DB Deflect](https://poe2db.tw/us/Deflect)). Map them in the classes/items batches. Demon Magus matters for the Infernalist shortlist candidate.


## Trigger-tagged gems
- 134 gems carry the "trigger" tag in game data (includes supports and triggered actives). Full list on demand from skill_gems.json.

## Not yet sourced
- Spirit cost per meta gem; energy thresholds per meta gem (skills.json stat data).
