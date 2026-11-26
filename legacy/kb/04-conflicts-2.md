# Source Conflicts — part 2 (batches 23–37, from 2026-11-26)

Continues [[04-conflicts]] (same format). Part 1 holds everything up to batch 22. Status updates to part-1 entries are listed at the end.

## Lightning Rod chain count
- Doc: kb/gems/bow-attack-gems.md
- Source A: [PoE2DB Lightning Rod](https://poe2db.tw/us/Lightning_Rod) skill description, tier 2, crawl 2026-11-23 — chains 6 times
- Source B: same page, stat/level table, tier 2 — 8 chains
- Status: open. Probably description vs stat-line drift. Check the tooltip in game.

## Ice Shot shard damage
- Doc: kb/gems/bow-attack-gems.md
- Source A: [PoE2DB Ice Shot](https://poe2db.tw/us/Ice_Shot) level table, tier 2 — shard damage scales 178–344% across levels
- Source B: same page, shard sub-skill text — 100% of base damage
- Status: open. May be two different multipliers (attack damage vs shard sub-skill). Check in game.

## Total unique count: 441 or 448
- Doc: kb/items/uniques-index.md, kb/items/uniques-drop-sources.md
- Source A: kb/items/uniques-index.md (poe2wiki / earlier count, 0.5.5.9) — 441
- Source B: [PoE2DB Unique item](https://poe2db.tw/us/Unique_item) section headers, crawl 2026-11-23 — Weapon 88 + Armour 221 + Other 139 = 448 (plus 48 Cultivated)
- Status: open. Difference may be placeholder/disabled entries or variants. Not material for play.

## Zarokh, the Temporal — what he drops
- Doc: kb/items/uniques-drop-sources.md, kb/endgame/sekhemas.md
- Source A: item pages (Temporalis, Sandstorm Visage, Eshtera's Path, Zaida's Longevity, Safrin's Resolve, Against the Darkness, Grand Spectrum, five relics) — tagged 「Zarokh, the Temporal」Dropped by
- Source B: [PoE2DB Zarokh](https://poe2db.tw/us/Zarokh_2C_the_Temporal) Drops list — only six relics; uniques come from a "challenge run" relic mapping (e.g. Last Flame → Temporalis)
- Source C: [PoE2DB The Burden of Leadership](https://poe2db.tw/us/The_Burden_of_Leadership) relic text — Zarokh drops Sekhema's Resolve (relic-conditional)
- Status: open. Reading B/C (relic decides the unique) fits the challenge-run mechanic; A may be a flattened tag. Check in game. All tier 2, crawl 2026-11-23.

## The Aberration and Vessel of Kulemak drop lists
- Doc: kb/items/uniques-drop-sources.md
- Source A: item pages — Eyes of the Runefather / The Unleashed tagged Aberration; Darkness Enthroned / Undying Hate tagged Abyss
- Source B: boss pages' Drops lists — Aberration lists ores labelled with those uniques plus Olroth's Conviction; Vessel lists Darkness Enthroned, Undying Hate, Tecrod's Revenge among others
- Status: open. Likely ore-linked or encounter-linked drops rather than direct ones. PoE2DB, tier 2, crawl 2026-11-23.

## Light-stun floor: 15% or 10%
- Doc: kb/mechanics/stun.md
- Source A: [PoE2DB Stun](https://poe2db.tw/us/Stun) / Keywords light-stun text, tier 2 — chances below 15% count as 0
- Source B: [PoE2DB Keywords](https://poe2db.tw/us/Keywords) player stun-threshold text, tier 2 — chances below 10% count as 0
- Status: open. May be enemy-side vs player-side values (same page, different entries). Check in game.

## Secondary Regrading Lens target vs support gem quality
- Doc: kb/gems/quality.md
- Source A: [PoE2DB Secondary Regrading Lens](https://poe2db.tw/us/Secondary_Regrading_Lens), tier 2 — rerolls the quality type of "a support gem with quality"
- Source B: support gem pages in the same crawl, tier 2 — no support gem shows any quality effect
- Status: open, low impact (the lens is marked "Not in game"). Check at 1.0.

## Druid: transform while spells are active?
- Doc: kb/mechanics/shapeshifting.md
- Source A: [PoE2DB Druid](https://poe2db.tw/us/Druid) class page, Exilecon 2023 blurb — transform into a bear while your spells are active
- Source B: [PoE2DB Keywords](https://poe2db.tw/us/Keywords) Shapeshifting/Talismans entries, tier 2 — using a skill not compatible with the form returns you to human form; a Talisman forces its form
- Status: open, leaning B (A reads as old design text). Check in game.

## What makes you shapeshift: the skill or the Talisman
- Doc: kb/mechanics/shapeshifting.md
- Source A: [PoE2DB Keywords](https://poe2db.tw/us/Keywords) Shapeshifting entry — using a form skill shapeshifts you
- Source B: same page, Talismans entry; [PoE2DB Talismans](https://poe2db.tw/us/Talismans) — having a Talisman in the active weapon set puts you in its form
- Status: open; may both be true (two triggers). Check in game.

## "Deferred" unique variants on PoE2DB list pages (pending b35 inspection)
- Doc: kb/items/uniques-mods-* (armour)
- Source A: PoE2DB armour unique list — a "Deferred" variant with different base, level and mods for 10 uniques (Edyrn's Tusks, The Fallen Formation, Apron of Emiran, Radiant Grief, Alpha's Howl, Deathblow, Blueflame Bracers, Kaom's Roots, Beetlebite, Redblade Banner)
- Source B: the 0.5.5 block on the same pages — current values (used in the docs)
- Status: open. Unclear which is live in 0.5.x. Recheck at 1.0.

## Keelhaul values: 0.5.5 block vs summary block
- Doc: kb/items/uniques-mods-jewellery-4.md
- Source A: [PoE2DB Keelhaul](https://poe2db.tw/us/Keelhaul) 0.5.5 block, tier 2 — 20–30% increased mana recovery from flasks, flask life/mana recovery rate −25 to +25%, flasks gain 0.25 charges/s
- Source B: same page, summary block (headed Deferred) — Geyser skill, 38% mana recovery, 50% reduced flask recovery, 1.7/1.72 charges
- Status: open; doc uses A. Recheck at 1.0.

## Minion resistances: display vs data block
- Doc: kb/gems/minion-stats.md, kb/mechanics/minions.md
- Source A: PoE2DB gem-page minion blocks (display), tier 2 — 50% on one element for Skeletal Arsonist (fire), Frost Mage (cold), Storm Mage (lightning), Infernal Hound (fire)
- Source B: the PoB-format data block on the same pages — all resistances 0
- Status: open. Check a minion's resistances in game.

## Which Monster Stats column feeds player minions
- Doc: kb/gems/minion-stats-2.md
- Source A: [PoE2DB Monster](https://poe2db.tw/us/Monster) "Minion Life" / "Minion Damage" columns — the minion blocks' "Minion Life" values match these × Life %
- Source B: same blocks also show plain "Life" (e.g. Warrior L68 7,266 vs Minion Life 6,098), and basic-attack ranges follow the plain "Damage" column
- Status: open. Docs assume "Minion Life" for life [INFERRED]; damage column unclear. Check minion life in game at a known level.

## Idol socket slots vs effect text
- Doc: kb/items/soul-core-idol-effects-2.md, -3.md
- Source A: [PoE2DB Idol of Grold](https://poe2db.tw/us/Idol_of_Grold) effect lines — Boots effect; [Idol of the Martyr](https://poe2db.tw/us/Idol_of_the_Martyr) / Pharisee / Sycophant — Sceptre effect lines
- Source B: same pages' "socket into" text — Grold: Gloves or a Sceptre; Martyr/Pharisee/Sycophant: a Weapon
- Status: open. Check in game which slot accepts them.

## Rune of Confrontation Bonded value
- Doc: kb/items/rune-effects-5.md
- Source: [PoE2DB Rune of Confrontation](https://poe2db.tw/us/Rune_of_Confrontation) — Bonded line is an unfilled internal placeholder ("rage effect +% [10]")
- Status: open (no second source). Value unknown until seen in game.

## Xesht resistances
- Doc: kb/endgame/breach.md, kb/endgame/pinnacle-bosses-2.md
- Source A: [PoE2DB Xesht](https://poe2db.tw/us/Xesht_2C_We_That_Are_One) main stat table — 15/15/15/0
- Source B: same page, later blocks and the Twisted Domain map row — 30/30/30/0
- Status: open. Check in game.

## Delirium pinnacle: Kosis or the Raven Trickster
- Doc: kb/endgame/delirium.md, kb/endgame/pinnacle-bosses.md
- Source A: [PoE2DB Delirium](https://poe2db.tw/us/Delirium) — "Simulacrum Encounter, Kosis" listed as pinnacle
- Source B: [PoE2DB The Withered Willow](https://poe2db.tw/us/The_Withered_Willow) — tagged pinnacle_boss area with the Raven Trickster (Raven's Reflection key)
- Status: open; likely two separate endgame bosses. Check at 1.0.

## Atziri's Temple beacon locations
- Doc: kb/endgame/vaal-temple.md
- Source A: [PoE2DB Ancient Beacons](https://poe2db.tw/us/Ancient_Beacons) quest — beacons in Acts 1, 2, 3
- Source B: [PoE2DB Version 0.5.0](https://poe2db.tw/us/Version_0.5.0) — first 6 in Act 3, second 6 in the Interludes
- Status: open; moot after 1.0 removes Interludes. Check at 1.0.

## Sekhemas floor 2 boss
- Doc: kb/endgame/sekhemas.md, sekhemas-2.md
- Source A: [PoE2DB Trial of the Sekhemas](https://poe2db.tw/us/Trial_of_the_Sekhemas) — Test of Will boss Terracotta Sentinels
- Source B: Act 2 area data on the same site — Rafiq of the Frozen Spring and Hadi of the Flaming River for floor 2
- Status: open. Check in game.

## Map death rule
- Doc: kb/endgame/atlas.md
- Source A: old intro text on [PoE2DB Waystone](https://poe2db.tw/us/Waystone) — dying removes access to the map
- Source B: [PoE2DB Revival Availability](https://poe2db.tw/us/Revival_Availability) — limited revivals per map, fewer with more waystone mods
- Status: open, leaning B (newer system). Check in game.

## Status updates to part-1 entries
- **Essence of Ice effect** — resolved by game data (batch 24, 2026-11-26) in favour of B: PoE2DB pages for all four Ice tiers give added cold damage on weapons (Perfect: % of damage as extra cold); spell crit belongs to Essence of Seeking. → [[crafting/essences]]
- **Do alternate gem quality types exist?** — resolved for 0.5.x (batch 29, 2026-11-26): not obtainable. Secondary Regrading Lens is "Not in game" on PoE2DB; no Prime lens page exists. Recheck at 1.0. → [[gems/quality]]
- **Quality added per quality currency** — still resolved toward B (direction); the PoE2DB crawl has no per-use amounts (batch 27). A tier-5 lead says ~3% per Armourer's Scrap (unverified).
