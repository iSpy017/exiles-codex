---
title: Unique Helmet mods (0.5.x) - part 1 of 2
status: partial  # not in tracker
defaults: v=0.5.x vol=may-change conf=single-source
merged_from: [uniques-mods-helmet-1.md, uniques-mods-helmet-2.md]
data: [data/uniques.csv, data/unique_mods.csv]  # generated from the crawl; query these instead of reading the tables
---

Status: done for this slot part (rows sorted by required level as listed by PoE2DB). Version: 0.5.x data (PoE2DB crawl 2026-11-23); not checked against 1.0. Volatility: may-change.
Source: poe2db:Unique_item (armour list, tier 2) plus each unique's own PoE2DB page (mod blocks, boss-drop and release-league lines), crawl 2026-11-23. Confidence: single-source.
Names per slot: [[items/uniques-armour]]. Drop restrictions and sources: [[items/uniques-drop-sources]]. Total uniques: [[items/uniques-index]].
Other parts of this slot: [[items/uniques-mods-helmet]]. Other slots: [[items/uniques-mods-body]], [[items/uniques-mods-helmet]], [[items/uniques-mods-gloves]], [[items/uniques-mods-boots]], [[items/uniques-mods-shields]].

## How to read
- Mods are paraphrased compactly; (a–b) are rolled ranges, fixed numbers are not rolled. Mod order follows PoE2DB mod blocks, not in-game order. Implicits and base defences are omitted. Req lvl = level only (attribute requirements omitted).
- Tag column: "Boss: X" = PoE2DB page says the item is dropped by that boss; "Rel: X" = release league shown on the page (blank = since 0.1.0 base data); "Drop disabled" = page carries the 「Drop disabled」 marker (22 item pages in the corpus carry it; the 12 armour ones are not on the Unique_item armour list and are appended here by hand, so the armour total is 221 listed + 12 = 233).
- Items whose PoE2DB page also shows a "Deferred" variant (differing base/level/mods) use the 0.5.5 block here.

## Helmet uniques

| Name | Base | Req lvl | Explicit mods | Tag |
|---|---|---|---|---|
| Wings of Caelyn | Rusted Greathelm | 1 | +(20–30) to Dexterity; (5–15)% increased Rarity of Items found; Gain 1 Rage on Melee Hit; Every Rage also grants 1% increased Stun Threshold; +20 to Armour |  |
| Horns of Bynden | Rusted Greathelm | 1 | +(20–30) to Strength; (5–15)% increased Rarity of Items found; Gain 1 Rage on Melee Hit; Every Rage also grants 1% increased Armour; +20 to Armour |  |
| Demigod's Virtue | Golden Visage | 1 | 25% increased Rarity of Items found | Drop disabled |
| Ezomyte Peak | Soldier Greathelm | 12 | (50–100)% increased Armour; +(50–80) to maximum Life; (10–20)% increased Area of Effect; Keystone: Unwavering Stance; (3–6) Life Regeneration per second |  |
| Black Sun Crest | Wrapped Greathelm | 16 | (50–80)% increased Armour; 20% reduced Light Radius; (5–15)% increased Strength; (5–15)% increased Dexterity; (5–15)% increased Intelligence |  |
| Forbidden Gaze | Chain Tiara | 26 | (60–100)% increased Energy Shield; +(3–5)% to Maximum Cold Resistance; +(30–50)% to Cold Resistance; 25% reduced Light Radius | Drop disabled; no longer drops since 0.3.0 (version history) |
| Thrillsteel | Spired Greathelm | 27 | Onslaught |  |
| Deidbell | Elite Greathelm | 33 | (60–100)% increased Armour; (20–30)% increased Warcry Speed; Warcries Explode Corpses dealing 10% of their Life as Physical Damage; Warcry Skills have (20–30)% increased Area of Effect; +(10–20) to Strength |  |
| Corona of the Red Sun | Warrior Greathelm | 36 | +(100–150) to Accuracy Rating; +(60–80) to maximum Life; 25% increased Light Radius; Leeching Life from your Hits causes Allies in your Presence to also Leech the same amount of Life; +(20–25)% to Fire Resistance |  |
| The Deepest Tower | Spiritbone Crown | 45 | (70–130)% increased Armour and Energy Shield; +(70–100) to maximum Life; +(17–23)% to Chaos Resistance; 50% reduced Presence Area of Effect; 10% reduced Light Radius; Enemies in your Presence count as being on Low Life | Drop disabled; no longer drops since 0.3.0 (version history); Rel: Dawn of the Hunt |
| Blood Price | Fierce Greathelm | 51 | (80–120)% increased Armour; (10–15) Life Regeneration per second; +(100–150) to Stun Threshold; (30–60)% increased Presence Area of Effect; Enemies in your Presence have at least 10% of Life Reserved | Rel: Dawn of the Hunt |
| Innsmouth | Shabby Hood | 1 | 25% reduced maximum Mana; +(10–20)% to Cold Resistance; +(13–19)% to Chaos Resistance; 100% increased Mana Regeneration Rate; +(20–30) to Evasion Rating |  |
| Goldrim | Felt Cap | 10 | +(30–50) to Evasion Rating; 10% increased Rarity of Items found; +(25–35)% to all Elemental Resistances |  |
| Radiant Grief | Lace Hood | 16 | (80–100)% increased Evasion Rating; +(15–25)% to Fire Resistance; 30% increased Light Radius; Enemies in your Presence are Ignited as though dealt 200 Base Fire Damage | 0.5.5 data (page also shows a Deferred variant) |
| Elevore | Hunter Hood | 33 | (50–80)% increased Evasion Rating; +(20–30) to Dexterity; Charms gain 1 charge per Second; +(1–2) Charm Slots |  |
| Constricting Command | Viper Cap | 38 | +(80–120) to maximum Life; +(10–15) to all Attributes; (8–12) Life Regeneration per second; Require (2–4) fewer enemies to be Surrounded | Rel: Dawn of the Hunt |
| The Black Insignia | Corsair Cap | 45 | (70–100)% increased Evasion Rating; (10–20)% increased Rarity of Items found; +(15–25)% to Lightning Resistance; Gain Tailwind on Critical Hit , no more than once per second; Lose all Tailwind when Hit | Rel: Dawn of the Hunt |
| Starkonja's Head | Leatherbound Hood | 50 | (100–200)% increased Evasion Rating; (15–25)% increased Critical Hit Chance; +(30–40) to Dexterity; 150% increased Global Evasion Rating when on Low Life; 15% of Damage from Hits is taken from your Damageable Companion 's Life before you | Rel: Dawn of the Hunt |
| Heatshiver | Velvet Cap | 52 | (50–70)% increased Evasion Rating; +(60–100) to maximum Mana; +(20–30)% to Fire Resistance; +(20–30)% to Cold Resistance; Gain 1% of Cold damage as Extra Fire damage per 1% Chill Magnitude on enemy | Rel: Dawn of the Hunt |
| Myris Uxor | Covert Hood | 56 | (40–60)% increased Evasion Rating; +(100–150) to Accuracy Rating; +(40–60) to maximum Mana; 100% increased Culling Strike Threshold |  |
| Alpha's Howl | Armoured Cap | 65 | (80–100)% increased Evasion Rating; +100 to Spirit; +(50–75)% to Cold Resistance; Presence Radius is doubled | 0.5.5 data (page also shows a Deferred variant) |
| Crown of Thorns | Twig Circlet | 1 | +(100–150) to maximum Energy Shield; (3–5) to (6–10) Physical Thorns damage; Lose 5 Life when you use a Skill; Keystone: Pain Attunement |  |
| The Devouring Diadem | Wicker Tiara | 10 | (60–100)% increased Energy Shield; +(10–20) to Intelligence; +(13–19)% to Chaos Resistance; Every 3 seconds, Consume a nearby Corpse to Recover 20% of maximum Life; +(40–60) to maximum Life |  |
| Visage of Ayah | Beaded Circlet | 16 | (50–80)% increased Energy Shield; (10–15)% increased Rarity of Items found; (20–30)% increased Critical Hit Chance; Keystone: Eldritch Battery; +(10–20)% to Lightning Resistance |  |
| Sandstorm Visage | Chain Tiara | 52 | +(80–120) to maximum Energy Shield; +(20–30) to Dexterity; Enemies in your Presence are Blinded; Every second, inflicts Critical Weakness on enemies in your Presence for (15–20) seconds | Boss: Zarokh, the Temporal |
| Mask of the Stitched Demon | Feathered Tiara | 33 | (120–160)% increased Energy Shield; +(17–23)% to Chaos Resistance; Cannot have Energy Shield; Regenerate 0.05 Life per second per Maximum Energy Shield |  |
| Atziri's Disdain | Gold Circlet | 40 | +(60–100) to maximum Mana; (10–20)% increased Rarity of Items found; Gain (10–15)% of maximum Life as Extra maximum Energy Shield; 10% of Damage taken bypasses Energy Shield |  |
| Crown of Eyes | Vermeil Circlet | 45 | (100–140)% increased Energy Shield; +(150–200) to Accuracy Rating; +(10–15) to all Attributes; -10% to Fire Resistance; Increases and Reductions to Spell damage also apply to Attacks | Rel: Dawn of the Hunt |
| Scold's Bridle | Jade Tiara | 50 | +(75–150) to maximum Energy Shield; (60–100)% increased Spell Damage; +(80–100) to maximum Mana; 15% reduced Cast Speed; Take (25–100)% of Mana Costs you pay for Skills as Physical Damage | Rel: Dawn of the Hunt |
| Indigon | Magus Tiara | 65 | (100–140)% increased Energy Shield; +(80–120) to maximum Mana; (5–10)% increased Cost of Skills for each 200 total Mana Spent Recently; (10–15)% increased Spell damage for each 200 total Mana you have Spent Recently; Mana Recovery other than Regeneration cannot Recover Mana | Rel: Dawn of the Hunt |
| Greymake | Brimmed Helm | 5 | +(30–50) to Strength; +(30–50) to Dexterity; +(30–50) to Intelligence; -1 to all Attributes per Level |  |
| Erian's Cobble | Guarded Helm | 11 | +(0–40) to Armour; +(0–30) to Evasion Rating; +(0–20) to maximum Energy Shield; +(0–30) to maximum Life; +(0–20) to maximum Mana; +(0–60) to Accuracy Rating; (0–6) Life Regeneration per second; +(0–10)% to Fire Resistance; +(0–10)% to Cold Resistance; +(0–10)% to Lightning Resistance; (0–30)% increased Critical Hit Chance; (0–20)% increased Rarity of Items found; +(0–10) to Strength; +(0–10) to Dexterity; +(0–10) to Intelligence |  |

<!-- merged from kb/items/uniques-mods-helmet-2.md -->
Part title: Unique Helmet mods (0.5.x) - part 2 of 2

Status: done for this slot part (rows sorted by required level as listed by PoE2DB). Version: 0.5.x data (PoE2DB crawl 2026-11-23); not checked against 1.0. Volatility: may-change.
Source: poe2db:Unique_item (armour list, tier 2) plus each unique's own PoE2DB page (mod blocks, boss-drop and release-league lines), crawl 2026-11-23. Confidence: single-source.
Names per slot: [[items/uniques-armour]]. Drop restrictions and sources: [[items/uniques-drop-sources]]. Total uniques: [[items/uniques-index]].
Other parts of this slot: [[items/uniques-mods-helmet]]. Other slots: [[items/uniques-mods-body]], [[items/uniques-mods-helmet]], [[items/uniques-mods-gloves]], [[items/uniques-mods-boots]], [[items/uniques-mods-shields]].

## How to read
- Mods are paraphrased compactly; (a–b) are rolled ranges, fixed numbers are not rolled. Mod order follows PoE2DB mod blocks, not in-game order. Implicits and base defences are omitted. Req lvl = level only (attribute requirements omitted).
- Tag column: "Boss: X" = PoE2DB page says the item is dropped by that boss; "Rel: X" = release league shown on the page (blank = since 0.1.0 base data); "Drop disabled" = page carries the 「Drop disabled」 marker (22 item pages in the corpus carry it; the 12 armour ones are not on the Unique_item armour list and are appended here by hand, so the armour total is 221 listed + 12 = 233).
- Items whose PoE2DB page also shows a "Deferred" variant (differing base/level/mods) use the 0.5.5 block here.

## Helmet uniques

| Name | Base | Req lvl | Explicit mods | Tag |
|---|---|---|---|---|
| Ironride | Visored Helm | 16 | (60–80)% increased Armour and Evasion; +(10–15)% to Lightning Resistance; +(30–50) to maximum Mana; You have no Accuracy Penalty at Distance; +(30–50) to maximum Life |  |
| The Smiling Knight | Cowled Helm | 26 | (150–200)% increased Armour and Evasion; +(50–100) to Accuracy Rating; (15–25)% increased Critical Hit Chance; Aggravate Bleeding on targets you Critically Hit with Attacks |  |
| The Vile Knight | Shielded Helm | 33 | (60–100)% increased Armour and Evasion; Deal 4% increased Damage with Hits to Rare or Unique Enemies for each second they've ever been in your Presence , up to a maximum of 200%; (10–15) Life Regeneration per second; +(75–125) to Accuracy Rating |  |
| Assailum | Closed Helm | 45 | (200–300)% increased Armour and Evasion; +(200–400) to Accuracy Rating; (30–50)% increased Critical Hit Chance; Skills have a (100–150)% longer Perfect Timing window | Boss: Kosis, The Revelation |
| The Bringer of Rain | Decorated Helm | 52 | (600–800)% increased Armour and Evasion; +(200–300) to Accuracy Rating; (30–60) Life Regeneration per second; Can't use Body Armour; You can wield Two-Handed Axes , Maces and Swords in one hand; 100% increased Critical Hit Chance; This item gains bonuses from Socketed Items as though it was a Body Armour | Rel: Dawn of the Hunt |
| Decree of Acuity | Ancient Visor | 65 | (150–250)% increased Armour and Evasion; +(25–35) to Dexterity; Gain (15–30)% of Evasion Rating as extra Armour; You are Blind; The Effect of Blind on you is reversed | Boss: The Arbiter of Divinity; Rel: Runes of Aldur |
| Crown of the Victor | Iron Crown | 5 | (10–15)% increased Rarity of Items found; Gain 10 Life per enemy killed; Gain 10 Mana per enemy killed; +1 to Level of all Skills |  |
| Bronzebeard | Horned Crown | 10 | (50–100)% increased Armour and Energy Shield; +100 to maximum Life; (35–50)% reduced Magnitude of Ignite on you; (35–50)% reduced Effect of Chill on you; (35–50)% reduced effect of Shock on you; 10% reduced Movement Speed |  |
| Crown of the Pale King | Cultist Crown | 16 | (50–100)% increased Armour and Energy Shield; +(40–80) to maximum Life; 10% increased Rarity of Items found; Thorns can Retaliate against all Hits; (10–15) to (20–25) Physical Thorns damage |  |
| Veil of the Night | Martyr Crown | 28 | 50% increased maximum Life; +(10–20) to all Attributes; 40% reduced Light Radius; You have no Elemental Resistances |  |
| Cornathaum | Heavy Crown | 33 | (10–20)% increased Rarity of Items found; +(40–50) to Intelligence; 30% increased Light Radius; 5% increased Experience gain |  |
| Keeper of the Arc | Spiritbone Crown | 62 | (240–340)% increased Armour and Energy Shield; (15–25) Life Regeneration per second; (15–25)% increased Mana Regeneration Rate; Alternating every 5 seconds: Take 40% less Damage from Hits Take 40% less Damage over time | Boss: Olroth, Origin of the Fall |
| Vestige of Darkness | Tenebrous Crown | 65 | (150–200)% increased Armour and Energy Shield; +(20–30) to Strength and Intelligence; Physical damage from Hits Contributes to Chill Magnitude and Freeze Buildup; Enemies in your Presence are Blinded; The Bodach haunts your Presence (page follows this with an unrendered internal stat string — effect details not readable) | Boss: The Bodach; Rel: Runes of Aldur |
| The Hollow Mask | Hewn Mask | 5 | Grants Wildwood's Gifts (Lv2); +(60–80) to maximum Life; -10% to all Elemental Resistances; 15% additional Physical Damage Reduction; +13% to Chaos Resistance; Remnants you create affect Allies in your Presence as well as you when collected; (80–100)% increased Reservation Efficiency of Remnant Skills | Rel: Runes of Aldur |
| Mask of the Sanguimancer | Face Mask | 10 | (20–40)% increased Critical Hit Chance for Spells; +(10–20) to Strength; +(10–20) to Intelligence; Keystone: Blood Magic; +(20–25) to Evasion Rating +(10–15) to maximum Energy Shield |  |
| Leer Cast | Hooded Mask | 16 | +(30–50) to maximum Life; +(30–50) to maximum Mana; 25% reduced Damage; Allies in your Presence deal 50% increased Damage; +(10–20) to Dexterity |  |
| Atsak's Sight | Veiled Mask | 28 | +(10–20) to Dexterity; +(10–20) to Intelligence; (30–40)% increased Critical Hit Chance; Critical Hits Poison the enemy; (100–150)% increased Evasion and Energy Shield |  |
| The Vertex | Tribal Mask | 33 | Has no Attribute Requirements; (100–150)% increased Evasion and Energy Shield; (20–30)% increased Critical Hit Chance; +(13–17)% to Chaos Resistance; Skill Gems have no Attribute Requirements |  |
| Glimpse of Chaos | Tribal Mask | 52 | Can be modified while Corrupted; +(50–150) to maximum Life; +(50–150) to maximum Mana; (-30–30)% to Fire Resistance; (-30–30)% to Cold Resistance; (-30–30)% to Lightning Resistance; Chaos Resistance is zero | Boss: The Trialmaster |
| The Three Dragons | Solid Mask | 45 | (40–60)% increased Evasion and Energy Shield; +(10–20)% to all Elemental Resistances; Fire Damage from Hits Contributes to Shock Chance instead of Flammability and Ignite Magnitudes; Cold Damage from Hits Contributes to Flammability and Ignite Magnitudes instead of Chill Magnitude or Freeze Buildup; Lightning Damage from Hits Contributes to Freeze Buildup instead of Shock Chance |  |
| Mind of the Council | Death Mask | 65 | (150–200)% increased Evasion and Energy Shield; +(60–90) to maximum Mana; +(20–30)% to Lightning Resistance; Attacks cost an additional 6% of your maximum Mana; Attacks have Added maximum Lightning Damage equal to (6–9)% of maximum Mana | Rel: Dawn of the Hunt |
| Solus Ipse | Grand Visage | 65 | +(60–100) to maximum Mana; 25% increased Light Radius; (150–200)% increased Armour , Evasion and Energy Shield; Equipment and Skill Gems have 25% increased Attribute Requirements; You can Socket 2 additional copies of each Lineage Support Gem , in different Skills | Boss: The Arbiter of Ash |
