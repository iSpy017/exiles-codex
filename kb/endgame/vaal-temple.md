---
title: Atziri's Temple (Fate of the Vaal league mechanic; "Vaal temple")
status: partial
tracker_topic: "Atziri's Temple (Vaal temple)"
tracker_note: "partial (0.5.x; rooms, medallions, devices, Atziri/Architect; phase mechanics missing)"
defaults: v=0.5.x
---

Status: partial. Missing: Temple Atlas tree (out of scope), Tablet mods, room-card draw rules, room-boss mapping.
Version: 0.5.x (introduced 0.4.0 as the Fate of the Vaal league; core game from 0.5.0). Not checked for 1.0.
Sources: PoE2DB crawl 2026-11-23 pages (Atziri's Temple, Atziri boss pages, Vaal Beacon, Energised Crystal, currency pages) plus PoE2DB patch-note pages 0.4.0 to 0.5.5.
Name check: the PoE2DB page is "Atziri's Temple" (id IncursionTemple). Internal "Incursion" ids. Not the same thing as Trial of Chaos (see [[endgame/trial-of-chaos]]).

## Naming and what it is
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
The mechanic is called Atziri's Temple. You build a Temple layout out of rooms on a console, run it, and fight the Architect (Xipocado) and then Atziri, the Red Queen. Rooms upgrade by sitting next to rooms that benefit them.
- src: poe2db:Fate_of_the_Vaal_league, tier 2, crawl 2026-11-23; poe2db:Atziris_Temple line 1451
- conf: single-source (the two pages agree in substance)
- notes: atlas-dependent.


## Access flow: beacons, crystals, ruins
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Activating Vaal Beacons (monsters around each beacon must be killed first) gives Energised Crystals. 6 crystals power the Temple Console. The Vaal Ruins console lets you shape the Temple, then a portal sends you back in time. Campaign quest "Ancient Beacons" (Acts 1, 2, 3): activate 6 beacons, enter the Vaal Ruins, place rooms, open a first Temple. Endgame Vaal Ruins hub is area level 65.
- src: poe2db:Energised_Crystal, poe2db:Ancient_Beacons, poe2db:Vaal_Ruins, tier 2, crawl 2026-11-23
- conf: single-source per fact
- notes: tag atlas-dependent. A 0.5.0 patch note says the first 6 beacons are in Act 3 and a second 6 in the Interludes, which disagrees with the quest page (Acts 1, 2, 3). Logged in report as a conflict.


## Beacons in maps, tablets, crystal cap
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Maps inside Lira Vaal on the atlas always have Energised Crystals (and give points for the Fate of the Vaal atlas tree). Temple Precursor Tablets add Vaal Beacons to a map (10 uses). Tablet-linked atlas passives: +50% chance beacons summon extra monsters; one Rare or Unique corrupted when beacons activate; 50% chance beacon Uniques get an Essence mod; 20% chance each beacon adds a Vaal Unique. Default crystal cap 60 and medallion cap 6 since 0.5.0. Monster level of the Temple factors in the area levels where your crystals came from.
- src: poe2db:Vaal_Beacon, poe2db:Version_0.5.0, tier 2, crawl 2026-11-23
- notes: atlas-dependent. Xopec's and Azcapa's medallions (+6 crystals up to 60; +1 medallion up to 6) were declared unnecessary in 0.5.0 but still exist on the page.


## Temple level vs player level
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Temple level equals player level up to 65, then flattens. Samples (player to temple): 65:65, 70:68, 75:72, 80:76, 90:81, 100:81. Max listed temple level 81.
- src: poe2db:Atziris_Temple lines 1346-1447, tier 2, crawl 2026-11-23
- notes: Version 0.5.0 note says monster level also factors where crystals were obtained.


## Room families (what each does, tier 1 to 4)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Rooms scale in 4 tiers. Key families and their stated bonus at Tier 1 / Tier 4:

| Room family | Tier 1 | Tier 4 | Notes |
|---|---|---|---|
| Garrison | +8% packs | +20% packs, +18% effectiveness | needs Commander/Armoury chain |
| Commander | +10% effectiveness | +40% | may drop Quipolatl/Uromoti/Zantipi medallions |
| Armoury | +10% | +40% | Tier 3-4 hold Rare equipment |
| Smithy | +15% item rarity from chests | +50% | Forging/Masterwork workbenches |
| Alchemy Lab | +10% rarity | +40% rarity, +60% gold | Soul Core Infuser at T3-4 |
| Synthflesh Lab | +10% XP | +35% XP | |
| Thaumaturge | +8% temple room effect | +25% | Gemcutting at T2, Gem Corrupter T3 |
| Corruption Chamber | +10% rare mod chance | +40% | Corruption Altar |
| Sacrificial Chamber | +15% rare chests, one Unique item | +50% | Morphology Mechanism T3-4 |
| Generator | power for nearby rooms | | many rooms need Power |

- src: poe2db:Atziris_Temple lines 59-1082, tier 2, crawl 2026-11-23
- notes: atlas-dependent (Tier 4 needs a Temple Atlas passive per 0.5.0 notes). Full list on PoE2DB page. Some rooms need Generator power (Smithy 1, Synthflesh 1, Golem Works 2).


## Reward vaults (unlocked from the Architect console)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Defeating the Architect unlocks Xipocado's Console (place restricted rooms) and medallions. Vault rooms: Kishara's Vault (rare currency chests), Vault of Reverence (a random Lineage support gem), Jiquani's Vault (a Rune cache), Tablet Research Vault (corrupt a Tablet), Ancient Reliquary Vault (a Reliquary display with a Unique), Extraction Chamber (destroy gear to return augments). Royal Access Chamber completion unlocks Atziri's Chamber, whose arena door stays shut until you interact with the Access Chamber. Vault rooms destabilise once accessible.
- src: poe2db:Atziris_Temple lines 957-1026, poe2db:Atziri_2C_the_Red_Queen «PoE2DB Atziri, the Red Queen» lines 4726-4734, tier 2, crawl 2026-11-23
- conf: confirmed (2 pages)
- notes: 0.4.0c halved the rooms destabilised after the Architect and cut those after Atziri by 25%; the Extraction Chamber became much rarer (max 1 offered).


## Medallions (9)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Juatalotli's: block the next destabilisation of a room. Hayoxi's: reroll a Restricted Room. Quipolatl's: raise a room's tier (does not stack). Uromoti's: add a room. Xopec's: +6 max crystals (to 60). Azcapa's: +1 max medallions (to 6). Estazunti's: extra Restricted Room card after the Architect. Puhuarte's: reroll room cards (not restricted ones). Zantipi's: +1 random waystone modifier on the Temple, up to 8 modifiers; this count drops by 1 per 10 Temples opened. Room medallions cannot be used inside an active Temple (0.5.0).
- src: poe2db:Atziris_Temple lines 1100-1156, tier 2, crawl 2026-11-23
- notes: medallion drop rate scales with path count (0.5.0).


## Crafting devices and what they take
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Room devices and the item each takes: Corruption Altar (Vaal Orb), Gem Corrupter (Crystallised Corruption), Soul Core Infuser (Core Destabiliser), Precursor Machine (Ancient Infuser, Tablets), Morphology Mechanism (Vaal Cultivation Orb; replaces up to 2 mods on a corrupted Vaal Unique), Forging Mechanism (Divine Orb; augment socket), Gemcutting Workbench (Greater Jeweller's Orb; 3 support sockets), Gemcutting Mechanism (gem quality), Extraction Workbench. Exalted, Regal and Alchemy workbenches (Pristine versions on Past-side temples) cost Regal, Augmentation and Greater Transmutation respectively. Masterwork/Triumphant Forges push quality past maximum with a corruption chance, using the four Infusers (Armourer's, Blacksmith's, Arcanist's, Catalysing).
- src: poe2db:Atziris_Temple lines 1157-1344, tier 2, crawl 2026-11-23
- notes: Architect's Orb modifies a corrupted Equipment/Jewel or destroys it; Orb of Extraction destroys equipment and returns non-socket-bound augments; Vaal Siphoner adds a kill threshold to corrupted rare jewellery. All Infusers need item quality at or above 20% (0.5.0 note). Transcension Device (Flesh Surgeon T3-4) swaps up to 2 arms and 2 legs for temporary limbs, lost on death.


## Atziri, the Red Queen (boss)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Two phases: Red Queen then Fell Serpent. PoE2DB multipliers: phase 1 life 742%, damage 380%; phase 2 life 990%, damage 450%. At the page's reference level 68: phase 1 life 61,267, phase 2 life 81,744. Skill ids: phase 1 flame wall, blood spear, lightning dash; phase 2 adds clones, cataclysm, flameblast, storm call, blood cannon, beast teleport and dash, flesh bubble.
- src: poe2db:Atziri_2C_the_Red_Queen «PoE2DB Atziri, the Red Queen» lines 22-72, poe2db:Atziri_2C_the_Fell_Serpent «PoE2DB Atziri, the Fell Serpent» lines 21-72, tier 2, crawl 2026-11-23
- notes: skill ids are internal names; their behaviour is not described. [INFERRED]: names suggest flame, storm, blood themes, but real telegraphs are not in the corpus.


## Atziri drops and keys
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Atziri drops Atziri's Medallion (a vault key). Take it to the checkpoint at Atziri's Chamber entrance; it unlocks Atziri's Vault plus six Royal Trove chests (currency). Vault always has one of: Drillneck, Atziri's Splendour, Atziri's Rule, Atziri's Contempt, Flesh Crucible. Also: Sacrificial Regalia (100%, magic or rare), several rares, Atziri's Impatience, Zerphi's Infamy. Since 0.5.4 the vault can drop 1 of 4 Orb of Sacrifice currencies (upgrade a corrupted enchantment, remove a random explicit).
- src: poe2db:Atziri_2C_the_Red_Queen «PoE2DB Atziri, the Red Queen» lines 4739-4775, poe2db:Version_0.5.4 line 32, tier 2, crawl 2026-11-23
- conf: confirmed (2 sources)
- notes: Royal Troves hold Greater/Perfect currency plus the Temple-exclusive currencies listed under crafting devices.


## Architect (Xipocado) and room bosses
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Xipocado, Royal Architect: life 371%, damage 300%, boss tier 2; reference level 80 life 115,251. Skills include tablet shuffle and tablet warp (names only). Other named uniques: Pakteni, Kulka (life 330%, damage 300%, 3 tiers), Xalapa, Xolotl, Cualli.
- src: poe2db:Xipocado_2C_Royal_Architect «PoE2DB Xipocado» lines 19-66, poe2db:Kulka_2C_Vaal_Thaumaturge «PoE2DB Kulka», tier 2, crawl 2026-11-23
- notes: [INFERRED] that Xalapa is the Spymaster boss (audio ids Spymaster_) and Pakteni the Flesh Surgeon (title); Xolotl and Cualli room links not found.
