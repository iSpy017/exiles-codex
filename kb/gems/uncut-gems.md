---
title: Uncut Skill, Spirit & Support Gems
status: done
tracker_topic: "Uncut skill / spirit / support gems"
tracker_note: "done (0.5.5.9; recheck 1.0)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 (base_items.json + skill_gems.json, RePoE) + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.

## Three kinds
@ v=0.5.5.9 vol=? conf=confirmed date=2026-11-17 missing=vol
- Uncut Skill Gem — engraves an active skill gem, or levels one up.
- Uncut Spirit Gem — engraves a persistent skill gem (buff/aura/herald/permanent minion/meta), or levels one up.
- Uncut Support Gem — engraves a support gem.

- src: RePoE poe2 base_items.json [S002] item descriptions, tier 2; poe2wiki Uncut gem [S729], tier 2; Mobalytics Skill Gem System [S086], tier 3; retrieved 2026-11-17

## Levels and drop levels (game data)
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
- Uncut Skill Gem: levels 1–20. Item drop level: L1 1 · L2 4 · L3 7 · L4 11 · L5 15 · L6 19 · L7 23 · L8 27 · L9 32 · L10 37 · L11 42 · L12 47 · L13 53 · L14 59 · L15–20 62.
- Uncut Spirit Gem: levels 4–20 only (lowest is 4). Same drop levels as skill gems from L4 up (L4 11 … L14 59, L15–20 62).
- Uncut Support Gem: levels 1–5. Drop level: L1 1 · L2 16 · L3 33 · L4 45 · L5 55.
- src: RePoE poe2 base_items.json [S002], tier 2; poe2wiki Uncut gem [S729] (spirit lowest 4, drop level breakpoints exist, area level 40 normal monster → L10), tier 2; retrieved 2026-11-17
- conf: confirmed (spirit min L4); single-source (full drop table)
- notes: wiki says from drop level 62+ several uncut tiers can drop — so L15–20 all share drop level 62. Earlier patches used fewer fixed levels (poedb old text: skill 1/3/5/7/9/11/13, support 1/2/3, buff 4/8/12) — superseded.


## Gem tiers gate what you can engrave
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Every cuttable gem has a tier; you need an uncut gem of at least that level to engrave it (e.g. a tier-7 skill needs a L7+ uncut). Same rule for upgrading.

- src: Poe-Vault Gems Guide [S661], tier 3; game data skill_gems.json `crafting_level` matches wiki tiers (Sniper's Mark 7, Fork 3, Pierce III 5), tier 2; retrieved 2026-11-17

## Active-skill tiers (game data counts, cuttable gems only)
@ v=0.5.5.9 vol=? conf=confirmed date=2026-11-17 missing=vol
- Tier 1: 33 · 3: 30 · 4: 24 · 5: 31 · 7: 29 · 8: 15 · 9: 24 · 11: 22 · 13: 24 · 14: 13. (Tiers 2/6/10/12 unused.)
- Spirit/persistent gems sit at tiers 4, 8 and 14 (plus a few minion/meta exceptions), e.g. heralds and Arctic Armour 4; Blink, Defiance Banner 8; Archmage, Berserk, Trinity, Cast on Critical 14.
- src: RePoE skill_gems.json, tier 2; poe2wiki Engraving [S614] (persistent tiers IV/VIII/XIV), tier 2; retrieved 2026-11-17
- conf: confirmed (persistent tiers 4/8/14)
- notes: means L4 spirit uncut = first heralds; L8 = second tier; L14 = top persistents. Data includes some "Coming Soon"/[DNT] placeholders — ignored.


## Where gems come from
@ v=0.5.5.9 vol=? conf=? date=2026-11-17 fill=v missing=vol,conf
- Uncut gems drop from monsters (level set by area) and quest rewards. Lineage supports can't be engraved — see [[gems/lineage-supports]].
- src: Poe-Vault Gems Guide [S661], tier 3; poe2wiki Lineage [S699], tier 2.


## Price lesson
- See [[strategy/league-lifecycle-pricing]]: low-level uncut spirit gems spike late-league.
