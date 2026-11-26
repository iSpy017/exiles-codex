---
title: Unique Shield / buckler / focus mods (0.5.x) - part 1 of 2
status: partial  # not in tracker
defaults: v=0.5.x vol=may-change conf=single-source
merged_from: [uniques-mods-shields-1.md, uniques-mods-shields-2.md]
data: [data/uniques.csv, data/unique_mods.csv]  # generated from the crawl; query these instead of reading the tables
---

Status: done for this slot part (rows sorted by required level as listed by PoE2DB). Version: 0.5.x data (PoE2DB crawl 2026-11-23); not checked against 1.0. Volatility: may-change.
Source: poe2db:Unique_item (armour list, tier 2) plus each unique's own PoE2DB page (mod blocks, boss-drop and release-league lines), crawl 2026-11-23. Confidence: single-source.
Names per slot: [[items/uniques-armour]]. Drop restrictions and sources: [[items/uniques-drop-sources]]. Total uniques: [[items/uniques-index]].
Other parts of this slot: [[items/uniques-mods-shields]]. Other slots: [[items/uniques-mods-body]], [[items/uniques-mods-helmet]], [[items/uniques-mods-gloves]], [[items/uniques-mods-boots]], [[items/uniques-mods-shields]].

## How to read
- Mods are paraphrased compactly; (a–b) are rolled ranges, fixed numbers are not rolled. Mod order follows PoE2DB mod blocks, not in-game order. Implicits and base defences are omitted. Req lvl = level only (attribute requirements omitted).
- Tag column: "Boss: X" = PoE2DB page says the item is dropped by that boss; "Rel: X" = release league shown on the page (blank = since 0.1.0 base data); "Drop disabled" = page carries the 「Drop disabled」 marker (22 item pages in the corpus carry it; the 12 armour ones are not on the Unique_item armour list and are appended here by hand, so the armour total is 221 listed + 12 = 233).
- Items whose PoE2DB page also shows a "Deferred" variant (differing base/level/mods) use the 0.5.5 block here.

## Shield / buckler / focus uniques

| Name | Base | Req lvl | Explicit mods | Tag |
|---|---|---|---|---|
| Dionadair | Splintered Tower Shield | 1 | (60–80)% increased Armour; +(10–15) to Strength; 20% reduced Stun Threshold; Double Stun Threshold while Shield is Raised; (3–5) Life Regeneration per second |  |
| Wulfsbane | Painted Tower Shield | 6 | +(40–60) to maximum Life; +(10–15) to Strength; +(60–80) to Stun Threshold; Intimidate Enemies on Block for 8 seconds |  |
| Merit of Service | Pelage Targe | 8 | Grants Raise Shield; (20–25)% increased Block chance; (60–80)% increased Armour and Evasion; +(60–80) to Stun Threshold; Allies in your Presence have Block Chance equal to yours | Drop disabled |
| Doomgate | Braced Tower Shield | 12 | (80–100)% increased Block chance; (100–150)% increased Armour; You take (25–40)% of damage from Blocked Hits; Enemies are Culled on Block; +(13–17)% to Chaos Resistance |  |
| Window to Paradise | Barricade Tower Shield | 16 | (60–120)% increased Armour; +(60–100) to maximum Mana; +(10–15)% to all Elemental Resistances; Inflict Elemental Exposure to Enemies 3 metres in front of you for 4 seconds, every 0.25 seconds while raised | Rel: Dawn of the Hunt |
| The Wailing Wall | Effigial Tower Shield | 21 | Grants Raise Shield; 10% reduced Movement Speed; (100–150)% increased Armour; +(100–150) to Stun Threshold; Cannot use Shield Skills | Drop disabled; no longer drops since 0.3.0 (version history) |
| Lycosidae | Rampart Tower Shield | 28 | (10–15)% increased Block chance; (60–100)% increased Armour; Accuracy Rating is Doubled; Blocking Damage Poisons the Enemy as though dealing 200 Base Chaos Damage |  |
| Redblade Banner | Heraldric Tower Shield | 33 | (10–15)% increased Block chance; (60–100)% increased Armour; +(20–30) to Strength; +(100–150) to Stun Threshold; Enemies in your Presence count as having double Power | 0.5.5 data (page also shows a Deferred variant); Rel: Dawn of the Hunt |
| Svalinn | Crucible Tower Shield | 60 | (200–300)% increased Armour; You take (0–20)% of damage from Blocked Hits; Chance to Block Damage is Lucky; Grants Cast on Block (Lv14); +(50–100) to maximum Runic Ward | Boss: Olroth, Origin of the Fall |
| Chernobog's Pillar | Blacksteel Tower Shield | 65 | +(30–40)% to Fire Resistance; (100–150)% increased Armour; +(23–29)% to Chaos Resistance; +(150–200) to Stun Threshold; Gain 1% of damage as Fire damage per 1% Chance to Block | Rel: Dawn of the Hunt |
| Arvil's Wheel | Hardwood Targe | 1 | (60–100)% increased Armour and Evasion; Lose 1% of maximum Life on Kill; Lose 1% of maximum Mana on Kill; (30–50)% increased Skill Effect Duration; +(40–60) to maximum Life; +(40–60) to maximum Mana |  |
| Feathered Fortress | Crescent Targe | 26 | +(20–30)% to Fire Resistance; +(20–30)% to Cold Resistance; +(20–30) to Dexterity; +(20–30) to Strength; No Movement Speed Penalty while Shield is Raised |  |
| Alkem Eira | Blazon Crest Shield | 1 | (30–50)% increased Armour and Energy Shield; (15–20)% increased Block chance; +(50–70) to maximum Mana; Damage Blocked is Recouped as Mana |  |
| Oaksworn | Sigil Crest Shield | 7 | (20–30)% increased Block chance; (80–120)% increased Armour and Energy Shield; +(17–23)% to Chaos Resistance; 50% increased Life Regeneration rate |  |
| Saffell's Frame | Emblem Crest Shield | 16 | +(15–25)% to Fire Resistance; +(15–25)% to Cold Resistance; +(15–25)% to Lightning Resistance; Cannot Block; Modifiers to Maximum Block Chance instead apply to Maximum Resistances |  |
| Crest of Ardura | Jingling Crest Shield | 28 | (60–100)% increased Armour and Energy Shield; (30–50)% increased Mana Regeneration Rate; +(10–20) to Intelligence; (30–50)% increased Cooldown Recovery Rate |  |
| Mahuxotl's Machination | Omen Crest Shield | 48 | (333–666)% increased Armour and Energy Shield; (66–333)% increased effect of Socketed Soul Cores; Keystone: Everlasting Sacrifice | Boss: The Trialmaster |
| Rise of the Phoenix | Omen Crest Shield | 36 | +(20–25)% to Fire Resistance; +5% to Maximum Fire Resistance; Regenerate 3% of maximum Life per second; Regenerate 3% of maximum Life per second while on Low Life; +25% to Fire Resistance while on Low Life |  |
| Dunkelhalt | Leather Buckler | 1 | (20–30)% increased Block chance; +(20–30) to Evasion Rating; You take 50% of damage from Blocked Hits; 50% increased Parried Debuff Magnitude | Rel: Dawn of the Hunt |
| Nocturne | Wooden Buckler | 5 | +(60–80) to maximum Mana; +(10–15)% to all Elemental Resistances; 20% increased Accuracy Rating; Parried enemies take more Spell Damage instead of more Attack Damage; 100% increased Parried Debuff Duration | Rel: Dawn of the Hunt |
| Rondel de Ezo | Plated Buckler | 11 | (50–150)% increased Evasion Rating; +(10–20) to Dexterity; 5 Life Regeneration per second; 100% increased Block chance against Projectiles; Curse Enemies with Enfeeble on Block | Rel: Dawn of the Hunt |
| Bloodbarrier | Iron Buckler | 16 | (10–15)% increased Block chance; +(13–17)% to Chaos Resistance; (5–10) Life Regeneration per second; Inflict Corrupted Blood for 5 seconds on Block , dealing 50% of your maximum Life as Physical damage per second | Rel: Dawn of the Hunt |

<!-- merged from kb/items/uniques-mods-shields-2.md -->
Part title: Unique Shield / buckler / focus mods (0.5.x) - part 2 of 2

Status: done for this slot part (rows sorted by required level as listed by PoE2DB). Version: 0.5.x data (PoE2DB crawl 2026-11-23); not checked against 1.0. Volatility: may-change.
Source: poe2db:Unique_item (armour list, tier 2) plus each unique's own PoE2DB page (mod blocks, boss-drop and release-league lines), crawl 2026-11-23. Confidence: single-source.
Names per slot: [[items/uniques-armour]]. Drop restrictions and sources: [[items/uniques-drop-sources]]. Total uniques: [[items/uniques-index]].
Other parts of this slot: [[items/uniques-mods-shields]]. Other slots: [[items/uniques-mods-body]], [[items/uniques-mods-helmet]], [[items/uniques-mods-gloves]], [[items/uniques-mods-boots]], [[items/uniques-mods-shields]].

## How to read
- Mods are paraphrased compactly; (a–b) are rolled ranges, fixed numbers are not rolled. Mod order follows PoE2DB mod blocks, not in-game order. Implicits and base defences are omitted. Req lvl = level only (attribute requirements omitted).
- Tag column: "Boss: X" = PoE2DB page says the item is dropped by that boss; "Rel: X" = release league shown on the page (blank = since 0.1.0 base data); "Drop disabled" = page carries the 「Drop disabled」 marker (22 item pages in the corpus carry it; the 12 armour ones are not on the Unique_item armour list and are appended here by hand, so the armour total is 221 listed + 12 = 233).
- Items whose PoE2DB page also shows a "Deferred" variant (differing base/level/mods) use the 0.5.5 block here.

## Shield / buckler / focus uniques

| Name | Base | Req lvl | Explicit mods | Tag |
|---|---|---|---|---|
| Kaltenhalt | Ridged Buckler | 22 | (80–120)% increased Evasion Rating; +5% to Maximum Cold Resistance; +40% to Cold Resistance; Modifiers to Stun Buildup apply to Freeze Buildup instead for Parry; 100% of Parry Physical Damage Converted to Cold Damage; 25 to 35 Cold Thorns damage | Rel: Rise of the Abyssal |
| Silverthorne | Spiked Buckler | 26 | (60–100)% increased Evasion Rating; +(10–15)% to all Elemental Resistances; Parrying applies 10 Stacks of Critical Weakness; 100% increased Parry Damage | Rel: Dawn of the Hunt |
| Calgyra's Arc | Ornate Buckler | 52 | (60–100)% increased Evasion Rating; +(60–100) to maximum Mana; +(10–20) to Intelligence; Infinite Parry Range; 50% increased Parried Debuff Duration | Rel: Dawn of the Hunt |
| Sunsplinter | Array Buckler | 55 | (100–300)% increased Evasion Rating; +1% to Maximum Fire Resistance +2% to Maximum Cold Resistance +3% to Maximum Lightning Resistance; +1 to Level of all Fire Skills +2 to Level of all Cold Skills +3 to Level of all Lightning Skills | Rel: Dawn of the Hunt |
| Deathrattle | Twig Focus | 1 | +(10–20) to maximum Energy Shield; (20–40)% increased Spell Damage; +(5–10) to Intelligence; 20% chance for Energy Shield Recharge to start when you Kill an Enemy |  |
| Threaded Light | Woven Focus | 6 | (50–70)% increased Energy Shield; (30–40)% increased Mana Regeneration Rate; 20% increased Light Radius; (8–12)% increased Spell Damage per 10 Spirit |  |
| Effigy of Cruelty | Antler Focus | 10 | +(20–30) to maximum Energy Shield; (40–50)% increased Spell Damage; +10 to Intelligence; +(7–13)% to Chaos Resistance; Critical Hits with Spells apply (1–3) Stacks of Critical Weakness | Rel: Dawn of the Hunt |
| Carrion Call | Engraved Focus | 16 | +(30–40) to maximum Energy Shield; Minions have (20–30)% increased maximum Life; (20–30)% increased Mana Regeneration Rate; Minions deal (20–30)% increased Damage; Minions' Resistances are equal to yours |  |
| Serpent's Lesson | Tonal Focus | 22 | +(60–100) to maximum Life; +(60–100) to maximum Mana; You count as on Low Life while at 35% of maximum Mana or below; You count as on Low Mana while at 35% of maximum Life or below |  |
| The Eternal Spark | Crystal Focus | 26 | (50–70)% increased Energy Shield; 40% increased Mana Regeneration Rate while stationary; +(20–30)% to Lightning Resistance; +5% to Maximum Lightning Resistance; 40% increased Mana Regeneration Rate |  |
| Apep's Supremacy | Voodoo Focus | 33 | (100–200)% increased Energy Shield; (30–50)% increased Energy Shield Recharge Rate; 20% of Elemental damage from Hits taken as Chaos damage; +25% chance to be Poisoned; 100% chance to Poison on Hit with Spell Damage | Rel: Dawn of the Hunt |
| The Surrender | Vaal Tower Shield | 75 | (40–60)% increased Block chance; (150–200)% increased Armour; +(150–200) to Stun Threshold; Recover 4% of maximum Life when you Block |  |
| Nightfall | Glacial Fortress | 70 | Grants Soaring Midnight (Lv16); +150 Strength Requirement; (10–20)% increased Block chance; (350–450)% increased Armour; +(30–40)% to Cold Resistance; (10–20)% of Fire damage taken as Cold damage; (10–20)% of Lightning damage taken as Cold damage | Rel: Runes of Aldur |
| Eyes of the Runefather | Venerable Defender | 62 | (300–400)% increased Armour and Evasion; +(40–50)% to Cold Resistance; Off-hand Hits inflict Runefather's Challenge; Inflicts Runefather's Challenge on enemies 6 metres in front of you when raised, no more than once every 2 seconds Gain 1 Runefather's Boast per Power of targets affected by Runefather's Challenge you kill | Boss: The Aberration; Rel: Runes of Aldur |
| Prism Guardian | Intricate Crest Shield | 65 | (150–200)% increased Armour and Energy Shield; +(20–30) to Dexterity; +(10–20)% to all Elemental Resistances; 1% increased Spirit Reservation Efficiency of Buff Skills per 100 Maximum Life; +50 to Spirit | Rel: Dawn of the Hunt |
| Rathpith Globe | Sacred Focus | 75 | (60–100)% increased Energy Shield; +(60–100) to maximum Life; Non-Channelling Spells cost an additional 6% of your maximum Life; Non-Channelling Spells have 3% increased Critical Hit Chance per 100 maximum Life; Non-Channelling Spells deal 6% increased Damage per 100 maximum Life | Rel: Dawn of the Hunt |

Drop disabled (not tabulated; page shows no readable explicit mods, only an internal string): Demigod's Fortitude (Golden Shield, Lv1).
