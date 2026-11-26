# Essence table: Lesser and Normal tiers

Status: done for Lesser and Normal (one row per class group). Greater and Perfect are in [[crafting/essence-table-high]]. Overview, mechanics and conflicts: [[crafting/essences]].
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against 1.0.
Source summary: per-class tables on each essence page of PoE2DB.

## Lesser and Normal essence mods by family
- Claim: Lesser and Normal essences upgrade a Magic item to Rare and add the guaranteed mod below. Classes not listed for a family cannot take it.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Essence](https://poe2db.tw/us/Essence) plus each `Lesser_/Greater_/Perfect_Essence_of_<X>` and `Essence_of_<X>` page, tier 2, crawl 2026-11-23
- Confidence: single-source (PoE2DB game data; the Essence overview page and per-essence pages agree on the numbers checked)
- Notes: Legend: P/S = prefix/suffix. Mod lvl = required modifier level shown by PoE2DB. "1H wpn+Bow" = 1H Sword/Axe/Mace, Spear, Dagger, Bow, Flail. "2H wpn+Xbow+Talisman" = 2H Sword/Axe/Mace, Quarterstaff, Crossbow, Talisman. "armour" = Helm, Body, Gloves, Boots, Shield, Buckler. "all 13 attack-weapon classes" = both groups. Drop lvl = DropLevel field. All numbers are 0.5.x-era PoE2DB data, not checked for 1.0.

| Family | Tier | Drop lvl | Mod (range) | P/S | Mod lvl | Classes |
|---|---|---|---|---|---|---|
| the Body | Lesser | 25 | +(30-39) to maximum Life | P | 12 | armour+Focus, Belt |
| the Body | Lesser | 25 | +(20-29) to maximum Life | P | 4 | Amulet, Ring |
| the Body | Normal | 40 | +(85-99) to maximum Life | P | 36 | Belt, Body, Buckler, Helm, Shield |
| the Body | Normal | 40 | +(70-84) to maximum Life | P | 30 | Amulet, Boots, Gloves, Ring |
| the Mind | Lesser | 25 | +(25-34) to maximum Mana | P | 12 | Amulet, Belt, Boots, Gloves, Helm, Ring |
| the Mind | Normal | 40 | +(65-79) to maximum Mana | P | 30 | Belt, Boots, Gloves, Helm |
| the Mind | Normal | 40 | +(80-89) to maximum Mana | P | 36 | Amulet, Ring |
| Enhancement | Lesser | 20 | (27-42)% increased Armour, Evasion and Energy Shield | P | 12 | armour+Focus |
| Enhancement | Normal | 40 | (56-67)% increased Armour, Evasion and Energy Shield | P | 36 | armour+Focus |
| Abrasion | Lesser | 25 | Adds (4-6) to (7-11) Physical Damage | P | 6 | 1H wpn+Bow |
| Abrasion | Lesser | 25 | Adds (5-8) to (10-15) Physical Damage | P | 6 | 2H wpn+Xbow+Talisman |
| Abrasion | Normal | 40 | Adds (10-15) to (18-26) Physical Damage | P | 36 | 1H wpn+Bow |
| Abrasion | Normal | 40 | Adds (14-21) to (25-37) Physical Damage | P | 36 | 2H wpn+Xbow+Talisman |
| Flames | Lesser | 25 | Adds (4-6) to (7-10) Fire Damage | P | 6 | 1H wpn+Bow |
| Flames | Lesser | 25 | Adds (6-9) to (10-16) Fire Damage | P | 6 | 2H wpn+Xbow+Talisman |
| Flames | Normal | 40 | Adds (20-24) to (32-37) Fire Damage | P | 36 | 1H wpn+Bow |
| Flames | Normal | 40 | Adds (30-37) to (45-56) Fire Damage | P | 36 | 2H wpn+Xbow+Talisman |
| Ice | Lesser | 25 | Adds (3-5) to (6-9) Cold Damage | P | 6 | 1H wpn+Bow |
| Ice | Lesser | 25 | Adds (5-8) to (9-14) Cold Damage | P | 6 | 2H wpn+Xbow+Talisman |
| Ice | Normal | 40 | Adds (17-20) to (26-32) Cold Damage | P | 36 | 1H wpn+Bow |
| Ice | Normal | 40 | Adds (25-30) to (38-46) Cold Damage | P | 36 | 2H wpn+Xbow+Talisman |
| Electricity | Lesser | 25 | Adds 1 to (13-19) Lightning Damage | P | 6 | 1H wpn+Bow |
| Electricity | Lesser | 25 | Adds (1-2) to (19-27) Lightning Damage | P | 6 | 2H wpn+Xbow+Talisman |
| Electricity | Normal | 40 | Adds (1-3) to (55-60) Lightning Damage | P | 36 | 1H wpn+Bow |
| Electricity | Normal | 40 | Adds (1-4) to (80-88) Lightning Damage | P | 36 | 2H wpn+Xbow+Talisman |
| Ruin | Lesser | 25 | +(4-7)% to Chaos Resistance | S | 12 | armour+Focus+rings/amulets/belts |
| Ruin | Normal | 40 | +(8-11)% to Chaos Resistance | S | 24 | armour+Focus+rings/amulets/belts |
| Battle | Lesser | 20 | +(61-84) to Accuracy Rating | P | 14 | all 13 attack-weapon classes |
| Battle | Normal | 40 | +(124-167) to Accuracy Rating | P | 28 | all 13 attack-weapon classes |
| Sorcery | Lesser | 20 | (35-44)% increased Spell Damage | P | 6 | Focus, Wand |
| Sorcery | Lesser | 20 | (69-88)% increased Spell Damage | P | 6 | Staff |
| Sorcery | Normal | 40 | (55-64)% increased Spell Damage | P | 26 | Focus, Wand |
| Sorcery | Normal | 40 | (109-128)% increased Spell Damage | P | 26 | Staff |
| Alacrity | Lesser | 1 | (13-16)% increased Cast Speed | S | 12 | Focus, Wand |
| Alacrity | Lesser | 1 | (20-25)% increased Cast Speed | S | 12 | Staff |
| Alacrity | Normal | 1 | (17-20)% increased Cast Speed | S | 24 | Focus, Wand |
| Alacrity | Normal | 1 | (26-31)% increased Cast Speed | S | 24 | Staff |
| Haste | Lesser | 25 | (11-13)% increased Attack Speed | S | 17 | Dagger, Flail, 1H Axe, 1H Mace, 1H Sword, Qstaff, Spear, Talisman, 2H Axe, 2H Mace, 2H Sword |
| Haste | Lesser | 25 | (8-10)% increased Attack Speed | S | 8 | Bow, Xbow |
| Haste | Normal | 40 | (17-19)% increased Attack Speed | S | 29 | Dagger, Flail, 1H Axe, 1H Mace, 1H Sword, Qstaff, Spear, Talisman, 2H Axe, 2H Mace, 2H Sword |
| Haste | Normal | 40 | (11-13)% increased Attack Speed | S | 17 | Bow, Xbow |
| Seeking | Lesser | 20 | +(1.51-2.1)% to Critical Hit Chance | S | 16 | all 13 attack-weapon classes |
| Seeking | Lesser | 20 | (34-39)% increased Critical Hit Chance for Spells | S | 16 | Focus, Wand |
| Seeking | Lesser | 20 | (50-59)% increased Critical Hit Chance for Spells | S | 16 | Staff |
| Seeking | Normal | 40 | +(2.11-2.7)% to Critical Hit Chance | S | 24 | all 13 attack-weapon classes |
| Seeking | Normal | 40 | (40-46)% increased Critical Hit Chance for Spells | S | 22 | Focus, Wand |
| Seeking | Normal | 40 | (60-69)% increased Critical Hit Chance for Spells | S | 22 | Staff |
| the Infinite | Lesser | 20 | +(9-12) to Strength, Dexterity or Intelligence | S | 8 | all gear |
| the Infinite | Normal | 40 | +(17-20) to Strength, Dexterity or Intelligence | S | 26 | all gear |
| Command | Lesser | 1 | Allies in your Presence deal (35-44)% increased Damage | P | 6 | Sceptre |
| Command | Normal | 1 | Allies in your Presence deal (55-64)% increased Damage | P | 26 | Sceptre |
| Insulation | Lesser | 1 | +(11-15)% to Fire Resistance | S | 9 | armour+Focus+rings/amulets/belts |
| Insulation | Normal | 1 | +(21-25)% to Fire Resistance | S | 28 | armour+Focus+rings/amulets/belts |
| Thawing | Lesser | 1 | +(11-15)% to Cold Resistance | S | 11 | armour+Focus+rings/amulets/belts |
| Thawing | Normal | 1 | +(21-25)% to Cold Resistance | S | 30 | armour+Focus+rings/amulets/belts |
| Grounding | Lesser | 1 | +(11-15)% to Lightning Resistance | S | 10 | armour+Focus+rings/amulets/belts |
| Grounding | Normal | 1 | +(21-25)% to Lightning Resistance | S | 29 | armour+Focus+rings/amulets/belts |
| Opulence | Lesser | 1 | (6-10)% increased Rarity of Items found | S | 2 | Amulet, Boots, Gloves, Helm, Ring |
| Opulence | Normal | 1 | (11-14)% increased Rarity of Items found | S | 19 | Amulet, Boots, Gloves, Helm, Ring |

