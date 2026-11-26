---
title: Reading poe.ninja & poe2scout
status: done
tracker_topic: "Reading poe.ninja / poe2scout (vol/hr vs rate)"
tracker_note: "done (sites unreachable from workspace)"
---

## Where PoE2 currency prices come from
@ v=? vol=may-change conf=confirmed date=2026-11-17
GGG publishes a public Currency Exchange API (`GET https://web.poecdn.com/api/currency-exchange/poe2/<id>`, id = unix timestamp truncated to the hour). It returns historical hourly digests for every currency pair that traded that hour, across all leagues: league, pair ids, volume traded, lowest/highest stock and lowest/highest ratio per side. The current hour can't be fetched, and old history may be removed later.
- src: GGG Developer Docs — Currency Exchange [S014], tier 1, retrieved 2026-11-17; same text pasted by David 2026-11-17
- v: current (2026)
- conf: confirmed (doc + live test)
- notes: poe.ninja's PoE2 economy section is built on the Currency Exchange rather than stash listings ([poe.ninja announcement](https://poe.ninja/posts/poe2-economy-and-rise-of-the-abyssal), tier 4).


## Live test of the GGG API (2026-11-17)
@ v=? vol=volatile conf=single-source date=2026-11-17
The endpoint is readable via web fetch (not via the workspace shell — proxy refuses web.poecdn.com). Calling it without an id returns the first hour of history (empty). The hour 2026-11-17 16:00 UTC (id 1794931200) returned a ~1.7 MB page; the readable part showed Standard-league markets, e.g. Greater Chaos ↔ Divine traded 174 / 288 units that hour, Greater Exalted ↔ Divine 8 / 2 units.
- src: web.poecdn.com/api/currency-exchange/poe2/1794931200 [S650], tier 1, retrieved 2026-11-17
- v: live data, 2026-11-17
- conf: single-source; the fetch tool truncates at 100k characters and summarises — usable for spot checks of a named pair, not bulk pulls
- notes: How lowest/highest_ratio encode a price isn't defined in the doc (values look like integer pairs per side) — [INFERRED] don't derive prices from them without testing against in-game Market Ratio. Item ids are internal (e.g. CurrencyModValues = Divine, CurrencyRerollRare = Chaos, CurrencyAddModToRare = Exalted; "2"/"3" suffix = Greater/Perfect), mapped via RePoE base_items.json. Volume_traded is per hour by definition — confirms David's per-hour reading of poe.ninja volume.


## poe.ninja (PoE2)
@ v=? vol=may-change conf=confirmed date=2026-11-17
PoE2 currency-type data (currency, fragments, essences, runes…) comes from an exchange overview: each line has a price in the primary reference currency, traded volume in that currency, the highest-volume paired currency and its rate, and a sparkline. Refreshes about hourly. Uniques are priced separately from trade listings (no exchange data), with up to 120 days of history.
- src: poe.ninja API docs [S104], tier 4; poe.ninja PoE2 uniques post [S105], tier 4; retrieved 2026-11-17
- v: current (2026)
- notes: Unique prices = asking prices from listings, not completed sales → more prone to bait/stale prices than exchange data [INFERRED]. poe.ninja economy pages render client-side and its host is blocked from the shell, so Claude can't read them here.


## poe2scout
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Community tracker for unique and currency price history in PoE2; quotes relative to the Exalted Orb (RelativePrice 1.0) in 0.5.
- src: PoE2DB Tools list [S118], tier 2; Timesaver currency-exchange guide (cites poe2scout values), tier 5; retrieved 2026-11-17
- notes: Not readable from the workspace (client-rendered; shell blocked). For prices, David pastes or screenshots poe.ninja, or Claude spot-checks a pair via the GGG API.


## How to read them
@ v=0.5.x vol=may-change conf=single-source date=2026-11-10
(1) Price = last hour's clearing rate, not the live order book — check Market Ratio in game before acting. (2) Check volume before trusting a price; under ~1 div/day volume, prices are often stale placeholders (late-league "exactly 1 div"). (3) Use the 7-day trend/sparkline to spot spikes. (4) Compare in Divines, not Exalts, across days (Exalt inflation).
- src: user's analysis — [[league-lifecycle-pricing]], claude/flipping-strategy.md, claude/reveal-notes-and-price-findings.md (tier 4, 2026-11-10 / 11-17); GGG API docs (tier 1) for the hourly basis
- conf: single-source (user experience) + tier 1 for data basis
