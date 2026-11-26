# Rune effects 1: basics + tiered runes (Desert, Glacial, Storm, Iron, Body)

- Status: partial set; this file done
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-rune pages and the Rune/Augment index pages, tier 2.

## Rune basics: tiers, sockets, Bonded
- Claim: Runes are Kalguuran-made Augments, stack 10, socketed into an empty Augment Socket of a weapon or armour; once in, a normal rune cannot be retrieved but can be replaced by another Augment (socket-bound ones cannot). Each rune lists effects per slot class: Martial Weapon (non-caster weapons), Wand or Staff (caster weapons), Armour, or a named slot. Tiers: Lesser (no level req, drop lvl 5-21), normal (req 15, drop 31-45), Greater (req 30, drop 52-62), Perfect (req 50, drop 65). Crafting Bench 'Three to One Reforge' turns 3 Lesser into 1 normal and 3 normal into 1 Greater; Perfect pages show no recipe, Masterwork Rune upgrades a socketed tiered rune. 'Bonded' lines are extra effects shown on the item that only work for a Druid who took the Shaman Ascendancy notable 'Wisdom of the Maji'; Fox Idol on a body armour also gives Bonded benefits to idols socketed in that item. Standard-rune Bonded armour effect is +20 life and +20 mana (0.5.0 notes).
- Version: 0.5.x
- Volatility: may-change
- Source: [Rune](https://poe2db.tw/us/Rune), [Augment](https://poe2db.tw/us/Augment), [Bonded Modifiers](https://poe2db.tw/us/Bonded_Modifiers), [Wisdom of the Maji](https://poe2db.tw/us/Wisdom_of_the_Maji), [Fox Idol](https://poe2db.tw/us/Fox_Idol), [Version 0.5.0](https://poe2db.tw/us/Version_0.5.0), [Desert Rune](https://poe2db.tw/us/Desert_Rune), tier 2, crawl 2026-11-23
- Confidence: confirmed (several pages agree)
- Notes: Older patch note Version_0.2.0f: lower tiers removed from drop pool as tiers unlock (Lesser stops past lvl 31, normal past 52) - 0.2.x era, may be outdated. Blank Rune / Blank Greater Rune are quest items exchanged with Renly / Dannig for a chosen rune ([Blank Rune](https://poe2db.tw/us/Blank_Rune)). Bonded grant by anything other than Wisdom of the Maji and Fox Idol: not found. See [[items/soul-core-idol-effects]].

## Desert Rune family
- Claim: effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Desert | -/5 | Martial Weapon: Adds 4 to 6 Fire Damage ; Wand or Staff: Gain 6% of Damage as Extra Fire Damage ; Armour: +10% to Fire Resistance |
| Desert | 15/31 | Martial Weapon: Adds 7 to 11 Fire Damage ; Wand or Staff: Gain 8% of Damage as Extra Fire Damage ; Armour: +14% to Fire Resistance |
| Greater Desert | 30/52 | Martial Weapon: Adds 13 to 16 Fire Damage ; Wand or Staff: Gain 10% of Damage as Extra Fire Damage ; Armour: +18% to Fire Resistance |
| Perfect Desert | 50/65 | Martial Weapon: Adds 17 to 20 Fire Damage ; Wand or Staff: Gain 12% of Damage as Extra Fire Damage ; Armour: +22% to Fire Resistance |
Bonded (all tiers): Martial Weapon: 30% increased Ignite Magnitude ; Wand or Staff: 30% increased Ignite Magnitude ; Armour: +20 to maximum Life, +20 to maximum Mana
- Version: 0.5.x
- Volatility: may-change
- Source: [Lesser_Desert_Rune](https://poe2db.tw/us/Lesser_Desert_Rune), [Desert_Rune](https://poe2db.tw/us/Desert_Rune), [Greater_Desert_Rune](https://poe2db.tw/us/Greater_Desert_Rune), [Perfect_Desert_Rune](https://poe2db.tw/us/Perfect_Desert_Rune), tier 2, crawl 2026-11-23
- Confidence: single-source (per-tier pages; Rune/Augment index pages agree)
- Notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).

## Glacial Rune family
- Claim: effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Glacial | -/5 | Martial Weapon: Adds 3 to 5 Cold Damage ; Wand or Staff: Gain 6% of Damage as Extra Cold Damage ; Armour: +10% to Cold Resistance |
| Glacial | 15/31 | Martial Weapon: Adds 6 to 10 Cold Damage ; Wand or Staff: Gain 8% of Damage as Extra Cold Damage ; Armour: +14% to Cold Resistance |
| Greater Glacial | 30/52 | Martial Weapon: Adds 9 to 15 Cold Damage ; Wand or Staff: Gain 10% of Damage as Extra Cold Damage ; Armour: +18% to Cold Resistance |
| Perfect Glacial | 50/65 | Martial Weapon: Adds 16 to 20 Cold Damage ; Wand or Staff: Gain 12% of Damage as Extra Cold Damage ; Armour: +22% to Cold Resistance |
Bonded (all tiers): Martial Weapon: 30% increased Freeze Buildup ; Wand or Staff: 30% increased Freeze Buildup ; Armour: +20 to maximum Life, +20 to maximum Mana
- Version: 0.5.x
- Volatility: may-change
- Source: [Lesser_Glacial_Rune](https://poe2db.tw/us/Lesser_Glacial_Rune), [Glacial_Rune](https://poe2db.tw/us/Glacial_Rune), [Greater_Glacial_Rune](https://poe2db.tw/us/Greater_Glacial_Rune), [Perfect_Glacial_Rune](https://poe2db.tw/us/Perfect_Glacial_Rune), tier 2, crawl 2026-11-23
- Confidence: single-source (per-tier pages; Rune/Augment index pages agree)
- Notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).

## Storm Rune family
- Claim: effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Storm | -/5 | Martial Weapon: Adds 1 to 10 Lightning Damage ; Wand or Staff: Gain 6% of Damage as Extra Lightning Damage ; Armour: +10% to Lightning Resistance |
| Storm | 15/31 | Martial Weapon: Adds 1 to 20 Lightning Damage ; Wand or Staff: Gain 8% of Damage as Extra Lightning Damage ; Armour: +14% to Lightning Resistance |
| Greater Storm | 30/52 | Martial Weapon: Adds 1 to 30 Lightning Damage ; Wand or Staff: Gain 10% of Damage as Extra Lightning Damage ; Armour: +18% to Lightning Resistance |
| Perfect Storm | 50/65 | Martial Weapon: Adds 1 to 40 Lightning Damage ; Wand or Staff: Gain 12% of Damage as Extra Lightning Damage ; Armour: +22% to Lightning Resistance |
Bonded (all tiers): Martial Weapon: 30% increased Magnitude of Shock you inflict ; Wand or Staff: 30% increased Magnitude of Shock you inflict ; Armour: +20 to maximum Life, +20 to maximum Mana
- Version: 0.5.x
- Volatility: may-change
- Source: [Lesser_Storm_Rune](https://poe2db.tw/us/Lesser_Storm_Rune), [Storm_Rune](https://poe2db.tw/us/Storm_Rune), [Greater_Storm_Rune](https://poe2db.tw/us/Greater_Storm_Rune), [Perfect_Storm_Rune](https://poe2db.tw/us/Perfect_Storm_Rune), tier 2, crawl 2026-11-23
- Confidence: single-source (per-tier pages; Rune/Augment index pages agree)
- Notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).

## Iron Rune family
- Claim: effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Iron | -/5 | Martial Weapon: 14% increased Physical Damage ; Wand or Staff: 20% increased Spell Damage ; Armour: 14% increased Armour, Evasion and Energy Shield |
| Iron | 15/31 | Martial Weapon: 16% increased Physical Damage ; Wand or Staff: 25% increased Spell Damage ; Armour: 16% increased Armour, Evasion and Energy Shield |
| Greater Iron | 30/52 | Martial Weapon: 18% increased Physical Damage ; Wand or Staff: 30% increased Spell Damage ; Armour: 18% increased Armour, Evasion and Energy Shield |
| Perfect Iron | 50/65 | Martial Weapon: 20% increased Physical Damage ; Wand or Staff: 35% increased Spell Damage ; Armour: 20% increased Armour, Evasion and Energy Shield |
Bonded (all tiers): Martial Weapon: 20% increased effect of Fully Broken Armour ; Wand or Staff: Break Armour on Critical Hit with Spells equal to 12% of Physical Damage dealt ; Armour: +20 to maximum Life, +20 to maximum Mana
- Version: 0.5.x
- Volatility: may-change
- Source: [Lesser_Iron_Rune](https://poe2db.tw/us/Lesser_Iron_Rune), [Iron_Rune](https://poe2db.tw/us/Iron_Rune), [Greater_Iron_Rune](https://poe2db.tw/us/Greater_Iron_Rune), [Perfect_Iron_Rune](https://poe2db.tw/us/Perfect_Iron_Rune), tier 2, crawl 2026-11-23
- Confidence: single-source (per-tier pages; Rune/Augment index pages agree)
- Notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).

## Body Rune family
- Claim: effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Body | -/11 | Martial Weapon: Leeches 3% of Physical Damage as Life ; Wand or Staff: +30 to maximum Energy Shield ; Armour: +30 to maximum Life |
| Body | 15/37 | Martial Weapon: Leeches 4% of Physical Damage as Life ; Wand or Staff: +40 to maximum Energy Shield ; Armour: +45 to maximum Life |
| Greater Body | 30/57 | Martial Weapon: Leeches 5% of Physical Damage as Life ; Wand or Staff: +50 to maximum Energy Shield ; Armour: +60 to maximum Life |
| Perfect Body | 50/65 | Martial Weapon: Leeches 6% of Physical Damage as Life ; Wand or Staff: +60 to maximum Energy Shield ; Armour: +75 to maximum Life |
Bonded (all tiers): Martial Weapon: 5% increased maximum Life ; Wand or Staff: 5% increased maximum Life ; Armour: +20 to maximum Life, +20 to maximum Mana
- Version: 0.5.x
- Volatility: may-change
- Source: [Lesser_Body_Rune](https://poe2db.tw/us/Lesser_Body_Rune), [Body_Rune](https://poe2db.tw/us/Body_Rune), [Greater_Body_Rune](https://poe2db.tw/us/Greater_Body_Rune), [Perfect_Body_Rune](https://poe2db.tw/us/Perfect_Body_Rune), tier 2, crawl 2026-11-23
- Confidence: single-source (per-tier pages; Rune/Augment index pages agree)
- Notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).
