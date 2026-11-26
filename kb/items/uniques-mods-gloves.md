---
title: Unique Gloves mods (0.5.x) - part 1 of 2
status: partial  # not in tracker
defaults: v=0.5.x vol=may-change conf=single-source
merged_from: [uniques-mods-gloves-1.md, uniques-mods-gloves-2.md]
data: [data/uniques.csv, data/unique_mods.csv]  # generated from the crawl; query these instead of reading the tables
---

Status: done for this slot part (rows sorted by required level as listed by PoE2DB). Version: 0.5.x data (PoE2DB crawl 2026-11-23); not checked against 1.0. Volatility: may-change.
Source: poe2db:Unique_item (armour list, tier 2) plus each unique's own PoE2DB page (mod blocks, boss-drop and release-league lines), crawl 2026-11-23. Confidence: single-source.
Names per slot: [[items/uniques-armour]]. Drop restrictions and sources: [[items/uniques-drop-sources]]. Total uniques: [[items/uniques-index]].
Other parts of this slot: [[items/uniques-mods-gloves]]. Other slots: [[items/uniques-mods-body]], [[items/uniques-mods-helmet]], [[items/uniques-mods-gloves]], [[items/uniques-mods-boots]], [[items/uniques-mods-shields]].

## How to read
- Mods are paraphrased compactly; (a–b) are rolled ranges, fixed numbers are not rolled. Mod order follows PoE2DB mod blocks, not in-game order. Implicits and base defences are omitted. Req lvl = level only (attribute requirements omitted).
- Tag column: "Boss: X" = PoE2DB page says the item is dropped by that boss; "Rel: X" = release league shown on the page (blank = since 0.1.0 base data); "Drop disabled" = page carries the 「Drop disabled」 marker (22 item pages in the corpus carry it; the 12 armour ones are not on the Unique_item armour list and are appended here by hand, so the armour total is 221 listed + 12 = 233).
- Items whose PoE2DB page also shows a "Deferred" variant (differing base/level/mods) use the 0.5.5 block here.

## Gloves uniques

| Name | Base | Req lvl | Explicit mods | Tag |
|---|---|---|---|---|
| Facebreaker | Stocky Mitts | 1 | Has 8 to 12 Physical damage, +3 to +4 per Boss's Face Broken; (30–50)% increased Stun Buildup; 1% more Unarmed Damage per 5 Strength; +0.3 metres to Melee Strike Range while Unarmed; +1 to Armour per Strength; Can Attack as though using a One Handed Mace while both of your hand slots are empty Unarmed Attacks that would use an Equipped One Hand Mace 's damage use this Item's damage | Rel: Runes of Aldur |
| Treefingers | Riveted Mitts | 11 | (30–60)% increased Armour; Adds (6–10) to (12–16) Physical Damage to Attacks; Keystone: Giant's Blood; (20–30)% increased Stun Buildup; 5% reduced Attack Speed; +(15–20) to Strength |  |
| Lochtonial Caress | Tempered Mitts | 16 | Share Charges with Allies in your Presence; (10–15)% increased Skill Speed; (10–15)% reduced maximum Mana; +(40–60) to maximum Life; +(15–25) to Armour |  |
| Dreadfist | Bolstered Mitts | 27 | (60–100)% increased Armour; (20–30)% increased Critical Damage Bonus; Critical Hits inflict Impale; Critical Hits cannot Extract Impale; (20–31) to (32–49) Physical Thorns damage | Rel: Dawn of the Hunt |
| Atziri's Acuity | Moulded Mitts | 33 | Grants Herald of the Royal Queen (Lv9); (150–200)% increased Armour; +(100–150) to maximum Life; Leech 10% of Physical Attack Damage as Life; 10% of Physical damage dealt by your Hits causes Blood Loss; Keystone: Vaal Pact |  |
| Blessed Bonds | Linen Wraps | 56 | +(60–100) to Evasion Rating; +(30–50) to maximum Energy Shield; Gain (25–35) Mana per enemy killed; Inflict Cold Exposure on Igniting an Enemy; Inflict Fire Exposure on Shocking an Enemy; Inflict Lightning Exposure on Critical Hit | Drop disabled |
| Hateforge | Moulded Mitts | 60 | (300–400)% increased Armour; Gain a random Charge on reaching Maximum Rage , no more than once every (3–6) seconds; Lose all Rage on reaching Maximum Rage; (-10–10) to Maximum Rage; Gain (3–6) Rage on Hit | Boss: The Trialmaster |
| Empire's Grasp | Titan Mitts | 52 | (150–200)% increased Armour; +(20–30) to Strength; Gain (30–50) Life per enemy killed; (10–20)% increased Global Physical Damage; Knockback direction is reversed | Rel: Dawn of the Hunt |
| Northpaw | Suede Bracers | 1 | (10–15)% increased Critical Damage Bonus; Adds (3–5) to (8–10) Physical Damage to Attacks; Base Critical Hit Chance for Attacks with Weapons is 7%; +(15–25) to Evasion Rating |  |
| Grip of Winter | Firm Bracers | 11 | (30–50)% increased Evasion Rating; Adds (3–5) to (6–8) Cold damage to Attacks; (40–50)% increased Freeze Buildup; (20–30)% increased Magnitude of Chill you inflict; +(20–30)% to Cold Resistance |  |
| Idle Hands | Sectioned Bracers | 28 | (40–60)% increased Evasion Rating; You count as on Full Mana while at 90% of maximum Mana or above; 25% increased Attack Speed while on Full Mana; +(60–100) to Accuracy Rating; +(5–10) to Intelligence |  |
| Snakebite | Spined Bracers | 33 | (40–60)% increased Evasion Rating; +(7–17)% to Chaos Resistance; (20–30)% chance to Poison on Hit; Targets can be affected by +1 of your Poisons at the same time; (6–10) Life Regeneration per second |  |
| Maligaro's Virtuosity | Fine Bracers | 45 | (60–80)% increased Evasion Rating; (20–30)% increased Critical Hit Chance; 5% increased Attack Speed; +(10–20) to Dexterity; Your Critical Damage Bonus is 250%; Your Critical Hit Chance cannot be Rerolled |  |
| Horror's Flight | Engraved Bracers | 65 | Grants Crushing Fear (Lv15); (200–300)% increased Evasion Rating; (7–17)% increased Attack Speed; +(13–23) to Dexterity; Adds (19–23) to (31–37) Chaos Damage to Attacks; Gain 1 Fear Incarnate when you Cull a target | Boss: The Raven Trickster; Rel: Runes of Aldur |
| Painter's Servant | Torn Gloves | 1 | Gain (5–10)% of Elemental Damage as Extra Fire Damage; Gain (5–10)% of Elemental Damage as Extra Cold Damage; Gain (5–10)% of Elemental Damage as Extra Lightning Damage; 33% of Elemental Damage Converted to Fire Damage; 33% of Elemental Damage Converted to Cold Damage; 33% of Elemental Damage Converted to Lightning Damage |  |
| Candlemaker | Sombre Gloves | 12 | (50–80)% increased Energy Shield; +(20–40)% to Fire Resistance; (-20 to -10)% to Cold Resistance; Flammability Magnitude is doubled; (20–40)% increased Fire Damage; (10–20)% reduced Cold Damage |  |
| Doedre's Tenure | Stitched Gloves | 16 | (15–25)% reduced Cast Speed; 100% increased Spell Damage; +(10–15) to Intelligence; +(20–30) to maximum Energy Shield |  |
| Kitoko's Current | Jewelled Gloves | 26 | (30–50)% increased Energy Shield; +(10–20) to Dexterity; (10–15)% reduced Attack and Cast Speed; Lightning damage from Hits Contributes to Electrocution Buildup |  |
| Demon Stitcher | Intricate Gloves | 33 | (6–12)% increased Cast Speed; +(40–60) to maximum Energy Shield; +(80–120) to maximum Life; Sacrifice (5–15)% of maximum Life to gain that much Energy Shield when you Cast a Spell |  |
| Nightscale | Pauascale Gloves | 45 | (60–100)% increased Energy Shield; (30–50)% increased Critical Hit Chance; +(10–20) to Intelligence; +(20–30)% to Cold Resistance; 150% increased Mana Regeneration Rate if you've dealt a Critical Hit Recently; Cannot Regenerate Mana if you haven't dealt a Critical Hit Recently | Rel: Dawn of the Hunt |

<!-- merged from kb/items/uniques-mods-gloves-2.md -->
Part title: Unique Gloves mods (0.5.x) - part 2 of 2

Status: done for this slot part (rows sorted by required level as listed by PoE2DB). Version: 0.5.x data (PoE2DB crawl 2026-11-23); not checked against 1.0. Volatility: may-change.
Source: poe2db:Unique_item (armour list, tier 2) plus each unique's own PoE2DB page (mod blocks, boss-drop and release-league lines), crawl 2026-11-23. Confidence: single-source.
Names per slot: [[items/uniques-armour]]. Drop restrictions and sources: [[items/uniques-drop-sources]]. Total uniques: [[items/uniques-index]].
Other parts of this slot: [[items/uniques-mods-gloves]]. Other slots: [[items/uniques-mods-body]], [[items/uniques-mods-helmet]], [[items/uniques-mods-gloves]], [[items/uniques-mods-boots]], [[items/uniques-mods-shields]].

## How to read
- Mods are paraphrased compactly; (a–b) are rolled ranges, fixed numbers are not rolled. Mod order follows PoE2DB mod blocks, not in-game order. Implicits and base defences are omitted. Req lvl = level only (attribute requirements omitted).
- Tag column: "Boss: X" = PoE2DB page says the item is dropped by that boss; "Rel: X" = release league shown on the page (blank = since 0.1.0 base data); "Drop disabled" = page carries the 「Drop disabled」 marker (22 item pages in the corpus carry it; the 12 armour ones are not on the Unique_item armour list and are appended here by hand, so the armour total is 221 listed + 12 = 233).
- Items whose PoE2DB page also shows a "Deferred" variant (differing base/level/mods) use the 0.5.5 block here.

## Gloves uniques

| Name | Base | Req lvl | Explicit mods | Tag |
|---|---|---|---|---|
| Leopold's Applause | Embroidered Gloves | 52 | (60–100)% increased Energy Shield; +(60–100) to maximum Mana; (10–15)% increased Rarity of Items found; Damage Penetrates 10% Elemental Resistances; Your Hits can Penetrate Elemental Resistances down to a minimum of -50% | Rel: Dawn of the Hunt |
| Jarngreipr | Ringmail Gauntlets | 6 | +(30–50) to maximum Life; Adds (2–3) to (5–6) Physical Damage to Attacks; (4–8)% increased Attack Speed; Strength can satisfy other Attribute Requirements of Melee Weapons and Melee Skills; 50% increased Armour and Evasion |  |
| Aurseize | Layered Gauntlets | 16 | (40–60)% increased Armour and Evasion; (40–50)% increased Rarity of Items found; Lose 2% of maximum Life on Kill |  |
| Deathblow | Doubled Gauntlets | 33 | (100–150)% increased Armour and Evasion; Gain (20–30) Life per enemy killed; Gain (20–30) Mana per enemy killed; Culling Strike; (5–10)% increased Attack Speed | 0.5.5 data (page also shows a Deferred variant) |
| Valako's Vice | Plate Gauntlets | 45 | (50–100)% increased Armour and Evasion; (5–10)% increased Attack Speed; +(20–30) to Strength; +(20–30) to Dexterity; +(30–50)% to Lightning Resistance; 100% of Fire damage Converted to Lightning damage | Rel: Dawn of the Hunt |
| Aerisvane's Wings | Burnished Gauntlets | 52 | (50–70)% increased Armour and Evasion; (5–10)% increased Attack Speed; +(20–30) to Intelligence; Decimating Strike |  |
| Death Articulated | Ornate Gauntlets | 65 | (100–150)% increased Armour and Evasion; (5–10)% increased Attack Speed; +(17–23)% to Chaos Resistance; Lose 5% of maximum Life per second; Regenerate 5 Rage per second; No Inherent loss of Rage | Rel: Dawn of the Hunt |
| Gravebind | Rope Cuffs | 5 | (40–60)% increased Armour and Energy Shield; Gain (7–10) Life per enemy killed; Gain (4–6) Mana per enemy killed; 20% increased Rarity of Items found Your other Modifiers to Rarity of Items found do not apply Enemies in your Presence killed by anyone count as being killed by you instead; +(10–15)% to Cold Resistance |  |
| Shackles of the Wretched | Aged Cuffs | 16 | (30–50)% increased Armour and Energy Shield; You cannot be Chilled for 6 seconds after being Chilled; You cannot be Frozen for 6 seconds after being Frozen; You cannot be Ignited for 6 seconds after being Ignited; You cannot be Shocked for 6 seconds after being Shocked; Curses you inflict are reflected back to you |  |
| Blueflame Bracers | Goldcast Cuffs | 33 | +(10–20) to Intelligence; +(5–15)% to Fire Resistance; +(5–15)% to Cold Resistance; 100% of Fire Damage Converted to Cold Damage; +20 to maximum Energy Shield | 0.5.5 data (page also shows a Deferred variant) |
| The Prisoner's Manacles | Kalguuran Cuffs | 45 | (200–300)% increased Armour and Energy Shield; +100 to maximum Life; 100% increased Attribute Requirements; +(20–40)% to Lightning Resistance; (15–30) Life Regeneration per second; Debuffs you inflict have (20–30)% increased Slow Magnitude; Cannot Immobilise enemies | Rel: Dawn of the Hunt |
| Plaguefinger | Gauze Wraps | 4 | (30–50)% increased Evasion and Energy Shield; (4–6)% increased Attack Speed; Cannot inflict Elemental Ailments; (20–30)% chance to Poison on Hit; All Damage from Hits Contributes to Poison Magnitude |  |
| Killjoy | Linen Wraps | 16 | (30–60)% increased Evasion and Energy Shield; +(30–50) to maximum Life; Flasks do not recover Life; On-Kill Effects happen twice; (20–30)% increased Critical Damage Bonus |  |
| Hand of Wisdom and Action | Spiral Wraps | 33 | +(15–25) to Dexterity; +(15–25) to Intelligence; 1% increased Attack Speed per 20 Dexterity; Adds 1 to 10 Lightning Damage to Attacks per 20 Intelligence | Boss: Xesht, We That Are One |
| Essentia Sanguis | Furtive Wraps | 52 | (50–70)% increased Evasion and Energy Shield; Adds 1 to (30–50) Lightning damage to Attacks; +(15–25) to Intelligence; +(25–35)% to Lightning Resistance; Life Leech is Converted to Energy Shield Leech | Rel: Dawn of the Hunt |
| Thunderfist | Utility Wraps | 65 | Grants Crackling Palm (Lv15); (1–111)% increased Evasion and Energy Shield; (1–11)% increased Attack Speed; +(1–33)% to Lightning Resistance; Adds 1 to (77–111) Lightning Damage to Unarmed Melee Hits; +(0.1–1.1)% to Unarmed Melee Attack Critical Hit Chance | Rel: Rise of the Abyssal |
| Sine Aequo | Grand Manchettes | 65 | (10–15)% increased Skill Speed; (150–200)% increased Armour , Evasion and Energy Shield; Immobilise enemies at 50% buildup instead of 100%; (30–50)% increased Damage against Immobilised Enemies | Boss: The Arbiter of Ash |
| The Master's Reach | Tethering Bands | 65 | Grants Untether (Lv15); (200–300)% increased Armour and Energy Shield; +(75–125) to maximum Life; +(15–25) to Intelligence; Reveal Weaknesses against Rare and Unique; Eat a Soul when you Hit an enemy with an Open Weakness; (80–100)% of damage taken from enemies with an Open Weakness Recouped as Life | Boss: Vessel of Kulemak; Rel: Runes of Aldur |

Drop disabled (not tabulated; page shows no readable explicit mods, only an internal string): Demigod's Duty (Golden Bracers, Lv1).
