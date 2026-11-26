# Druid Ascendancies (Shaman, Oracle)

Status: done for 0.5.x node text; partial otherwise (no node layout/order, no trial info, no 1.0 check; notable-vs-small flag is inferred, see below).
Version: 0.5.x (PoE2DB crawl 2026-11-23). NOT verified for 1.0.
Sources: PoE2DB class page [Druid](https://poe2db.tw/us/Druid), ascendancy pages [Shaman](https://poe2db.tw/us/Shaman) and [Oracle](https://poe2db.tw/us/Oracle), skill pages [Apocalypse](https://poe2db.tw/us/Apocalypse), [Moment of Vulnerability](https://poe2db.tw/us/Moment_of_Vulnerability), [Align Fate](https://poe2db.tw/us/Align_Fate). All tier 2, crawl 2026-11-23.

## Which Druid ascendancies exist
- Claim: Only two Druid ascendancies appear in the corpus: Shaman (14 nodes incl. start) and Oracle (17 nodes incl. start). Start-node IDs are AscendancyDruid1Start (Oracle) and AscendancyDruid2Start (Shaman); no third ID found.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Oracle](https://poe2db.tw/us/Oracle), [PoE2DB Shaman](https://poe2db.tw/us/Shaman), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Druid class page itself has no ascendancy list, only an "Oracle Passives" image link. Corpus grep for AscendancyDruid3 not conclusive (grep errored on a filename); [INFERRED] two only because no other page names one.

## Druid class basics
- Claim: Starting attributes Str 11, Dex 7, Int 11. Weapon type: Primal (new weapon type: Talismans). Class blurb advertises Shapeshifting (Bear, Werewolf, Wyvern), "Lasting Destruction" and "Nature's Bounty".
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Druid](https://poe2db.tw/us/Druid), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Page says "Werewolf" in the blurb but the skill list calls it Wolf Form. Rage: the class page only shows Bear skill text (Maul generates Rage, Rampage consumes it). No Rage cap/mechanics on the page. See [[mechanics/shapeshifting]] if it exists (not checked).

## Druid forms and skills listed on class page
- Claim: Wolf Form: Shred, Lunar Assault, Pounce, Arctic Howl, Cross Slash, Lunar Blessing. Bear Form: Maul, Furious Slam, Fury of the Mountain, Ferocious Roar, Rampage, Walking Calamity. Wyvern Form: Rend, Rolling Magma, Wing Blast, Devour, Oil Barrage, Flame Breath. Spells: Volcano, Entangle, Thunderstorm, Spell Totem, Tornado, Thrashing Vines. Spirit: Briarpatch, Savage Fury, Wolf Pack, Barkskin, Eternal Rage, Feral Invocation.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Druid](https://poe2db.tw/us/Druid), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Gem tier list also names Shockwave Totem, Trinity. Class passive-tree overrides exist (14 rows) but are out of scope here.

## Shaman: overview
- Claim: 14-node ascendancy (start + 5 unnamed small nodes + 8 named nodes). Flavour: "vengeance incarnate". Page does not state node order, branch layout, or which nodes are notables.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Shaman](https://poe2db.tw/us/Shaman), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: The page lists the 5 unnamed ones first (generic stat nodes), then the 8 named ones. [INFERRED] named = notables, unnamed = small nodes; reason: naming pattern matches Oracle/Sorceress pages, page has no explicit flag. Compare [[classes/sorceress-ascendancies]]. Build use: [[builds/storm-shaman]].

## Shaman: small (unnamed) nodes
- Claim: (a) 12% increased Elemental Damage; (b) +3 to Maximum Rage; (c) +3% to all Elemental Resistances; (d) 12% increased Life and Mana Recovery from Flasks; (e) 10% increased Armour, Evasion and Energy Shield.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Shaman](https://poe2db.tw/us/Shaman), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Page shows node "shaman1" (the +3% all Elemental Resistances node) with a numeric hash; no other layout data.

## Shaman: named nodes
- Claim:
  - **Turning of the Seasons**: enemies in your Presence have Exposure; gain 10% of Damage as Extra Damage of a random Element.
  - **Bringer of the Apocalypse**: grants skill Apocalypse (see below).
  - **Druidic Champion**: every 2 Rage also grants 1% more Spell damage.
  - **Reactive Growth**: 10% less Elemental Damage taken; Adapt 1 time to the highest Elemental Damage Type of each Hit taken; 10% less Damage taken of each Elemental type per matching Adaptation; base max adaptations 3.
  - **Avatar of Evolution**: 5% of Physical damage taken as Fire, 5% as Lightning, 5% as Cold; Adaptations last 5 seconds; double Adaptation effect.
  - **Furious Wellspring**: no inherent Rage loss; regenerate 6% of max Rage per second; your mana-regeneration-rate modifiers also scale this Rage regen; skills have +5 Rage cost; +7 to Maximum Rage.
  - **Sacred Flow**: +40 Spirit for each empty Charm slot.
  - **Wisdom of the Maji**: gain the benefits of Bonded modifiers on Runes and Idols.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Shaman](https://poe2db.tw/us/Shaman), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: "Exposure" type (which element) not stated on the node line; it is not clear from the page whether Exposure matches the random element. Bonded modifiers: not defined on this page.

## Shaman: granted skill Apocalypse
- Claim: Spell/Buff, Lightning/Cold/Fire, Trigger. Cast time 1.00 s, mana cost (8-55) by level, level 1-20, requires character level 1-90. Needs 100 Glory to use; Glory is built by hitting enemies with Elemental damage (100 Glory-generation stat per elemental hit shown). On max Glory you become the Apocalypse for 12 seconds, triggering one of three disasters every 0.75 s. Disasters: Hailstorm (Cold, 2 m radius, 9 ice chunks, 12% crit), Meteor (Fire, lands after 2 s, 1.6 m explosion, 7% crit), Crash Lightning (Lightning, 3 pulses then final strike after 3 s, 1.6 m, 10% crit). Skill base AoE radius 70; movement speed -70% (final) while performing the action.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Apocalypse](https://poe2db.tw/us/Apocalypse), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Damage grows steeply with gem level (L1 → L20): Hailstorm cold 3–4 → 128–192; Meteor fire 19–28 → 902–1,352; Crash Lightning per pulse 1–7 → 59–335, final strike 3–20 → 169–958. Full per-level table not recorded. Quality: (0-15)% increased frequency of Hailstorm triggers. Quality text for other disasters not checked.

## Oracle: overview
- Claim: 17-node ascendancy (start + 2 passive-point nodes + 6 small stat nodes + 8 named nodes). Flavour: "many paths to achieve your goals". Page gives no layout or order.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Oracle](https://poe2db.tw/us/Oracle), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Same inference as Shaman: named = notables [INFERRED], no explicit flag. Totem/spell/crit theme, relevant only if comparing to Shaman.

## Oracle: small nodes
- Claim: Two "Passive Point" nodes each grant 1 passive skill point (one is tagged with mastery Ultimatum on the page). Six stat nodes: 8% increased Life Regeneration rate and 8% increased Mana Regeneration Rate; 20% increased Immobilisation buildup; 12% increased Spell Damage; Spells cast by Totems 5% increased Cast Speed and Attacks used by Totems 5% increased Attack Speed; Hits against you have 12% reduced Critical Damage Bonus; 12% increased Critical Hit Chance.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Oracle](https://poe2db.tw/us/Oracle), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Node IDs shown oracle8-oracle11 only; no layout.

## Oracle: named nodes
- Claim:
  - **Entwined Realities**: passives (not keystones) within a medium radius of a keystone you hold can be taken even if they aren't linked to the rest of your tree.
  - **The Unseen Path**: "Walk the Paths Not Taken" (no mechanical text given on the page).
  - **Harmony Within**: Hit damage is taken from Mana before Life while current Mana > current Life; 15% less maximum Life; 15% less maximum Mana.
  - **Converging Paths**: grants skill Moment of Vulnerability.
  - **Fateful Vision**: grants skill Align Fate.
  - **Unnamed Heartwood**: +1 maximum Summoned Totems; Totems die 6 seconds after Life reaches 0.
  - **The Lesser Harm**: enemy Critical Hit Chance against you is Unlucky; damage of enemies Hitting you is Unlucky.
  - **Forced Outcome**: Inevitable Critical Hits.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Oracle](https://poe2db.tw/us/Oracle), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: The Unseen Path and Forced Outcome have only keyword text; "Inevitable Critical Hits" definition not on page. Node named "Unnamed Heartwood" is as written on the page.

## Oracle: granted skills
- Claim: Moment of Vulnerability: Spell/AoE/Nova, cast 0.65 s, cooldown 1.00 s, mana (6-18), nova radius 4 m, Physical damage 1-2 at level 1. When it hits an enemy that is primed for stun, electrocute or freeze, it spawns a time-copy of that enemy for as long as the ailment would have lasted; 10 s before the enemy can be affected again; 60% (L1) rising to 98% (top level) of damage dealt to visages is also dealt to the original. Align Fate: persistent buff, no cost listed. Visages of you appear every 12 s at L1 down to 9.15 s at L20 and cast one of your spells from the first valid weapon set; damaging, non-Channelling, non-Buff spells without cooldown only. Casting the matching spell before the next visage empowers it: 30% more damage. 25% more Visage frequency per spell the visages could cast. Cooldown Recovery Rate modifiers also apply to visage frequency.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Moment of Vulnerability](https://poe2db.tw/us/Moment_of_Vulnerability), [PoE2DB Align Fate](https://poe2db.tw/us/Align_Fate), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: Align Fate quality: (0-20)% more Visage frequency. Moment of Vulnerability quality: +(0-20)% damage shared to the original.

## 1.0 status
- Claim: GGG's 1.0 press release names four ascendancy reworks — Mercenary, Infernalist, Blood Mage, Acolyte of Chayula. Shaman and Oracle aren't among them. The 1.0 passive-tree overhaul could still change these nodes, so re-check at 1.0.
- Version: 1.0 announcement (pre-patch-notes)
- Volatility: volatile
- Source: [GGG 1.0 press release](https://www.pathofexile.com/forum/view-thread/4013917/page/1), tier 1, 2026-11-11, as recorded in [[builds/starter-archetypes]] and [[02-sources]]; tree overhaul per [[strategy/official-1.0-reveal]]
- Confidence: single-source (tier 1); "not reworked" = absence from that list, so changes outside it are still possible
- Notes: tracker row → needs-1.0-check once the patch notes are out.
