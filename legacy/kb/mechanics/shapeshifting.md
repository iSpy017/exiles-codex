# Shapeshifting, Rage and Glory (Druid)

Status: partial. Missing: which form each Talisman base grants (not in corpus), exact spell-casting-while-shifted behaviour, Rage gain/loss numbers beyond the Keywords entry, Glory per-skill numbers other than those below, any 1.0 checks.
Version: all entries 0.5.x (PoE2DB crawl 2026-11-23). None checked against 1.0.
Sources: PoE2DB Keywords, form pages, skill pages, Talismans, Shaman ascendancy nodes (tier 2); one 0.4/0.5-era official-text mirror via PoE2DB (tier 1 text hosted on PoE2DB).
Note: PoE2DB has no "Wolf Form" page; the form is named Werewolf Form.

## Shapeshifting definition
- Claim: Shapeshifting turns you into a non-human form. Shapeshift skills still use your character's stats unless the skill says otherwise. Using a skill not compatible with the current form automatically returns you to human form.
- Version: 0.5.x | Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: single-source (also repeated on [PoE2DB Shapeshifting](https://poe2db.tw/us/Shapeshifting))
- Notes: This is the rule that decides whether spells can be cast mid-form; see next entry.

## Three animal forms
- Claim: Forms are Bear, Werewolf and Wyvern. Each form page lists its skills and a passive bonus. A separate Demon Form skill (Shapeshift tag) exists as an ascendancy gem and is not a Talisman form.
- Version: 0.5.x | Volatility: may-change
- Source: [Bear Form](https://poe2db.tw/us/Bear_Form), [Werewolf Form](https://poe2db.tw/us/Werewolf_Form), [Wyvern Form](https://poe2db.tw/us/Wyvern_Form), [Demon Form](https://poe2db.tw/us/Demon_Form), tier 2, crawl 2026-11-23
- Confidence: confirmed (form pages and Keywords agree)

| Form | Passive bonus while in form | Skills listed (PoE2DB) |
|---|---|---|
| Bear | +10 Armour per level; 30% of Armour also applies to Elemental damage; 1 Endurance Charge per 15 Rage spent | Maul, Rampage, Furious Slam, Molten Crash, Fury of the Mountain, Ferocious Roar, Walking Calamity |
| Werewolf | Drops to all fours after moving briefly: 30% increased movement speed when not Sprinting | Shred, Pounce, Cross Slash, Lunar Assault, Lunar Blessing, Arctic Howl |
| Wyvern | 50% increased Stun Threshold; 50% increased Elemental Ailment Threshold; 50% faster start of ES recharge | Rend, Rolling Magma, Wing Blast, Oil Barrage, Flame Breath, Devour |

## Entering and leaving a form
- Claim: Each form skill says "Shapeshift into X"; using it puts you in that form. Maul adds 0.3 s to base use time when Shapeshifting; Furious Slam adds 0.4 s; Molten Crash adds 0.55 s to total attack time. Using an incompatible skill returns you to human form.
- Version: 0.5.x | Volatility: may-change
- Source: [Maul](https://poe2db.tw/us/Maul), [Furious Slam](https://poe2db.tw/us/Furious_Slam), [Molten Crash](https://poe2db.tw/us/Molten_Crash), tier 2, crawl 2026-11-23
- Confidence: single-source per number
- Notes: Walking Calamity effects pause (not end) when you leave Bear form and resume if you return before the duration ends ([Walking Calamity](https://poe2db.tw/us/Walking_Calamity)). Commanding minions no longer reverts you to human form, except channelled commands ([Version 0.4.0b](https://poe2db.tw/us/Version_0.4.0b)).

## Talismans: the weapon
- Claim: Talismans are two-handed melee weapons needing Strength and Intelligence. They let you use Shapeshift skills of the Talisman's current form and give a basic attack for that form; you can change the Talisman's form at any time. Having a Talisman in the active weapon set puts you in its form; any skill barred from Shapeshift forms is then also barred while that Talisman is equipped. Triggered and Persistent skills keep working.
- Version: 0.5.x | Volatility: may-change
- Source: [Keywords](https://poe2db.tw/us/Keywords) (Talismans entry), [PoE2DB Talismans](https://poe2db.tw/us/Talismans), tier 2, crawl 2026-11-23
- Confidence: confirmed (two pages)
- Notes: Form skill gems show "Requires: Talismans". Spirit Vessel and Feral Invocation carry hidden stats ignoring the Talisman requirement / form restriction ([Spirit Vessel](https://poe2db.tw/us/Spirit_Vessel), [Feral Invocation](https://poe2db.tw/us/Feral_Invocation)).

## Can spells be cast in form? (relevant to Storm Shaman)
- Claim: Spell gems checked (Thunderstorm, Volcano, Tornado) have no "Requires: Talismans" line and use staff-style weapon rules like normal spells. Per the Keywords rule, a Talisman in the active weapon set forces the form, and non-form skills are unusable with it.
- Version: 0.5.x | Volatility: may-change
- Source: [Thunderstorm](https://poe2db.tw/us/Thunderstorm), [Volcano](https://poe2db.tw/us/Volcano), [Tornado](https://poe2db.tw/us/Tornado), [Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: [INFERRED]: no page states "spells cannot be cast with a Talisman"; derived from the Keywords Talisman rule plus the absent Talisman requirement on spells.
- Notes: Release text describes human form as the staff-wielding spell form whose skills "aid his animal-form abilities" ([Fate of the Vaal league page](https://poe2db.tw/us/Fate_of_the_Vaal_league)). Druid class page's Exilecon 2023 blurb ("while your spells are active, transform into a bear") reads as outdated design text; see Conflicts. Hits with spell damage can still grant Rage via Druidic Prowess (below).

## Rage: base rules
- Claim: Rage grants 1% more Attack damage per Rage. Default max 30. You lose 1 Rage every 0.2 s. Loss is paused 4 s after gaining Rage or after taking damage. Only one Hit per 0.5 s can grant Rage.
- Version: 0.5.x | Volatility: may-change
- Source: [Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: single-source. Confirms [[mechanics/recovery]]; correction: the pause also triggers on taking damage (library said only "after 4 s").
- Notes: Rage can be Leeched (one instance at a time, removed when full; hits over 40,000 damage count as 40,000).

## Rage: gain sources
- Claim: Maul gives 5 Rage on Hit. Rage I support gives 3 Rage on Melee Hit. Ferocious Roar grants Rage when enemies are near. Druidic Prowess (stacking buff, max 3, 10 s each) gives 10% increased Skill Speed and 3 Rage per stack on Hits with Spell damage. Helbrym's Composure grants Rage equal to 3% of stored damage. Eternal Rage (spirit gem, 100 Spirit) regenerates 0.25-5 Rage/s by gem level. Walking Calamity buff regenerates 5 Rage/s for 10 s.
- Version: 0.5.x | Volatility: may-change
- Source: [Maul](https://poe2db.tw/us/Maul), [Rage I](https://poe2db.tw/us/Rage_I), [Druidic Prowess](https://poe2db.tw/us/Druidic_Prowess), [Eternal Rage](https://poe2db.tw/us/Eternal_Rage), [Walking Calamity](https://poe2db.tw/us/Walking_Calamity), tier 2, crawl 2026-11-23
- Confidence: single-source each

## Rage: spenders
- Claim: Rampage costs 5 Rage/s (ignored for first 2.5 s of channel); Flame Breath 6 Rage/s (ignored first 4 s; Power Charge empowered halves it); Furious Slam spends 10 Rage for the enraged slam; Molten Crash consumes 10 Rage on landing for 1 extra Fissure; Lunar Blessing spends all Rage to extend its buff. Rampage and Flame Breath cannot gain Rage while channelling.
- Version: 0.5.x | Volatility: may-change
- Source: [Rampage](https://poe2db.tw/us/Rampage), [Flame Breath](https://poe2db.tw/us/Flame_Breath), [Furious Slam](https://poe2db.tw/us/Furious_Slam), [Molten Crash](https://poe2db.tw/us/Molten_Crash), [Werewolf Form](https://poe2db.tw/us/Werewolf_Form), tier 2, crawl 2026-11-23
- Confidence: single-source each
- Notes: Bear form grants an Endurance Charge per 15 Rage spent.

## Shaman nodes on Rage
- Claim: Druidic Champion: every 2 Rage also grants 1% more Spell damage. Furious Wellspring: no inherent Rage loss, regenerate 6% of max Rage per second, mana regeneration rate modifiers also apply to Rage regeneration, skills have +5 Rage cost, +7 max Rage. Shaman also has a +3 max Rage small node. Bringer of the Apocalypse grants Apocalypse.
- Version: 0.5.x | Volatility: may-change
- Source: [Druidic Champion](https://poe2db.tw/us/Druidic_Champion), [Furious Wellspring](https://poe2db.tw/us/Furious_Wellspring), [Shaman](https://poe2db.tw/us/Shaman), tier 2, crawl 2026-11-23
- Confidence: confirmed against [[classes/druid-ascendancies]] (library)
- Notes: [INFERRED]: with default max 30, Druidic Champion alone is up to 15% more Spell damage; with Wellspring max 37 (+3 node, plus other max-Rage sources) it rises, because 1% per 2 Rage is simple arithmetic on the node text. Primal Hunger keystone (100% more max Rage, regen 1 Rage/s per 4 Rage spent Recently, no Rage effect) exists on the tree ([Primal Hunger](https://poe2db.tw/us/Primal_Hunger)).

## Glory
- Claim: Glory is a resource spent to use certain powerful skills. Each such skill has its own generation method; actions against enemies generate Glory equal to the monster's Power; skills track Glory separately; each skill generates Glory at most once per 0.5 s per monster. Skills lose 2 Glory/s if they have not gained Glory in the past 15 s. You cannot gain Glory for a skill while an instance of it is active (unless Banner).
- Version: 0.5.x | Volatility: may-change
- Source: [Glory](https://poe2db.tw/us/Glory), [Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: confirmed (two pages)

## Apocalypse (Shaman) and Glory
- Claim: Apocalypse is a Spell/Buff/Trigger skill that builds Glory by Hitting enemies with Elemental damage; requires 100 Glory; lasts 12 s; triggers one of three disasters every 0.75 s (Hailstorm, Meteor, Crash Lightning). Cost 8-55 Mana, 1.00 s cast.
- Version: 0.5.x | Volatility: may-change
- Source: [Apocalypse](https://poe2db.tw/us/Apocalypse), tier 2, crawl 2026-11-23
- Confidence: single-source. 
- Notes: Walking Calamity (Bear) uses 50 Glory, built by gaining Rage while at max Rage. Passive "Glory Generation" nodes give 15% increased Glory generation each ([Glory Generation](https://poe2db.tw/us/Glory_Generation)).

Talisman bases, implicits and unique Talismans → [[items/talismans]].
