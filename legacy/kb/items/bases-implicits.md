# Item bases & implicits

Scope: what a base type is, how base stats and implicits work, the jewellery implicit list, culture tags. Version 0.5.5.9 unless noted. Unique lists → items/uniques-<slot> (batch 8).

## What a base type decides
- Claim: The base type fixes the item's class, inventory size, base defences or weapon damage, attribute and level requirement, drop level, and any implicit modifier. Explicit (random) mods come on top.
- Version: 0.5.5.9
- Volatility: stable
- Source: [RePoE poe2 base_items.json](https://github.com/repoe-fork/poe2), tier 2 (game data 0.5.5.9), retrieved 2026-11-17
- Confidence: confirmed (game data + [poe2wiki Item](https://poe2wiki.net/wiki/Item), tier 2)
- Notes: e.g. Rusted Cuirass = 45 armour, drop level 1, −5% movement speed (stored as −500). Higher-tier bases generally have higher drop level; for equipment drop level usually = base required level. See [[item-level]].

## Base counts per class (game data, released bases)
- Claim: Armour classes have many bases (body armour ~347 distinct names, helmets ~256, gloves ~202, boots ~191, shields ~150, bucklers 52, foci 51). Jewellery is small: rings 26 names, amulets 23, belts 16. Weapon classes 13–44 each.
- Version: 0.5.5.9
- Volatility: may-change (1.0 adds bases, e.g. swords for Duelist)
- Source: RePoE base_items.json, tier 2, retrieved 2026-11-17 (counted by me)
- Confidence: [INFERRED] counts include data-only entries. "released" state in the export doesn't guarantee a base actually drops — claws, daggers, swords, axes and flails exist in data with drop levels but weren't used by any 0.5 class. Verify against 1.0 notes.

## Armour culture tags
- Claim: Armour and most martial weapon bases carry one of four culture tags: Ezomyte, Maraketh, Vaal, Karui. Jewellery, sceptres, wands and staves don't.
- Version: 0.5.5.9
- Volatility: stable
- Source: RePoE base_items.json tags (`*_basetype`), tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Separate from "Unique Culture" (an icon on uniques tying them to a culture, which the game text says can be used to manipulate them) — keyword "Unique Culture". Mechanic detail → batch 8/9.

## Implicits: which classes have them
- Claim: Every ring, amulet, belt, quiver and spear base has an implicit. About half of bows/crossbows/talismans/maces do. Most helmets, gloves, shields, bucklers, foci, sceptres and staves have none. ~93 of the body-armour bases have one.
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE base_items.json `implicits`, tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Ring implicits (base → drop level → implicit)
- Claim: Iron (1, adds 1–4 phys to attacks) · Lazuli (1, +20–30 mana) · Ruby (8, +20–30% fire res) · Sapphire (12, cold) · Topaz (16, lightning) · Amethyst (20, +7–13% chaos res) · Emerald (26, +120–160 accuracy) · Pearl (32, 7–10% cast speed) · Prismatic (35, +7–10% all ele res) · Two-Stone (35, +12–16% to two elements, 3 variants) · Gold (40, 6–15% rarity) · Vitalic (40, 4–6% inc life) · Mnemonic (40, 4–6% inc mana) · Kinetic (40, adds 6–9 to 11–15 phys) · Abyssal Signet (40, Abyssal Wasting on hit) · Grasping (40, gets socket bonuses as if gloves) · Unset (44, +1 skill slot) · Oneiric (47, 11–23% chaos dmg) · Biostatic (52, +1% all max res). Breach Ring (+20% max quality) and Refined Breach Ring (+25%).
- Version: 0.5.5.9 (some are league-mechanic bases)
- Volatility: may-change
- Source: RePoE base_items.json + mods.json, tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Dusk/Gloam/Penumbra/Tenebrous rings and amulets shift the prefix/suffix limits (+1/−1 or +2/−2); keyword "Fragmented Mirror" says Delirium mirrors offer rare items of these bases. → endgame/delirium.

## Amulet implicits
- Claim: Crimson (1, 2–4 life regen/s) · Azure (1, 20–30% mana regen) · Amber/Jade/Lapis (8, +10–15 Str/Dex/Int) · Pearlescent (8, +7–10% all ele res) · Lunar (14, +20–30 ES) · Bloodstone (18, +30–40 life) · Stellar (25, +5–7 all attributes) · Solar (30, +10–15 spirit) · Gold (35, 12–20% rarity) · Corona (40, gets socket bonuses as if helmet) · Lament/Portent (42, −1 prefix / −1 suffix) · Absent (50, −1 of each) · Veridical Chain (52, Runic Ward) and Runemastered variants (65).
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE base_items.json + mods.json, tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Solar = the spirit amulet. Lament/Portent/Absent are presumably for forcing outcomes in crafting — [INFERRED] from the reduced-affix implicit; check in crafting batch.

## Belt implicits
- Claim: Rawhide (1, 20–30% life flask recovery) · Linen (1, mana flask recovery) · Wide (14, flask charges gained) · Long (20, charm duration) · Plate (25, +140–180 armour) · Ornate (31, reduced charm charges used) · Invoking/Sinew/Forking (32, 1 charm slot + cast speed / Str / lightning to attacks) · Mail (40, reduced flask charges used) · Double (44, charm charges gained) · Heavy (50, stun threshold) · Stalking (50, 1 charm slot + socket bonuses as boots) · Utility (55, 20% flask recovery instant) · Fine (62, flasks gain 0.17 charges/s) · Runemastered Heavy (65, 4 variants).
- Version: 0.5.5.9
- Volatility: may-change
- Source: RePoE base_items.json + mods.json, tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Charm slots → [[charms]]. "Gains bonuses from socketed items as though it was X" bases (Grasping Ring, Corona Amulet, Stalking Belt) let jewellery use rune/soul core armour-slot effects — see [[sockets-augments]].

## Base vs modified stats
- Claim: Local explicit mods (e.g. "% increased Armour", "% increased Physical Damage" on the weapon) modify the base stat shown on the item; quality also multiplies base defences/phys damage. Global mods apply to the character.
- Version: 0.5.x
- Volatility: stable
- Source: [Mobalytics Item Modifiers](https://mobalytics.gg/poe-2/guides/item-modifiers), tier 3, retrieved 2026-11-17; quality keyword (game data)
- Confidence: confirmed (tier 3 + game keyword for quality)
- Notes: See [[quality]] (items), [[affix-tiers]].
