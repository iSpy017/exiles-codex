# Chill and Freeze
Status: partial. Have: durations, chill magnitude bounds, freeze priming %, player ailment threshold. Missing: monster freeze threshold numbers, buildup-per-hit formula, chill magnitude curve between 30% and 50%.
Version: 0.5.x data (PoE2DB crawl 2026-11-23). All values must be re-checked at 1.0. Merged with the earlier library doc (2026-11-17 entries kept under "Carried over").
Sources: PoE2DB Keywords/Chill/Freeze/Monster pages (tier 2).

## Chill: duration and magnitude
- Claim: Chill slows the target. Default duration 2 s on players, 8 s on non-players. Magnitude scales with chilling damage relative to the target's Elemental Ailment Threshold; minimum 30%, default maximum 50%. Chills under 30% are discarded, so small hits can fail to chill.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Chill](https://poe2db.tw/us/Chill) and [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: confirmed (same text on both pages; both are the same dataset)
- Notes: exact scaling formula between 30% and 50% is not stated on PoE2DB. Cold damage from hits chills by default; no chill chance needed. Related [[mechanics/ailments]].

## Chill: buff internals
- Claim: the Chilled buff applies an "action speed final from chill" stat; a second buff, "additional chill", applies a separate action-speed stat from a second chill.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Chilled](https://poe2db.tw/us/Chilled), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: the page lists stat names only, no numbers.

## Chill modifiers seen on tree nodes
- Claim: Invoker small node gives 15% increased magnitude of Chill you inflict. Stormweaver small nodes give 25% increased Chill duration on enemies.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Chill Effect](https://poe2db.tw/us/Chill_Effect), [PoE2DB Chill Duration](https://poe2db.tw/us/Chill_Duration), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: see [[classes/sorceress-ascendancies]].

## Freeze: duration and buildup
- Claim: Freeze leaves the target unable to move or act; default duration 4 s. Cold damage from hits builds Freeze buildup; target becomes Frozen at 100% buildup.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), [PoE2DB Freeze](https://poe2db.tw/us/Freeze), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: Block and other actions are unavailable to a frozen player (Block keyword text on the [PoE2DB Freeze](https://poe2db.tw/us/Freeze) page: cannot Block while Stunned or Frozen).

## Primed for Freeze
- Claim: an enemy is Primed for Freeze at this share of freeze buildup: Normal 40%, Magic 50%, Rare 60%, Unique 70%.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: single-source (repeated on Freeze page)
- Notes: priming is used by skills that "consume" or "freeze primed" enemies, e.g. the Shattering Concoction note in the Freeze version history.

## Freeze Threshold and Elemental Ailment Threshold
- Claim: Freeze Threshold sets how much Freeze buildup is needed to Freeze. Elemental Ailment Threshold also affects it: higher means less chance of elemental ailments and less Freeze/Electrocute buildup received; a player's default is half their Life.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), [PoE2DB Freeze Threshold](https://poe2db.tw/us/Freeze_Threshold), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: not found in PoE2DB: a monster freeze threshold value, a formula converting hit damage to buildup %, or any per-level monster ailment-threshold column. The Monster page "Monster Default", "Monster Stats" and rarity tables contain no freeze or ailment-threshold row. Monster threshold only appears as waystone/map mods: Unwavering suffix gives monsters 30-39 / 50-59 / 70-79 / 70-79 percent increased Ailment Threshold across the four map tiers (low / medium / high / highest), and a unique mod type gives 80-100% or 50% (see PoE2DB Ailment page).

## Defensive freeze/chill stats (player side)
- Claim: Freeze Threshold passive nodes give 15% increased Freeze Threshold each. Liquid-emotion notables seen: Chillproof (30% increased Freeze Threshold, 30% reduced Chill effect on you), Warm the Heart (60% increased Freeze Threshold, 25% reduced Freeze duration on you), Icebreaker (gain 50% of maximum Energy Shield as extra Freeze Threshold), Cold Coat (25% increased Freeze Threshold, 25% reduced Freeze duration).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Freeze Threshold](https://poe2db.tw/us/Freeze_Threshold), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: boots suffixes seen: reduced Freeze duration on you in tiers 36-40% up to 56-60% (Freeze page mod table). Icebreaker was nerfed in 0.2.0 from 100% to 50% of max ES.

## Freeze buildup sources
- Claim: Glaciation (Freeze Support, tier 2 per Freeze.txt gem block): supported skills cause 50% more Freeze buildup. Freezing Salvo in 0.5.0: 34-68% more chill magnitude and freeze buildup across gem levels 3-20.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Freeze](https://poe2db.tw/us/Freeze), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: historical: 0.2.0 made Freeze build up about 48% slower on enemies.

## Immunities
- Claim: Chill Immunity and Freeze Immunity buffs remove the ailment and block it. Bosses can have freeze/stun immunity windows; 0.5.4b removed most of them from all Tor Gul versions.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Chill Immunity](https://poe2db.tw/us/Chill_Immunity), [PoE2DB Freeze Immunity](https://poe2db.tw/us/Freeze_Immunity), [PoE2DB Freeze version history](https://poe2db.tw/us/Freeze), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: per-boss windows are not itemised here.

## Carried over from earlier version (2026-11-17)
- Claim: Chilled Ground chills anyone standing in it, 6 s default. "Slow magnitude" mods scale only the slow part of a debuff. Brittle: hits get up to +6% crit chance vs the target, scaled by the applying cold hit; 4 s. Cold hits build Freeze and can't build Heavy Stun ([[mechanics/stun]]). Thawing Charm gives freeze immunity ([[mechanics/charms]]).
- Version: 0.5.5.9 · Volatility: may-change
- Source: RePoE poe2 keywords.json ("Chilled Ground", "Brittle", "Freeze"), tier 2; [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; retrieved 2026-11-17
- Confidence: single-source (game data)

- Claim: For most monsters the ailment threshold equals max life; Unique bosses and some Rares have a lower threshold relative to life. Exact buildup formula is unknown per poe2wiki. Each time a boss is frozen its freeze threshold rises, then decays back over time (step and decay not stated). "Increased Freeze Buildup" mods give no base freeze chance on their own; blocking a hit does not stop its buildup.
- Version: 0.5.x · Volatility: may-change
- Source: [Mobalytics Chill](https://mobalytics.gg/poe-2/guides/chill), [Mobalytics Freeze](https://mobalytics.gg/poe-2/guides/freeze), tier 3; [poe2wiki Ailment](https://poe2wiki.net/wiki/Ailment), [poe2wiki Freeze](https://poe2wiki.net/wiki/Freeze), tier 2 (search snippets); retrieved 2026-11-17
- Confidence: confirmed for threshold ≈ max life (2 sources); single-source for boss threshold rise
- Notes: the 2026-11-23 PoE2DB crawl has no monster threshold table, so no numbers. Don't use PoE1 formulas from tier-5 dumps.
