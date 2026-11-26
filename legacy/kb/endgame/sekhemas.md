# Trial of the Sekhemas (0.5.x baseline)

Status: partial — written 2026-11-23 for the 0.5.5 kb-test build. Endgame docs are otherwise deferred to the 1.0 notes (David, 2026-11-17); treat this as the 0.5 baseline and re-check at 1.0.
Source unless noted: [PoE2DB Trial of the Sekhemas](https://poe2db.tw/us/Trial_of_the_Sekhemas), [Honour](https://poe2db.tw/us/Honour), [Honour Resistance](https://poe2db.tw/us/Honour_Resistance), [Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23 ([[tools/poe2db-corpus]]). Single-source (game-data derived).
Profit view (creator, tier 5) → [[strategy/sekhemas-currency-farm]]. Ascendancy points and Barya levels → [[classes/ascendancy-trials]].

## Honour
- Claim: Honour is a resource used only inside the trial. A percentage of the damage you take from enemies is also taken from Honour; at zero Honour the trial fails. Starting and max Honour = max Life + max ES + max Runic Ward (+ max Mana if you have Mind Over Matter). Honour Resistance = you lose that much less Honour; capped at 75% by default, never above 90%.
- Version: 0.5.x · Volatility: may-change
- Confidence: single-source (game keyword text)
- Notes: the % of damage that becomes Honour loss is not stated → gap. [INFERRED] build implications: (1) avoiding hits matters more than recovering from them; (2) ES counts toward Honour like life, so an ES build has a bigger Honour pool; (3) mana only counts with Mind Over Matter.

## Floors and bosses
- Claim: Four floors: Test of Strength (boss Rattlecage, the Earthbreaker), Test of Will (Terracotta Sentinels), Test of Cunning (Ashar, the Sand Mother), Test of Time (Zarokh, the Temporal). Higher-level Baryas unlock more floors.
- Room types include timed (Hourglass), Ritual, Chalice, Escape, Gauntlet, Collapsing Cavern; reward rooms: Sacred Water fountains, Pledges, Honour shrines (Halani: restore + Sacred Water; Ahkeli: big restore + Affliction; Orbala: restore + Boon; Tabana: restore), Merchant, Bronze/Silver keys.
- A 4-floor run = 32 rooms ([[classes/ascendancy-trials]], poe2wiki).
- Version: 0.5.x · Confidence: single-source

## Afflictions (debuffs) that hit an ES caster hardest
- Corrosive Concoction (major): no armour, evasion or ES. Shattered Shield (minor): 50% less ES. Orb of Negation (major): non-unique relics have no effect. Worn Sandals (minor): 30% reduced movement speed if hit recently. Fiendish Wings (minor): monsters 25% increased attack/cast/move speed, can't be slowed below base.
- [INFERRED] Corrosive Concoction and Shattered Shield also cut max Honour for an ES build (Honour = life + ES) — check whether max Honour updates mid-run.

## Useful Boons / Pledges
- Lustrous Lacquer: 50% more armour/evasion/ES. Orbala Statuette: 25% more max Honour. Black Pearl: traps deal 50% reduced damage. Adrenaline Vial: restore Honour on entering a boss room.
- Pledge to the Powerful: 50% less Honour lost in boss rooms, 100% more in non-boss rooms. Pledge to the Guileful: open 1 reward chest per room without a key (take phys damage). Pledge to the Deserted: 50% cheaper merchant, no Sacred Water from monsters.

## Unique relics (Zarokh drops)
- The Last Flame (Incense): Zarokh drops Temporalis; damage taken can't be Absorbed; max Honour is 1; only Trials level 80+.
- The Desperate Alliance (Vase): Zarokh drops Against the Darkness; **Zarokh deals 100% more damage and takes 75% less damage**.
- The Burden of Leadership (Tapestry): Zarokh drops Sekhema's Resolve; rooms are unknown on the Trial Map.
- The Peacemaker's Draught (Amphora): Zarokh drops 1 additional Barya; your armour, evasion and ES are zero.
- The Changing Seasons (Seal): Zarokh drops Sandstorm Visage; can't restore Honour.
- All are destroyed when applied.
- Version: 0.5.x · Confidence: single-source
- Notes: Desperate Alliance = 4× Zarokh's effective life (75% less damage taken) and double his damage → the Against the Darkness farm needs much more DPS and defence than a plain run [INFERRED arithmetic]. Peacemaker's Draught zeroes ES — a pure ES build can't use it.

## Relic inventory
- 12 slots, unlocked by completing floors (Strength, Will, Cunning, Time).

## Zarokh, the Temporal
- Life 750% of base, 7% ES from life; page level 22 = 2,288 life before rarity; elemental res 15% each on the page (PoB spectre data: 0%) → kb/04-conflicts.md. Effective life at a given Barya level → [[mechanics/monster-life]].

## Unique rewards (names)
- Temporalis (body armour), Sandstorm Visage (helmet), Sekhema's Resolve / Safrin's Resolve (rings), Against the Darkness (Time-Lost Diamond), Grand Spectrum (Ruby/Emerald/Sapphire). Mods on PoE2DB page; prices → [[strategy/sekhemas-currency-farm]] (tier 5, undated).
