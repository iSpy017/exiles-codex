# Rarity

Scope: item rarity levels, affix limits, identification, the hidden 10-tier rarity system, tiered unidentified items, exceptional items, unique tiers. Version 0.5.5.9 unless noted.

## The four rarities and affix limits
- Claim: Items are Normal (grey), Magic (blue), Rare (yellow) or Unique (brown). Magic = up to 1 prefix + 1 suffix. Rare = up to 3 prefixes + 3 suffixes. Normal has no explicit mods. Currency and similar classes have no rarity (each item has its own drop weight).
- Version: 0.5.5.9
- Volatility: stable
- Source: RePoE poe2 keywords.json "Item Rarity", tier 2 (game data), retrieved 2026-11-17; [poe2wiki Rarity](https://poe2wiki.net/wiki/Rarity), tier 2
- Confidence: confirmed
- Notes: Some bases change the limits (Dusk/Gloam/Penumbra/Tenebrous, Lament/Portent/Absent) → [[bases-implicits]]. Regal Orb upgrades magic → rare, adding a mod (poe2wiki Rare). Full currency list → crafting batch.

## Identification
- Claim: Magic and higher items generally drop unidentified. Identify with a Scroll of Wisdom or at an NPC (Hooded One, Doryani).
- Version: 0.5.x
- Volatility: stable
- Source: [poe2wiki Item](https://poe2wiki.net/wiki/Item), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: Identification matters because tiered unidentified items only apply their mod-pool filter at identification time (below).

## The hidden 10-tier rarity roll
- Claim: When an item drops, the game picks one of 10 rarity tiers; increased item rarity (IIR) pushes the pick upward. Tiers 1–5 raise the chance to be magic/rare/unique and reduce the chance the drop is converted to gold. Tiers 6–9 produce tiered unidentified items (Unidentified Tier 2–5). Rarity also raises the chance to upgrade currency to higher-value currency and to skip bases far below the area's level.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Rarity](https://poe2wiki.net/wiki/Rarity), tier 2, retrieved 2026-11-17 (wiki cites developer-sourced info)
- Confidence: single-source
- Notes: The wiki says IIR's benefit is most noticeable around 100–150% with strong diminishing returns beyond — that's from player testing plus info relayed privately via a streamer, so treat as tier 5. Matters for the farm choice (rarity on gear vs on waystones). → strategy/farm-ranking.

## Tiered unidentified items
- Claim: Endgame rares/magics can drop as "Unidentified (Tier 2–5)". On identification, each tier removes low-level mods from the possible pool (it's the mod's item level that matters, not its tier number): Tier 2 needs ilvl 66+ and allows only mods of level 11+; Tier 3 = ilvl 71 / mods 23+; Tier 4 = ilvl 76 / mods 35+; Tier 5 = ilvl 79 / mods 48+.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Rarity](https://poe2wiki.net/wiki/Rarity), tier 2, retrieved 2026-11-17
- Confidence: single-source (consistent with a Reddit answer linking the same table, tier 5)
- Notes: Only affects mods rolled at identification — later crafting is unaffected. A GGG forum user notes an untiered rare can still be better than a T5 one (forum thread 3669740, tier 5). Patch 0.2.0g made tiered rares/magics drop more often and cull more low mods (Mobalytics patch-notes copy, tier 3). Implication: pick up / identify T4–T5 rares on relevant bases; ignore low tiers. [INFERRED] from the filter thresholds.

## Exceptional items
- Claim: High-tier rare drops of ilvl 78+ can rarely come as a Normal "Exceptional" base with over 20% quality (max 30%) or an extra augment socket; the "Exceptional" prefix shows until identified.
- Version: 0.5.0+
- Volatility: may-change
- Source: [poe2wiki Item / Exceptional items](https://www.poe2wiki.net/wiki/Exceptional_items), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: Crafting bases with 30% quality or a third body socket — likely the best crafting bases; price check in economy batch. See [[quality]], [[sockets-augments]].

## Unique item rarity tiers
- Claim: Uniques sit in four hidden tiers — Common, Uncommon, Rare, Mythic. When a unique is generated the tier is picked first, then a unique within it. IIR and quantity affect the rate.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Unique item](https://poe2wiki.net/wiki/Unique_item), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: Some uniques are drop-restricted (boss-only, league-only) → items/uniques-<slot> (batch 8).

## Monster rarity
- Claim: Monsters are also normal/magic/rare/unique. Magic and rare monsters get +1 monster level and bosses +2, which raises the item level of their drops. Monster Rarity mods raise the chance of magic/rare monsters and, for rares, the chance of extra monster modifiers.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Level](https://poe2wiki.net/wiki/Level), tier 2; keywords "Monster Rarity" (game data), retrieved 2026-11-17
- Confidence: confirmed
- Notes: [poe2wiki Item](https://poe2wiki.net/wiki/Item) phrases it as "rare monsters +1 item level" — consistent. → [[item-level]].
