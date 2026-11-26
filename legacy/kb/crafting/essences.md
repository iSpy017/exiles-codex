# Essences

Status: done for 0.5.x-era game data (all tiers, per-class values and drop levels in the table docs). Partial gaps: how essences drop (sources not found in corpus), Forge-recipe coverage for every family, 1.0 recheck.
Version: 0.5.x (PoE2DB crawl 2026-11-23). Nothing here is confirmed for 1.0.
Source summary: PoE2DB `Essence` overview plus individual essence pages (Lesser/normal/Greater/Perfect and corrupted). Merged with the earlier doc (batch 24): older entries kept under "Carried over".

## Tiers and how they apply
- Claim: Four plain tiers exist: Lesser, Normal, Greater, Perfect. Lesser, Normal and Greater take a Magic item to Rare and add one guaranteed mod. Perfect and the six corrupted essences work on a Rare item: remove one random mod, then add the guaranteed mod. Stack size 10. Applied by right-clicking the essence, then left-clicking the item.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Essence](https://poe2db.tw/us/Essence), [PoE2DB Perfect Essence of Ice](https://poe2db.tw/us/Perfect_Essence_of_Ice), [PoE2DB Essence of Hysteria](https://poe2db.tw/us/Essence_of_Hysteria), tier 2, crawl 2026-11-23
- Confidence: confirmed (overview and individual pages agree)
- Notes: per-class numbers in [[crafting/essence-table]] and [[crafting/essence-table-high]].

## Drop levels
- Claim: DropLevel by tier. Weapon/life/mana/damage/crit-type families: Lesser 20 or 25, Normal 40, Greater 60, Perfect 72. Utility families (Alacrity, Command, Insulation, Thawing, Grounding, Opulence) have DropLevel 1 at every tier. Corrupted essences: DropLevel 1. Exact value per row is in the table docs. Lesser 20 families: Enhancement, Battle, Sorcery, Seeking, Infinite; Lesser 25: Body, Mind, Abrasion, Flames, Ice, Electricity, Ruin, Haste.
- Version: 0.5.x
- Volatility: may-change
- Source: DropLevel field on each page, e.g. [PoE2DB Lesser Essence of Ice](https://poe2db.tw/us/Lesser_Essence_of_Ice) (25), [Essence of Ice](https://poe2db.tw/us/Essence_of_Ice) (40), [Greater](https://poe2db.tw/us/Greater_Essence_of_Ice) (60), [Perfect](https://poe2db.tw/us/Perfect_Essence_of_Ice) (72), tier 2, crawl 2026-11-23
- Confidence: single-source (PoE2DB game data)
- Notes: drop level is not the same as the required modifier level on the item.

## Upgrading by Forge recipe
- Claim: Three Lesser Essence of Ice combine into one Essence of Ice, and three Essence of Ice into one Greater (Three to One Reforge, crafting bench). Same pattern seen for Body. No Greater-to-Perfect recipe shown on the Ice page.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Essence of Ice](https://poe2db.tw/us/Essence_of_Ice), [PoE2DB Essence of the Body](https://poe2db.tw/us/Essence_of_the_Body), tier 2, crawl 2026-11-23
- Confidence: single-source; only Ice and Body inspected
- Notes: other families probably follow the same rule. [INFERRED]: 57 essence pages contain a Forge Recipe block, but I opened only these two.

## Essence of Ice: cold damage, not spell crit
- Claim: Game data gives Ice a flat added cold damage mod, weapons only (prefix). Lesser: adds (3-5)-(6-9) cold on 1H/Bow, (5-8)-(9-14) on 2H/Xbow/Talisman. Normal: (17-20)-(26-32) / (25-30)-(38-46). Greater: (31-38)-(47-59) / (46-57)-(70-88). Perfect: gains (15-20)% / (25-33)% of damage as extra cold. No Ice tier targets wands, staves, foci or spell crit.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Essence of Ice](https://poe2db.tw/us/Essence_of_Ice) and its Lesser/Greater/Perfect pages, tier 2, crawl 2026-11-23
- Confidence: confirmed across four tier pages of one source (game data)
- Notes: Spell crit sits on Essence of Seeking (next entry). Conflict recorded below.

## Essence of Seeking: the crit essence
- Claim: Seeking gives crit. Weapons: +(1.51-2.1)% Lesser, +(2.11-2.7)% Normal, +(3.11-3.8)% Greater to Critical Hit Chance. Focus/Wand: (34-39)%, (40-46)%, (47-53)% increased Critical Hit Chance for Spells. Staff: (50-59)%, (60-69)%, (70-79)%. Perfect Seeking is different: Body Armour, hits against you have (40-50)% reduced Critical Damage Bonus.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Essence of Seeking](https://poe2db.tw/us/Essence_of_Seeking), Lesser/Greater/Perfect pages, tier 2, crawl 2026-11-23
- Confidence: single-source (game data)
- Notes: all tiers are suffixes. Table: [[crafting/essence-table]].

## Corrupted essences
- Claim: Six corrupted essences, all DropLevel 1, all "remove a random mod, add guaranteed mod" on Rares. Table below (Hysteria has one mod per item class).
- Version: 0.5.x
- Volatility: may-change
- Source: [Hysteria](https://poe2db.tw/us/Essence_of_Hysteria), [Delirium](https://poe2db.tw/us/Essence_of_Delirium), [Horror](https://poe2db.tw/us/Essence_of_Horror), [Insanity](https://poe2db.tw/us/Essence_of_Insanity), [the Abyss](https://poe2db.tw/us/Essence_of_the_Abyss), [the Breach](https://poe2db.tw/us/Essence_of_the_Breach), tier 2, crawl 2026-11-23
- Confidence: single-source (game data)
- Notes: when an item with the Mark of the Abyssal Lord is desecrated, the Mark is the mod lost, swapped for a better-tier unrevealed desecrated mod; see [[crafting/desecration]]. Insanity's text refers to corruption; whether the others act immediately is not stated on the pages.

| Family | Tier | Drop lvl | Mod (range) | P/S | Mod lvl | Classes |
|---|---|---|---|---|---|---|
| Delirium | Corrupt | 1 | Allocates a random Notable Passive Skill | P | 0 | Body |
| Horror | Corrupt | 1 | 60% increased effect of Socketed Augment Items | S | 0 | Boots, Gloves |
| Hysteria | Corrupt | 1 | +1 to Level of all Minion Skills | S | 4 | Helm |
| Hysteria | Corrupt | 1 | (64-97) to (98-145) Physical Thorns damage | P | 50 | Body |
| Hysteria | Corrupt | 1 | (25-29)% increased Critical Damage Bonus | S | 36 | Gloves |
| Hysteria | Corrupt | 1 | 30% increased Movement Speed | P | 52 | Boots |
| Hysteria | Corrupt | 1 | (50-59)% increased Mana Regeneration Rate | S | 44 | Ring |
| Hysteria | Corrupt | 1 | (19-21)% of Damage taken Recouped as Life | S | 54 | Amulet |
| Hysteria | Corrupt | 1 | +(254-304) to Stun Threshold | S | 57 | Belt |
| Hysteria | Corrupt | 1 | (20-24)% increased Block chance | P | 26 | Buckler, Shield |
| Hysteria | Corrupt | 1 | (43-50)% increased Damage with Bow Skills | P | 48 | Quiver |
| Hysteria | Corrupt | 1 | (20-23)% increased Energy Shield Recharge Rate | S | 52 | Focus |
| Insanity | Corrupt | 1 | On Corruption, Item gains two Enchantments | S | 0 | Belt |
| the Abyss | Corrupt | 1 | Mark of the Abyssal Lord | P | 0 | all 27 listed classes (weapons, quiver, armour, focus, sceptre, jewellery, belt) |
| the Abyss | Corrupt | 1 | Mark of the Abyssal Lord | S | 0 | all 27 listed classes |
| the Breach | Corrupt | 1 | +20% to Maximum Quality | P | 0 | Amulet, Ring |

## Atlas pattern notes (drop/quantity)
- Claim: PoE2DB's Essence page lists Atlas "pattern" effects: Greater Pattern gives a 2% chance for minions of Essence Monsters to drop a random Greater Essence (level 70+ areas, needs an Eastern or Western Gateway completed). Flawless Patterns gives 30% increased chance to find Perfect Essences (same requirements).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Essence](https://poe2db.tw/us/Essence), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: general essence drop sources not found in the corpus (gap).

## Non-currency "essence" pages
- Claim: Pages named Essence of Anger, Hatred, Wrath, Misery, Virtue, the Mountain, the Storm exist but show buff or modifier text (e.g. Mountain: 5% extra cold, 20% increased freeze buildup; Storm: 5% extra lightning, 30% increased chance to shock), not currency. Not tabulated.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Essence of the Storm](https://poe2db.tw/us/Essence_of_the_Storm), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: [INFERRED] these are monster or buff effects tied to Essence Monsters; the pages do not say.

## Conflicts
- Essence of Ice effect (library: [[04-conflicts]] "Essence of Ice effect"). The library records an earlier Mobalytics (Lolcohol guide) wording of spell crit chance versus a cold modifier from Mobalytics (Paintmaster) and Poe-Vault. I did not read those pages in this run; their wording is unverified here and is taken from the library entry, not cited directly. PoE2DB game data (tier 2, 0.5.x): Ice = cold damage; the spell crit chance mod belongs to Essence of Seeking. [INFERRED] The spell-crit version likely confused Seeking with Ice, because no Ice tier touches wands, staves, foci or crit. Resolution rests on PoE2DB only.

## Carried over from earlier version (2026-11-17)
- Claim: Omens of Sinistral / Dextral Crystallisation make Perfect and corrupted essences remove only a prefix / suffix ([[crafting/omens]]). Essences drop from monsters imprisoned in essences (poe2wiki). Pre-0.3 guides (e.g. game8) describing essences as normal → magic are outdated. Essence-only mods exist in data (e.g. Perfect Body life% at mod level 72).
- Version: 0.5.5.9 · Volatility: may-change
- Source: RePoE poe2 base_items.json omen text, tier 2; [poe2wiki Essence](https://www.poe2wiki.net/wiki/Essence), tier 2; retrieved 2026-11-17
- Confidence: single-source each
