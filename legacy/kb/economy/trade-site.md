# Trade site, async trade & bulk exchange

Scope: trading non-stackable items. Currency → [[currency-exchange]]. Version 0.3+ (still 0.5.x).

## Three ways to trade
- Claim: (1) Currency Exchange — stackables, gold fee, works offline. (2) Asynchronous trade via Merchant's Tabs — gear, uniques, other non-stackables; instant buyout, works offline. (3) Direct trade — anything except gold, both players online, free.
- Version: 0.5.x
- Volatility: may-change
- Source: [NextTier PoE2 trade guide](https://nexttier.pro/guide/poe2-trade-guide), tier 3; [poe2wiki Asynchronous trading](https://www.poe2wiki.net/wiki/Asynchronous_trading), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Asynchronous trade (Merchant's Tabs)
- Claim: Added in 0.3 (The Third Edict). Items listed in a Merchant's Tab appear on the official trade site and the in-game market panel and can be bought instantly, even while you're offline. Faustus manages the tabs (met in Act 6 Lioneye's Watch or Kingsmarch, then in your hideout). The seller pays nothing; the buyer pays a gold fee shown on the listing — the formula is unknown (appears to depend on item rarity tier, item level and other factors). The gold doesn't go to the seller.
- Version: 0.3.0+
- Volatility: may-change (1.0 campaign has new acts; Act 6 meeting point may move)
- Source: [poe2wiki Asynchronous trading](https://www.poe2wiki.net/wiki/Asynchronous_trading), tier 2 (cites GGG Async Trade FAQ, 2025-08-25, and dev Q&A); [PoE2DB Merchant's Tab](https://poedb.tw/jp/Merchants_Tab), tier 2; [game8 async trade](https://game8.co/games/Path-of-Exile-2/archives/545617), tier 5; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Merchant's Tabs aren't usable in SSF. Earnings collect in "Ange's Earnings Tab" (game8, tier 5). Premium tabs bought before 0.3 could be converted; later tabs are bought as Merchant's Tabs (MTX).

## Trade site search
- Claim: pathofexile.com/trade2 searches listings; the "instant buyout" filter limits results to async listings; "any" includes old whisper-trade listings. You can travel to the seller's hideout from the site for a buyout.
- Version: 0.3+
- Volatility: may-change
- Source: GGG forum thread [3921564](https://web.poecdn.com/forum/view-thread/3921564), tier 5; [Mobalytics async trading with Faustus](https://mobalytics.gg/poe/guides/merchant-tabs-and-async-trading-with-faustus) (PoE1 version, same flow), tier 3; retrieved 2026-11-17
- Confidence: confirmed (two sources)
- Notes: Built-in price check (Shift + Alt + Click, since 0.5.0) and Exiled Exchange 2 overlay — from David's flipping doc (claude/flipping-strategy.md), not independently verified. [INFERRED] OK to rely on: both are standard community tools.

## Bulk exchange
- Claim: The old trade-site "bulk item exchange" role is covered by the in-game Currency Exchange for stackables; async trade only handles non-stackables.
- Version: 0.3+
- Volatility: may-change
- Source: GGG forum thread [3921564](https://web.poecdn.com/forum/view-thread/3921564) (async = non-stackables only), tier 5; Timesaver currency-exchange guide (calls it "Bulk Item Exchange"), tier 5; retrieved 2026-11-17
- Confidence: [INFERRED] from two tier-5 sources — confirm whether the trade site still has a separate bulk tab
