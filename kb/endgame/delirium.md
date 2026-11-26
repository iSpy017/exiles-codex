---
title: Delirium (endgame league mechanic, Trial of Madness / Simulacrum)
status: done
tracker_topic: "Delirium"
tracker_note: "done (0.5.x baseline; Simulacrum final boss unclear; recheck 1.0)"
defaults: v=0.5.x
---

Status: done for flow, currencies, keys, bosses (base stats) and uniques as listed by PoE2DB; partial on boss mechanics (skill names only) and on the exact Simulacrum final boss. No atlas passive tree content by design.
Version: 0.5.x only. Nothing here is verified for the later full release.
Sources: PoE2DB corpus crawl 2026-11-23 (Delirium, Simulacrum, Raven Trickster, Kosis, Omniphobia, item pages), tier 2.

## How the encounter works
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
A map with a Mirror of Delirium lets you walk through it to release a rolling fog ring; you must stay inside the expanding fog or the Delirium ends. A bar shows depth into the fog and time left. Coloured mirror shards appear at set depths; walking into them triggers extra encounters. The fog direction always points at the map boss, and map bosses are always 100% delirious. Magic monsters in fog gain Delirium modifiers; rare/unique monsters in fog may manifest Delirium Demons that use their own skills (item text, Delirium.txt lines 253-256); an atlas node makes rare monsters always manifest them (Delirium.txt lines 822-825, atlas-dependent).
- src: poe2db:Delirium, tier 2, crawl 2026-11-23 (lines 245-265; league notes ~2490-2520)
- notes: tag atlas-dependent (mirror count per map comes from tablets/atlas). Delirium damage and life bonuses on monsters were reduced per the league notes (amount not given).


## Shards, mirrors, scaling
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Fracturing Mirrors (in fog) shatter when you approach and spawn monsters. Shard types: Escalation (add mods to rare Delirium monsters, tougher/better monsters, or pause the fog), Deceptive (summon Delirium bosses or an extra Delirious area), Capricious (not present by default once unlocked; may summon a mirrored map boss or make bosses spawn Grand Mirrors). Deliriousness is the scaling number: Players in Area are X% Delirious from emotions; fog spreading can take maps to 200% Delirious.
- src: poe2db:Fracturing_Mirror_Shards, poe2db:Delirium, tier 2, crawl 2026-11-23
- notes: Capricious unlock and shard odds are atlas-dependent; not covered here.


## Grand Mirror -> Simulacrum chain
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Completing a Delirium Mirror has a chance to spawn a Grand Mirror on a nearby map. A Grand Mirror duplicates the map boss; killing both bosses spreads fog to nearby maps. When fog reaches 100% Deliriousness, one remaining map becomes a Simulacrum. Fog on it starts the whole map at 10% Delirious; killing rares and the map boss raises it.
- src: poe2db:Grand_Mirror, poe2db:Delirium, tier 2, crawl 2026-11-23
- notes: atlas-dependent. Grand Mirror odds nodes not listed.


## Simulacrum (7 waves) and its splinters
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-23
Simulacrum Splinter stacks to 300; 300 combine into a Simulacrum (map fragment, drop level 75, Currency Exchange 1000 gold). Right-click it, then left-click an endgame area with at least 100% Deliriousness. It is a 7-wave encounter with loot after each wave and a leave-or-continue choice. Area "Simulacrum of Delusion" is area level 80 and needs waystone tier 14 or higher; no league tablets drop and portals are disabled there. Completing one gives a key to the Delirium pinnacle boss and points in the Delirium atlas section.
- src: poe2db:Simulacrum, poe2db:Simulacrum_Splinter, poe2db:Simulacrum_of_Delusion, poe2db:Delirium, tier 2, crawl 2026-11-23
- conf: confirmed for 300 stack and 100% requirement (two pages agree); single-source for the rest
- notes: atlas-dependent (waystone tier, level 75+ splinter drop node). Splinter price: see [PoE2DB Economy Delirium](https://poe2db.tw/us/Economy_Delirium); the value-column units are ambiguous, so none recorded.


## Delirium Tablet
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Delirium Tablet adds a Mirror of Delirium to a map, 10 uses. Unique tablet "Clear Skies": fog never dissipates, and -10 to +10% Deliriousness to players. Delirium tablet suffixes (fog duration, pack size, mirrors, shards, unique boss chance, splinter stack size) are listed on the PoE2DB Delirium page, not copied.
- src: poe2db:Delirium, tier 2, crawl 2026-11-23 (lines 21-36, 652-760)
- notes: atlas-dependent.


## Liquid Emotions (Delirium currency, decision rows)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Emotions are exclusive Delirium drops. Each adds Delirious % to the area plus a monster/loot buff, and also crafts onto a Rare Basic Jewel (removes a random mod, adds a guaranteed mod). Tiers: Diluted, regular, Concentrated, Potent (boss drops) and Ancient (Time-Lost jewels). Emotions can also instil a notable passive onto an amulet; a notable you already allocated gives no second effect.
| Emotion | Delirious | Area buff | Jewel craft examples |
|---|---|---|---|
| Diluted Ire | 7% | 20% increased magic monsters | % armour / ES / evasion |
| Diluted Guilt | 9% | 8% pack size | % fire / cold / lightning damage |
| Diluted Greed | 10% | 8% item rarity | physical / chaos / elemental damage |
| Liquid Envy | 15% | 30% increased waystones found | spell damage, cooldown recovery |
| Liquid Disgust | 18% | 30% increased tablets found | life regen, recover life/mana on kill |
| Liquid Despair | 20% | 30% bigger Simulacrum Splinter stacks | crit chance |
| Concentrated Isolation | 50% | none | +1% max resistance (one element or chaos) |
- src: poe2db:Delirium, tier 2, crawl 2026-11-23 (lines 286-650)
- notes: other tiers (Paranoia, Fear, Suffering, Potent Melancholy/Ferocity/Contempt, Ancient set) on the same page. Potent emotions drop 5% from unique monsters in fog (Humanoids: Melancholy, Beasts: Ferocity, Constructs: Contempt), requiring an atlas node (atlas-dependent). Ancient emotions need atlas unlock. Full list: [PoE2DB Liquid Emotions](https://poe2db.tw/us/Liquid_Emotions).


## Key and chase item
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Raven's Reflection is the pinnacle key (Map Fragment, 1500 gold): bring it to the Mirror in the Withered Willow hub. The quest "Strange Reflection" rewards 5 Simulacrum Splinters, a Delirium Tablet, Diluted Liquid Ire, an Amber Amulet and Raven's Reflection. Raven-Touched Shard (augment, limit 1, requires level 60, socket-bound helmets) is an endgame socketable, drop level 65.
- src: poe2db:Ravens_Reflection «PoE2DB Raven's Reflection», poe2db:Strange_Reflection, poe2db:Raven-Touched_Shard, tier 2, crawl 2026-11-23
- notes: [INFERRED]: the Simulacrum-completion key and Raven's Reflection are the same pinnacle access path; the league notes say completion gives "a key", and the item text points to the Withered Willow mirror.


## Boss: The Raven Trickster (Delirium pinnacle)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Arena The Withered Willow, boss tier 3. Level 79 base stats: 246,035 life (life multiplier 990%), 24,603 energy shield, 5,221 armour, 887 evasion, 1,459 damage, basic attack 1167-1751. Resistances 0/0/0/0. Skills named include mirror teleports/activations, frost shards, fireballs, frost wall/comet, storm call, mirror beams of 5 element types, phase-change blast.
- src: poe2db:The_Raven_Trickster, tier 2, crawl 2026-11-23 (lines 282-398; stats lines 349-358)
- notes: values exclude map and difficulty bonuses.


## Other Delirium bosses on PoE2DB
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Kosis, The Revelation: tier 2, level 68, 10,321 life, 1,032 ES, 874 damage; it cannot recharge energy shield and has its ES start at zero. Omniphobia, Fear Manifest: tier 2, level 68, 12,386 life, 699 damage. Both are listed as Delirium bosses on the Delirium page.
- src: poe2db:Kosis%2C_The_Revelation «PoE2DB Kosis», poe2db:Omniphobia%2C_Fear_Manifest «PoE2DB Omniphobia», tier 2, crawl 2026-11-23
- notes: the Delirium page names "Simulacrum Encounter, Kosis" as the pinnacle line. Whether Kosis is the Simulacrum wave-7 boss is not stated; see Gaps in the report. Stats shown are base metadata and may not be the in-Simulacrum values.


## Unique drops tied to Delirium
@ v=0.5.x vol=stable conf=single-source date=2026-11-23
Kosis list: Assailum (helm), Melting Maelstrom (ultimate mana flask), Perfidy (body), Collapsing Horizon (quarterstaff, "difficulty 2+"), Strugglescream (amulet, "difficulty 4"), Megalomaniac (diamond jewel, "difficulty 4"). Raven Trickster list: Sadist's Mercy, Horror's Flight, The Raven's Flock, Veilpiercer, The Auspex, Split Personality (Ruby jewel); The Raven Trickster page marks Horror's Flight and The Auspex as able to drop Raven-Touched (The_Raven_Trickster.txt lines 3043-3052). Others: Clear Skies (tablet), Voices (3 Sapphire jewels allocating 2-4 Sinister sockets).
- src: poe2db:Delirium (lines 62-226, ~2460-2490), poe2db:The_Raven_Trickster (lines 3036-3053), tier 2, crawl 2026-11-23
- notes: mods on those pages. Delirium unique "Difficulty" labels come from the community text and are not explained there.
