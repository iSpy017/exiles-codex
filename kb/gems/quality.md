---
title: Gem Quality
status: done
tracker_topic: "Quality & alternate qualities"
tracker_note: "done (0.5.x; alt gem quality not obtainable — Secondary Regrading Lens 'Not in game')"
defaults: v=0.5.x
---

Version: 0.5.x (researched 2026-11-17; updated batch 29, 2026-11-26). Re-check at 1.0.
Status: done for 0.5.x — alternate gem quality checked against the PoE2DB crawl.

## Quality basics
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Gemcutter's Prism raises a skill gem's quality, max 20%. Since 0.1.0c each prism adds +5% (so 4 prisms = 20%); before that it was +1%. Each gem's quality bonus is specific to that gem ("Additional Effects From 1–20% Quality").
- src: poe2wiki Gemcutter's Prism [S620], poe2wiki Quality [S717], tier 2; PoE2DB Quality [S110], tier 2; Mobalytics Level 21 guide [S075] (4 prisms per gem), tier 3; retrieved 2026-11-17
- notes: PoE1 sources say +1% per prism — don't confuse. Prism price spike late league: [[strategy/league-lifecycle-pricing]] (~26.5 ex, Forbidden Rites, 2026-11-17).


## Gemcutter's Prism details
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
The prism only works on skill gems (no support-gem option in its text). Drop level 12; Currency Exchange gold cost 1,000.
- src: poe2db:Gemcutters_Prism «PoE2DB Gemcutter's Prism», tier 2, crawl 2026-11-23
- notes: the same page shows an economy widget (1 Divine ≈ 34.2 prisms at crawl time) but names no league — not used as a price. Dated league prices → [[economy/price-snapshot-2026-11-17]].


## One quality bonus per skill (no quality choice)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Every skill gem page in the crawl shows a single quality-bonus block per skill or sub-skill; gems with two or three blocks have one per stat set (e.g. Hailstorm Rounds), not a choice between types. PoE2DB's Quality page says skills from gems or gear get their own skill-specific bonus, default max 20%.

- src: poe2db:Ice_Shot, poe2db:Rolling_Slam, poe2db:Quality, tier 2, crawl 2026-11-23 (428 pages carry a quality block)
- conf: single-source; "one block per stat set" reading [INFERRED] from block placement

## Corruption and quality
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17 fill=vol
Add quality (and sockets) before corrupting; you can't add quality to a corrupted gem.

- src: Mobalytics High Level Gems [S070], tier 3; Maxroll Corruption outcomes [S039], tier 3; retrieved 2026-11-17

## Support gem quality
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Support gem pages in the crawl show no quality bonus. Exceptions that touch quality: Dialla's Desire (lineage) gives supported skills +5% quality; Gemling Legionnaire ascendancy nodes add skill quality and (Advanced Thaumaturgy) give socketed skills an extra quality effect.

- src: poe2db:Diallas_Desire «PoE2DB Dialla's Desire», poe2db:Skill_Gem_Quality, tier 2, crawl 2026-11-23
- conf: single-source (absence in a scan, not proof)

## Alternate qualities — not obtainable in 0.5.x
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
No alternate gem quality can be obtained in 0.5.x. Secondary Regrading Lens exists in game data (would reroll the quality type of a support gem with quality) but PoE2DB marks its acquisition "Not in game", with no price or drop source. No Prime Regrading Lens page exists in the crawl (the RePoE data entry is unconfirmed). The only "alternate quality" in the 0.5.0 notes is Breach catalyst quality on jewellery ([[crafting/catalysts]]).
- src: poe2db:Secondary_Regrading_Lens, poe2db:Version_0.5.0, tier 2, crawl 2026-11-23; RePoE base_items.json (lens entries), tier 2
- vol: may-change (watch the 1.0 notes)
- conf: single-source (game-data page + absence)
- notes: resolves the open conflict "Do alternate gem quality types exist?" for 0.5.x → [[conflicts]]. New minor conflict logged: the lens text targets "a support gem with quality" while support gems show no quality effect.
