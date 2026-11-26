---
title: Socketing & Gem Slot Limits
status: done
tracker_topic: "Socketing & gem slot limits"
tracker_note: "done (0.5.x; Jeweller's resolved, 1 conflict open)"
defaults: v=0.5.x
---

Version: 0.5.x (researched 2026-11-17). Re-check at 1.0.

## Skill gem slots
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Characters have 9 skill gem slots by default; some classes/ascendancies (e.g. Gemling Legionnaire) add more.
- src: PoE2DB early-access notes [S120], tier 2; Deltia's Gaming skill gems guide, tier 5; retrieved 2026-11-17
- conf: single-source (tier 2) — verify current number in game
- notes: Unset Ring implicit grants +1 skill slot ([[bases-implicits]]).


## Support sockets per skill
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Each skill gem starts with 2 support sockets and can go up to 5. Lesser Jeweller's Orb sets a skill gem to 3 support sockets, Greater sets it to 4, Perfect sets it to 5 (each sets the count; it doesn't add one).
- src: RePoE poe2 base_items.json [S002] currency descriptions, tier 2 (game data), retrieved 2026-11-17; Mobalytics Skill Gem System [S086], tier 3 (2 → 5)
- conf: confirmed (game text)
- notes: Drop levels: Lesser 25, Greater 45, Perfect 65. Earlier conflict (Poe-Vault vs old PoE2DB text) resolved by game data — see [[conflicts]]. Item-granted skills get sockets by item/character level, not Jeweller's Orbs. Vaal Orb on a gem can also add a socket or remove one ([[corruption]]).


## Attribute cost of supports
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Each support socketed raises one attribute requirement of the skill by +5 (the support's colour).

- src: Mobalytics Skill Gem System [S086], tier 3; support entries show "Support Requirements: +5 Str/Dex/Int" on poe2wiki Lineage Supports [S700], tier 2; game keyword "Support Gem Requirements" (cumulative, generally +5 per support); retrieved 2026-11-17

## Duplicate rules
@ v=0.5.x vol=may-change conf=? date=2026-11-17 missing=conf
- Skills: since 0.3.0 you can't socket two copies of the same skill gem in your main skill slots (skills not from gems, and skills inside persistent/meta gems, don't count; spectres/beasts: one of each monster).
- Supports — category: you can't socket two supports of the same category in one skill.
- Supports — across skills: CONFLICT. Some poe2wiki pages say one copy of each support per character; poe2wiki's Spirit Gem version history says that restriction was removed ("use as many copies as you like"). → kb/04-conflicts.md.
- Lineage supports: one copy each per character (Solus Ipse bypasses). Gemling's Gem Studded passive also bypasses support-copy limits per poe2wiki.
- src: poe2wiki Spirit Gem [S724], poe2wiki Skill gem [S635], poe2wiki Gem [S619], poe2wiki Abyss lineage support [S664], tier 2; retrieved 2026-11-17
- v: 0.5.x, volatility may-change
