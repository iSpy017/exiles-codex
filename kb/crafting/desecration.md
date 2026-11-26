---
title: Desecration and abyssal bones
status: partial
tracker_topic: "Desecration & abyssal bones"
tracker_note: "partial (bone table + restrictions done; Ancient min-mod-level vs pool unclear; drop sources missing)"
defaults: v=0.5.x
---

Status: partial. Done: every bone's item class, min modifier level / max item level, drop level, omens, Well of Souls basics (0.5.x data). Missing: what each Preserved bone guarantees (page states no restriction), how the Ancient "minimum modifier level 40" interacts with the desecrated mod pool (all gear desecrated mods listed at level 65), exact bone drop sources, and the Well of Souls reveal UI details. Merged with the earlier library doc (2026-11-17 entries kept under "Carried over").
Version: 0.5.x (PoE2DB crawl 2026-11-23). Not checked against 1.0.
Source summary: PoE2DB bone currency pages, Abyss, Desecrated Modifiers, Crafting, omen pages.

## What desecration does
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Desecrating a Rare item adds an Unrevealed Desecrated modifier. If the item has no free mod slot, a random existing mod is removed first. Reveal happens at the Well of Souls (found in Act 2); an item that already has desecrated mods cannot be desecrated again. At reveal you pick from three options.
- src: poe2db:Desecrated_Modifiers, poe2db:Abyss, tier 2, crawl 2026-11-23
- conf: confirmed (two pages agree on reveal at the Well; "three options" and "Act 2" only on Abyss page, single-source)
- notes: Abyss page also says desecration in the campaign eases adding regular mods. Omens modify the roll (below).


## Bones: class, restriction, drop level
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Twelve bone currencies, stack size 20 each, applied to a Rare item. Max item level only on Gnawed; minimum modifier level only on Ancient.

| Bone | Applies to | Restriction | Drop lvl | Exchange gold |
|---|---|---|---|---|
| Gnawed Jawbone | Weapon or Quiver | max item level 64 | 25 | 180 |
| Gnawed Rib | Armour | max item level 64 | 25 | 180 |
| Gnawed Collarbone | Amulet, Ring, Belt | max item level 64 | 25 | 180 |
| Preserved Jawbone | Weapon or Quiver | none shown | 61 | 540 |
| Preserved Rib | Armour | none shown | 61 | 540 |
| Preserved Collarbone | Amulet, Ring, Belt | none shown | 61 | 540 |
| Preserved Cranium | Jewel | none shown | 65 | 540 |
| Preserved Vertebrae | Waystone | none shown | 65 | 540 |
| Ancient Jawbone | Weapon or Quiver | minimum modifier level 40 | 75 | 1500 |
| Ancient Rib | Armour | minimum modifier level 40 | 75 | 1500 |
| Ancient Collarbone | Amulet, Ring, Belt | minimum modifier level 40 | 75 | 1500 |
| Altered Collarbone | Amulet, Ring, Belt, with a chance for otherworldly modifiers | none shown | 1 | 1500 |

- src: poe2db:Gnawed_Jawbone, poe2db:Gnawed_Rib, poe2db:Gnawed_Collarbone, poe2db:Preserved_Jawbone, poe2db:Preserved_Rib, poe2db:Preserved_Collarbone, poe2db:Preserved_Cranium, poe2db:Preserved_Vertebrae, poe2db:Ancient_Jawbone, poe2db:Ancient_Rib, poe2db:Ancient_Collarbone, poe2db:Altered_Collarbone, tier 2, crawl 2026-11-23
- conf: confirmed for restrictions (individual pages and the Abyss overview list the same Max Item Level / Minimum Modifier Level lines)
- notes: "Exchange gold" is the Currency Exchange gold figure printed on each page. "Armour" means all armour pieces as worded by the pages; Crafting page words it "Rare Armor". Gnawed: items above ilvl 64 cannot take them. Prices not recorded here (volatile).


## Ancient bones: minimum modifier level 40
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Ancient bones set a minimum modifier level of 40 for the desecrated mod. PoE2DB's list of gear desecrated mods (198 entries) shows every Amanamu, Kurgal and Ulaman mod at level 65; the jewel list (32 mods, "Lightless" and "of the Abyss") shows level 1; the waystone list (19 mods) shows no level.
- src: poe2db:Ancient_Rib, poe2db:Desecrated_Modifiers, tier 2, crawl 2026-11-23
- notes: [INFERRED] the Unrevealed mod options may come from a wider pool than this named list, since a level-40 floor would be meaningless if only level-65 mods existed; the corpus does not say. Gap.


## Omens for desecration
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Abyssal Echoes: reroll the three reveal options once. Sinistral Necromancy: only prefixes. Dextral Necromancy: only suffixes. Putrefaction: replaces all mods, up to 6 unrevealed desecrated mods, and corrupts the item. The Blackblooded / The Liege / The Sovereign: guarantee a random Kurgal / Amanamu / Ulaman mod on a weapon or jewellery desecration. Light: the next Orb of Annulment removes only desecrated mods. Omens stack size 10.
- src: poe2db:Abyss, poe2db:Crafting, tier 2, crawl 2026-11-23
- conf: confirmed (Abyss and Crafting pages agree)
- notes: Abyss page also says Abyss Omens no longer drop in areas below level 65.


## Where bones come from
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Closed Abyss pits can spawn an Abyssal Trove granting "pieces of Preserved Bone". Altered Collarbone page ties to Breach art/tags (BreachDesecration icon). Per-bone drop sources are not listed.
- src: poe2db:Abyss, tier 2, crawl 2026-11-23
- notes: Kulemak's Invitation is an Abyss tablet (per the Abyss page); not tabulated here.


## Mark of the Abyssal Lord
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Essence of the Abyss adds the Mark of the Abyssal Lord. If an item carrying the Mark is desecrated, the Mark is the mod that gets taken off, and an unrevealed desecrated mod of a better tier takes its place.
- src: poe2db:Mark_of_the_Abyssal_Lord, poe2db:Essence_of_the_Abyss, tier 2, crawl 2026-11-23
- notes: see [[crafting/essences]].


## Abyssal Eyes (not bones)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Kurgal's, Amanamu's and Ulaman's Gaze are Abyssal Eye augments, a separate item type from bones. Per their pages: one allowed per item, level 60 needed, DropLevel 65. They are used by putting them into a free augment socket on weapons or armour; a socketed one stays put but another augment can overwrite it.
- src: poe2db:Kurgals_Gaze «PoE2DB Kurgal's Gaze», tier 2, crawl 2026-11-23
- notes: mods not tabulated here.


## Carried over from earlier version (2026-11-17)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
The Well of Souls quest starts on entering the Mastodon Badlands (Act 2); clear the Lightless Passage to reach the Well; afterwards it's reachable from the map screen. Optional quest. A reveal option is sometimes a mod that can't normally roll on that item. Each Abyssal lord can be fought for targeted rolls via Kulemak's Invitation at the Well. Jewel desecrated mods ("Lightless"/"of the Abyss") don't work with lord omens. Unstable Desecration (e.g. Timeless Jewels): desecrate with a Preserved Cranium, destroy chance rising per use.
- src: poe2wiki The Well of Souls (quest) [S727]), poe2wiki Abyss [S663], poe2wiki Desecrated modifier [S687], tier 2; Poe-Vault Rise of the Abyssal [S662], tier 3; RePoE keywords "Unstable Desecration", tier 2; retrieved 2026-11-17
- v: 0.3+ (0.5.x)
- vol: may-change (1.0 campaign changes)
- conf: confirmed for the Well quest (2 sources); single-source for the rest
- notes: Gnawed bones reportedly can't roll lord mods (timesaver.gg, tier 5 lead, unverified). Skip-route decision → [[strategy/skip-route]].
