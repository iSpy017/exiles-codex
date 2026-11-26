---
title: Sockets, runes, soul cores, idols (augments)
status: partial
tracker_topic: "Sockets, runes, soul cores, idols"
tracker_note: "partial"
defaults: v=0.5.5.9
---

Scope: augment sockets on equipment, how many, how to add them, augment families and their level tiers. Gem sockets → [[socketing-limits]]. Version 0.5.5.9 unless noted.

## Augments and augment sockets
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Augments go into augment sockets, usually on equipment. Once socketed they can be overwritten by another augment but not removed. Each augment lists which item types it fits and the bonus per type. Families: Runes (Kalguuran), Soul Cores (Vaal), Idols (Azmeri), plus a few special kinds (Abyssal Eye, Congealed Mist).
- src: RePoE poe2 keywords.json "Augment", "Rune", "Soul Core", "Idol"; augments.json; tier 2 (game data), retrieved 2026-11-17
- conf: confirmed (game data + [poe2wiki Soul cores](https://www.poe2wiki.net/wiki/Soul_cores))
- notes: Counts in data: 221 runes (incl. unused), 52 soul cores, 35 idols, 4 Abyssal Eyes, 1 Congealed Mist.


## Special augment rules
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Ancient Augments — strong single effects, only one socketed at a time. Socket-bound augments permanently fill the socket (can't be removed, replaced or extracted). Some rune/idol mods are "Bonded" (only with Shaman's Wisdom of the Maji). Some runes are limited to "1 Aldur's Legacy".

- src: RePoE keywords.json + augments.json `limit`, tier 2, retrieved 2026-11-17
- conf: single-source (game data)

## Max sockets per item
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Body armours and two-handed weapons: up to 2. Other armour and weapons: up to 1 (foci, shields, bucklers 1). Quivers: none. Rings/amulets/belts: none by default. Some uniques have more; corruption can add one beyond the limit.
- src: poe2wiki Item socket [S723], poe2wiki Rune socket [S634], tier 2, retrieved 2026-11-17
- conf: confirmed (game8 tier 5 agrees: 2 weapon + 2 body + 1 each gloves/boots/helmet)
- notes: Exceptional drops can have an extra socket ([[rarity]]). Grasping Ring / Corona Amulet / Stalking Belt use socketed items as gloves/helmet/boots ([[bases-implicits]]) — [INFERRED] they have a socket; check in game.


## Adding sockets
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Artificer's Orb adds an augment socket to a martial weapon, wand, staff or armour. 10 Artificer's Shards make an orb; shards come from salvaging socketed items at the Salvage Bench (Act 1).
- src: RePoE base_items.json (Artificer's Orb text, drop level 5), tier 2; Maxroll Runes and Soul Cores [S043], tier 3; retrieved 2026-11-17
- notes: Levelling tip: salvage every socketed drop for shards [INFERRED from the recipe].


## Rune ladder (level requirement)
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Standard runes come in four steps: Lesser (no req) → base (15) → Greater (30) → Perfect (50). Elemental/attribute/defence lines: Adept, Body, Charging, Desert, Glacial, Inspiration, Iron, Mind, Rebirth, Resolve, Robust, Stone, Storm, Tempered (no Perfect), Vision, Ward. Other rune sets: "Rune of X" (15), Warding runes (15/30/45), Ancient runes (30), named Azmeri-spirit runes (50, e.g. Farrul's, Saqawal's, Fenumus', Craiceann's), Emergent (60, ancient), Legacy of <unique> (65, Aldur's Legacy limit).
- src: RePoE augments.json `required_level`, tier 2, retrieved 2026-11-17
- vol: may-change (league content)
- conf: single-source (game data)
- notes: Effects per slot not listed here — e.g. Body Rune: weapon life leech / armour +life (game8, tier 5). Full table → crafting batch if needed. "[DNT-Unused]" runes excluded.


## Soul cores and idols (level requirement)
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Basic soul cores (named after Vaal gods/kings, e.g. Atmohua, Jiquani, Xopec) have no level req; the "<Name>'s Soul Core of <X>" set needs 50; Theses (ancient) 60. Idols: animal idols (Bear, Boar, Cat, Fox, Owl, Ox, Primate, Rabbit, Snake, Stag, Wolf) no req; named idols (Idol of Alira, Kraityn, Oak…) and Hawk/Panther/Stoat 50; Carved idols (ancient) 60.
- src: RePoE augments.json, tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: Soul core examples: Jiquani = martial weapon life on kill / body armour 3% inc life; a soul core giving +15 spirit to martial weapons and +5% ele res to armour ([poe2wiki Soul cores](https://www.poe2wiki.net/wiki/Soul_cores)). Soul cores tie into Vaal temple → [[vaal-temple]].
