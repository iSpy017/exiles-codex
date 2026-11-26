# Uber / Quest vs Farm Versions of Pinnacle Bosses

Status: partial. 0.5.x corpus shows no separate "uber" tier; it shows Quest vs Infinite Farm versions. Differences in stats between the two not found.
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against 1.0.
Sources: PoE2DB patch-note pages 0.3.0, 0.5.0, 0.5.1, 0.5.5, plus key-item pages (tier 2).

## Uber ladder (history)
- Claim: 0.3.0 added an Uber version of The Arbiter of Ash, gated by Primary, Secondary and Tertiary Calamity Fragments dropped by Citadel bosses once the Boss atlas tree was maxed (so Citadels sat at highest difficulty). 0.5.0 removed that path: Calamity Fragments can no longer be obtained, and existing ones were converted: Primary to Ancient Crisis, Secondary to Faded Crisis, Tertiary to Weathered Crisis Fragment.
- Version: 0.5.x (history from 0.3.0)
- Volatility: may-change
- Source: [PoE2DB 0.3.0 notes](https://poe2db.tw/us/Version_0.3.0), [0.5.0 notes](https://poe2db.tw/us/Version_0.5.0), [Pinnacle Keys](https://poe2db.tw/us/Pinnacle_Keys), tier 2, crawl 2026-11-23
- Confidence: confirmed (0.3.0 + 0.5.0 + item pages agree)
- Notes: Calamity Fragment pages still exist in the corpus (Primary/Secondary/Tertiary, internal ids PinnacleKeyUber1-3) as legacy items. `atlas-dependent` (historical unlock needed a maxed boss atlas tree).

## Quest version vs Infinite Farm version
- Claim: 0.5.0: every pinnacle boss has a Quest version (deterministic access via the endgame quest chain) and an Infinite Farm version (repeatable, non-quest, described as the greater challenge). Crisis Fragments exist in separate Quest Item and tradeable Pinnacle Key variants (internal ids "...Quest" vs plain), so each fragment exists as quest-flagged and farmable. Quest fragments are given by Count Geonor and Doryani in the Western and Eastern Enigma Chambers (0.5.5c).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB 0.5.0 notes](https://poe2db.tw/us/Version_0.5.0), [Ancient Crisis Fragment](https://poe2db.tw/us/Ancient_Crisis_Fragment), [0.5.5c notes](https://poe2db.tw/us/Version_0.5.5c), [Western Enigma Chamber](https://poe2db.tw/us/Western_Enigma_Chamber), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Which areas are the Infinite Farm versions vs the quest versions on the map pages is not labelled; the pinnacle area pages carry "map is quest area". `atlas-dependent`.

## What differs between the versions (known)
- Claim: (1) Origin Core: killing Arbiter of Divinity with the non-quest core completes the entire Precursor Fortress for the map owner (atlas tree unlock); the quest core no longer completes a section (0.5.5). (2) Monster levels of the six pinnacle areas could be set to 82 before the quest kill was done (0.5.1 fix), so level is tied to quest status. (3) Pinnacle unique drops are allocated to the map owner (0.5.2). (4) Non-quest keys are tradeable on the Currency Exchange (0.5.1 fix mentions tradeable Call of the Shadows and Origin fragments).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB 0.5.5 notes](https://poe2db.tw/us/Version_0.5.5), [0.5.1 notes](https://poe2db.tw/us/Version_0.5.1), [0.5.2 notes](https://poe2db.tw/us/Version_0.5.2), tier 2, crawl 2026-11-23
- Confidence: single-source per point
- Notes: [INFERRED] the farm version runs at monster level 82 (see [[endgame/pinnacle-bosses]]); no explicit stat table for the farm version exists in the corpus, and the PoE2DB area rows (74 / 79) are the quest-area levels.

## "Uber" in internal ids
- Claim: Area ids use the prefix MapUberBoss for the pinnacle maps and the Citadels (e.g. MapUberBoss_Monolith, MapUberBoss_StoneCitadel, MapUberBoss_IronCitadel_Quest); this is an internal id prefix, not a difficulty tier.
- Version: 0.5.x
- Volatility: stable
- Source: [PoE2DB The Burning Monolith](https://poe2db.tw/us/The_Burning_Monolith), [Eastern Enigma Chamber](https://poe2db.tw/us/Eastern_Enigma_Chamber), tier 2, crawl 2026-11-23
- Confidence: confirmed (several pages)
- Notes: Citadel second-phase bosses (Geonor the Putrid Wolf, Doryani's Triumph) are listed on the Citadel pages with higher life than their first forms, e.g. Count Geonor 2,675,628 vs Putrid Wolf 4,135,062 at area 80.

## Atlas difficulty and points
- Claim: Arbiter of Divinity kills (5) can substitute for fortress-map completion to gain atlas tree points (0.5.0 note). PoE2DB marks some Kosis drops "(Difficulty 2+)" and "(Difficulty 4)", and 0.5.1 fixed Kulemak granting atlas credit per difficulty increase; the difficulty scale is not explained in the corpus.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB EndGame](https://poe2db.tw/us/EndGame), [0.5.1 notes](https://poe2db.tw/us/Version_0.5.1), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: `atlas-dependent`. No atlas passive content written here.
