---
title: Currency Exchange & order book
status: done
tracker_topic: "Currency Exchange & order book"
tracker_note: "done (0.5.x; 2 conflicts open)"
defaults: v=0.5.x
---

Scope: how the in-game Currency Exchange works. Reading price sites → [[price-sites]]. Flipping playbook → claude/flipping-strategy.md. Version 0.5.x unless noted.

## What it is
@ v=0.5.x vol=stable conf=confirmed date=2026-11-17
An automated order book for stackable/bulk items. You post "I have X, I want Y at ratio R"; it matches against other players' orders, also while you're offline. Placing an order costs gold. Non-stackables (gear, uniques) go through async trade instead.
- src: poe2wiki Currency exchange market [S684], tier 2; NextTier PoE2 trade guide [S100], tier 3; retrieved 2026-11-17
- v: 0.1+ (still 0.5.x)
- notes: Tradeable on it: currency, distilled emotions, catalysts, expedition artifacts, essences, runes, omens, soul cores, boss invitations ([poe2wiki](https://poe2wiki.net/wiki/Currency_Exchange)).


## Where/when it unlocks
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Since 0.3 the exchange is run by Ange, unlocked in Act 4 (undocumented change per wiki); earlier it was Alva (Act 3 / hideout), with campaign NPCs Finn (Act 1) and Risu (Act 2) also offering it.
- src: poe2wiki Currency exchange market [S684] version history, tier 2; Mobalytics Currency Exchange [S059], tier 3; retrieved 2026-11-17
- v: 0.3+ (Ange); older text for Alva/Finn/Risu
- vol: may-change (1.0 campaign restructure)
- conf: single-source for current (wiki); sources disagree → [[conflicts]]
- notes: Matters for the skip route — when can you first sell drops? Re-check in the 1.0 campaign batch.


## Matching: instant vs limit orders
@ v=0.5.x vol=stable conf=confirmed date=2026-11-17
Hovering "Market Ratio" shows the best available ratios and stock. An order at or better than the market ratio fills immediately against existing orders; a greedier ratio becomes a standing order that waits for a match. Orders can partly fill; you can close an order at any time and collect what has filled.
- src: NextTier trade guide [S100], tier 3; Maxroll Currency Guide [S040], tier 3; poewiki Currency Exchange Market [S735] (PoE1 version of the same system), tier 2; retrieved 2026-11-17
- conf: confirmed (tier 3 ×2)
- notes: "Blocking order" (Mobalytics flipping guide): one huge or badly priced order at the top blocks less competitive orders behind it until it clears — only the best order matters for fill speed.


## Order limits and fees
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Gold is paid when placing an order and isn't refunded if you cancel (cancelling returns the items). Up to 10 active orders (PoE1 wiki for the shared system; tier-5 PoE2 source agrees).
- src: Mobalytics Currency Exchange [S059], tier 3; poewiki Currency Exchange Market [S735], tier 2 (PoE1); retrieved 2026-11-17
- conf: confirmed for no-refund; 10-order limit single tier-2 (PoE1) + tier 5
- notes: How the fee scales is a conflict — Maxroll: scales with number of items traded; PoE1 wiki: fixed per item by rarity, scaling linearly; poe2wiki lists per-item gold costs (Scroll of Wisdom 1, Gemcutter's Prism 1,000). → [[conflicts]]. [INFERRED] fee ≈ per-item cost (by currency rarity) × quantity. Fee cost matters for flipping: margin must clear it.


## Order book visibility
@ v=? vol=may-change conf=confirmed date=2026-11-17
The live order book (open orders) is only visible in game; external sites see completed-trade history. GGG's public exchange API returns purely historical hourly digests per currency pair (volume traded, lowest/highest stock, lowest/highest ratio) — the current hour can't be fetched.
- src: GGG Developer Docs — Currency Exchange [S014], tier 1; user's own observation in [[league-lifecycle-pricing]]; retrieved 2026-11-17
- v: current API (2026)
- notes: So any site price is at least ~1 hour old. Check Market Ratio in game before a big swap.


## Base unit
@ v=0.5 vol=volatile conf=confirmed date=2026-11-10
In 0.5 economies the Exalted Orb is the base unit and the Divine Orb the store of value; Exalted inflated hard over Runes of Aldur (1 div = 38 ex day 1 → 61 day 3 → 406 day 30 → 549 on 2026-11-10).
- src: user's poe.ninja pull, Runes of Aldur, 2026-11-10 (claude/reveal-notes-and-price-findings.md), tier 4; Timesaver (poe2scout, 2026-07-11: 1 div ≈ 522 ex), tier 5
- v: 0.5 (Runes of Aldur)
- conf: confirmed (two dated data points agree on order of magnitude)
- notes: → [[value-retention]]: store wealth in Divines.
