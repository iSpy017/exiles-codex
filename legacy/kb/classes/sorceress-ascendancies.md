# Sorceress ascendancies — node text (0.5.x)

Version: 0.5.x (PoE2DB crawl 2026-11-23). 1.0 overhauls the tree; re-check every node at patch day.
Source: PoE2DB ascendancy pages in the local corpus ([[tools/poe2db-corpus]]) — [Stormweaver](https://poe2db.tw/us/Stormweaver), [Chronomancer](https://poe2db.tw/us/Chronomancer), [Disciple of Varashta](https://poe2db.tw/us/Disciple_of_Varashta), tier 2, crawl 2026-11-23. Single-source. Pathing order/adjacency isn't in the text crawl (tree is drawn by JavaScript) → which notables need which small nodes is a gap; check the in-game tree.
Points: 8 total, 2 per trial step ([[classes/ascendancy-trials]]).

## Stormweaver
- Small nodes: 12% increased mana regeneration · 12% increased spell crit chance · 20% increased shock chance · 25% increased chill duration · remnants collected 25% further away.
- Notables:
  - Constant Gale — you have Arcane Surge (permanently).
  - Force of Will — 20% of damage taken from mana before life; 20% increased Arcane Surge effect per 10% missing mana.
  - Tempest Caller — grants Elemental Storm; triggers it on spell critical hit.
  - Multiplying Squalls — +2 to limit for elemental skills.
  - Strike Twice — targets can have two of your Shocks; 25% less shock magnitude.
  - Shaper of Storms — all hit damage contributes to shock chance.
  - Heavy Snows — targets can have two of your Chills; your chills slow up to 35%; 25% less chill magnitude.
  - Shaper of Winter — all hit damage contributes to chill magnitude.
  - Storm's Recollection — remnants 50% further; remnants reappear once 3 s after collection.
  - Refracted Infusion — collecting an Elemental Infusion gives another, different one.
- Arcane Surge = 15% increased cast speed and 20% more mana regeneration rate, 4 s by default ([PoE2DB Keywords](https://poe2db.tw/us/Keywords)).

## Chronomancer
- Small nodes: buffs on you expire 10% slower · 8% increased AoE · 6% increased cast speed · 6% increased cooldown recovery · 6% increased slow magnitude · 4% increased skill speed + 6% increased AoE.
- Notables:
  - Now and Again — Cascadable spells 20% chance to Echo; **Repeatable spells 20% chance to Repeat**.
  - Phased Form — take **30% less damage**; 4 s after being damaged by a hit, take damage equal to 30% of that hit.
  - Apex of the Moment — enemies in your Presence are Slowed by 20%.
  - Footprints in the Sand — grants Temporal Rift. Ultimate Command — grants Time Freeze. Inevitability — grants Inevitable Agony. Unbound Encore — grants Time Snap. Quicksand Hourglass — grants Sands of Time. (Granted-skill text not captured here → gap.)
- Notes: Repeat = the skill fires its projectiles/effects again from one use; triggered, instant and channelled skills can't Repeat ([PoE2DB Keywords](https://poe2db.tw/us/Keywords)). Frostbolt and Ice Nova are Repeatable ([[gems/cold-spell-gems]]). Phased Form [INFERRED]: net 30% less + 30% later ≈ same total from that hit but spread over time — big for one-shots, not for sustained damage; it's unclear whether the delayed 30% is itself mitigated.

## Disciple of Varashta
- Small nodes: 20% increased max ES · 4% increased cast speed · 3% increased max mana · 8% increased AoE.
- Notables:
  - Sacred Rituals — 60% of current ES added to armour for physical damage reduction.
  - The Fourth Teaching — −1 s base ES recharge delay; 40% more ES recharge rate while on Low ES.
  - Varashta's Intuition — 100% of elemental damage taken from mana before life.
  - Instruments of Power — can equip a Focus with a Staff; 50% reduced bonuses from the Focus.
  - Baryanic Leylines — non-unique Time-Lost jewels 40% increased radius.
  - Djinn skills: Navira, the Last Mirage · Kelari, the Tainted Sands · Ruzhan, the Blazing Sword (+ follow-ups: Navira's Fracturing/Well/Oasis, Kelari's Deception/Judgment/Malediction, Ruzhan's Trap/Reckoning/Fury).
- Notes: ES base recharge delay is 4 s → 3 s with The Fourth Teaching ([[mechanics/energy-shield]]) [INFERRED arithmetic].

## Tier-list view (context)
- 0.5 Mobalytics tiers: Disciple A, Stormweaver B, Chronomancer C ([[builds/starter-archetypes]]). Those rate whole builds, not single nodes.
- Version: 0.5.x · Volatility: may-change · Confidence: single-source (node text)
