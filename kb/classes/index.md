---
title: Classes & Ascendancies — Index
status: done
tracker_topic: "Class & ascendancy index (enumerate from tier 1–2)"
tracker_note: "done (0.5.5.9 + 1.0 announced; Master-at-Arms day-one now confirmed tier 1 — apply on next edit; rebuild at 1.0)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 1.0 announcements (researched 2026-11-17). 1.0 adds 2 classes — rebuild this list from the 1.0 game data after launch.

## Live classes in 0.5.5.9 (8) and their ascendancies (22)
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
| Class | Start attributes (Str/Dex/Int) | Ascendancies |
|---|---|---|
| Warrior | 15 / 7 / 7 | Titan · Warbringer · Smith of Kitava |
| Sorceress | 7 / 7 / 15 | Stormweaver · Chronomancer · Disciple of Varashta |
| Huntress | 7 / 15 / 7 | Amazon · Spirit Walker · Ritualist |
| Mercenary | 11 / 11 / 7 | Tactician · Witchhunter · Gemling Legionnaire |
| Monk | 7 / 11 / 11 | Martial Artist · Invoker · Acolyte of Chayula |
| Druid | 11 / 7 / 11 | Oracle · Shaman |
| Witch | 7 / 7 / 15 | Infernalist · Blood Mage · Lich (+ "Abyssal Lich" variant that overrides Lich's tree) |
| Ranger | 7 / 15 / 7 | Deadeye · Pathfinder |
- All classes start with 16 life and 30 mana base (before attribute/level gains).
- src: RePoE poe2 characters.json + ascendancies.json [S002], tier 2, retrieved 2026-11-17
- conf: single-source (game data) for the list; consistent with 1.0 announcement count below (22 + 4 = 26)
- notes: game data also holds Marauder, Duelist, Shadow and Templar class entries (PoE1-era slots) whose ascendancies are all "[DNT-UNUSED]" placeholders, plus unused Ranger, Druid placeholders — excluded. Martial Artist exists in data and is not flagged disabled; [INFERRED] live in 0.5.5 — confirm (it isn't in older guides).


## 1.0 additions: Shadow and Duelist
@ v=1.0 vol=may-change conf=confirmed date=2026-11-17
1.0 adds the Shadow and the Duelist, each with two ascendancies, for 10 classes and 26 ascendancies in total. Duelist ascendancies: Knight and Master-at-Arms. Shadow ascendancies: Assassin and Infiltrator.
- src: Mixed News 1.0 reveal [S044] (Duelist = Knight + Master-at-Arms), PoE2DB Conquerors of Wraeclast league page [S106], tier 2; The Outer Haven [S738] (10 classes, 26 ascendancies), tier 5; poe2-1.0-launch-brief.md (Shadow = Assassin, Infiltrator; Master-at-Arms possibly not day one), project doc; retrieved 2026-11-17
- v: 1.0 (announced, not patch notes)
- conf: confirmed (class names, 26 total, Knight + Master-at-Arms); single-source (Shadow ascendancy names)
- notes: launch brief flags Master-at-Arms day-one availability as uncertain (Steam vs press text) — still open in poe2-project-instructions.md. 1.0 class reworks named in reveal notes: Infernalist (Demon Magus, hounds), Acolyte of Chayula, Blood Mage (Exsanguinate, Corrupted Blood rework), Mercenary (background reload).


## Ascendancy node counts (game data, notables per ascendancy)
@ v=0.5.5.9 vol=? conf=? date=2026-11-17 fill=v missing=vol,conf
- Most ascendancies have 8 notables; larger trees: Smith of Kitava 18, Disciple of Varashta 17, Infernalist 11, Tactician 10, Stormweaver 10, Acolyte of Chayula 10, Amazon/Spirit Walker/Invoker/Blood Mage/Lich 9.
- src: RePoE passive_skill_trees/Default.json, tier 2. single-source. Large counts usually mean choice nodes (e.g. Smith's weapon-forging options) — [INFERRED].


## Per-class docs
- Deferred until 1.0 patch notes (ascendancy nodes are being reworked). Priority order when written: shortlist candidates in claude/starter-decision-sheet.md — Deadeye, Knight, Infernalist, Blood Mage; then Witchhunter (char 2).
