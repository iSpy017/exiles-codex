---
title: Area levels (campaign, 0.5.5.9)
status: done
tracker_topic: "Area levels"
tracker_note: "done (0.5.5.9; 1.0 restructure)"
---

Version note: 1.0 restructures the campaign (Acts 5–6 added, Interludes removed) — every number here is 0.5.5.9 and must be re-checked at the 1.0 refresh.

## Area level ranges by act
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Act 1 = area level 1–15 (Riverbank 1 → Ogham Manor 15) · Act 2 = 16–31 (Vastiri Outskirts 16 → Dreadnought 31; jump from 23 to 28 at Deshar) · Act 3 = 33–45 (Sandswept Marsh 33 → Black Chambers 45) · Act 4 = 46–53 · Interludes (3 chains) = 54–56 · endgame maps start at 65 (T1).
- src: RePoE poe2 world_areas.json [S002], tier 2 (game data), retrieved 2026-11-17; poe2db:Act_1, poe2db:Act_2, poe2db:Act_3, tier 2
- vol: may-change (1.0 campaign rework)
- conf: confirmed (game data + PoE2DB)
- notes: Interlude areas are tagged act "6" in the data (ids P1_/P2_/P3_). Towns carry higher nominal levels (Clearfell Encampment 15, Ardura Caravan 32, Ziggurat Encampment 44, Kingsmarch 53, interlude towns 64) — town level doesn't matter for drops [INFERRED: no monsters]. Gap Interlude 56 → endgame 65 is bridged by levelling in the last zones/early maps.


## What area level does
@ v=0.5.x vol=stable conf=single-source date=2026-11-17
Area level sets monster level (magic/rare +1, boss +2) and so item level of drops; it also sets the XP-penalty comparison with your character level.
- src: poe2wiki Level [S624], tier 2, retrieved 2026-11-17
- conf: single-source (tier 2)
- notes: → [[item-level]] for drop item levels and the XP-penalty formula (3 + charlevel/16).


## Practical levels for the skip route
@ v=0.5.5.9 vol=may-change conf=inferred
Uncut gem drop levels track area level ([[uncut-gems]]); e.g. the Act 2 → Act 3 transition (31 → 33) is where higher-level uncut gems can start dropping; Act 4 areas (46–53) can drop gems/bases at 46+.
- src: combination of world_areas.json (tier 2) and [[uncut-gems]] drop levels
- conf: [INFERRED] — arithmetic from two sourced tables
- notes: → strategy/skip-route once 1.0 acts are known.
