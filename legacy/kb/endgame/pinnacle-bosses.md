# Pinnacle Bosses: Roster, Unlock Keys, Areas

Status: partial. Roster, keys, area levels done. Exact drop rates for keys not in corpus. Stat profiles and big hits: [[endgame/pinnacle-bosses-2]]. Uber/quest-vs-farm versions: [[endgame/uber-bosses]].
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here checked against 1.0.
Sources: PoE2DB map/boss/item pages and 0.5.x patch-note pages (tier 2), local corpus.
Tag `atlas-dependent` = depends on atlas layout, waystone tier or atlas passives.

## Roster (map pages tagged pinnacle_boss, plus Kosis and Kulemak)
- Claim: PoE2DB tags six pinnacle-boss map areas, all Area Level 79 except the Burning Monolith (74): Burning Monolith (Arbiter of Ash), Origin Tower (Arbiter of Divinity), Twisted Domain (Xesht), Caer Tarth (The Bodach), Ruins of Kingsmarch (The Aberration), Withered Willow (The Raven Trickster). The Well of Souls endgame variant (Vessel of Kulemak, area 79) is a seventh. Kosis is the Simulacrum-encounter boss, not a map boss.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB The Burning Monolith](https://poe2db.tw/us/The_Burning_Monolith), [Twisted Domain](https://poe2db.tw/us/Twisted_Domain), [The Origin Tower](https://poe2db.tw/us/The_Origin_Tower), [Caer Tarth](https://poe2db.tw/us/Caer_Tarth), [Ruins of Kingsmarch](https://poe2db.tw/us/Ruins_of_Kingsmarch), [The Withered Willow](https://poe2db.tw/us/The_Withered_Willow), [The Well of Souls](https://poe2db.tw/us/The_Well_of_Souls), tier 2, crawl 2026-11-23
- Confidence: single-source (area pages), consistent across pages
- Notes: Sirus-style "uber ladder" not found; see [[endgame/uber-bosses]].

## Shared pinnacle-area rules
- Claim: Pinnacle map areas (Monolith, Origin Tower, Caer Tarth, Kingsmarch, Willow) list: players cannot gain or lose XP, unlimited revivals, 1 corrupted rare tablet drop, 5% rare socket-currency chance, 10% special gem drop chance (stat lines as shown, "% chance" units per the stat name). Twisted Domain lists no-XP and no league tablets but no revival line. 0.5.1 fix note: monster levels of these areas could rise to 82 before the quest version was killed with your own quest fragment.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB The Burning Monolith](https://poe2db.tw/us/The_Burning_Monolith), [Twisted Domain](https://poe2db.tw/us/Twisted_Domain), [0.5.1 notes](https://poe2db.tw/us/Version_0.5.1), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: [INFERRED] level 82 is the repeatable (non-quest) version's level, because the fix says levels rose to 82 only after the quest kill; the notes do not state the non-quest level outright. `atlas-dependent`.

## The Arbiter of Ash (The Burning Monolith, area 74)
- Claim: Entry needs three different Crisis Fragments, one from each Citadel type: Ancient from the Iron Citadel, Faded from the Copper Citadel, Weathered from the Stone Citadel. Each Citadel needs a Tier 15+ waystone; extra waystone drop chance can give extra fragments. Fragments are slotted into a door inside the Monolith. The Monolith itself needs the Ancient Gateway completed (quest chain).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Iron Citadel](https://poe2db.tw/us/Iron_Citadel), [Copper Citadel](https://poe2db.tw/us/Copper_Citadel), [Stone Citadel](https://poe2db.tw/us/Stone_Citadel), [Ancient Crisis Fragment](https://poe2db.tw/us/Ancient_Crisis_Fragment), [The Burning Monolith](https://poe2db.tw/us/The_Burning_Monolith), tier 2, crawl 2026-11-23
- Confidence: confirmed (Citadel pages + Monolith page agree)
- Notes: Citadel bosses: Count Geonor (Iron, area 80), Jamanra the Abomination (Copper, 80), Doryani Royal Thaumaturge plus Doryani's Triumph (Stone, 80). `atlas-dependent` (waystone tier, drop-chance passives). Quest versions of fragments come from two Enigma Chambers (Count Geonor, Doryani); see [[endgame/uber-bosses]].

## The Arbiter of Divinity (The Origin Tower, area 79)
- Claim: Needs an Origin Core, made by combining one Origin Spark and one Origin Cradle inside the Origin Tower. Tower access line: complete the Burning Monolith first. Spark/Cradle come from Phyx (Patriarch Halls) and Phya (Matriarch Halls), both area 65, Tier 15+ waystones; Spark and Cradle also tradeable on the Currency Exchange.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Origin Core](https://poe2db.tw/us/Origin_Core), [The Origin Tower](https://poe2db.tw/us/The_Origin_Tower), [The Patriarch Halls](https://poe2db.tw/us/The_Patriarch_Halls), [The Matriarch Halls](https://poe2db.tw/us/The_Matriarch_Halls), [0.5.5c notes](https://poe2db.tw/us/Version_0.5.5c), tier 2, crawl 2026-11-23
- Confidence: [INFERRED] that the Halls bosses are the Spark/Cradle source (0.5.5c note says you must be present when the Hall bosses die to pick up Spark/Cradle; the Hall pages themselves do not list the item)
- Notes: Non-quest Origin Core kill completes the whole Precursor Fortress for the map owner (0.5.5 note). `atlas-dependent`.

## Xesht, We That Are One (Twisted Domain, area 79)
- Claim: Breach pinnacle. Breachlord Sac is a map-fragment item (listed among the Keepers of the Flame quest rewards on the Breach page, also on the Currency Exchange); its text says to bring it to the Dreamer in the Monastery of the Keepers. 0.5.0 notes: Breach Fortresses hold bosses Tul and Esh whose kill gives a key to the existing Breach pinnacle boss. Which of the two (Sac vs Tul/Esh key) opens the repeatable fight is not stated in the corpus.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Breachlord Sac](https://poe2db.tw/us/Breachlord_Sac), [Breach](https://poe2db.tw/us/Breach), [Twisted Domain](https://poe2db.tw/us/Twisted_Domain), [0.5.0 notes](https://poe2db.tw/us/Version_0.5.0), tier 2, crawl 2026-11-23
- Confidence: single-source; ambiguity noted
- Notes: Xesht also appears in "Boss Rush Area 3" (area 35, a separate boss-rush chain); not detailed here. Twisted Domain mods: Breach timer 45,000 ms initial, 150,000 ms to portal, 200% more breach chest-ring and catalyst quantity. `atlas-dependent`.

## The Bodach (Caer Tarth, area 79)
- Claim: Ritual pinnacle. Perform the Rite of the Nameless at the effigy in Caer Tarth. Needs five "Call of the Shadows" (stack of 5, tradeable) or the five effigy pieces dropped from completing all altars in each Rite map. 0.5.0: killing The King in the Mists drops Head of the King (bring to Aoife in Caer Tarth to begin the Rite); each Rite map awards one element of the pinnacle key.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Call of the Shadows](https://poe2db.tw/us/Call_of_the_Shadows), [Rite of the Nameless](https://poe2db.tw/us/Rite_of_the_Nameless), [Head of the King](https://poe2db.tw/us/Head_of_the_King), [0.5.0 notes](https://poe2db.tw/us/Version_0.5.0), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Rite = chain of 5 maps; bosses reappear in later maps (0.5.0 note). `atlas-dependent`.

## The Aberration (Ruins of Kingsmarch / Fallen Star, area 79)
- Claim: Expedition (Runes of Aldur) pinnacle. Key is The Triskelion Reforged, made at the Verisium Anvil from Shattered Triskelion; use it at the Fallen Star after speaking to Makoru in the Ruins of Kingsmarch. Tradeable (Currency Exchange listing).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB The Triskelion Reforged](https://poe2db.tw/us/The_Triskelion_Reforged), [Shattered Triskelion](https://poe2db.tw/us/Shattered_Triskelion), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Shattered Triskelion drop source not found in corpus.

## The Raven Trickster (The Withered Willow, area 79)
- Claim: Delirium pinnacle. Key: Raven's Reflection, brought to the Mirror in the Withered Willow. Separate Delirium pinnacle encounter: Simulacrum (see Kosis).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Raven's Reflection](https://poe2db.tw/us/Ravens_Reflection), [Delirium](https://poe2db.tw/us/Delirium), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Raven's Reflection drop source not found in corpus.

## Kosis, The Revelation (Simulacrum)
- Claim: Delirium page lists the Simulacrum encounter plus Kosis as the Delirium "Pinnacle Boss". Simulacrum = 300 Simulacrum Splinters combined, then applied to a Delirium-fogged map with at least 100% Deliriousness. Simulacrum of Delusion maps: area 80, Tier 14+ waystone.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Simulacrum](https://poe2db.tw/us/Simulacrum), [Simulacrum Splinter](https://poe2db.tw/us/Simulacrum_Splinter), [Simulacrum of Delusion](https://poe2db.tw/us/Simulacrum_of_Delusion), [Delirium](https://poe2db.tw/us/Delirium), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Kosis' wave placement and the area level at which he spawns inside a Simulacrum are not in the corpus. `atlas-dependent`.

## Vessel of Kulemak (The Well of Souls endgame variant, area 79)
- Claim: Abyss pinnacle. Key: Kulemak's Invitation (reward line of the "Abyssal Power" quest; item text points to the Well). 0.5.4b notes: the pinnacle key is consumed on interaction.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Abyssal Power](https://poe2db.tw/us/Abyssal_Power), [Kulemak's Invitation](https://poe2db.tw/us/Kulemaks_Invitation), [The Well of Souls](https://poe2db.tw/us/The_Well_of_Souls), [0.5.4b notes](https://poe2db.tw/us/Version_0.5.4b), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: 0.5.1 notes mention Kulemak difficulty increases; PoE2DB marks some Kosis drops "(Difficulty 2+/4)"; scale not explained in corpus.

## Key prices
- Claim: Not recorded. PoE2DB's economy panels name no league, so figures are omitted per project rule. Check live prices on [PoE2DB economy fragments](https://poe2db.tw/us/Economy_Fragments) or poe.ninja at league start, with date and league.
- Version: 0.5.x
- Volatility: volatile
- Source: none (omitted)
- Confidence: n/a
- Notes: Keys are tradeable on the Currency Exchange per 0.5.1 notes (Call of the Shadows, Origin fragments).
