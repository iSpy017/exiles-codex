# Unique items with restricted drop sources (0.5.x)

Status: partial. Covers 111 PoE2DB unique pages that carry an explicit drop-source tag. Missing: Sekhema's Resolve page (not in corpus), reasons behind "Drop disabled", 1.0 changes.
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against 1.0.
Sources: per-item PoE2DB pages (field `Limit 「source」Dropped by`), PoE2DB boss pages (Drops sections), PoE2DB [Unique item](https://poe2db.tw/us/Unique_item) overview.

## How PoE2DB marks restricted drops
- Claim: Each unique page may show a "Limit" box naming where it drops, in the form 「source」Dropped by, or the text 「Drop disabled」. Source is a boss, a league/mechanic name, or a release/league name. Unrestricted uniques show no such box. 111 item pages in the corpus carry a tag: 22 disabled, 89 with a named source.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Sandstorm Visage (example Limit box)](https://poe2db.tw/us/Sandstorm_Visage), tier 2, crawl 2026-11-23
- Confidence: single-source (PoE2DB only; counts are my scan of the local corpus)
- Notes: The overview page [PoE2DB Unique item](https://poe2db.tw/us/Unique_item) lists mods and bases only; it has no drop-source column. Overview section headers (conflict: sum 448 vs library 441): Weapon /88, Armour /221, Other /139, Cultivated /48. See [[items/uniques-index]] (library) for the 441 figure; 88+221+139 = 448 (see report conflict). Caster picks: [[items/uniques-caster]].

## Drop disabled (22 pages)
- Claim: These pages show 「Drop disabled」. Page does not say why (legacy, removed, or event-only is not stated).
- Version: 0.5.x
- Volatility: may-change
- Source: individual PoE2DB pages (e.g. [Blessed Bonds](https://poe2db.tw/us/Blessed_Bonds), [Redbeak](https://poe2db.tw/us/Redbeak)), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Req. level = "Requires: Level" on the page.

| Item | Base / class | Req lvl |
|---|---|---|
| Blessed Bonds | Linen Wraps | 56 |
| Bluetongue | Shortsword | 1 |
| Demigod's Duty | Golden Bracers | 1 |
| Demigod's Fortitude | Golden Shield | 1 |
| Demigod's Judgement | Golden Blade | 1 |
| Demigod's Loyalty | Golden Greaves | 1 |
| Demigod's Valor | Golden Plate | 1 |
| Demigod's Virtue | Golden Visage | 1 |
| Forbidden Gaze | (not parsed) | 26 |
| Forgotten By Time | Expedition Tablet | - |
| Infernoclasp | Plate Belt | 24 |
| Merit of Service | Pelage Targe | 8 |
| Redbeak | Shortsword | 1 |
| The Dancing Dervish | Scimitar | 16 |
| The Endless Night | Roaring Staff | 49 |
| The Deepest Tower | Spiritbone Crown | 45 |
| The Remembered Tales | Coffer Relic | - |
| The Road Warrior | Raider Plate | 16 |
| The Wailing Wall | Effigial Tower Shield | 21 |
| Thunderstep | (not parsed) | 28 |
| Winter's Bite | Glass Shank | 1 |
| Wylund's Stake | Smithing Hammer | 4 |

## Boss-restricted drops
- Claim: Items below carry 「boss」Dropped by. Item-page tags were compared against each boss page's Drops list: they match for Trialmaster, Xesht, Kosis, Arbiter of Ash, Arbiter of Divinity, Olroth, Bodach, King in the Mists, Raven Trickster. Not matching: Zarokh (below); Aberration (its Drops list shows Twisted Empyrean, ores labelled The Unleashed and Eyes of the Runefather, and Olroth's Conviction; the two items appear ore-linked, not as direct drops); Vessel of Kulemak (Drops list names Master's Reach, Grip of Kulemak, The Unborn Lich, Darkness Enthroned, Undying Hate, Tecrod's Revenge; Darkness Enthroned and Undying Hate item pages are tagged Abyss, not the Vessel).
- Version: 0.5.x
- Volatility: may-change
- Source: item pages plus [Zarokh](https://poe2db.tw/us/Zarokh_2C_the_Temporal), [Xesht](https://poe2db.tw/us/Xesht_2C_We_That_Are_One), [Kosis](https://poe2db.tw/us/Kosis_2C_The_Revelation), [The Arbiter of Ash](https://poe2db.tw/us/The_Arbiter_of_Ash), [Olroth](https://poe2db.tw/us/Olroth_2C_Origin_of_the_Fall), [The Bodach](https://poe2db.tw/us/The_Bodach), [The Trialmaster](https://poe2db.tw/us/The_Trialmaster), tier 2, crawl 2026-11-23
- Confidence: confirmed for the matching bosses; conflicting for Zarokh, Aberration, Vessel (see above)
- Notes: Format: Item (base, req lvl). "-" = no level line (jewels, relics).

**Zarokh, the Temporal (Sekhemas final boss) - item pages and boss page DISAGREE.**
- Item pages tagged 「Zarokh, the Temporal」Dropped by: Temporalis (Silk Robe, 64), Sandstorm Visage (Chain Tiara, 52), Eshtera's Path (Ring, 1), Zaida's Longevity (Ring, 40), Safrin's Resolve (Ring, 40), Against the Darkness (Time-Lost Diamond, -), Grand Spectrum (Sapphire, -), plus relics The Burden of Leadership, The Changing Seasons, The Desperate Alliance, The Last Flame, The Peacemaker's Draught (-).
- Zarokh's own Drops list shows only six relics: Burden of Leadership, Changing Seasons, Desperate Alliance, Last Flame, Peacemaker's Draught, Remembered Tales. The uniques are not in that list.
- Zarokh's page has a separate "Unique items from challenge runs" mapping: Remembered Tales -> Blessed Bonds, Desperate Alliance -> Against the Darkness, Burden of Leadership -> Sekhema's Resolve, Last Flame -> Temporalis, Changing Seasons -> Sandstorm Visage.
- Zarokh's page also has a "Zarokh, the Temporal Unique /14" item-card block near the top (lines ~8-210). Eshtera's Path, Safrin's Resolve, Zaida's Longevity and Grand Spectrum appear there as item cards (not in the Drops list or challenge-run mapping). The same block has Against the Darkness; line ~161 reads "Zarokh, the Temporal drops Sekhema's Resolve" (relic text).
- Third reading: The Burden of Leadership relic page itself says Zarokh drops Sekhema's Resolve (relic text, Burden_of_Leadership.txt), i.e. relic-conditional drop.
- Both readings kept (logged in report Conflicts). Relics are placed on the Relic Altar at trial start and destroyed when applied (Last Flame, Burden of Leadership pages). Blessed Bonds is "Drop disabled" on its own page yet is the Remembered Tales reward, so a disabled drop may still be reachable via the challenge run (reading from page text; not tested).

**The Trialmaster (Trial of Chaos)**: always drops one of Glimpse of Chaos (Tribal Mask, 52), Mahuxotl's Machination (Omen Crest Shield, 48), Hateforge (Moulded Mitts, 60), Zerphi's Genesis (Heavy Belt, 56), The Adorned (Diamond, -).

**Xesht, We That Are One**: Beyond Reach (Visceral Quiver, 65), Choir of the Storm (Jade Amulet, 55), Hand of Wisdom and Action (Spiral Wraps, 33), Skin of the Loyal (Garment, 1), The Pandemonius (Lapis Amulet, 52), Xoph's Blood (52), Controlled Metamorphosis (-). Boss page calls these "Guaranteed Unique".

**Kosis, The Revelation**: Assailum (Closed Helm, 45), Perfidy (Knight Armour, 45), Melting Maelstrom (Ultimate Mana Flask, 60), Strugglescream (Stellar Amulet, 52; Difficulty 4), Collapsing Horizon (Wyrm Quarterstaff, 65; Difficulty 2+), Megalomaniac (Diamond, -; Difficulty 4). Megalomaniac page also says it cannot be chanced and drops in the Simulacrum.

**The Arbiter of Ash**: Ab Aeterno (Grand Cuisses, 65), Morior Invictus (Grand Regalia, 65), Sine Aequo (Grand Manchettes, 65), Solus Ipse (Grand Visage, 65), Sacred Flame (Shrine Sceptre, 55), Prism of Belief (Diamond, -).

**The Arbiter of Divinity**: Decree of Acuity (Ancient Visor, 65), Decree of Flight (Ancient Leggings, 65), Decree of Loyalty (Ancient Mail, 70), Opportunity (Ultimate Life Flask, 60), The Ordained (Grand Spear, 79).

**Olroth, Origin of the Fall (Expedition)**: Svalinn (Crucible Tower Shield, 60), Keeper of the Arc (Spiritbone Crown, 62), Olroth's Resolve (Ultimate Life Flask, 60), Olrovasara (Torment Club, 65), Heroic Tragedy (Timeless Jewel, -; Difficulty 4 per boss page).

**The Bodach**: Vestige of Darkness (Tenebrous Crown, 65), Liminal Coil (Twisted Wand, 65), Forgotten Warden (Primal Markings, 70), Periphery (Heartwood Shortbow, 67), Sylvan's Effigy (Stoic Sceptre, 62).

**The King in the Mists (Ritual)**: Beetlebite (16), Ingenuity (55), Pragmatism (Explorer Armour, 52), The Burden of Shadows (Chiming Staff, 78), From Nothing (-; page says Crux of Nothingness at Difficulty 4).

**The Raven Trickster**: Horror's Flight (Engraved Bracers, 65), Sadist's Mercy (Flanged Mace, 67), The Auspex (Exquisite Vest, 65), The Raven's Flock (Perching Staff, 65), Veilpiercer (Amethyst Ring, 20), Split Personality (-).

**The Aberration**: Eyes of the Runefather (Venerable Defender, 62), The Unleashed (Revered Vestments, 65), Twisted Empyrean (Aberrant Sledge, 70).

**Vessel of Kulemak (Abyss)**: The Master's Reach (Tethering Bands, 65); Grip of Kulemak (Abyssal Signet, 1) and The Unborn Lich (65) are tagged Abyss and "drop from Vessel of Kulemak".

## League / mechanic-restricted drops
- Claim: Items tagged with a mechanic name rather than a boss.
- Version: 0.5.x
- Volatility: may-change
- Source: item pages ([Clear Skies](https://poe2db.tw/us/Clear_Skies), [Rite of Passage](https://poe2db.tw/us/Rite_of_Passage), [Voices](https://poe2db.tw/us/Voices) etc.), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: "Fate of the Vaal" is also the Release Version on these pages, so it reads as a league/release tag, not a boss. [INFERRED]: reason is the matching Release Version field only.

- Abyss: Darkness Enthroned (Fine Belt, 62), Undying Hate (Timeless Jewel), Unforeseen Consequences (Abyss Tablet).
- Azmeri Spirit: Rite of Passage (Golden Charm, 50).
- Breach: Nightfall (Glacial Fortress, 70), Wraeclast Besieged (tablet).
- Corrupted Nexus: Bursting Decay (Unset Ring, 60), Death Articulated (Ornate Gauntlets, 65), The Gnashing Sash (Wide Belt, 60).
- Delirium: Clear Skies (tablet), Voices (jewel; page also says drops in the Simulacrum).
- Expedition: Eventide Petals (Veridical Chain, 55), Uhtred's Chalice (Transcendent Mana Flask, 50).
- Ritual: Freedom of Faith (tablet).
- Fate of the Vaal: Atziri's Contempt (Pronged Spear, 72), Atziri's Rule (Reflecting Staff, 70), Atziri's Splendour (Sacrificial Regalia, 65), Atziri's Step (Cinched Boots, 65), Drillneck (Penetrating Quiver, 55), Flesh Crucible (Diamond). Atziri's Rule page also shows a Vaal Cultivation Orb entry under "Cultivated Uniques".

## Other acquisition notes
- Claim: Palm of the Dreamer page says to use a Vaal Orb on Guiding Palm variants (no Limit tag). Grip of Kulemak and The Unborn Lich pages say they drop from Vessel of Kulemak.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Palm of the Dreamer](https://poe2db.tw/us/Palm_of_the_Dreamer), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Many other uniques (Runeforging / Forge recipe boxes) show crafting costs in Verisium plus a boss "Crest" item; not parsed here.
