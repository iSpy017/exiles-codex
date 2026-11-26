# Affix tiers & mod groups

Scope: prefix/suffix, mod level, mod groups, tier numbering, example ladders, special mod kinds. Version 0.5.5.9 unless noted. Crafting currencies → crafting/ (batch 9).

## How a random mod is defined
- Claim: Each random mod is a prefix or suffix, has a minimum mod level (item level needed for it to roll), belongs to one or more mod groups, and has spawn weights per item tag (weight 0 = can't roll on that tag).
- Version: 0.5.5.9
- Volatility: stable
- Source: [RePoE poe2 mods.json](https://github.com/repoe-fork/poe2), tier 2 (game data), retrieved 2026-11-17; [PoE2DB modifier notes](https://poedb.tw/th/markdown_raw?oldid=4585), tier 2
- Confidence: confirmed
- Notes: Game data has 1,407 item prefixes, 1,179 suffixes, 108 corruption mods and 5,457 unique-item mods (counted by me).

## One mod per group
- Claim: Mods in the same group can't both be randomly generated on one item — e.g. two flat-life prefixes can't stack.
- Version: 0.5.x
- Volatility: stable
- Source: [PoE2DB modifier notes](https://poedb.tw/us/markdown_raw?oldid=2390), tier 2, retrieved 2026-11-17
- Confidence: single-source (same rule as PoE1; game data stores `groups` per mod)

## Tier numbering: higher = better in PoE2
- Claim: In PoE2 a higher tier number means a stronger, higher-level mod (tier 1 = lowest). This is the reverse of PoE1. The number of tiers differs per mod and per item class.
- Version: 0.1+ (still 0.5.x)
- Volatility: stable
- Source: [poe2wiki Tier](https://poe2wiki.net/wiki/Tier), tier 2, retrieved 2026-11-17; GGG forum threads [3665378](https://www.pathofexile.com/forum/view-thread/3665378) and [3679890](https://www.pathofexile.com/forum/view-thread/3679890), tier 5 (players complaining about the reversal)
- Confidence: confirmed
- Notes: Conflict: Mobalytics "Crafting Basics" says "closer to Tier 1 the better" — PoE1 wording. Logged in [[04-conflicts]]. Practical: a "T5" can be the best tier of one mod and a weak tier of another — check the ladder.

## Example ladders (mod level → value)
- Claim:
  - Flat life, body armour (13 tiers): 1 → 10–19 · 6 → 20–29 · 16 → 30–39 · 24 → 40–59 · 33 → 60–69 · 38 → 70–84 · 46 → 85–99 · 54 → 100–119 · 60 → 120–149 · 65 → 150–174 · 70 → 175–189 · 75 → 190–199 · 80 → 200–214.
  - Fire res, ring (8): 1 → 6–10% · 12 → 11–15 · 24 → 16–20 · 36 → 21–25 · 48 → 26–30 · 60 → 31–35 · 71 → 36–40 · 82 → 41–45.
  - Movement speed, boots (6): 1 → 10% · 16 → 15 · 33 → 20 · 46 → 25 · 65 → 30 · 82 → 35.
  - % phys damage, weapon (8): 1 → 40–49% · 8 → 50–64 · 16 → 65–84 · 33 → 85–109 · 46 → 110–134 · 60 → 135–154 · 75 → 155–169 · 82 → 170–179.
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE mods.json, tier 2, retrieved 2026-11-17 (filtered to named, non-essence prefix/suffix mods)
- Confidence: single-source (game data). Mobalytics agrees boots' top MS tier needs ilvl 82 ([Crafting Basics](https://mobalytics.gg/poe-2/guides/crafting-basics-part-1), tier 3).
- Notes: Highest mod level in the data is 83 (two local chaos-damage weapon mods). Many top tiers sit at 75–82. So best-in-slot crafting bases need ilvl 82 → see [[item-level]] for how to get it.

## Level requirement from mods
- Claim: An item's required level is the higher of its base requirement and its mods' requirements.
- Version: 0.5.x
- Volatility: stable
- Source: [poe2wiki Level](https://poe2wiki.net/wiki/Level), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: In PoE1 a mod raises the requirement to 80% of its mod level (poewiki Affix, GGG forum 3736467). [INFERRED] PoE2 uses the same 80% rule — not confirmed by a PoE2 source.

## Special mod kinds (game keywords)
- Claim:
  - Crafted mods: an item can carry only one; shown in lighter blue.
  - Fractured mods: locked permanently, can't be removed or changed.
  - Desecrated mods: added unrevealed by desecration (removes a random mod if full); revealed at the Well of Souls; an item with one can't be desecrated again.
  - Unstable Desecration: can be desecrated with Preserved Cranium, rising chance to destroy the item each time.
  - Bonded mods: rune/idol mods only active with the Shaman's Wisdom of the Maji notable.
  - Minimum Modifier Level (on some currency): added mods are at least that level; can't be used on items below that ilvl.
  - Maximum Item Level (on some currency): can't be used on items above it.
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE keywords.json, tier 2 (game data), retrieved 2026-11-17
- Confidence: single-source (game text)
- Notes: Details and costs → crafting/desecration, crafting/currencies (batch 9).
