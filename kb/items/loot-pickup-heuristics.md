---
title: Loot pick-up heuristics (what to keep vs leave)
status: done
tracker_topic: "Loot pickup heuristics"
tracker_note: "done (tier 5, 0.5.x; 1 conflict)"
defaults: v=0.5.x vol=volatile
---

Source: YouTube transcript "Evaluating Loot and Item Tiers in PoE 2" (creator handle in the outro reads "meesoxure", ASR spelling), TranscriptX.ai, supplied by David, ingested 2026-11-17. Tier 5 (creator guide); transcript is auto-generated and imperfect, so numbers and item names below are unverified until checked against tier 1–2 sources. Version: 0.5.x (about 0.5.5). Volatility: volatile (meta-dependent). One line in the video mentions a "0.14" patch for another unique — likely PoE1 carry-over; ignored.

## Value tiers of magic/rare drops (creator's buckets)
@ v=0.5.x vol=volatile conf=single-source date=2026-11-17
Tier 1 (easiest value, highest ceiling): jewels, rings, amulets, weapons. Tier 2: boots (35% movement speed alone makes boots worth selling; value dips late league) and gloves (a few offensive lines). Tier 3 (needs 4–5 good lines): belts — useful at league start (easy survivability rolls) but rare belts become near-worthless after a couple of weeks because late-game belt slots go to chase uniques (Headhunter, Mageblood and others named).

- src: transcript, tier 5, 2026-11-17
- conf: single-source (opinion)

## Tier of an unidentified drop
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Unidentified items show a tier 0–5. Tier 5 means at least one high-tier mod on identification; no tier = none. Tiers don't affect mods added later by crafting. Creator picks up only tier-5 rares (and tier-5 magics) late, is more flexible early.

- src: transcript, tier 5; wiki table in [[items/rarity]] (tier 2: Tier 5 = ilvl 79+ and mod level 48+), 2026-11-17
- conf: confirmed in outline (two sources agree on the filter idea); creator's "at least one high-tier mod" is a simplification — the wiki table is the rule.

## Rules of thumb by item class
@ v=0.5.x vol=volatile conf=single-source date=2026-11-17 fill=v
- Armour/focus/shield: bigger defence number = better; level 65+ bases only matter in endgame; exceptions are bases with a special implicit (example named: Warlord Carapace with armour-also-applies-to-elemental implicit).
- Martial weapons/quivers: crit chance is king in 0.5.5 and bigger physical numbers; exceptions by implicit (example: Gemini Bow with extra-arrow chance).
- Wands/staves: required level follows the gem on it; elemental wands/staves only roll their element's +level mods; neutral bases (Dueling Wand, Chiming Staff, maybe Reaping Staff) can roll any element, which makes them valuable.
- Jewellery: pick up all; low-value bases listed (Iron Ring, Crimson Amulet, Lazuli Ring, Azure Amulet).
- src: transcript, tier 5
- notes: "Crit chance is king" is 0.5.5 only: GGG says crit chance leaves the tree in 1.0 and weapons/gear carry it → [[strategy/dev-statements-1.0-balance]]; this list needs a 1.0 re-check.


## Item level
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Creator says item level decides which mod tiers can roll (higher ilvl = higher tiers), and drops from "a T15 map (level 79 monsters)" always come as ilvl 79. For ilvl 82 he says T16 map plus an irradiated tablet plus a corrupted or cleansed area with +1 map level. He says rings, gloves and amulets only need ilvl 75 for the mods people want (flat damage), while helmets, off-hands, boots, body armour and weapons need 82 (weapon max physical, boots 35% movement speed, top resistances).

- src: transcript, tier 5, 2026-11-17; compared with [[items/item-level]] (tier 2, derived)
- conf: partly conflicting — "always 79 from T15" ignores the +1 magic/rare and +2 boss monster-level bonus in [[items/item-level]]; recorded in kb/04-conflicts.md. The 35% boots = ilvl 82 claim matches the existing doc.

## Exceptional and chanceable bases
@ v=0.5.x vol=volatile conf=single-source date=2026-11-17
Exceptional bases with extra sockets are the ones to pick up; the >20%-quality exceptional bases are worthless "right now" (creator). Any Normal base can take a Chance Orb to try for a unique; which bases are good changes league to league. Heavy Belt and Utility Belt (said to chance into Headhunter and Mageblood respectively) are always worth picking up.
- src: transcript, tier 5, 2026-11-17
- conf: single-source; unique-chance targets are [INFERRED] from ASR text and unverified → check [[items/uniques-index]] / PoE2DB
- notes: Exceptional items in [[items/rarity]] (extra augment socket or >20% quality).


## Disenchanting (league start only)
@ v=0.5.x vol=volatile conf=single-source date=2026-11-17
Superior flasks → Glassblower's Bauble; superior armour → Armourer's Scrap; superior weapons → Blacksmith's Whetstone; uniques → Chance Shards. Only worth it on day 1–2 of a league, except unique → Chance Shard stays useful.
- src: transcript, tier 5, 2026-11-17
- notes: David's 2026-11-17 poe.ninja snapshot shows these craft items priced at several exalts each late in a league (Forbidden Rites) → [[economy/price-snapshot-2026-11-17]], [[strategy/league-lifecycle-pricing]]; at 1.0 start expect the reverse.
