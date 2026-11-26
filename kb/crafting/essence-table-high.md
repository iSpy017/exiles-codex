---
title: Essence table: Greater and Perfect tiers
status: partial  # not in tracker
defaults: v=0.5.x
data: [data/poe2db/Essence.tsv]  # generated from the crawl; query these instead of reading the tables
---

Status: done for Greater and Perfect. Lesser and Normal are in [[crafting/essence-table]]. Overview, mechanics and conflicts: [[crafting/essences]].
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against 1.0.
Source summary: per-class tables on each essence page of PoE2DB.

## Greater and Perfect essence mods by family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Greater essences work like Lesser/Normal (Magic to Rare, guaranteed mod). Perfect essences instead act on a Rare item: remove a random modifier, then add the guaranteed mod. Perfect mods are different in kind (extra damage as, skill levels, recoup, etc.), not just bigger numbers.
- src: poe2db:Essence plus each `Lesser_/Greater_/Perfect_Essence_of_<X>` and `Essence_of_<X>` page, tier 2, crawl 2026-11-23
- conf: single-source (PoE2DB game data)
- notes: Legend: P/S = prefix/suffix. Mod lvl = required modifier level shown by PoE2DB. "1H wpn+Bow" = 1H Sword/Axe/Mace, Spear, Dagger, Bow, Flail. "2H wpn+Xbow+Talisman" = 2H Sword/Axe/Mace, Quarterstaff, Crossbow, Talisman. "armour" = Helm, Body, Gloves, Boots, Shield, Buckler. "all 13 attack-weapon classes" = both groups. Drop lvl = DropLevel field. All numbers are 0.5.x-era PoE2DB data, not checked for 1.0. Greater Battle also covers Gloves and Quivers.

| Family | Tier | Drop lvl | Mod (range) | P/S | Mod lvl | Classes |
|---|---|---|---|---|---|---|
| the Body | Greater | 60 | +(100-119) to maximum Life | P | 43 | Belt, Body, Buckler, Helm, Shield |
| the Body | Greater | 60 | +(85-99) to maximum Life | P | 36 | Amulet, Boots, Gloves |
| the Body | Perfect | 72 | (8-10)% increased maximum Life | P | 57 | Body |
| the Mind | Greater | 60 | +(80-89) to maximum Mana | P | 36 | Belt, Boots, Gloves, Helm |
| the Mind | Greater | 60 | +(90-104) to maximum Mana | P | 43 | Amulet, Ring |
| the Mind | Perfect | 72 | (4-6)% increased maximum Mana | P | 57 | Ring |
| Enhancement | Greater | 60 | (68-79)% increased Armour, Evasion and Energy Shield | P | 43 | armour+Focus |
| Enhancement | Perfect | 72 | (20-30)% increased Global Armour, Evasion and Energy Shield | P | 57 | Amulet |
| Abrasion | Greater | 60 | Adds (16-24) to (28-42) Physical Damage | P | 48 | 1H wpn+Bow |
| Abrasion | Greater | 60 | Adds (23-35) to (39-59) Physical Damage | P | 48 | 2H wpn+Xbow+Talisman |
| Abrasion | Perfect | 72 | Gain (15-20)% of Damage as Extra Physical Damage | P | 57 | 1H wpn+Bow |
| Abrasion | Perfect | 72 | Gain (25-33)% of Damage as Extra Physical Damage | P | 57 | 2H wpn+Xbow+Talisman |
| Flames | Greater | 60 | Adds (35-44) to (56-71) Fire Damage | P | 48 | 1H wpn+Bow |
| Flames | Greater | 60 | Adds (56-70) to (84-107) Fire Damage | P | 48 | 2H wpn+Xbow+Talisman |
| Flames | Perfect | 72 | Gain (15-20)% of Damage as Extra Fire Damage | P | 57 | 1H wpn+Bow |
| Flames | Perfect | 72 | Gain (25-33)% of Damage as Extra Fire Damage | P | 57 | 2H wpn+Xbow+Talisman |
| Ice | Greater | 60 | Adds (31-38) to (47-59) Cold Damage | P | 48 | 1H wpn+Bow |
| Ice | Greater | 60 | Adds (46-57) to (70-88) Cold Damage | P | 48 | 2H wpn+Xbow+Talisman |
| Ice | Perfect | 72 | Gain (15-20)% of Damage as Extra Cold Damage | P | 57 | 1H wpn+Bow |
| Ice | Perfect | 72 | Gain (25-33)% of Damage as Extra Cold Damage | P | 57 | 2H wpn+Xbow+Talisman |
| Electricity | Greater | 60 | Adds (1-6) to (85-107) Lightning Damage | P | 48 | 1H wpn+Bow |
| Electricity | Greater | 60 | Adds (1-8) to (128-162) Lightning Damage | P | 48 | 2H wpn+Xbow+Talisman |
| Electricity | Perfect | 72 | Gain (15-20)% of Damage as Extra Lightning Damage | P | 57 | 1H wpn+Bow |
| Electricity | Perfect | 72 | Gain (25-33)% of Damage as Extra Lightning Damage | P | 57 | 2H wpn+Xbow+Talisman |
| Ruin | Greater | 60 | +(16-19)% to Chaos Resistance | S | 44 | armour+Focus+rings/amulets/belts |
| Ruin | Perfect | 72 | (10-15)% of Physical Damage from Hits taken as Chaos Damage | P | 57 | Body |
| Battle | Greater | 60 | +(237-346) to Accuracy Rating | P | 46 | all 13 attack-weapon classes, Gloves, Quiver |
| Battle | Perfect | 72 | +2 to Level of all Attack Skills | S | 57 | 1H wpn+Bow |
| Battle | Perfect | 72 | +3 to Level of all Attack Skills | S | 57 | 2H wpn+Xbow+Talisman |
| Sorcery | Greater | 60 | (75-89)% increased Spell Damage | P | 48 | Focus, Wand |
| Sorcery | Greater | 60 | (149-188)% increased Spell Damage | P | 48 | Staff |
| Sorcery | Perfect | 72 | +3 to Level of all Spell Skills | S | 57 | Wand |
| Sorcery | Perfect | 72 | +5 to Level of all Spell Skills | S | 57 | Staff |
| Alacrity | Greater | 1 | (25-28)% increased Cast Speed | S | 48 | Focus, Wand |
| Alacrity | Greater | 1 | (38-43)% increased Cast Speed | S | 48 | Staff |
| Alacrity | Perfect | 1 | (18-20)% increased Mana Cost Efficiency | S | 57 | Focus, Wand |
| Alacrity | Perfect | 1 | (28-32)% increased Mana Cost Efficiency | S | 57 | Staff |
| Haste | Greater | 60 | (23-25)% increased Attack Speed | S | 48 | Dagger, Flail, 1H Axe, 1H Mace, 1H Sword, Qstaff, Spear, Talisman, 2H Axe, 2H Mace, 2H Sword |
| Haste | Greater | 60 | (14-16)% increased Attack Speed | S | 24 | Bow, Xbow |
| Haste | Perfect | 72 | (20-25)% chance to gain Onslaught on Killing Hits with this Weapon | S | 57 | all 13 attack-weapon classes |
| Seeking | Greater | 60 | +(3.11-3.8)% to Critical Hit Chance | S | 35 | all 13 attack-weapon classes |
| Seeking | Greater | 60 | (47-53)% increased Critical Hit Chance for Spells | S | 32 | Focus, Wand |
| Seeking | Greater | 60 | (70-79)% increased Critical Hit Chance for Spells | S | 32 | Staff |
| Seeking | Perfect | 72 | Hits against you have (40-50)% reduced Critical Damage Bonus | S | 57 | Body |
| the Infinite | Greater | 60 | +(25-27) to Strength, Dexterity or Intelligence | S | 44 | all gear |
| the Infinite | Perfect | 72 | (7-10)% increased Strength, Dexterity or Intelligence | S | 57 | Amulet |
| Command | Greater | 1 | Allies in your Presence deal (75-89)% increased Damage | P | 48 | Sceptre |
| Command | Perfect | 1 | Aura Skills have (15-20)% increased Magnitudes | S | 57 | Sceptre |
| Insulation | Greater | 1 | +(31-35)% to Fire Resistance | S | 48 | armour+Focus+rings/amulets/belts |
| Insulation | Perfect | 1 | (26-30)% of Fire Damage taken Recouped as Life | S | 57 | Belt |
| Thawing | Greater | 1 | +(31-35)% to Cold Resistance | S | 48 | armour+Focus+rings/amulets/belts |
| Thawing | Perfect | 1 | (26-30)% of Cold Damage taken Recouped as Life | S | 57 | Helm |
| Grounding | Greater | 1 | +(31-35)% to Lightning Resistance | S | 48 | armour+Focus+rings/amulets/belts |
| Grounding | Perfect | 1 | (26-30)% of Lightning Damage taken Recouped as Life | S | 57 | Gloves |
| Opulence | Greater | 1 | (15-18)% increased Rarity of Items found | S | 32 | Amulet, Boots, Gloves, Helm, Ring |
| Opulence | Perfect | 1 | (10-15)% increased Quantity of Gold Dropped by Slain Enemies | S | 57 | Gloves |
