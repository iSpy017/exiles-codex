---
title: Unique Body armour mods (0.5.x) - part 1 of 3
status: partial  # not in tracker
defaults: v=0.5.x vol=may-change conf=single-source
merged_from: [uniques-mods-body-1.md, uniques-mods-body-2.md, uniques-mods-body-3.md]
data: [data/uniques.csv, data/unique_mods.csv]  # generated from the crawl; query these instead of reading the tables
---

Status: done for this slot part (rows sorted by required level as listed by PoE2DB). Version: 0.5.x data (PoE2DB crawl 2026-11-23); not checked against 1.0. Volatility: may-change.
Source: poe2db:Unique_item (armour list, tier 2) plus each unique's own PoE2DB page (mod blocks, boss-drop and release-league lines), crawl 2026-11-23. Confidence: single-source.
Names per slot: [[items/uniques-armour]]. Drop restrictions and sources: [[items/uniques-drop-sources]]. Total uniques: [[items/uniques-index]].
Other parts of this slot: [[items/uniques-mods-body]], [[items/uniques-mods-body]]. Other slots: [[items/uniques-mods-body]], [[items/uniques-mods-helmet]], [[items/uniques-mods-gloves]], [[items/uniques-mods-boots]], [[items/uniques-mods-shields]].

## How to read
- Mods are paraphrased compactly; (a–b) are rolled ranges, fixed numbers are not rolled. Mod order follows PoE2DB mod blocks, not in-game order. Implicits and base defences are omitted. Req lvl = level only (attribute requirements omitted).
- Tag column: "Boss: X" = PoE2DB page says the item is dropped by that boss; "Rel: X" = release league shown on the page (blank = since 0.1.0 base data); "Drop disabled" = page carries the 「Drop disabled」 marker (22 item pages in the corpus carry it; the 12 armour ones are not on the Unique_item armour list and are appended here by hand, so the armour total is 221 listed + 12 = 233).
- Items whose PoE2DB page also shows a "Deferred" variant (differing base/level/mods) use the 0.5.5 block here.

## Body armour uniques

| Name | Base | Req lvl | Explicit mods | Tag |
|---|---|---|---|---|
| Bramblejack | Rusted Cuirass | 1 | +(60–100) to maximum Life; +(60–100) to Stun Threshold; 250% of Melee Physical Damage taken reflected to Attacker; Cannot Evade Enemy Attacks; Regenerate 5% of maximum Life per second while Surrounded |  |
| Blackbraid | Fur Plate | 4 | +(5–15) to Strength; +(5–15) to Intelligence; +(40–60) to Stun Threshold; +(100–150)% of Armour also applies to Elemental Damage; +(40–60) to Armour; +10% to all Elemental Resistances |  |
| Edyrn's Tusks | Iron Cuirass | 11 | (120–160)% increased Armour; 50% chance to inflict Bleeding on Hit; 50% reduced Slowing Potency of Debuffs on You; (15–20) to (25–30) Physical Thorns damage | 0.5.5 data (page also shows a Deferred variant) |
| The Road Warrior | Raider Plate | 16 | +(10–15) to all Attributes; +(15–30)% to Fire Resistance; +(15–30)% to Lightning Resistance; (10–15) Life Regeneration per second; Moving while Bleeding doesn't cause you to take extra damage | Drop disabled |
| Titanrot Cataphract | Maraketh Cuirass | 20 | (400–500)% increased Armour; (15–30)% increased Strength; 10% reduced Dexterity; 10% reduced Intelligence; You have no Life Regeneration |  |
| Wandering Reliquary | Steel Plate | 27 | (50–100)% increased Armour; +(40–60) to maximum Mana; +(10–20) to Strength; 50% of Physical Damage prevented Recouped as Life; +(60–80) to Stun Threshold |  |
| Kingsguard | Full Plate | 33 | +(60–80) to maximum Life; +(40–60) to maximum Mana; +(5–10)% to all Elemental Resistances; 25% reduced Endurance Charge Duration; Recover 5% of maximum Life for each Endurance Charge consumed |  |
| Greed's Embrace | Vaal Cuirass | 37 | 50% increased Strength Requirement; 20% reduced Movement Speed; (100–150)% increased Armour; (30–50)% increased Rarity of Items found; +(20–30)% to Fire Resistance |  |
| The Brass Dome | Champion Cuirass | 58 | (500–600)% increased Armour; (-5 to -1)% to all Maximum Elemental Resistances; +(200–300) to Stun Threshold; Take no Extra Damage from Critical Hits |  |
| Kaom's Heart | Conqueror Plate | 68 | (30–40)% increased Stun Threshold; +1500 to maximum Life; You have no Spirit |  |
| Bristleboar | Leather Vest | 1 | 50% reduced Evasion Rating; +(40–60) to maximum Life; Gain 5 Rage when Hit by an Enemy; Gain 10 Rage when Critically Hit by an Enemy; (3–5) Life Regeneration per second |  |
| Foxshade | Quilted Vest | 4 | +(20–30) to Dexterity; +(50–70) to Evasion Rating; 100% increased Evasion Rating when on Full Life; 10% increased Movement Speed when on Full Life |  |
| Ashrend | Pathfinder Coat | 11 | +(40–60) to maximum Life; +(30–40)% to Fire Resistance; Cannot be Ignited; -10 Physical Damage taken from Attack Hits; +(10–20) to Strength |  |
| Sands of Silk | Shrouded Vest | 16 | (50–100)% increased Evasion Rating; +(50–80) to maximum Mana; +(10–20) to Dexterity; +(10–20) to Intelligence; +(10–15)% to Fire Resistance; (15–30)% increased Cooldown Recovery Rate; Grants Blink (Lv5) | Rel: Dawn of the Hunt |
| Briskwrap | Rhoahide Coat | 22 | (40–60)% increased Flask Life Recovery rate; (40–60)% increased Flask Mana Recovery rate; +(20–30) to Dexterity; +(20–30)% to Cold Resistance; (60–100)% increased Evasion Rating; Gain Deflection Rating equal to (20–30)% of Evasion Rating |  |
| Dustbloom | Studded Vest | 26 | (100–150)% increased Evasion Rating; Maximum 10 Fragile Regrowth 0.5% of maximum Life Regenerated per second per Fragile Regrowth 10% increased Mana Regeneration Rate per Fragile Regrowth Lose all Fragile Regrowth when Hit Gain 1 Fragile Regrowth each second; +(20–30)% to Cold Resistance |  |
| The Rat Cage | Scout's Vest | 33 | (100–150)% increased Evasion Rating; +300 to maximum Life; 25% reduced Attribute Requirements; 100% of Fire Damage from Hits taken as Physical Damage |  |
| Quatl's Molt | Serpentscale Coat | 36 | +(60–80) to maximum Life; +(17–23)% to Chaos Resistance; (10–20) Life Regeneration per second; Cannot be Poisoned; (60–80)% increased Evasion Rating; Gain Deflection Rating equal to (40–60)% of Evasion Rating |  |
| Queen of the Forest | Smuggler Coat | 51 | (250–300)% increased Evasion Rating; (-15 to -10)% to Fire Resistance; +(25–30)% to Cold Resistance; +(10–15)% to Lightning Resistance; Increases Movement Speed by 25%, plus 1% per 600 Evasion Rating, up to a maximum of 75% Other Modifiers to Movement Speed except for Sprinting do not apply |  |
| Yriel's Fostering | Strider Vest | 52 | (100–150)% increased Evasion Rating; +(80–120) to maximum Life; +(10–30) to Spirit; (40–60)% reduced Duration of Bleeding on You; (40–60)% reduced Poison Duration on you; You can have two Companions of different types | Rel: Dawn of the Hunt |
| The Auspex | Exquisite Vest | 65 | Grants Mist Raven (Lv15); (210–240)% increased Evasion Rating; +(70–120) to maximum Life; 100% increased Attribute Requirements; Chance to Deflect is Lucky while on Low Life; Enemies in your Presence gain 1 Gruelling Madness each second | Boss: The Raven Trickster; Rel: Runes of Aldur |
| Hyrri's Ire | Armoured Vest | 73 | (30–40)% increased Elemental Ailment Threshold; (100–150)% increased Evasion Rating; +(30–40) to Dexterity; Evasion Rating is doubled if you have not been Hit Recently; Gain (10–20)% of Damage as Extra Cold Damage; 25% increased Freeze Duration on Enemies | Rel: Dawn of the Hunt |
| Ghostwrithe | Tattered Robe | 1 | +(29–37)% to Chaos Resistance; +100 to maximum Energy Shield; 35% of Maximum Life Converted to Energy Shield |  |
| Bitterbloom | Feathered Robe | 5 | (50–100)% increased Energy Shield; +(50–100) to maximum Mana; 50% increased Energy Shield Recharge Rate; Energy Shield Recharge starts when you use a Mana Flask |  |
| The Black Doubt | Hexer's Robe | 11 | (60–100)% increased Energy Shield; +(10–30) to Intelligence; Damage over Time bypasses your Energy Shield While not on Full Life, Sacrifice 10% of maximum Mana per Second to Recover that much Life; +(10–20)% to Cold Resistance |  |
| Necromantle | Bone Raiment | 16 | +(40–60) to maximum Life; +(30–50) to maximum Mana; Minions Revive 50% faster; Minions gain (20–30)% of their maximum Life as Extra maximum Energy Shield; Minions have +(17–23)% to Chaos Resistance |  |
| Cloak of Flame | Silk Robe | 22 | +(30–50)% to Fire Resistance; (30–50)% reduced Ignite Duration on you; 25 to 35 Fire Thorns damage; 50% of Physical Damage taken as Fire Damage; +(30–50) to maximum Energy Shield |  |
| Temporalis | Silk Robe | 64 | +(100–150) to maximum Energy Shield; +(10–20)% to all Elemental Resistances; (5–30)% of Damage taken Recouped as Life; (5–30)% of Damage taken Recouped as Mana; Skills have (-2 to -1) seconds to Cooldown | Boss: Zarokh, the Temporal |

<!-- merged from kb/items/uniques-mods-body-2.md -->
Part title: Unique Body armour mods (0.5.x) - part 2 of 3

Status: done for this slot part (rows sorted by required level as listed by PoE2DB). Version: 0.5.x data (PoE2DB crawl 2026-11-23); not checked against 1.0. Volatility: may-change.
Source: poe2db:Unique_item (armour list, tier 2) plus each unique's own PoE2DB page (mod blocks, boss-drop and release-league lines), crawl 2026-11-23. Confidence: single-source.
Names per slot: [[items/uniques-armour]]. Drop restrictions and sources: [[items/uniques-drop-sources]]. Total uniques: [[items/uniques-index]].
Other parts of this slot: [[items/uniques-mods-body]], [[items/uniques-mods-body]]. Other slots: [[items/uniques-mods-body]], [[items/uniques-mods-helmet]], [[items/uniques-mods-gloves]], [[items/uniques-mods-boots]], [[items/uniques-mods-shields]].

## How to read
- Mods are paraphrased compactly; (a–b) are rolled ranges, fixed numbers are not rolled. Mod order follows PoE2DB mod blocks, not in-game order. Implicits and base defences are omitted. Req lvl = level only (attribute requirements omitted).
- Tag column: "Boss: X" = PoE2DB page says the item is dropped by that boss; "Rel: X" = release league shown on the page (blank = since 0.1.0 base data); "Drop disabled" = page carries the 「Drop disabled」 marker (22 item pages in the corpus carry it; the 12 armour ones are not on the Unique_item armour list and are appended here by hand, so the armour total is 221 listed + 12 = 233).
- Items whose PoE2DB page also shows a "Deferred" variant (differing base/level/mods) use the 0.5.5 block here.

## Body armour uniques

| Name | Base | Req lvl | Explicit mods | Tag |
|---|---|---|---|---|
| Prayers for Rain | Keth Raiment | 28 | (60–100)% increased Energy Shield; +(10–15) to Intelligence; 30% slower start of Energy Shield Recharge; Energy Shield Recharge is not interrupted by Damage if Recharge began Recently; +(10–20)% to Lightning Resistance |  |
| Tetzlapokal's Desire | Votive Raiment | 33 | (100–150)% increased Energy Shield; +(20–30) to Strength; +(17–23)% to Chaos Resistance; Life Recharges; +(20–30) to Intelligence |  |
| The Covenant | Altar Robe | 40 | Grants Life Remnants (Lv10); (100–150)% increased Energy Shield; +(100–150) to maximum Life; 10% of Spell Damage Leeched as Life; Skills Gain 100% of Mana Cost as Extra Life Cost |  |
| Gloamgown | Elementalist Robe | 45 | (100–140)% increased Energy Shield; +(30–40) to Spirit; +(25–35)% to Cold Resistance; 1000% increased Energy Shield Recharge Rate; Your base Energy Shield Recharge Delay is 10 seconds | Rel: Dawn of the Hunt |
| Vis Mortis | Plated Raiment | 58 | (70–100)% increased Energy Shield; +(70–100) to maximum Mana; Minions have 50% reduced maximum Life; Minions have Unholy Might | Rel: Dawn of the Hunt |
| Cloak of Defiance | Havoc Raiment | 65 | (50–100)% increased Energy Shield; +(100–150) to maximum Mana; (50–100)% increased Mana Regeneration Rate; 50% of Damage is taken from Mana before Life | Rel: Dawn of the Hunt |
| Silks of Veneration | Enlightened Robe | 68 | (40–50)% increased Mana Regeneration Rate; +(30–50) to Spirit; +(20–30) to Intelligence; (30–50)% increased Energy Shield Recharge Rate; Current Energy Shield also grants Elemental Damage reduction; (150–200)% increased Energy Shield | Rel: Dawn of the Hunt |
| Coat of Red | Chain Mail | 1 | +(80–100) to maximum Life; +(75–150) to Stun Threshold; (80–100)% increased Armour and Evasion; 25% chance to be inflicted with Bleeding when Hit |  |
| The Barrow Dweller | Rogue Armour | 11 | (60–100)% increased Armour and Evasion; (-20 to -10)% to Fire Resistance; +50% to Cold Resistance; 50% chance to Avoid Death from Hits; Damage of Enemies Hitting you is Unlucky while you are on Low Life |  |
| Irongrasp | Vagabond Armour | 16 | (100–150)% increased Armour and Evasion; +(100–150) to Stun Threshold; Keystone: Iron Grip; Keystone: Iron Will; +(20–30) to Strength |  |
| Pariah's Embrace | Cloaked Mail | 26 | (50–80)% increased Armour and Evasion; (10–15) Life Regeneration per second; +50 to Spirit; +(10–15) to all Attributes; (20–40)% increased Mana Cost Efficiency |  |
| Belly of the Beast | Explorer Armour | 33 | (100–150)% increased Armour and Evasion; +(100–150) to maximum Life; +(100–150) to Stun Threshold; Life Recovery from Flasks is instant; (25–30) to (35–40) Physical Thorns damage |  |
| Pragmatism | Explorer Armour | 52 | (200–300)% increased Armour and Evasion; +(10–20)% to all Elemental Resistances; -17% to Chaos Resistance; Charms use no Charges | Boss: The King in the Mists |
| Doryani's Prototype | Scale Mail | 37 | (50–100)% increased Armour and Evasion; +(60–80) to maximum Life; +100% of Armour also applies to Lightning Damage; Enemies in your Presence have Lightning Resistance equal to yours; Lightning Resistance does not affect Lightning damage taken |  |
| Widow's Reign | Knight Armour | 45 | (100–150)% increased Armour and Evasion; +(100–150) to maximum Life; +(17–23)% to Chaos Resistance; +(200–300) to Ailment Threshold; Life that would be lost by taking Damage is instead Reserved until you take no Damage to Life for 3 seconds | Rel: Dawn of the Hunt |
| Perfidy | Knight Armour | 45 | (300–450)% increased Armour and Evasion; (10–30)% chance to Avoid Physical Damage from Hits; (10–30)% chance to Avoid Chaos Damage from Hits; Enemies in your Presence are Intimidated; (10–30)% chance to Avoid Fire Damage from Hits; (10–30)% chance to Avoid Cold Damage from Hits; (10–30)% chance to Avoid Lightning Damage from Hits | Boss: Kosis, The Revelation |
| The Sunken Vessel | Knight Armour | 45 | (120–180)% increased Armour and Evasion; +(80–120) to maximum Life; 30% reduced Life Recovery rate; 33% chance to avoid Projectiles; Physical Damage of Enemies Hitting you is Unlucky; Convert All Armour to Evasion Rating | Rel: Runes of Aldur |
| Lightning Coil | Ancestral Mail | 50 | Grants Valako's Charge (Lv12); (80–120)% increased Armour and Evasion; +(80–100) to maximum Life; +(20–30) to Dexterity; (-40 to -30)% to Lightning Resistance; (30–50)% of Physical damage from Hits taken as Lightning damage | Rel: Rise of the Abyssal |
| The Fallen Formation | Lamellar Mail | 52 | (100–200)% increased Armour and Evasion; +(20–30) to Strength; +(20–30) to Dexterity; (8–12) Life Regeneration per second; -20 to maximum Valour; Banners always have maximum Valour | 0.5.5 data (page also shows a Deferred variant); Rel: Dawn of the Hunt; No longer drops since 0.3.0 (page version history; "reintroduced at a later date") |
| The Coming Calamity | Heroic Armour | 65 | +(60–80) to maximum Life; +(30–40)% to all Elemental Resistances; Enemies in your Presence have no Elemental Resistances; Herald Skills deal (50–100)% increased Damage | Rel: Dawn of the Hunt |
| Enfolding Dawn | Pilgrim Vestments | 1 | (50–100)% increased Armour and Energy Shield; +100 to Spirit; +(5–15)% to all Elemental Resistances; Gain no inherent bonus from Intelligence |  |
| Icetomb | Mail Vestments | 16 | +(20–30) to Strength; +(20–30) to Intelligence; +(30–40)% to Cold Resistance; Gain Cold Thorns Damage equal to (10–18)% of your maximum Mana |  |
| Reverie | Shaman Mantle | 28 | Grants Rite of Restoration (Lv8); (100–150)% increased Armour and Energy Shield; +(17–23)% to Chaos Resistance; -10% to Fire Resistance; Cannot use Life Flasks Non-Unique Life Flasks apply their Effects constantly Recovery from Life Flasks cannot be Instant Recovery from your Life Flasks cannot be applied to anything other than you; (40–60)% less Life Flask Recovery | Rel: Runes of Aldur |
| Soul Mantle | Sacrificial Mantle | 36 | (80–120)% increased Armour and Energy Shield; +10 to Strength; +15 to Intelligence; +1 to maximum number of Summoned Totems; Inflicts a random Curse on you when your Totems die, ignoring Curse limit; +75 to Spirit | Rel: Dawn of the Hunt |
| The Mutable Star | Cleric Vestments | 45 | (100–150)% increased Armour and Energy Shield; (50–100)% increased Energy Shield Recharge Rate; (25–35) Life Regeneration per second; (30–50)% reduced Duration of Bleeding on You; (30–50)% reduced Ignite Duration on you; Defend against Hits as though you had 1% more Armour per 1% current Energy Shield | Rel: Dawn of the Hunt |

<!-- merged from kb/items/uniques-mods-body-3.md -->
Part title: Unique Body armour mods (0.5.x) - part 3 of 3

Status: done for this slot part (rows sorted by required level as listed by PoE2DB). Version: 0.5.x data (PoE2DB crawl 2026-11-23); not checked against 1.0. Volatility: may-change.
Source: poe2db:Unique_item (armour list, tier 2) plus each unique's own PoE2DB page (mod blocks, boss-drop and release-league lines), crawl 2026-11-23. Confidence: single-source.
Names per slot: [[items/uniques-armour]]. Drop restrictions and sources: [[items/uniques-drop-sources]]. Total uniques: [[items/uniques-index]].
Other parts of this slot: [[items/uniques-mods-body]], [[items/uniques-mods-body]]. Other slots: [[items/uniques-mods-body]], [[items/uniques-mods-helmet]], [[items/uniques-mods-gloves]], [[items/uniques-mods-boots]], [[items/uniques-mods-shields]].

## How to read
- Mods are paraphrased compactly; (a–b) are rolled ranges, fixed numbers are not rolled. Mod order follows PoE2DB mod blocks, not in-game order. Implicits and base defences are omitted. Req lvl = level only (attribute requirements omitted).
- Tag column: "Boss: X" = PoE2DB page says the item is dropped by that boss; "Rel: X" = release league shown on the page (blank = since 0.1.0 base data); "Drop disabled" = page carries the 「Drop disabled」 marker (22 item pages in the corpus carry it; the 12 armour ones are not on the Unique_item armour list and are appended here by hand, so the armour total is 221 listed + 12 = 233).
- Items whose PoE2DB page also shows a "Deferred" variant (differing base/level/mods) use the 0.5.5 block here.

## Body armour uniques

| Name | Base | Req lvl | Explicit mods | Tag |
|---|---|---|---|---|
| Waveshaper | Tideseer Mantle | 51 | +(100–200) to maximum Energy Shield; +(20–40) to Spirit; +(25–35)% to Fire Resistance; +(25–35)% to Cold Resistance; Increases and Reductions to Mana Regeneration Rate also apply to Energy Shield Recharge Rate; Gain (30–50)% of Maximum Mana as Armour | Rel: Dawn of the Hunt |
| Couture of Crimson | Gilded Vestments | 52 | (50–100)% increased Armour and Energy Shield; (10–15)% increased maximum Life; (40–60)% reduced Duration of Bleeding on You; Life Leech can Overflow Maximum Life |  |
| Geofri's Sanctuary | Revered Vestments | 65 | +1% to all Maximum Elemental Resistances; (150–200)% increased Armour; +(10–20)% to all Elemental Resistances; Your maximum Energy Shield is equal to (200–300)% of your Strength; Maximum Energy Shield cannot be Converted; Regenerate 2 Life per second for every 10 Intelligence; Keystone: Zealot's Oath | Rel: Runes of Aldur |
| The Unleashed | Revered Vestments | 65 | +1% to all Maximum Elemental Resistances; (150–250)% increased Armour and Energy Shield; +(10–20) to Strength and Intelligence; (15–25)% of Damage taken from Hits bypasses Energy Shield if Energy Shield is below half; Gain 1 Runic Binding on Hit with Spells, no more than once every 0.5 seconds Lose all Runic Bindings when you Shapeshift to gain that much Unbound Potential | Boss: The Aberration; Rel: Runes of Aldur |
| Sacrosanctum | Corvus Mantle | 68 | +(20–30) to Spirit; (80–120)% increased Armour and Energy Shield; +(20–30) to Strength; +(20–30) to Intelligence; +(17–23)% to Chaos Resistance; (10–20)% of Damage taken Recouped as Life; Damage taken Recouped as Life is also Recouped as Energy Shield | Rel: Dawn of the Hunt |
| Loreweave | Ornate Ringmail | 43 | Adds (1–4) to (8–12) Physical Damage to Attacks; +(200–300) to Accuracy Rating; +(20–30) to maximum Mana; (6–15)% increased Rarity of Items found; +(2–5)% to Quality of all Skills; (7–10)% increased Cast Speed; Your Maximum Resistances are (75–80)% | Rel: Runes of Aldur |
| Decree of Loyalty | Ancient Mail | 70 | (200–300)% increased Armour and Energy Shield; +(15–25) to Strength and Intelligence; +(1–5)% to Maximum Chaos Resistance; Convert 1% of maximum Life to twice as much Armour per 1% Chaos Resistance above 0%; Defend with (150–200)% of Armour while you have Energy Shield; Damage over Time cannot bypass your Energy Shield | Boss: The Arbiter of Divinity; Rel: Runes of Aldur |
| Apron of Emiran | Hermit Garb | 1 | (30–50)% increased Evasion and Energy Shield; +(10–20) to Dexterity; (40–60)% reduced Duration of Bleeding on You; Bleeding you inflict is Aggravated | 0.5.5 data (page also shows a Deferred variant) |
| Gloomform | Waxed Jacket | 11 | (100–150)% increased Evasion Rating; +(10–20) to Dexterity; 20% reduced Light Radius; You have a Smoke Cloud around you while stationary; +(10–20)% to Fire Resistance |  |
| Sierran Inheritance | Marabout Garb | 16 | (50–80)% increased Evasion and Energy Shield; +(30–40)% to Lightning Resistance; (15–30)% increased Energy Shield Recharge Rate; The Effect of Chill on you is reversed; -15% to Cold Resistance; All Damage taken from Hits Contributes to Magnitude of Chill inflicted on you |  |
| The Dancing Mirage | Wayfarer Jacket | 28 | (150–200)% increased Evasion and Energy Shield; +(10–20)% to Lightning Resistance; 20% less Damage taken if you have not been Hit Recently; 100% increased Evasion Rating if you have been Hit Recently |  |
| Redflare Conduit | Anchorite Garb | 33 | +(50–70) to maximum Mana; +(20–30)% to Lightning Resistance; 20% chance to gain a Power Charge on Hit; Lose all Power Charges on reaching maximum Power Charges; Shocks you when you reach maximum Power Charges |  |
| Zerphi's Serape | Scalper's Jacket | 39 | (60–80)% increased Evasion and Energy Shield; +(40–60) to maximum Mana; 50% increased Attribute Requirements; (-30–30)% reduced Life Regeneration rate; (-30–30)% reduced Mana Regeneration Rate; Soul Eater | Rel: Dawn of the Hunt |
| Cospri's Will | Assassin Garb | 73 | 5% increased Movement Speed; (150–200)% increased Evasion and Energy Shield; +(23–29)% to Chaos Resistance; Curses you inflict have infinite Duration; Curses you inflict can affect Hexproof Enemies; Withered you inflict has infinite Duration | Rel: Rise of the Abyssal |
| Tabula Rasa | Garment | 1 | Has 6 Jewel Sockets (Hidden) | Rel: Dawn of the Hunt |
| Skin of the Loyal | Garment | 1 | +(5–40)% to all Elemental Resistances; Elemental Ailment Threshold is increased by Uncapped Chaos Resistance; Armour is increased by Uncapped Fire Resistance; Energy Shield is increased by Uncapped Cold Resistance; Evasion Rating is increased by Uncapped Lightning Resistance | Boss: Xesht, We That Are One |
| Morior Invictus | Grand Regalia | 65 | (300–400)% increased Armour , Evasion and Energy Shield | Boss: The Arbiter of Ash |
| Atziri's Splendour | Sacrificial Regalia | 65 | +1 to Level of all Corrupted Skill Gems; Only Soul Cores can be Socketed in this item; (80–120)% increased Armour , Evasion and Energy Shield; +(10–20)% to all Elemental Resistances; Skills from Corrupted Gems have 50% of Mana Costs Converted to Life Costs; Has no Attribute Requirements | Rel: Fate of the Vaal |
| Voll's Protector | Plated Vestments | 59 | (150–200)% increased Armour and Energy Shield; 25% reduced maximum Mana; 25% chance to gain a Power Charge on Critical Hit; +(13–17)% to Chaos Resistance |  |
| Forgotten Warden | Primal Markings | 70 | Grants Spirit Vessel (Lv16); +(70–100) to Deflection Rating per 50 missing Energy Shield; (200–300)% increased Evasion and Energy Shield; +(20–30) to Dexterity; Companions have (30–50)% increased maximum Life; (10–15)% of Damage from Deflected Hits is taken from Damageable Companion 's Life before you | Boss: The Bodach; Rel: Runes of Aldur |

Drop disabled (not tabulated; page shows no readable explicit mods, only an internal string): Demigod's Valor (Golden Plate, Lv1).
