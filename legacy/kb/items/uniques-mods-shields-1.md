# Unique Shield / buckler / focus mods (0.5.x) - part 1 of 2

Status: done for this slot part (rows sorted by required level as listed by PoE2DB). Version: 0.5.x data (PoE2DB crawl 2026-11-23); not checked against 1.0. Volatility: may-change.
Source: [PoE2DB Unique_item](https://poe2db.tw/us/Unique_item) (armour list, tier 2) plus each unique's own PoE2DB page (mod blocks, boss-drop and release-league lines), crawl 2026-11-23. Confidence: single-source.
Names per slot: [[items/uniques-armour]]. Drop restrictions and sources: [[items/uniques-drop-sources]]. Total uniques: [[items/uniques-index]].
Other parts of this slot: [[items/uniques-mods-shields-2]]. Other slots: [[items/uniques-mods-body-1]], [[items/uniques-mods-helmet-1]], [[items/uniques-mods-gloves-1]], [[items/uniques-mods-boots]], [[items/uniques-mods-shields-1]].

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
