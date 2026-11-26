# Gem Quality

Version: 0.5.x (researched 2026-11-17; updated batch 29, 2026-11-26). Re-check at 1.0.
Status: done for 0.5.x — alternate gem quality checked against the PoE2DB crawl.

## Quality basics
- Claim: Gemcutter's Prism raises a skill gem's quality, max 20%. Since 0.1.0c each prism adds +5% (so 4 prisms = 20%); before that it was +1%. Each gem's quality bonus is specific to that gem ("Additional Effects From 1–20% Quality").
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Gemcutter's Prism](https://poe2wiki.net/wiki/Gemcutter%27s_Prism), [poe2wiki Quality](https://www.poe2wiki.net/wiki/Quality), tier 2; [PoE2DB Quality](https://poe2db.tw/Quality), tier 2; [Mobalytics Level 21 guide](https://mobalytics.gg/poe-2/guides/level-21-skill-gems-guide-by-ignatius) (4 prisms per gem), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: PoE1 sources say +1% per prism — don't confuse. Prism price spike late league: [[strategy/league-lifecycle-pricing]] (~26.5 ex, Forbidden Rites, 2026-11-17).

## Gemcutter's Prism details
- Claim: The prism only works on skill gems (no support-gem option in its text). Drop level 12; Currency Exchange gold cost 1,000.
- Version: 0.5.x · Volatility: may-change
- Source: [PoE2DB Gemcutter's Prism](https://poe2db.tw/us/Gemcutters_Prism), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: the same page shows an economy widget (1 Divine ≈ 34.2 prisms at crawl time) but names no league — not used as a price. Dated league prices → [[economy/price-snapshot-2026-11-17]].

## One quality bonus per skill (no quality choice)
- Claim: Every skill gem page in the crawl shows a single quality-bonus block per skill or sub-skill; gems with two or three blocks have one per stat set (e.g. Hailstorm Rounds), not a choice between types. PoE2DB's Quality page says skills from gems or gear get their own skill-specific bonus, default max 20%.
- Version: 0.5.x · Volatility: may-change
- Source: [PoE2DB Ice Shot](https://poe2db.tw/us/Ice_Shot), [PoE2DB Rolling Slam](https://poe2db.tw/us/Rolling_Slam), [PoE2DB Quality](https://poe2db.tw/us/Quality), tier 2, crawl 2026-11-23 (428 pages carry a quality block)
- Confidence: single-source; "one block per stat set" reading [INFERRED] from block placement

## Corruption and quality
- Claim: Add quality (and sockets) before corrupting; you can't add quality to a corrupted gem.
- Version: 0.5.x
- Source: [Mobalytics High Level Gems](https://mobalytics.gg/poe-2/guides/high-level-gems), tier 3; [Maxroll Corruption outcomes](https://maxroll.gg/poe2/resources/corruption-outcomes), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Support gem quality
- Claim: Support gem pages in the crawl show no quality bonus. Exceptions that touch quality: Dialla's Desire (lineage) gives supported skills +5% quality; Gemling Legionnaire ascendancy nodes add skill quality and (Advanced Thaumaturgy) give socketed skills an extra quality effect.
- Version: 0.5.x · Volatility: may-change
- Source: [PoE2DB Dialla's Desire](https://poe2db.tw/us/Diallas_Desire), [PoE2DB Skill Gem Quality](https://poe2db.tw/us/Skill_Gem_Quality), tier 2, crawl 2026-11-23
- Confidence: single-source (absence in a scan, not proof)

## Alternate qualities — not obtainable in 0.5.x
- Claim: No alternate gem quality can be obtained in 0.5.x. Secondary Regrading Lens exists in game data (would reroll the quality type of a support gem with quality) but PoE2DB marks its acquisition "Not in game", with no price or drop source. No Prime Regrading Lens page exists in the crawl (the RePoE data entry is unconfirmed). The only "alternate quality" in the 0.5.0 notes is Breach catalyst quality on jewellery ([[crafting/catalysts]]).
- Version: 0.5.x · Volatility: may-change (watch the 1.0 notes)
- Source: [PoE2DB Secondary Regrading Lens](https://poe2db.tw/us/Secondary_Regrading_Lens), [PoE2DB Version 0.5.0](https://poe2db.tw/us/Version_0.5.0), tier 2, crawl 2026-11-23; RePoE base_items.json (lens entries), tier 2
- Confidence: single-source (game-data page + absence)
- Notes: resolves the open conflict "Do alternate gem quality types exist?" for 0.5.x → [[04-conflicts]]. New minor conflict logged: the lens text targets "a support gem with quality" while support gems show no quality effect.
