---
title: Levelling Gear Breakpoints
status: done
tracker_topic: "Levelling gear breakpoints"
tracker_note: "done (0.5.5.9; 1.0 adds bases; 1 conflict)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x guides (researched 2026-11-17). Re-check at 1.0: 200+ new bases are announced, and Acts 5–6 replace the Interludes, so the later breakpoints will move.
"Game data" = [RePoE poe2 export](https://github.com/repoe-fork/poe2) (base_items.json, mods.json), tier 2.

## Rule of thumb: attacks follow the base, spells follow +levels
@ v=0.5.x vol=stable conf=confirmed date=2026-11-17
Attack builds get most of their levelling damage from the weapon base and its flat/% physical mods, so they re-craft at each new base tier. Spell builds get theirs from gem level and "+X to level of spell skills" mods.
- src: Mobalytics Campaign Martial Weapons [S055] (updated 2025-12-11), tier 3; Maxroll Comprehensive League Start Leveling Guide [S032] (updated 2025-04-06), tier 3; retrieved 2026-11-17
- notes: gem-level timing → [[gems/gem-levels]].


## Weapon base tiers (drop level = earliest item level)
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Campaign weapon bases arrive in steps at roughly the same levels for every weapon class. Excerpt (drop level in brackets):

| Class | Campaign steps |
|---|---|
| Bow | Crude (1) · Shortbow (5) · Warden (11) · Recurve (16) · Composite (22) · Dualstring (28) · Cultist (33) · Zealot (39) · Artillery (45) · Twin (54) |
| Crossbow | Makeshift (1) · Tense (4) · Sturdy (10) · Varnished (16) · Dyad (20) · Alloy (26) · Bombard (33) · Construct (38) · Blackfire/Taut (45) · Cannonade (59) |
| Quarterstaff | Wrapped (1) · Long (4) · Gothic (11) · Crackling (16) · Crescent (20) · Steelpoint (28) · Slicing (33) · Barrier (37) · Hefty/Reaching (45) |
| Spear | Hardwood (1) · Ironhead (5) · Hunting (10) · Winged (16) · War (21) · Forked (26) · Barbed (33) · Broad (40) · Crossblade/Steelhead (45) |
| 1H Mace | Wooden Club (1) · Smithing Hammer (4) · Slim (10) · Spiked Club (16) · Warpick (22) · Plated (26) · Brigand (33) · Construct Hammer (36) |
| 2H Mace | Felled Greatclub (1) · Oak (4) · Forge Maul (11) · Studded (16) · Cultist (22) · Temple Maul (28) · Leaden (33) · Crumbling (38) |
| Talisman | Changeling (1) · Nettle (5) · Cinderbark (10) · Familial (16) · Frenzied (22) · Primal (28) · Rabid (34) · Vicious (40) |
| 1H/2H Sword (live in data; class arrives 1.0) | 1H: Shortsword (1) · Broadsword (6) · Vampiric (11) · Scimitar (16) · Charred (21) · Sickle (28) · Falchion (33) · Treasured (40) |

- src: game data base_items.json `drop_level`, tier 2, retrieved 2026-11-17. Bow/crossbow steps cross-checked against Mobalytics Campaign Martial Weapons (Tense/Shortbow early, Sturdy 10 / Warden 11, Varnished/Recurve 16, Dualstring 28, Bombard 33), tier 3
- vol: may-change (1.0 adds 200+ bases)
- conf: confirmed (bow/crossbow); single-source (game data) for the other classes
- notes: "Runeforged"/"Runemastered" variants (drop level 38–70) and "[DNT]" placeholder bases exist in the data — excluded. Endgame top bases sit at drop level 77–79 (e.g. Obliterator/Gemini Bow 78, Fanatic Bow 79, Siege Crossbow 79). Sword bases are in the 0.5.5 data before the Duelist ships — [INFERRED] they'll be live at 1.0.
- Practical breakpoints [INFERRED from the table]: 10–11, 16, 20–22, 26–28, 33, then ~45 and ~52–59.


## Martial weapon process (Mobalytics, bows/crossbows, all martial classes)
@ v=0.5 vol=may-change conf=confirmed date=2026-11-17
Save regals, exalts, alchemy orbs and runes for Act 2. At level 11 (10 for crossbows) buy or roll a Warden Bow / Sturdy Crossbow with transmutes and augments for flat damage or % physical. At 16 vendor-check each level for Recurve Bow / Varnished Crossbow, then craft: good magic base → essence (or regal) → exalts to 3 prefixes → runes → whetstones. That carries to 28 (Dualstring Bow) or 33 (Bombard Crossbow), where you repeat.
- src: Mobalytics Campaign Martial Weapons [S055], tier 3, retrieved 2026-11-17; matches the level-16 and 28/33 upgrade points in [[campaign/levelling-routes]]
- v: 0.4–0.5 (guide updated 2025-12-11; references Interludes)
- conf: confirmed (two tier-3 sources agree on 16 and 28/33)
- notes: Rune priority given: Storm > Desert > Glacial > Iron (Iron higher on high flat-phys bases). Ogham Village has a Blank Rune that trades with Renly for a Lesser Storm Rune. From Act 3 use normal essences, not lesser ones. Whetstones become worthwhile on attack weapons from about level 30 (Maxroll). Late-league whetstones sell for ~6.5 ex each ([[strategy/league-lifecycle-pricing]]) — check before using.


## Caster weapon +level mod breakpoints
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
"+X to level of (all/element) spell skills" mods unlock by item level:

| Base | +all spell skills | +one element's spell skills |
|---|---|---|
| Wand | +1 at 5 · +2 at 25 · +3 at 55 · +4 at 78 | +1 at 2 · +2 at 18 · +3 at 36 · +4 at 55 · +5 at 81 |
| Staff | +2 at 5 · +3 at 25 · +4 at 55 · +5–6 at 78 | +1 at 2 · +2 at 18 · +3–4 at 36 · +5–6 at 55 · +7 at 81 |
| Focus | +1 at 10 · +2 at 41 | — |
| Amulet | +1 at 10 · +2 at 41 · +3 at 75 | — |

- src: game data mods.json (`spell_skill_gem_level_+` and element variants, required level + spawn tags), tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: in the campaign, item level ≈ area level ([[items/item-level]]), so a wand rolled in a level-25+ zone can carry +2 all spells. [INFERRED] caster breakpoints: 18 (element +2), 25 (all +2/+3), 36 (element +3), 55 (all +3/+4).


## Boots movement speed tiers
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Movement speed on boots: 10% (Runner's, ilvl 1) · 15% (Sprinter's, 16) · 20% (Stallion's, 33) · 25% (Gazelle's, 46) · 30% (65) · 35% (Hellion's, 82).
- src: game data mods.json MovementVelocity1–6, tier 2; Maxroll Comprehensive League Start Leveling Guide [S032] (10/15/20/25 tiers, Spires of Deshar vendor), tier 3; Grindout leveling guide [S025] (levels 1/16/33/46/65), tier 5; retrieved 2026-11-17
- conf: confirmed (levels and values)
- notes: name of the 30% tier differs — game data "Cheetah's", Grindout "Sokaris's" → kb/04-conflicts.md. Maxroll ranks movement speed first in its stat priority for levelling gear.


## Other levelling pickups (0.2–0.5 era, Maxroll)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Sapphire Ring before Count Ogham (cold res); Topaz Ring from Act 2; Solar Amulet adds a support to a spirit skill; "of Symbolism" belt for an extra charm slot; Stone Charm against repeated stuns; buy Grand flasks early in Act 2 because Act 1 vendors cap at item level 15.
- src: Maxroll Comprehensive League Start Leveling Guide [S032], tier 3, retrieved 2026-11-17
- v: 0.2 (guide updated 2025-04-06; still references Cruel)
- vol: may-change — needs-1.0-check
- conf: single-source; Cruel-difficulty items are retired (Cruel was replaced by Interludes, now removed in 1.0 → [[campaign/interludes]])
- notes: Maxroll's stat priority for levelling gear: movement speed > resistances > life > base damage > damage scaling > defences. A good magic item can beat a rare.


## Resist checkpoints during the campaign
@ v=0.5 vol=may-change conf=single-source date=2026-11-17
Act 1: cold res for Count Ogham (many players want 30–40%; Beira gives +10%). Act 2: fire res before Rudja (Mawdun Mines). Act 3: fire res before the Azak Bog boss.
- src: Maxroll Comprehensive League Start Leveling Guide [S032], tier 3, retrieved 2026-11-17
- v: 0.2–0.5
- notes: penalty schedule → [[mechanics/resistances]]; quest resist rewards → [[campaign/permanent-rewards]].
