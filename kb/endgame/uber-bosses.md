---
title: Uber / Quest vs Farm Versions of Pinnacle Bosses
status: partial
tracker_topic: "Uber bosses"
tracker_note: "partial (0.5.x: no uber tier — quest vs farm versions; farm stats missing)"
defaults: v=0.5.x
---

Status: partial. 0.5.x corpus shows no separate "uber" tier; it shows Quest vs Infinite Farm versions. Differences in stats between the two not found.
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against 1.0.
Sources: PoE2DB patch-note pages 0.3.0, 0.5.0, 0.5.1, 0.5.5, plus key-item pages (tier 2).

## Uber ladder (history)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
0.3.0 added an Uber version of The Arbiter of Ash, gated by Primary, Secondary and Tertiary Calamity Fragments dropped by Citadel bosses once the Boss atlas tree was maxed (so Citadels sat at highest difficulty). 0.5.0 removed that path: Calamity Fragments can no longer be obtained, and existing ones were converted: Primary to Ancient Crisis, Secondary to Faded Crisis, Tertiary to Weathered Crisis Fragment.
- src: poe2db:Version_0.3.0 «PoE2DB 0.3.0 notes», poe2db:Version_0.5.0 «0.5.0 notes», poe2db:Pinnacle_Keys, tier 2, crawl 2026-11-23
- v: 0.5.x (history from 0.3.0)
- conf: confirmed (0.3.0 + 0.5.0 + item pages agree)
- notes: Calamity Fragment pages still exist in the corpus (Primary/Secondary/Tertiary, internal ids PinnacleKeyUber1-3) as legacy items. `atlas-dependent` (historical unlock needed a maxed boss atlas tree).


## Quest version vs Infinite Farm version
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
0.5.0: every pinnacle boss has a Quest version (deterministic access via the endgame quest chain) and an Infinite Farm version (repeatable, non-quest, described as the greater challenge). Crisis Fragments exist in separate Quest Item and tradeable Pinnacle Key variants (internal ids "...Quest" vs plain), so each fragment exists as quest-flagged and farmable. Quest fragments are given by Count Geonor and Doryani in the Western and Eastern Enigma Chambers (0.5.5c).
- src: poe2db:Version_0.5.0 «PoE2DB 0.5.0 notes», poe2db:Ancient_Crisis_Fragment, poe2db:Version_0.5.5c «0.5.5c notes», poe2db:Western_Enigma_Chamber, tier 2, crawl 2026-11-23
- notes: Which areas are the Infinite Farm versions vs the quest versions on the map pages is not labelled; the pinnacle area pages carry "map is quest area". `atlas-dependent`.


## What differs between the versions (known)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
(1) Origin Core: killing Arbiter of Divinity with the non-quest core completes the entire Precursor Fortress for the map owner (atlas tree unlock); the quest core no longer completes a section (0.5.5). (2) Monster levels of the six pinnacle areas could be set to 82 before the quest kill was done (0.5.1 fix), so level is tied to quest status. (3) Pinnacle unique drops are allocated to the map owner (0.5.2). (4) Non-quest keys are tradeable on the Currency Exchange (0.5.1 fix mentions tradeable Call of the Shadows and Origin fragments).
- src: poe2db:Version_0.5.5 «PoE2DB 0.5.5 notes», poe2db:Version_0.5.1 «0.5.1 notes», poe2db:Version_0.5.2 «0.5.2 notes», tier 2, crawl 2026-11-23
- conf: single-source per point
- notes: [INFERRED] the farm version runs at monster level 82 (see [[endgame/pinnacle-bosses]]); no explicit stat table for the farm version exists in the corpus, and the PoE2DB area rows (74 / 79) are the quest-area levels.


## "Uber" in internal ids
@ v=0.5.x vol=stable conf=confirmed date=2026-11-23
Area ids use the prefix MapUberBoss for the pinnacle maps and the Citadels (e.g. MapUberBoss_Monolith, MapUberBoss_StoneCitadel, MapUberBoss_IronCitadel_Quest); this is an internal id prefix, not a difficulty tier.
- src: poe2db:The_Burning_Monolith, poe2db:Eastern_Enigma_Chamber, tier 2, crawl 2026-11-23
- conf: confirmed (several pages)
- notes: Citadel second-phase bosses (Geonor the Putrid Wolf, Doryani's Triumph) are listed on the Citadel pages with higher life than their first forms, e.g. Count Geonor 2,675,628 vs Putrid Wolf 4,135,062 at area 80.


## Atlas difficulty and points
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Arbiter of Divinity kills (5) can substitute for fortress-map completion to gain atlas tree points (0.5.0 note). PoE2DB marks some Kosis drops "(Difficulty 2+)" and "(Difficulty 4)", and 0.5.1 fixed Kulemak granting atlas credit per difficulty increase; the difficulty scale is not explained in the corpus.
- src: poe2db:EndGame, poe2db:Version_0.5.1 «0.5.1 notes», tier 2, crawl 2026-11-23
- notes: `atlas-dependent`. No atlas passive content written here.
