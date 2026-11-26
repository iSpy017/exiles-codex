---
title: Rune effects 1: basics + tiered runes (Desert, Glacial, Storm, Iron, Body)
status: done
tracker_topic: "Rune effects by slot"
tracker_note: "done (0.5.x; every rune incl. Warding, Ancient, named, Aldur, 63 Legacy runes; Bonded effects; drop sources not in corpus)"
defaults: v=0.5.x
merged_from: [rune-effects.md, rune-effects-2.md, rune-effects-3.md, rune-effects-4.md, rune-effects-5.md, rune-effects-6.md, rune-effects-7.md, rune-effects-8.md]
data: [data/poe2db/Adept_Rune.tsv, data/poe2db/Aldurs_Legacy.tsv, data/poe2db/Ancient_Rune_of_Decay.tsv, data/poe2db/Body_Rune.tsv, data/poe2db/Breath_of_Aldur.tsv, data/poe2db/Cadigans_Epiphany.tsv, data/poe2db/Charging_Rune.tsv, data/poe2db/Countess_Seskes_Rune_of_Archery.tsv, data/poe2db/Courtesan_Mannans_Rune_of_Cruelty.tsv, data/poe2db/Craiceanns_Rune_of_Recovery.tsv, data/poe2db/Desert_Rune.tsv, data/poe2db/Fox_Idol.tsv]  # generated from the crawl; query these instead of reading the tables
---

- Status: partial set; this file done
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-rune pages and the Rune/Augment index pages, tier 2.

## Rune basics: tiers, sockets, Bonded
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Runes are Kalguuran-made Augments, stack 10, socketed into an empty Augment Socket of a weapon or armour; once in, a normal rune cannot be retrieved but can be replaced by another Augment (socket-bound ones cannot). Each rune lists effects per slot class: Martial Weapon (non-caster weapons), Wand or Staff (caster weapons), Armour, or a named slot. Tiers: Lesser (no level req, drop lvl 5-21), normal (req 15, drop 31-45), Greater (req 30, drop 52-62), Perfect (req 50, drop 65). Crafting Bench 'Three to One Reforge' turns 3 Lesser into 1 normal and 3 normal into 1 Greater; Perfect pages show no recipe, Masterwork Rune upgrades a socketed tiered rune. 'Bonded' lines are extra effects shown on the item that only work for a Druid who took the Shaman Ascendancy notable 'Wisdom of the Maji'; Fox Idol on a body armour also gives Bonded benefits to idols socketed in that item. Standard-rune Bonded armour effect is +20 life and +20 mana (0.5.0 notes).
- src: poe2db:Rune, poe2db:Augment, poe2db:Bonded_Modifiers, poe2db:Wisdom_of_the_Maji, poe2db:Fox_Idol, poe2db:Version_0.5.0, poe2db:Desert_Rune, tier 2, crawl 2026-11-23
- conf: confirmed (several pages agree)
- notes: Older patch note Version_0.2.0f: lower tiers removed from drop pool as tiers unlock (Lesser stops past lvl 31, normal past 52) - 0.2.x era, may be outdated. Blank Rune / Blank Greater Rune are quest items exchanged with Renly / Dannig for a chosen rune ([Blank Rune](https://poe2db.tw/us/Blank_Rune)). Bonded grant by anything other than Wisdom of the Maji and Fox Idol: not found. See [[items/soul-core-idol-effects]].


## Desert Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Desert | -/5 | Martial Weapon: Adds 4 to 6 Fire Damage ; Wand or Staff: Gain 6% of Damage as Extra Fire Damage ; Armour: +10% to Fire Resistance |
| Desert | 15/31 | Martial Weapon: Adds 7 to 11 Fire Damage ; Wand or Staff: Gain 8% of Damage as Extra Fire Damage ; Armour: +14% to Fire Resistance |
| Greater Desert | 30/52 | Martial Weapon: Adds 13 to 16 Fire Damage ; Wand or Staff: Gain 10% of Damage as Extra Fire Damage ; Armour: +18% to Fire Resistance |
| Perfect Desert | 50/65 | Martial Weapon: Adds 17 to 20 Fire Damage ; Wand or Staff: Gain 12% of Damage as Extra Fire Damage ; Armour: +22% to Fire Resistance |
Bonded (all tiers): Martial Weapon: 30% increased Ignite Magnitude ; Wand or Staff: 30% increased Ignite Magnitude ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Desert_Rune, poe2db:Desert_Rune, poe2db:Greater_Desert_Rune, poe2db:Perfect_Desert_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Glacial Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Glacial | -/5 | Martial Weapon: Adds 3 to 5 Cold Damage ; Wand or Staff: Gain 6% of Damage as Extra Cold Damage ; Armour: +10% to Cold Resistance |
| Glacial | 15/31 | Martial Weapon: Adds 6 to 10 Cold Damage ; Wand or Staff: Gain 8% of Damage as Extra Cold Damage ; Armour: +14% to Cold Resistance |
| Greater Glacial | 30/52 | Martial Weapon: Adds 9 to 15 Cold Damage ; Wand or Staff: Gain 10% of Damage as Extra Cold Damage ; Armour: +18% to Cold Resistance |
| Perfect Glacial | 50/65 | Martial Weapon: Adds 16 to 20 Cold Damage ; Wand or Staff: Gain 12% of Damage as Extra Cold Damage ; Armour: +22% to Cold Resistance |
Bonded (all tiers): Martial Weapon: 30% increased Freeze Buildup ; Wand or Staff: 30% increased Freeze Buildup ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Glacial_Rune, poe2db:Glacial_Rune, poe2db:Greater_Glacial_Rune, poe2db:Perfect_Glacial_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Storm Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Storm | -/5 | Martial Weapon: Adds 1 to 10 Lightning Damage ; Wand or Staff: Gain 6% of Damage as Extra Lightning Damage ; Armour: +10% to Lightning Resistance |
| Storm | 15/31 | Martial Weapon: Adds 1 to 20 Lightning Damage ; Wand or Staff: Gain 8% of Damage as Extra Lightning Damage ; Armour: +14% to Lightning Resistance |
| Greater Storm | 30/52 | Martial Weapon: Adds 1 to 30 Lightning Damage ; Wand or Staff: Gain 10% of Damage as Extra Lightning Damage ; Armour: +18% to Lightning Resistance |
| Perfect Storm | 50/65 | Martial Weapon: Adds 1 to 40 Lightning Damage ; Wand or Staff: Gain 12% of Damage as Extra Lightning Damage ; Armour: +22% to Lightning Resistance |
Bonded (all tiers): Martial Weapon: 30% increased Magnitude of Shock you inflict ; Wand or Staff: 30% increased Magnitude of Shock you inflict ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Storm_Rune, poe2db:Storm_Rune, poe2db:Greater_Storm_Rune, poe2db:Perfect_Storm_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Iron Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Iron | -/5 | Martial Weapon: 14% increased Physical Damage ; Wand or Staff: 20% increased Spell Damage ; Armour: 14% increased Armour, Evasion and Energy Shield |
| Iron | 15/31 | Martial Weapon: 16% increased Physical Damage ; Wand or Staff: 25% increased Spell Damage ; Armour: 16% increased Armour, Evasion and Energy Shield |
| Greater Iron | 30/52 | Martial Weapon: 18% increased Physical Damage ; Wand or Staff: 30% increased Spell Damage ; Armour: 18% increased Armour, Evasion and Energy Shield |
| Perfect Iron | 50/65 | Martial Weapon: 20% increased Physical Damage ; Wand or Staff: 35% increased Spell Damage ; Armour: 20% increased Armour, Evasion and Energy Shield |
Bonded (all tiers): Martial Weapon: 20% increased effect of Fully Broken Armour ; Wand or Staff: Break Armour on Critical Hit with Spells equal to 12% of Physical Damage dealt ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Iron_Rune, poe2db:Iron_Rune, poe2db:Greater_Iron_Rune, poe2db:Perfect_Iron_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Body Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Body | -/11 | Martial Weapon: Leeches 3% of Physical Damage as Life ; Wand or Staff: +30 to maximum Energy Shield ; Armour: +30 to maximum Life |
| Body | 15/37 | Martial Weapon: Leeches 4% of Physical Damage as Life ; Wand or Staff: +40 to maximum Energy Shield ; Armour: +45 to maximum Life |
| Greater Body | 30/57 | Martial Weapon: Leeches 5% of Physical Damage as Life ; Wand or Staff: +50 to maximum Energy Shield ; Armour: +60 to maximum Life |
| Perfect Body | 50/65 | Martial Weapon: Leeches 6% of Physical Damage as Life ; Wand or Staff: +60 to maximum Energy Shield ; Armour: +75 to maximum Life |
Bonded (all tiers): Martial Weapon: 5% increased maximum Life ; Wand or Staff: 5% increased maximum Life ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Body_Rune, poe2db:Body_Rune, poe2db:Greater_Body_Rune, poe2db:Perfect_Body_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


<!-- merged from kb/items/rune-effects-2.md -->
Part title: Rune effects 2: tiered runes (Mind, Rebirth, Inspiration, Stone, Vision)

- Status: done
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-rune pages and the Rune/Augment index pages, tier 2.

## Mind Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Mind | -/11 | Martial Weapon: Leeches 2% of Physical Damage as Mana ; Wand or Staff: +45 to maximum Mana ; Armour: +20 to maximum Mana |
| Mind | 15/37 | Martial Weapon: Leeches 3% of Physical Damage as Mana ; Wand or Staff: +60 to maximum Mana ; Armour: +30 to maximum Mana |
| Greater Mind | 30/57 | Martial Weapon: Leeches 4% of Physical Damage as Mana ; Wand or Staff: +75 to maximum Mana ; Armour: +40 to maximum Mana |
| Perfect Mind | 50/65 | Martial Weapon: Leeches 5% of Physical Damage as Mana ; Wand or Staff: +90 to maximum Mana ; Armour: +50 to maximum Mana |
Bonded (all tiers): Martial Weapon: 5% increased maximum Mana ; Wand or Staff: 5% increased maximum Mana ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Mind_Rune, poe2db:Mind_Rune, poe2db:Greater_Mind_Rune, poe2db:Perfect_Mind_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Rebirth Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Rebirth | -/21 | Martial Weapon: Gain 15 Life per enemy killed ; Wand or Staff: 6% increased Energy Shield Recharge Rate ; Armour: Regenerate 0.35% of maximum Life per second |
| Rebirth | 15/45 | Martial Weapon: Gain 25 Life per enemy killed ; Wand or Staff: 8% increased Energy Shield Recharge Rate ; Armour: Regenerate 0.4% of maximum Life per second |
| Greater Rebirth | 30/62 | Martial Weapon: Gain 35 Life per enemy killed ; Wand or Staff: 10% increased Energy Shield Recharge Rate ; Armour: Regenerate 0.45% of maximum Life per second |
| Perfect Rebirth | 50/65 | Martial Weapon: Gain 45 Life per enemy killed ; Wand or Staff: 12% increased Energy Shield Recharge Rate ; Armour: Regenerate 0.5% of maximum Life per second |
Bonded (all tiers): Martial Weapon: Regenerate 0.4% of maximum Life per second ; Wand or Staff: 8% of Damage taken Recouped as Life ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Rebirth_Rune, poe2db:Rebirth_Rune, poe2db:Greater_Rebirth_Rune, poe2db:Perfect_Rebirth_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Inspiration Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Inspiration | -/21 | Martial Weapon: Gain 10 Mana per enemy killed ; Wand or Staff: 20% increased Mana Regeneration Rate ; Armour: 12% increased Mana Regeneration Rate |
| Inspiration | 15/45 | Martial Weapon: Gain 20 Mana per enemy killed ; Wand or Staff: 25% increased Mana Regeneration Rate ; Armour: 15% increased Mana Regeneration Rate |
| Greater Inspiration | 30/62 | Martial Weapon: Gain 30 Mana per enemy killed ; Wand or Staff: 30% increased Mana Regeneration Rate ; Armour: 18% increased Mana Regeneration Rate |
| Perfect Inspiration | 50/65 | Martial Weapon: Gain 40 Mana per enemy killed ; Wand or Staff: 35% increased Mana Regeneration Rate ; Armour: 21% increased Mana Regeneration Rate |
Bonded (all tiers): Martial Weapon: 12% of Skill Mana Costs Converted to Life Costs ; Wand or Staff: 16% increased Mana Cost Efficiency ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Inspiration_Rune, poe2db:Inspiration_Rune, poe2db:Greater_Inspiration_Rune, poe2db:Perfect_Inspiration_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Stone Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Stone | -/16 | Martial Weapon: Causes 20% increased Stun Buildup ; Wand or Staff: Gain additional Stun Threshold equal to 10% of maximum Energy Shield ; Armour: +50 to Stun Threshold |
| Stone | 15/41 | Martial Weapon: Causes 30% increased Stun Buildup ; Wand or Staff: Gain additional Stun Threshold equal to 12% of maximum Energy Shield ; Armour: +75 to Stun Threshold |
| Greater Stone | 30/59 | Martial Weapon: Causes 40% increased Stun Buildup ; Wand or Staff: Gain additional Stun Threshold equal to 14% of maximum Energy Shield ; Armour: +100 to Stun Threshold |
| Perfect Stone | 50/65 | Martial Weapon: Causes 50% increased Stun Buildup ; Wand or Staff: Gain additional Stun Threshold equal to 16% of maximum Energy Shield ; Armour: +125 to Stun Threshold |
Bonded (all tiers): Martial Weapon: 40% increased Damage against Immobilised Enemies ; Wand or Staff: 30% increased Immobilisation buildup ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Stone_Rune, poe2db:Stone_Rune, poe2db:Greater_Stone_Rune, poe2db:Perfect_Stone_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Vision Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Vision | -/16 | Martial Weapon: +60 to Accuracy Rating ; Wand or Staff: 16% increased Critical Hit Chance for Spells ; Armour: 8% increased Life and Mana Recovery from Flasks |
| Vision | 15/41 | Martial Weapon: +90 to Accuracy Rating ; Wand or Staff: 20% increased Critical Hit Chance for Spells ; Armour: 12% increased Life and Mana Recovery from Flasks |
| Greater Vision | 30/59 | Martial Weapon: +120 to Accuracy Rating ; Wand or Staff: 24% increased Critical Hit Chance for Spells ; Armour: 16% increased Life and Mana Recovery from Flasks |
| Perfect Vision | 50/65 | Martial Weapon: +150 to Accuracy Rating ; Wand or Staff: 28% increased Critical Hit Chance for Spells ; Armour: 20% increased Life and Mana Recovery from Flasks |
Bonded (all tiers): Martial Weapon: Attacks have +1% to Critical Hit Chance ; Wand or Staff: 25% increased Critical Damage Bonus ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Vision_Rune, poe2db:Vision_Rune, poe2db:Greater_Vision_Rune, poe2db:Perfect_Vision_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


<!-- merged from kb/items/rune-effects-3.md -->
Part title: Rune effects 3: attribute runes, Ward, Charging, Tempered, Masterwork, Greater Rune of X

- Status: done
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-rune pages and the Rune/Augment index pages, tier 2.

## Robust Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Robust | -/5 | All Equipment: +6 to Strength |
| Robust | 15/31 | All Equipment: +9 to Strength |
| Greater Robust | 30/52 | All Equipment: +12 to Strength |
| Perfect Robust | 50/65 | All Equipment: +15 to Strength |
Bonded (all tiers): Martial Weapon: Adds 6 to 10 Physical Damage to Attacks, Adds 6 to 10 Fire damage to Attacks ; Wand or Staff: +100 to Armour ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Robust_Rune, poe2db:Robust_Rune, poe2db:Greater_Robust_Rune, poe2db:Perfect_Robust_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Adept Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Adept | -/5 | All Equipment: +6 to Dexterity |
| Adept | 15/31 | All Equipment: +9 to Dexterity |
| Greater Adept | 30/52 | All Equipment: +12 to Dexterity |
| Perfect Adept | 50/65 | All Equipment: +15 to Dexterity |
Bonded (all tiers): Martial Weapon: Adds 6 to 10 Physical Damage to Attacks, Adds 1 to 16 Lightning damage to Attacks ; Wand or Staff: +80 to Evasion Rating ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Adept_Rune, poe2db:Adept_Rune, poe2db:Greater_Adept_Rune, poe2db:Perfect_Adept_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Resolve Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Resolve | -/5 | All Equipment: +6 to Intelligence |
| Resolve | 15/31 | All Equipment: +9 to Intelligence |
| Greater Resolve | 30/52 | All Equipment: +12 to Intelligence |
| Perfect Resolve | 50/65 | All Equipment: +15 to Intelligence |
Bonded (all tiers): Martial Weapon: Adds 6 to 10 Physical Damage to Attacks, Adds 5 to 8 Cold damage to Attacks ; Wand or Staff: +50 to maximum Energy Shield ; Armour: +20 to maximum Life, +20 to maximum Mana
- src: poe2db:Lesser_Resolve_Rune, poe2db:Resolve_Rune, poe2db:Greater_Resolve_Rune, poe2db:Perfect_Resolve_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Ward Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Ward | -/5 | Armour: +15 to maximum Runic Ward |
| Ward | 15/31 | Armour: +20 to maximum Runic Ward |
| Greater Ward | 30/52 | Armour: +25 to maximum Runic Ward |
| Perfect Ward | 50/65 | Armour: +30 to maximum Runic Ward |
Bonded (all tiers): Armour: 15% increased Global Armour, Evasion and Energy Shield
- src: poe2db:Lesser_Ward_Rune, poe2db:Ward_Rune, poe2db:Greater_Ward_Rune, poe2db:Perfect_Ward_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Charging Rune family
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Charging | -/5 | Armour: 8% increased Runic Ward Regeneration Rate |
| Charging | 15/31 | Armour: 12% increased Runic Ward Regeneration Rate |
| Greater Charging | 30/52 | Armour: 16% increased Runic Ward Regeneration Rate |
| Perfect Charging | 50/65 | Armour: 20% increased Runic Ward Regeneration Rate |
Bonded by tier: Lesser Charging: Armour: Regenerate 10 Runic Ward per second // Charging: Armour: Regenerate 15 Runic Ward per second // Greater Charging: Armour: Regenerate 20 Runic Ward per second // Perfect Charging: Armour: Regenerate 25 Runic Ward per second
- src: poe2db:Lesser_Charging_Rune, poe2db:Charging_Rune, poe2db:Greater_Charging_Rune, poe2db:Perfect_Charging_Rune, tier 2, crawl 2026-11-23
- conf: single-source (per-tier pages; Rune/Augment index pages agree)
- notes: Req/drop shown as requirement level / drop level; "-" = no requirement shown. Lesser has no level requirement line. Martial Weapon = non-caster weapons; Wand or Staff = caster weapons. Bonded effects apply only with Shaman "Wisdom of the Maji" (see basics).


## Tempered Rune family (physical / thorns)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Tier | Req lvl/drop lvl | Effect by slot |
|---|---|---|
| Lesser Tempered | -/5 | Martial Weapon: Adds 3 to 4 Physical Damage ; Armour: 6 to 9 Physical Thorns damage |
| Tempered | 15/31 | Martial Weapon: Adds 6 to 9 Physical Damage ; Armour: 14 to 21 Physical Thorns damage |
| Greater Tempered | 30/52 | Martial Weapon: Adds 9 to 12 Physical Damage ; Armour: 31 to 52 Physical Thorns damage |
No Bonded line shown. No Perfect Tempered Rune page found in corpus.
- src: poe2db:Lesser_Tempered_Rune, poe2db:Tempered_Rune, poe2db:Greater_Tempered_Rune, tier 2, crawl 2026-11-23
- notes: Only 3 tiers exist in the corpus; forge recipe Lesser x3 -> Tempered, Tempered x3 -> Greater (Tempered page recipe table).


## Masterwork Rune
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Socket into an Augment Socket holding any tiered rune to upgrade that rune. Drop level 37, Currency Exchange cost 1500 gold. No Perfect-tier forge recipe appears on Perfect rune pages.
- src: poe2db:Masterwork_Rune, tier 2, crawl 2026-11-23
- notes: Perfect rune pages list no 3-to-1 forge recipe (checked Perfect Desert, Ward, Vision).


## Greater Rune of X (4 runes)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Rune of | Req/drop | Effect by slot | Bonded |
|---|---|---|---|
| Leadership | -/65 | Martial Weapon: Minions gain 10% of their Physical Damage as Extra Lightning Damage ; Armour: Minions take 10% of Physical Damage as Lightning Damage | Martial Weapon: Minions deal 20% increased Damage ; Armour: Minions have +10% to all Elemental Resistances |
| Tithing | -/65 | Martial Weapon: Meta Skills gain 10% increased Energy ; Armour: 1 to 100 Lightning Thorns damage | Martial Weapon: Invocated Spells have 25% chance to consume half as much Energy ; Armour: 15% increased Thorns damage |
| Alacrity | -/65 | Martial Weapon: 8% increased Skill Speed ; Armour: Debuffs on you expire 8% faster | Martial Weapon: 15% increased Reservation Efficiency of Herald Skills ; Armour: 15% increased Elemental Ailment Threshold |
| Nobility | -/65 | Martial Weapon: Attacks with this Weapon have 10% chance to inflict Exposure ; Armour: 10% reduced effect of Shock on you | Martial Weapon: 20% increased Exposure Effect ; Armour: 10% reduced Shock duration on you |
- src: poe2db:Greater_Rune_of_Leadership, poe2db:Greater_Rune_of_Tithing, poe2db:Greater_Rune_of_Alacrity, poe2db:Greater_Rune_of_Nobility, tier 2, crawl 2026-11-23
- notes: Pages for Alacrity state it has restrictions on where or how it can drop (Greater_Rune_of_Alacrity page); drop source not given.


<!-- merged from kb/items/rune-effects-4.md -->
Part title: Rune effects 4: named runes and Ancient runes

- Status: done
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-rune pages and the Rune/Augment index pages, tier 2.

## Named runes (Hedgewitch Assandra, Saqawal, Fenumus, Farrul, Craiceann, Mannan, Grannell, Seske, Girt, Myrk, Hestra, Leld, Greatwolf) - 21 runes
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Limit 1 each.
| Rune | Req/drop | Effect by slot | Bonded |
|---|---|---|---|
| Countess Seske's Rune of Archery | 50/65 | Bows: Bow Attacks fire 1 additional Arrows | Bows: 20% increased Projectile Speed |
| Courtesan Mannan's Rune of Cruelty | 50/65 | Gloves: 20% increased Magnitude of Damaging Ailments you inflict | Gloves: 15% increased Duration of Damaging Ailments on Enemies |
| Craiceann's Rune of Recovery | 50/65 | Body Armours: 30% increased Energy Shield Recharge Rate | Body Armours: Gain additional Ailment Threshold equal to 50% of maximum Energy Shield, Gain additional Stun Threshold equal to 50% of maximum Energy Shield |
| Craiceann's Rune of Warding | 50/65 | Body Armours: 50% reduced effect of Curses on you | Body Armours: 8% increased Curse Magnitudes |
| Farrul's Rune of Grace | 50/65 | Boots: 8% increased Deflection Rating while moving | Boots: Prevent +3% of Damage from Deflected Hits |
| Farrul's Rune of the Chase | 50/65 | Boots: 5% increased Movement Speed | Boots: 10% increased Cooldown Recovery Rate |
| Farrul's Rune of the Hunt | 50/65 | Martial Weapon: 50% increased Attack Damage against Rare or Unique Enemies | Martial Weapon: +1 to Level of all Attack Skills |
| Fenumus' Rune of Agony | 50/65 | Martial Weapon: Gain 13% of Damage as Extra Chaos Damage ; Wand or Staff: Gain 13% of Damage as Extra Chaos Damage | Martial Weapon: Gain 8% of Damage as Extra Physical Damage ; Wand or Staff: Gain 8% of Damage as Extra Physical Damage |
| Fenumus' Rune of Draining | 50/65 | Gloves: 20% increased Withered Magnitude | Gloves: +7% to Chaos Resistance |
| Fenumus' Rune of Spinning | 50/65 | Gloves: 8% increased Cast Speed | Gloves: 20% increased Mana Cost Efficiency while on Low Mana |
| Hedgewitch Assandra's Rune of Wisdom | 50/65 | Wand or Staff: +1 to Level of all Spell Skills | Wand or Staff: Archon recovery period expires 30% faster |
| Lady Hestra's Rune of Winter | 50/65 | Martial Weapon: Adds 19 to 28 Cold Damage against Chilled Enemies | Martial Weapon: +2% to Maximum Cold Resistance |
| Saqawal's Rune of Erosion | 50/65 | Helmets: 25% increased Exposure Effect | Helmets: 15% increased Magnitude of Non-Damaging Ailments you inflict |
| Saqawal's Rune of Memory | 50/65 | Helmets: 2% increased Experience gain | Helmets: +10% to all Elemental Resistances |
| Saqawal's Rune of the Sky | 50/65 | Martial Weapon: Gain 5% of Damage as Extra Damage of all Elements ; Wand or Staff: Gain 5% of Damage as Extra Damage of all Elements | Martial Weapon: 8% chance to gain an additional random Charge when you gain a Charge ; Wand or Staff: 12% chance when collecting an Elemental Infusion to gain an additional Elemental Infusion of the same type |
| Thane Girt's Rune of Wildness | 50/65 | Wand or Staff: 25% chance for Spell Skills to fire 2 additional Projectiles | Wand or Staff: Every Rage also grants 1% increased Spell Damage |
| Thane Grannell's Rune of Mastery | 50/65 | Gloves: 30% increased Magnitude of Non-Damaging Ailments you inflict | Gloves: 15% increased Duration of Elemental Ailments on Enemies |
| Thane Leld's Rune of Spring | 50/65 | Martial Weapon: Adds 1 to 60 Lightning Damage against Shocked Enemies | Martial Weapon: +2% to Maximum Lightning Resistance |
| Thane Myrk's Rune of Summer | 50/65 | Martial Weapon: Adds 23 to 34 Fire Damage to Attacks against Ignited Enemies | Martial Weapon: +2% to Maximum Fire Resistance |
| The Greatwolf's Rune of Claws | 50/65 | Gloves: Adds 5 to 12 Physical Damage to Attacks | Gloves: Fissure Skills have +2 to Limit |
| The Greatwolf's Rune of Willpower | 50/65 | Body Armours: 15% of Damage is taken from Mana before Life | Body Armours: 8% of Maximum Life Converted to Energy Shield |
- src: per-row pages: poe2db:Countess_Seskes_Rune_of_Archery, poe2db:Courtesan_Mannans_Rune_of_Cruelty, poe2db:Craiceanns_Rune_of_Recovery (and the rest at https://poe2db.tw/us/<Page>, page names in Rune index poe2db:Rune), tier 2, crawl 2026-11-23
- notes: Drop source not stated on these pages. Runeshape Combinations rows exist for Farrul's Chase, Assandra's Wisdom, Seske's Archery, Girt, Mannan, Saqawal Memory, Grannell at Lv70+ (Runeshape_Combinations page).


## Ancient Rune of X (13 runes)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
All limit 1; each is tied to one weapon/shield class.
| Rune of | Req/drop | Effect (slot) | Bonded |
|---|---|---|---|
| Animosity | 30/12 | Talismans: Gain 2 Druidic Prowess when you Heavy Stun a Rare or Unique Enemy | Talismans: 40% increased Stun Buildup |
| Control | 30/12 | Quarterstaves: 50% increased Immobilisation buildup | Quarterstaves: 30% increased Damage against Immobilised Enemies |
| Decay | 30/12 | Wands: 25% increased Withered Magnitude | Wands: 15% chance that when Volatility on you explodes, you regain an equivalent amount of Volatility |
| Detonation | 30/12 | Crossbows: Grenades have 10% chance to activate a second time | Crossbows: 40% increased Crossbow Reload Speed |
| Discovery | 30/12 | Staves: 30% chance to create an additional Remnant | Staves: +1 to maximum number of Elemental Infusions |
| Dueling | 30/12 | Bucklers: 30% increased Parried Debuff Magnitude | Bucklers: 15% increased Block chance |
| Prowess | 30/12 | Spears: 30% chance when you gain a Charge to gain an additional Charge | Spears: 30% increased Endurance, Frenzy and Power Charge Duration |
| Retaliation | 30/12 | Shields: 8% increased Attack Speed if you have Blocked Recently | Shields: +3% to maximum Block chance |
| Shattering | 30/12 | One Hand Maces: 40% increased effect of Fully Broken Armour | One Hand Maces: Break 50% increased Armour |
| Splinters | 30/12 | Bows: +50% Surpassing chance to fire an additional Arrow | Bows: 30% increased Projectile Speed |
| Witchcraft | 30/12 | Foci: 40% increased Area of Effect of Curses | Foci: 15% faster Curse Activation |
| the Horde | 30/12 | Sceptres: Minions have 8% increased Attack and Cast Speed | Sceptres: Minions have 10% increased Movement Speed |
| the Titan | 30/12 | Two Hand Maces: 10% chance for Slam Skills you use yourself to cause an additional Aftershock | Two Hand Maces: 15% increased Area of Effect for Attacks |
- src: poe2db:Ancient_Rune_of_Animosity, poe2db:Ancient_Rune_of_Control, poe2db:Ancient_Rune_of_Decay and the rest at https://poe2db.tw/us/Ancient_Rune_of_<Name>, tier 2, crawl 2026-11-23
- notes: Runeshape_Combinations lists Ancient Rune of Splinters at Lv65-74 (Act4 note). Drop source otherwise not stated.


<!-- merged from kb/items/rune-effects-5.md -->
Part title: Rune effects 5: Warding runes and Rune of X (lvl 15)

- Status: done
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-rune pages and the Rune/Augment index pages, tier 2.

## Warding Rune of X (17 runes)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Rune of | Limit | Req/drop | Effect by slot | Bonded |
|---|---|---|---|---|
| Annihilation | 1 | 30/30 | Martial Weapon: Attacks spend 5% of your maximum Runic Ward if possible to gain that much added Physical damage | Martial Weapon: 10% reduced Runic Ward Cost Efficiency |
| Armature | 1 | 45/45 | Martial Weapon: Gain maximum Runic Ward equal to 15% of this Weapon's maximum damage | Martial Weapon: 5% increased Attack Speed while missing Runic Ward |
| Bodyguards | 1 | 45/45 | Sceptres: Minions in your Presence have Onslaught while you are on Low Runic Ward | Sceptres: Damage of Enemies Hitting you is Unlucky if your Runic Ward has been damaged Recently |
| Courage | - | 15/15 | Helmets: 25% increased Armour and Evasion Rating while on Low Runic Ward | Helmets: 20% increased Armour and Evasion Rating when on Low Life |
| Desperation | - | 15/15 | Wand or Staff: Spell damage Penetrates 25% of enemy Elemental Resistances while on Low Runic Ward | Wand or Staff: 12% increased Elemental Damage |
| Disintegration | - | 15/15 | Martial Weapon: Attacks Break Armour equal to 15% of maximum Runic Ward | Martial Weapon: Break 10% increased Armour |
| Equinox | 1 | 45/45 | Caster Weapon: 40% less Mana Regeneration Rate, Mana Recovery from Regeneration is also applied to Runic Ward | Caster Weapon: 20% increased Runic Ward Regeneration Rate if you've dealt a Critical Hit Recently |
| Glancing | - | 30/30 | Body Armours: +3 to Deflection Rating per 10 maximum Runic Ward | Body Armours: Prevent +1% of Damage from Deflected Hits |
| Heart | 1 | 30/30 | Body Armours: Gain 5% of maximum Life as Extra maximum Runic Ward | Body Armours: 1% more Runic Ward Regeneration rate per 2% of maximum Runic Ward lost from Hits Recently, up to 100% more |
| Hollowing | 1 | 45/45 | Caster Weapon: Gain 15% of maximum Life as Extra maximum Runic Ward, 15% less maximum Life | Caster Weapon: +1% to all Maximum Elemental Resistances while on full Runic Ward |
| Nourishment | 1 | 15/15 | Armour: 15% Life Recovery from Flasks also applies to Runic Ward | Armour: 15% increased Life Recovery from Flasks |
| Obsession | 1 | 45/45 | Wands: All damage taken bypasses Runic Ward, Runic Ward Regeneration Rate is doubled | Wands: 12% increased maximum Runic Ward |
| Protection | 1 | 15/15 | Armour: Every 4 seconds, gain Guard equal to 20% of maximum Runic Ward for 2 seconds | Armour: 8% increased Guard gained |
| Reinforcement | - | 15/15 | Armour: 20% increased Runic Ward | Armour: Gain 2% of maximum Life as Extra maximum Runic Ward |
| Salvaging | 1 | 30/30 | Sceptres: Recover 3% of maximum Runic Ward when one of your Reviving Minions is Killed | Sceptres: Recover 3% of maximum Life when one of your Minions is Revived |
| Stability | - | 30/30 | Shields and Bucklers: +4 to Stun Threshold per 10 maximum Runic Ward | Shields and Bucklers: 15% increased Stun buildup while Shapeshifted |
| Symbiosis | 1 | 30/30 | Boots: 1% increased Energy Shield Recharge Rate per 30 maximum Runic Ward | Boots: Regenerate 1% of maximum Energy Shield per second |
- src: poe2db:Warding_Rune_of_Annihilation, poe2db:Warding_Rune_of_Armature, poe2db:Warding_Rune_of_Bodyguards and the rest at https://poe2db.tw/us/Warding_Rune_of_<Name>, tier 2, crawl 2026-11-23
- notes: All concern Runic Ward. Corpus patch note (Version_0.5.2) says Warding Rune of Nourishment was not obtainable as a runic inscription reward until fixed. Drop source otherwise not stated.


## Rune of X, level-15 limit-1 runes (13 runes)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
effects per slot as in the table below.
| Rune of | Req/drop | Effect (slot) | Bonded |
|---|---|---|---|
| Accumulation | 15/15 | Gloves: Gain 3 Life per Enemy Hit with Attacks, Gain 1 Mana per Enemy Hit with Attacks ; Crossbow, Bow or Spear: On Hitting an enemy, gains maximum added Cold damage equal to the enemy's Power for 20 seconds, up to a total of 32 | Gloves: +30 to maximum Life, +30 to maximum Mana ; Crossbow, Bow or Spear: 30% increased Freeze Buildup |
| Acrobatics | 15/15 | Weapon: Flasks gain 0.2 charges per Second ; Boots: +0.3 metres to Dodge Roll distance | Weapon: Charms gain 0.25 charges per Second ; Boots: 30% increased Armour if you haven't Dodge Rolled Recently |
| Confrontation | 15/15 | Quarterstaff or Spear: Gain 4 Rage on Melee Hit, -10 to Maximum Rage | Quarterstaff or Spear: unfilled placeholder on page ("rage effect +% [10]") — real value unknown |
| Consistency | 15/15 | Helmets: 200% increased Critical Hit Chance, You have no Critical Damage Bonus ; Caster Weapon: 50% increased Spell Damage while your Companion is in your Presence | Helmets: Hits against you have 25% reduced Critical Damage Bonus ; Caster Weapon: 8% increased Mana Recovery rate while your Companion is in your Presence |
| Culmination | 15/15 | Gloves: 50% chance to build an additional Combo on Hit ; One Hand Mace or Quarterstaff: Rolls only the minimum or maximum Damage value for Physical Damage | Gloves: 5% increased Attack Speed ; One Hand Mace or Quarterstaff: 20% increased Bleeding Duration |
| Foundations | 15/15 | Body Armours: +30 to Armour, +30 to Evasion Rating, +10 to maximum Energy Shield | Body Armours: +20 to maximum Life, +20 to maximum Mana |
| Reach | 15/15 | Helmets: Remnants you create have 15% increased effect ; Wand or Staff: Remnants can be collected from 50% further away, Remnants you create have 25% reduced effect | Helmets: Recover 3% of Maximum Mana when you collect a Remnant ; Wand or Staff: 20% increased Exposure Effect |
| Renown | 15/15 | Gloves: 50% increased Glory generation ; Caster Weapon: Archon recovery period expires 30% faster | Gloves: Banner Skills have 20% increased Aura Magnitudes ; Caster Weapon: 30% increased Archon Buff duration |
| Vital Flame | 15/15 | One Hand Mace, Two Hand Mace or Talisman: Adds 13 to 16 Fire Damage, 15% of Skill Mana Costs Converted to Life Costs | One Hand Mace, Two Hand Mace or Talisman: 30% increased Ignite Magnitude |
| Vitality | 15/15 | Weapon: +80 to maximum Life ; Shields and Bucklers: Recover 15 Life when you Block | Weapon: 15% increased amount of Life Leeched ; Shields and Bucklers: 5% increased maximum Life |
| the Blossom | 15/15 | Body Armours: +50 to Spirit, -1 to Spirit per 2 Levels | Body Armours: 5% increased Spirit Reservation Efficiency of Skills |
| the Hunt | 15/15 | Boots: 8% increased Movement Speed while Sprinting ; Sceptres: Companions deal 30% increased Damage | Boots: 50% increased Stun Recovery ; Sceptres: 8% increased Mana Recovery rate while your Companion is in your Presence |
| the Prism | 15/15 | Body Armours: -10% to all Maximum Elemental Resistances, +20% to all Elemental Resistances | Body Armours: 20% of Damage is taken from Mana before Life |
- src: poe2db:Rune_of_Accumulation, poe2db:Rune_of_Acrobatics, poe2db:Rune_of_Confrontation and the rest at https://poe2db.tw/us/Rune_of_<Name>, tier 2, crawl 2026-11-23
- notes: Rune of Confrontation Bonded text on the page is an unfilled placeholder ("rage effect +% [10]"); see report conflicts. Rune of Vital Flame and Confrontation also have [DNT-Unused] duplicates.


<!-- merged from kb/items/rune-effects-6.md -->
Part title: Rune effects 6: conversion/socket-bound runes, Aldur Legacy intro, unused

- Status: done
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-rune pages and the Rune/Augment index pages, tier 2.

## Aldur conversion runes + socket-bound crafting runes (13)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Socket-bound = permanently fills the socket, cannot be removed/replaced ([Socket-bound Augments](https://poe2db.tw/us/Socket-bound_Augments)). Drop level 65, limit 1 where stated.
| Rune | Drop | Effect | Bonded |
|---|---|---|---|
| Passion of Aldur | 65 | SB Weapon: Transforms all Cold and Lightning modifiers on the item into equivalent Fire modifiers | Weapon: 25% increased Fire Damage |
| Breath of Aldur | 65 | SB Weapon: When socketed, transforms all Fire and Lightning modifiers to equivalent Cold modifiers | Weapon: 25% increased Cold Damage |
| Ire of Aldur | 65 | SB Weapon: Transforms all Fire and Cold modifiers on the item into equivalent Lightning modifiers | Weapon: 25% increased Lightning Damage |
| Betrayal of Aldur | 65 | SB Weapon: Transforms all Fire, Cold and Lightning modifiers on the item into equivalent Chaos modifiers | Weapon: 25% increased Chaos Damage |
| Serle's Triumph | 65 | SB All Equipment: +1 Suffix Modifier allowed, local maximum mods allowed + [1] | - |
| Cadigan's Epiphany | 65 | SB Gloves: Destroys all Augment Sockets on the item to create a Jewel Socket | - |
| Astrid's Creativity | 65 | All Equipment: Can have 1 additional Crafted Modifiers | - |
| Uhtred's Sidereus | 65 | SB Boots: Can roll Chronomancy modifiers | Boots: 10% increased Cooldown Recovery Rate |
| Kolr's Hunt | 65 | SB Gloves: Can roll Marksman modifiers | Gloves: 20% increased Projectile Damage |
| Vorana's Carnage | 65 | SB Helmets: Can roll Berserking modifiers | Helmets: Gain 2 Rage on Melee Hit |
| Thrud's Might | 65 | SB Weapon: Can roll Destruction modifiers | Weapon: +5% to all Elemental Resistances |
| Medved's Tending | 65 | SB Body Armours: Can roll Soul modifiers | Body Armours: 3% increased maximum Life, 3% increased maximum Mana |
| Katla's Gloom | 65 | SB Gloves: Can roll Decay modifiers | Gloves: 25% reduced Effect of Non-Damaging Ailments on you |
- src: poe2db:Passion_of_Aldur, poe2db:Breath_of_Aldur, poe2db:Serles_Triumph, poe2db:Cadigans_Epiphany, tier 2, crawl 2026-11-23
- notes: Item pages also carry lore flavour text (not reproduced). Runeshape_Combinations lists all of these at Lv70+ (Runes of Aldur league mechanic). Gold cost on Currency Exchange 1500 each.


## Aldur's Legacy rune
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Socketing Aldur's Legacy into a Unique Kalguuran or Ezomyte item destroys the item and creates a Legacy rune imbued with that item's power. Drop level 65, req lvl 65. 63 'Legacy of X' runes (limit 1, req 65, drop 65) are listed in [[items/rune-effects]] and [[items/rune-effects]].
- src: poe2db:Aldurs_Legacy, tier 2, crawl 2026-11-23
- notes: Runeshape_Combinations Lv78+ row for Aldur's Legacy.


## [DNT-Unused] runes (8)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Eight pages titled DNT-Unused Rune of Wild Ferocity, Partnership, Reverberation, Vital Flame, Confrontation, Chance, Confidence, Duplication; Requires Lv15 (drop level 15), limit 1; no effect text on the Rune index entries.
- src: poe2db:DNT-Unused_Rune_of_Chance, tier 2, crawl 2026-11-23
- notes: Internal "do not translate/unused" placeholders; not obtainable as real items as far as corpus shows. Do not treat as real runes.


<!-- merged from kb/items/rune-effects-7.md -->
Part title: Rune effects 7: Aldur's Legacy runes (1/3)

- Status: done
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-rune pages and the Rune/Augment index pages, tier 2.

## Aldur's Legacy runes, part 1: A Worthy Foe to Horns of Bynden (32 runes)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
All: limit 1, req lvl 65, drop level 65 (checked on [Legacy of A Worthy Foe](https://poe2db.tw/us/Legacy_of_A_Worthy_Foe) and the Aldur's Legacy index; per-row page is https://poe2db.tw/us/Legacy_of_<Name>).
| Legacy of | Effect (slot) | Bonded |
|---|---|---|
| A Worthy Foe | Shields: Off-hand Hits inflict Runefather's Challenge | Shields: +45% to Cold Resistance |
| Adonia's Ego | Wands: +1 to Maximum Power Charges | Wands: +65 to maximum Mana |
| Alkem Eira | Shields: 30% of damage Blocked is Recouped as Mana | Shields: 20% of damage Blocked is Recouped as Mana |
| Amor Mandragora | Talismans: Gain 1 Druidic Prowess for every 20 total Rage spent | Talismans: Enemies in your Presence are Hindered |
| Ashrend | Body Armours: Cannot be Ignited, -10 Physical Damage taken from Attack Hits | Body Armours: +35% to Fire Resistance |
| Blackbraid | Body Armours: +50% of Armour also applies to Elemental Damage | Body Armours: +15% to all Elemental Resistances |
| Brain Rattler | Two Hand Maces: All damage with this Weapon causes Electrocution buildup | Two Hand Maces: Damage Penetrates 10% Lightning Resistance |
| Bramblejack | Body Armours: 250% of Melee Physical Damage taken reflected to Attacker | Body Armours: Regenerate 3% of maximum Life per second while Surrounded |
| Briarpatch | Boots: +15% to Thorns Critical Hit Chance | Boots: 15% increased Thorns Critical Damage Bonus |
| Briskwrap | Body Armours: Gain Deflection Rating equal to 30% of Evasion Rating | Body Armours: 35% increased Flask Mana Recovery rate |
| Bristleboar | Body Armours: Gain 10 Rage when Critically Hit by an Enemy, Gain 5 Rage when Hit by an Enemy | Body Armours: +3 to Maximum Rage |
| Brynhand's Mark | One Hand Maces: Causes Double Stun Buildup | One Hand Maces: Adds 14 to 20 Physical Damage |
| Bushwhack | Boots: Physical Damage is Pinning | Boots: +20 to Dexterity |
| Candlemaker | Gloves: 40% increased Fire Damage, Flammability Magnitude is doubled | Gloves: 20% increased Ignite Duration on Enemies |
| Chernobog's Pillar | Shields: Gain 1% of damage as Fire damage per 2% Chance to Block | Shields: +30% to Chaos Resistance |
| Crown of Thorns | Helmets: Pain Attunement | Helmets: 17 to 26 Physical Thorns damage |
| Cursecarver | Wands: +3 to Level of all Curse Skills | Wands: 35% increased Mana Regeneration Rate |
| Deathblow | Gloves: Culling Strike | Gloves: Gain 30 Life per enemy killed |
| Deidbell | Helmets: Warcries Explode Corpses dealing 10% of their Life as Physical Damage | Helmets: Warcry Skills have 20% increased Area of Effect |
| Dionadair | Shields: Double Stun Threshold while Shield is Raised | Shields: 15% increased Stun Threshold |
| Duality | Quarterstaves: Gain 250 Guard for 0.5 seconds per Combo expended when using Skills | Quarterstaves: Gain Finality for 0.2 seconds per Combo expended when using Skills |
| Dunkelhalt | Bucklers: 50% increased Parried Debuff Magnitude | Bucklers: 50% increased Parry Damage |
| Dusk Vigil | Staves: Gain 30% of Physical Damage as Extra Fire Damage | Staves: Triggered Spells deal 20% increased Spell Damage |
| Edyrn's Tusks | Body Armours: 50% chance to inflict Bleeding on Hit, 50% reduced Slowing Potency of Debuffs on You | Body Armours: 35% increased Thorns damage |
| Elevore | Helmets: Charms gain 1 charge per Second, +1 Charm Slots | Helmets: Charms gain 0.5 charges per Second |
| Erian's Cobble | Helmets: +30 to Accuracy Rating, +10 to maximum Life, +10 to maximum Mana, 10% increased Rarity of Items found, 10% increased Critical Hit Chance, +5 to all Attributes, +5% to all Elemental Resistances, 3 Life Regeneration per second | Helmets: +20 to Armour, +20 to Evasion Rating, +20 to maximum Energy Shield |
| Ezomyte Peak | Helmets: 15% increased Area of Effect, Unwavering Stance | Helmets: 50% reduced Slowing Potency of Debuffs on You |
| Facebreaker | Gloves: +1 to Armour per Strength | Gloves: 1% increased Damage per 15 Strength |
| Foxshade | Body Armours: 10% increased Movement Speed when on Full Life, 100% increased Evasion Rating when on Full Life | Body Armours: 20% increased Evasion Rating |
| Greymake | Helmets: +50 to all Attributes | Helmets: +1 Maximum Life per Level |
| Hoghunt | Two Hand Maces: +5% to Critical Hit Chance, Maim on Critical Hit | Two Hand Maces: 25% increased Attack Damage against Maimed Enemies |
| Horns of Bynden | Helmets: Every Rage also grants 1% increased Armour, Gain 1 Rage on Melee Hit | Helmets: +3 to Maximum Rage |
- src: poe2db:Aldurs_Legacy «Aldur's Legacy», tier 2, crawl 2026-11-23
- notes: Created by socketing Aldur's Legacy into a Unique Kalguuran or Ezomyte item (destroys the item), Runes of Aldur league mechanic. Each rune named after the unique it came from.


<!-- merged from kb/items/rune-effects-8.md -->
Part title: Rune effects 8: Aldur's Legacy runes (2/3)

- Status: done
- Version: 0.5.x (PoE2DB game data crawled 2026-11-23; not checked against 1.0)
- Sources: PoE2DB per-rune pages and the Rune/Augment index pages, tier 2.

## Aldur's Legacy runes, part 2: Hrimnor's Hymn to Wulfsbane (31 runes)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
All: limit 1, req lvl 65, drop level 65 (checked on [Legacy of A Worthy Foe](https://poe2db.tw/us/Legacy_of_A_Worthy_Foe) and the Aldur's Legacy index; per-row page is https://poe2db.tw/us/Legacy_of_<Name>).
| Legacy of | Effect (slot) | Bonded |
|---|---|---|
| Hrimnor's Hymn | Two Hand Maces: 25% chance for Slam Skills you use yourself to cause an additional Aftershock | Two Hand Maces: 15% chance for Slam Skills you use yourself to cause an additional Aftershock |
| Ironbound | Bows: Hits with this weapon have 1 to 3 Added Physical Damage per 1% Block Chance | Bows: 3% increased Block chance per 100 total Item Armour on Equipped Armour Items |
| Keeper of the Arc | Helmets: Alternating every 5 seconds: Take 20% less Damage from Hits Take 20% less Damage over time | Helmets: 25% increased Mana Regeneration Rate |
| Kingsguard | Body Armours: Recover 5% of maximum Life for each Endurance Charge consumed | Body Armours: +30 to maximum Life |
| Legionstride | Boots: +10% to Block chance | Boots: 10% reduced Damage taken from Projectile Hits |
| Lifesprig | Wands: +2 to Level of all Spell Skills | Wands: Leeches 1% of maximum Life when you Cast a Spell |
| Mjölner | One Hand Maces: +200 Intelligence Requirement, +3 to Level of all Lightning Skills | One Hand Maces: +1 to Level of all Lightning Skills |
| Northpaw | Gloves: Base Critical Hit Chance for Attacks with Weapons is 7% | Gloves: 15% increased Critical Damage Bonus |
| Oaksworn | Shields: 50% increased Life Regeneration rate | Shields: 50 Life Regeneration per second |
| Obern's Bastion | Boots: 200% increased Stun Recovery | Boots: 40% reduced Chill Duration on you, 40% reduced Freeze Duration on you |
| Olrovasara | One Hand Maces: On Hitting an enemy, gains maximum added Lightning damage equal to the enemy's Power for 20 seconds, up to a total of 120 | One Hand Maces: 15% increased Attack Speed |
| Quill Rain | Bows: 50% increased Attack Speed, 20% less Attack Damage | Bows: 70% increased Arrow Speed |
| Rondel de Ezo | Bucklers: Curse Enemies with Enfeeble on Block | Bucklers: 100% increased Block chance against Projectiles |
| Runeseeker's Call | Wands: 75% increased effect of Socketed Runes | Wands: +100 to maximum Mana |
| Serle's Grit | One Hand Maces: Maximum Quality is 40% | One Hand Maces: Skills which Empower an Attack have 20% chance to not count that Attack |
| Spiteful Floret | Talismans: Every 5 Rage also grants 5% of Damage taken Recouped as Life | Talismans: Attacks have 20% chance to cause Bleeding |
| Starkonja's Head | Helmets: 100% increased Global Evasion Rating when on Low Life, 5% of Damage from Hits is taken from your Damageable Companion 's Life before you | Helmets: 5% of Damage from Hits is taken from your Damageable Companion 's Life before you |
| Svalinn | Shields: Chance to Block Damage is Lucky, You take 20% of damage from Blocked Hits | Shields: +50 to maximum Runic Ward |
| The Blood Thorn | Quarterstaves: Adds 4 to 8 Physical Damage, Causes Bleeding on Hit | Quarterstaves: 10% increased Magnitude of Bleeding you inflict |
| The Knight-errant | Boots: Iron Reflexes | Boots: 25% increased Elemental Ailment Threshold |
| The Sentry | Quarterstaves: Adds 23 to 34 Fire damage to Attacks, 100% increased Flammability Magnitude | Quarterstaves: +2% to Maximum Fire Resistance |
| The Smiling Knight | Helmets: Aggravate Bleeding on targets you Critically Hit with Attacks | Helmets: 20% increased Critical Hit Chance |
| The Unleashed | Body Armours: 25% of Damage taken from Hits bypasses Energy Shield if Energy Shield is below half | Body Armours: 20% increased Armour while Shapeshifted |
| The Vile Knight | Helmets: Deal 4% increased Damage with Hits to Rare or Unique Enemies for each second they've ever been in your Presence, up to a maximum of 200% | Helmets: 20% increased Presence Area of Effect |
| Trampletoe | Boots: Deal 10% of Overkill damage to enemies within 2 metres of the enemy killed | Boots: 15% increased Global Physical Damage |
| Trenchtimbre | One Hand Maces: Increases and Reductions to Minion Attack Speed also affect you | One Hand Maces: +1 to Level of all Minion Skills |
| Twisted Empyrean | Two Hand Maces: Attacks with this Weapon have Added Cold Damage equal to 6% to 10% of maximum Mana | Two Hand Maces: 15% of Damage is taken from Mana before Life |
| Tyranny's Grip | Spears: Strikes deal Splash Damage | Spears: Knocks Enemies Back on Hit |
| Wanderlust | Boots: Your speed is unaffected by Slows | Boots: 5% increased Movement Speed |
| Wings of Caelyn | Helmets: Gain 1 Rage on Melee Hit, Every Rage also grants 1% increased Stun Threshold | Helmets: Every five Rage also grants you 1% increased Movement Speed |
| Wulfsbane | Shields: Intimidate Enemies on Block for 8 seconds | Shields: +25 to Strength |
- src: poe2db:Aldurs_Legacy «Aldur's Legacy», tier 2, crawl 2026-11-23
- notes: Created by socketing Aldur's Legacy into a Unique Kalguuran or Ezomyte item (destroys the item), Runes of Aldur league mechanic. Each rune named after the unique it came from.
