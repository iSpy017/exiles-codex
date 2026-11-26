# Stun and Heavy Stun
Status: partial. Have: light/heavy stun rules, priming %, monster stun constants from game data. Missing: per-monster stun threshold numbers, heavy stun buildup formula, exact re-stun immunity length.
Version: 0.5.x data (PoE2DB crawl 2026-11-23). Re-check all at 1.0. Merged with the earlier library doc (2026-11-17 entries kept under "Carried over").
Sources: PoE2DB Stun, Heavy Stun, Keywords, Monster, Dazed (tier 2).

## Two kinds of stun
- Claim: any hit can cause a Light Stun, lasting a fraction of a second. Chance is damage-based, up to 100% for a hit equal to 100% of target max Life; chances below 15% count as 0. Heavy Stun happens when the target's Stun bar fills and lasts several seconds; hits add buildup based on damage.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Stun](https://poe2db.tw/us/Stun), [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: players and their minions usually cannot be heavy stunned, except specific actions (raising a shield, parrying with a buckler, riding a mount).

## Player stun threshold
- Claim: base player Stun Threshold equals max Life. A hit equal or above it guarantees a stun; chance scales down linearly below. Chances under 10% count as 0.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: passive nodes give 12% increased Stun Threshold each ([PoE2DB Stun Threshold](https://poe2db.tw/us/Stun_Threshold)). Note the light-stun floor differs: 15% for enemies/general text, 10% for player threshold text; both appear on the same page.

## Enemy stun threshold and priming
- Claim: lower enemy Stun Threshold means less buildup needed to stun or heavy stun. Primed for Stun at heavy-stun buildup: Normal 40%, Magic 50%, Rare 60%, Unique 70%.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: not found in PoE2DB: a base stun threshold number for monsters or a table by monster level. Map mods raise it: Unwavering suffix gives monsters 30-39 / 40-49 / 60-69 / 70-79 percent increased Stun Threshold across the four map tiers ([PoE2DB Ailment](https://poe2db.tw/us/Ailment)). Monster mods seen: Stun Resistant (250% increased Stun Threshold), Stuns (100% increased Stun buildup), Steadfast and a variant (cannot be stunned).

## Heavy stun duration and bar (monster game data)
- Claim: Monster Default stats list base heavy stun duration 2000 ms and base light stun duration override 500 ms. Separate stats "poise decay delay" = 8000 ms and "poise decay per second" = 5%.
- Claim [INFERRED]: poise is the heavy-stun bar, so it would decay 5% per second after an 8 s delay without new buildup. Reason: the poise stats sit beside the stun stats, but PoE2DB never states they govern the heavy-stun bar.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Monster](https://poe2db.tw/us/Monster) "Monster Default" table, tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: the poise mapping is [INFERRED] (see above); PoE2DB does not state it. Related mod: Amanamu shield suffix, Heavy Stun buildup empties 30-40% faster ([PoE2DB Heavy Stun](https://poe2db.tw/us/Heavy_Stun)).

## Stun buildup multipliers
- Claim: player Physical damage and player Melee damage each give 50% more Light Stun chance and heavy stun buildup (multiplicative together). Monster Physical gives 100% more and monster Melee 33% more; Monster Default stats show the same (physical 100, melee 33).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Stun](https://poe2db.tw/us/Stun), [PoE2DB Monster](https://poe2db.tw/us/Monster), tier 2, crawl 2026-11-23
- Confidence: confirmed (two pages)
- Notes: Daze: lasts 8 s, enemy takes 50% more Stun buildup ([PoE2DB Dazed](https://poe2db.tw/us/Dazed)).

## Monster rarity and party scaling of the stun bar
- Claim: the stat "poise threshold" gets final increases by rarity: Magic +26%, Rare +125%, Unique +500%. Per extra party player: default monster +50%; Magic +10%, Rare +30%, Unique +85%.
- Claim [INFERRED]: poise threshold is the heavy stun threshold. Reason: name proximity to stun stats only; not stated on PoE2DB.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Monster](https://poe2db.tw/us/Monster) Magic/Rare/Unique stats and Monster Default, tier 2, crawl 2026-11-23
- Confidence: [INFERRED]: reading poise threshold as the heavy stun threshold; also unclear whether the +50% default and rarity per-player values stack or replace each other.
- Notes: see [[mechanics/monster-life]].

## Stun immunity windows
- Claim: after a heavy stun, re-stunning is harder for a short time (no duration given). Some bosses have stun/freeze immunity windows; 0.5.4b removed most of them from Tor Gul fights.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Heavy Stun](https://poe2db.tw/us/Heavy_Stun), [PoE2DB Freeze version history](https://poe2db.tw/us/Freeze), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: not found: the numeric length of the post-stun resistance window.

## Carried over from earlier version (2026-11-17)
- Claim: Heavily stunned targets count as Immobilised. Heavily stunned players can't block, deflect or evade. The player heavy-stun bar only empties while not raising a shield / parrying / riding. "Unwavering Stance" = can't be light stunned, but no dodge roll or sprint. Blocked hits still apply stun ([[mechanics/block]]). Crushing Blows heavy-stun Primed enemies outright. Cold hits build Freeze, not heavy stun.
- Version: 0.5.5.9 · Volatility: may-change
- Source: RePoE poe2 keywords.json ("Heavy Stun", "Player Heavy Stun", "Crushing Blows"), tier 2; [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: phys + melee player hits ≈ 2.25× stun buildup ([INFERRED] arithmetic from the two 50% more multipliers). Light-stun floor 15% vs 10% wording → [[04-conflicts]].
