# Breach (endgame league mechanic, Keepers of the Flame content)

Status: done for encounter flow, rewards, bosses and uniques as listed by PoE2DB; partial on exact Genesis Tree crafting outputs and on Xesht phase mechanics (skill names only, no fight guide). No atlas passive tree content by design.
Version: 0.5.x only. Nothing here is verified for the later full release.
Sources: PoE2DB corpus crawl 2026-11-23 (Breach, Breachstone, boss pages, item pages), tier 2.

## Encounter types
- Claim: Unstable Breach = small tear that stays open longer when you kill Breach monsters; a progress bar shows time left and how much kills extend it. At 100% it becomes Stabilised and spawns a harder challenge at the start point (boss Vruun can appear there). Breach Hive = grown-out tear that needs Ailith; you burn through Hive walls (each wall destroyed adds monsters), then defend Ailith while she destroys the centre. If Ailith dies the Hive stays.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Breach](https://poe2db.tw/us/Breach), tier 2, crawl 2026-11-23 (lines 291-298 item text; lines 1221-1240 league notes)
- Confidence: single-source
- Notes: Sky Hives (multi-wave defend-Ailith encounter) and Fortresses (boss pair Tul and Esh) sit inside Breach domains reached with a Breachstone. Domain access is atlas-dependent. Clasped Hands on the floor open and drop extra items when run over.

## Breach Tablet (decision row)
- Claim: Breach Tablet adds one Breach to a map, 10 uses. Drop level 65. Unique tablet "Wraeclast Besieged" trades -10 to 20% pack size for 2-5 more Hive waves, +120 s collapse timer and 2-5 extra rares on stabilise.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Breach](https://poe2db.tw/us/Breach), [PoE2DB Breach Tablet](https://poe2db.tw/us/Breach_Tablet), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: tag atlas-dependent (map/tablet slots). Tablet suffix pool (pack size, Wombgift/Hiveblood quantity, Vruun chance, splinter quantity) is listed on the Breach page Tower mods table; not copied here.

## Currency and drops from Breach
| Item | What it is for | Source line |
|---|---|---|
| Breach Splinter | Stack 300. 300 combine into a Revelatory Wombgift, which grows into a Breachstone on the Genesis Tree (Revelatory Wombgift page: drop level 80) | Breach_Splinter.txt, Revelatory_Wombgift.txt |
| Hiveblood | Resource spent to grow Wombgifts at the Genesis Tree in the Monastery of the Keepers; cap 100,000 | Hiveblood.txt |
| Wombgifts (4 types: Lavish, Ornate, Banded, Signet) | Grow into Currency, Amulet, Belt, Ring respectively (Wombgifts.txt lines 12-20); the separate Revelatory Wombgift (from 300 splinters) grows into a Breachstone | Wombgifts.txt, Revelatory_Wombgift.txt |
| Catalysts (12 types, counted at Breach.txt lines 314-414: Flesh, Neural, Carapace, Uul-Netol's, Xoph's, Tul's, Esh's, Chayula's, Reaver, Sibilant, Skittering, Adaptive) | Quality on ring/amulet that boosts one mod family; stack 20 | Breach.txt lines 314-414 |
| Refined catalysts (jewel versions) | Same families, quality on jewels (e.g. Refined Sibilant = Caster mods on a jewel) | Refined_Sibilant_Catalyst.txt |
| Essence of the Breach | Corrupting essence: removes a mod, adds guaranteed +20% max quality on jewellery | Essence_of_the_Breach.txt |
| Breach Ring | Ring base, level 40, comes with +20% maximum quality; catalysts can take quality up to 50% | Breach_Ring.txt, Breach.txt line 1241 |
- Claim (above table): Catalysts no longer drop from monsters; the Genesis Tree is the only source. Genesis Tree makes 6 ring, 4 amulet and 4 belt bases exclusive to it, plus caster/minion mods on rings and belts.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Breach](https://poe2db.tw/us/Breach), tier 2, crawl 2026-11-23 (lines 1226-1232)
- Confidence: single-source
- Notes: prices change daily; see [PoE2DB Economy Breach](https://poe2db.tw/us/Economy_Breach) (crawl 2026-11-23; the unit/direction of its value column is ambiguous, so no price is recorded here). Wombgift quantity and Genesis passive points are atlas-dependent.

## Breachstones (keys to the Twisted Domain)
- Claim: Breachstone variants exist for five gods (Xoph, Tul, Esh, Uul-Netol, Chayula) in tiers base, Charged, Enriched, Pure, Flawless. Every base-tier stone gives rare monsters one extra reward type, +2 area modifiers and 100% increased XP (150% Uul-Netol, 200% Chayula). Charged adds 20% rarity and pack size, Enriched 40%, Pure 60%. Flawless: rare monsters drop 2 extra reward types, +4 area modifiers, 250% more monster life, 60% rarity and pack size, monster level 84.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Breachstone](https://poe2db.tw/us/Breachstone), tier 2, crawl 2026-11-23 (lines 12-181)
- Confidence: single-source
- Notes: monster level by tier varies by god (e.g. base Xoph 81, base Chayula 83, Charged Xoph 74, Flawless all 84). Use in a personal map device; single use (Chayula Flawless page). Which atlas domain a stone opens is atlas-dependent.

## Boss: Xesht, We That Are One (Breach pinnacle)
- Claim: Location Twisted Domain (boss rush area 3), boss tier 3. Level 79 base stats: 357,869 life, 17,893 energy shield, 4,540 armour, 887 evasion, 973 damage, basic attack 778-1167. Life multiplier 1440%. Resistance block reads 15/15/15/0 in the main table and 30/30/30/0 in later "Reservation" blocks. Skills named on page include hand slam, flick projectiles, head fireball, hand clap blast, summon Esh / Tul / both, open portals, teleport.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Xesht, We That Are One](https://poe2db.tw/us/Xesht%2C_We_That_Are_One), tier 2, crawl 2026-11-23 (lines 197-300)
- Confidence: single-source
- Notes: PoE2DB values exclude map/atlas bonuses; difficulty tiers raise it (devs mention difficulty four; thresholds not in sources). Resistance conflict logged in report.

## Boss: Vruun, Marshal of Xesht (Stabilised Breach boss)
- Claim: Tier 2 boss, level 68 base: 18,578 life, 2,413 armour, 708 evasion, 641 damage, attacks 513-769. Skills: combo attack, finger projectiles, warcry (15 s cooldown), ground slam (12 s, cannot be dodged/evaded/blocked), leap slam (10 s).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Vruun](https://poe2db.tw/us/Vruun%2C_Marshal_of_Xesht), tier 2, crawl 2026-11-23 (lines 59-78, 165-181)
- Confidence: single-source
- Notes: appears in Unstable Breaches after stabilising; chance raised by tablet suffix (20-50%) and atlas nodes (atlas-dependent). Tied lineage supports (unconfirmed drop): Vruun's Aftermath, Vruun's Inevitability. [INFERRED]: they are Vruun drops because of their names and the "50% increased chance to drop Lineage Supports" node text.

## Boss: It That Was Tul / It That Was Esh (Fortress pair)
- Claim: Both level 65, tier 3, 24,581 life (life multiplier 375%), 637 damage. Tul: 3,237 armour, shield throw, ground slam, shield stab. Esh: 2,458 energy shield, 2,023 armour, chaos/lightning projectiles, death beam, spider dash.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB It That Was Tul](https://poe2db.tw/us/It_That_Was_Tul), [PoE2DB It That Was Esh](https://poe2db.tw/us/It_That_Was_Esh), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: arena "Hive Colony". Killing both gives the key to the Breach pinnacle.

## Key to the pinnacle
- Claim: Defeating Tul and Esh grants the key to the existing pinnacle boss. The key item is the Breachlord Sac (Map Fragment, Currency Exchange 1500 gold), which is handed in to the Dreamer in the Monastery of the Keepers. Xesht is then reached via a Breachstone to the Twisted Domain.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Breach](https://poe2db.tw/us/Breach) line 1238, [PoE2DB Breachlord Sac](https://poe2db.tw/us/Breachlord_Sac), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: [INFERRED]: Sac = Tul/Esh key. Page says Sac is the pinnacle key (class "BreachPinnacleKey") and the quest "Keepers of the Flame" also gives one; the exact link to the Tul/Esh kill is from the league note only.

## Unique drops tied to Breach
- Claim: Xesht page lists 7 uniques: Beyond Reach (quiver), Choir of the Storm (amulet), Controlled Metamorphosis (jewel), Hand of Wisdom and Action (gloves), Skin of the Loyal (body), The Pandemonius (amulet), Xoph's Blood (amulet). Breach tablet unique: Wraeclast Besieged. Another listed unique: Nightfall (Glacial Fortress base).
- Version: 0.5.x
- Volatility: stable
- Source: [PoE2DB Xesht](https://poe2db.tw/us/Xesht%2C_We_That_Are_One), [PoE2DB Breach](https://poe2db.tw/us/Breach), tier 2, crawl 2026-11-23
- Confidence: confirmed (both pages list them)
- Notes: full mods on those pages; see [[items/uniques-mods-jewellery-1]] if covered. The Breach page's "Breach Unique /2" header holds Nightfall and Wraeclast Besieged.
