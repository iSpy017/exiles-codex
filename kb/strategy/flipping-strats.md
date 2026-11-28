---
title: Flipping and trading strategies (creator videos)
status: partial
tracker_topic: "Flipping / trading strategies"
tracker_note: "partial (3 creator videos, 0.5.5, tier 5; claims unverified unless marked)"
defaults: v=0.5.5 vol=volatile conf=single-source
---
# Flipping and trading strategies (creator videos)

David's goal on the Currency Exchange is always flipping (buy low, sell high, round trips). This doc distils three creator videos (tier 5: one creator's play, prices undated within the 0.5.5 league). Mechanics are checked against [[economy/currency-exchange]]; anything else is the creator's claim. Our own dated order-book reads go to `data/prices/` and the "today vs then" entry at the bottom.

Dates on entries are the videos' upload dates (prices are as of recording, at or before upload). Videos: XTheFarmerX "Zero To Mirror Hideout Only" Ep 1 [S748] and Ep 2 [S749] (rules: start with 1 exalt, never leave the hideout except gold-leeching groups, no picking up currency); Spud the King "Spud to Mageblood" [S750] (fresh Druid in late 0.5.5, campaign-only money).

## Low-tier currency arbitrage (scrolls, augs, transmutes)
@ v=0.5.5 vol=volatile conf=single-source date=2026-09-12
On a fresh hideout-only start he flipped Scrolls of Wisdom by buying around 89–98 scrolls per exalt and selling around 63–64 per exalt: about 25 scrolls kept per exalt, roughly 30% a round trip, at one point near 100%. He ran the same loop on Orbs of Augmentation, Greater Augmentation and Transmutation, going from 1 exalt to about 5 in 45 minutes (most of that time spent getting gold) and to about 190 exalts a little later. His reason the margin exists: buyers of scrolls are lazy or rich players who would rather pay double than find the vendor.
- src: XTheFarmerX, Zero To Mirror Hideout Only Ep 1 [S748], ~0:53–13:20, tier 5, retrieved 2026-11-27
- notes: early-league margins. David's 2026-11-27 book for the same pair shows a 2.3% spread (bottom of this doc), so this edge decays as the league ages [INFERRED from two points in time].

## Diversify across several markets
@ v=0.5.5 vol=may-change conf=single-source
Run several pairs at once (he had wisdom, augs, greater augs and transmutes going together and said he was working about 12 markets). His reason: someone undercuts or dumps into one market at a time; with several pairs running, one dead market doesn't stall the money. The video shows exactly that: the aug market and then the wisdom market got undercut minutes after he posted.
- src: [S748] ~3:49–9:40, tier 5, retrieved 2026-11-27

## Undercut by the smallest step
@ v=0.5.5 vol=may-change conf=single-source
To get filled first, he posts one 0.01 ratio step better than the best competing order ("perfect mathematical undercut by .01").
- src: [S748] ~16:29–16:37, tier 5, retrieved 2026-11-27
- notes: matches the two-decimal ratios on David's screenshots (e.g. 18.50, 3.05); the actual minimum step isn't documented in the KB ([[economy/currency-exchange]]).

## Cross-currency flips (buy in one currency, sell in another)
@ v=0.5.5 vol=volatile conf=single-source date=2026-09-12
Price the same item in two currencies and use the exchange rate between them: he bought a catalyst at about 140 exalts each and sold it for 6.25 chaos, with 1 chaos ≈ 28 exalts, so 6.25 chaos ≈ 175 exalts and about 1 chaos profit per item (~20%). He then turned chaos back into exalts and repeated, buying a bigger batch each lap; he calls this "trinity trading". He worked out the cross-rates on paper first (1 chaos = 27 exalts, a Greater Chaos Orb ≈ 2.5 chaos, and so on).
- src: [S748] ~13:45–21:55, tier 5, retrieved 2026-11-27
- notes: a three-way check (A in exalts vs A in chaos vs chaos-to-exalt rate) is a planned feature of the margin tool.

## Margin × volume, then gold
@ v=0.5.5 vol=stable conf=single-source
His rule for picking flips: profit per hour = percentage margin × how often it fills, so a 5% flip that turns over in seconds can beat a 100% flip that takes minutes. A third factor is gold spent per flip (order fees), which didn't matter for him because gold came free from leeching. Judge by percentage, not by currency per flip, because a percentage scales with stake.
- src: [S748] ~22:05–23:13, tier 5, retrieved 2026-11-27
- notes: fits the KB's poe.ninja rule that volume is per hour ([[strategy/league-lifecycle-pricing]]). Spud gives the same advice: sort poe.ninja by volume per hour, not price; spirit gems level 4 showed only about 2 div per hour of volume, so you can't sell many no matter the price ([S750] ~9:24–9:50).

## Gold from leech groups
@ v=0.5.5 vol=may-change conf=single-source
Gold for order fees came from joining "gold rotas": map leaders running Breach want the party quantity bonus, the leecher takes only the gold (about 1M gold per map in his groups), and both sides win. He hit 1.35M gold in about 35 minutes.
- src: [S748] ~2:16–2:36, ~20:30–21:00, tier 5, retrieved 2026-11-27
- notes: why gold matters is in [[economy/gold]] (order fees, no refund).

## Keep idle currency working; online vs offline
@ v=0.5.5 vol=may-change conf=single-source
Never leave a pile of currency doing nothing: keep orders up while doing anything else. In his PoE1 version of this challenge he made about 3× more from orders that filled while he was offline than online, because fewer people were watching and undercutting him.
- src: [S748] ~11:18, ~16:00–16:17, ~30:32–30:43, tier 5, retrieved 2026-11-27

## Tablet crafting for profit (rate the mods, sell by tier)
@ v=0.5.5 vol=volatile conf=single-source date=2026-09-13
Buy cheap normal or magic tablets in bulk (about 2 chaos each in his batch; magic ones a little cheaper), roll them (Regal, then Alchemy on misses), and price each by what it hit. His price guide at the time: map effectiveness about 3–4 chaos (15% about 4 chaos), item rarity or monster rarity about 2 chaos, effectiveness + rarity 7–16 chaos, and the "additional random modifier" hit 4–6 divines. 21 tablets for about 6 div returned about 10 div on his first batch; he estimated 20–30 div profit over about 20 minutes. Misses that hit nothing go three-to-one at the reforging bench.
- src: XTheFarmerX, Zero To Mirror Hideout Only Ep 2 [S749] ~0:08–15:31, tier 5, retrieved 2026-11-27
- notes: tablet mod names in [[endgame/tablets]]. Prices are one moment in 0.5.5; the method (price the outcomes, then check the roll is positive expected value) is what carries over.

## Sniping underpriced items and a failed gamble
@ v=0.5.5 vol=volatile conf=single-source date=2026-09-13
Scan trade for mispriced items: he bought an amulet with +7 to fire spell skills for 85 exalts that he valued at about 4 div after one more slam. Counter-example: 100 item-level-75+ amulet bases rolled with Perfect Augmentation for +3 spell or projectile skills (odds he quoted as 1 in 163 per base) cost 45 div and roughly broke even; he judged it "too much buying" to be worth it.
- src: [S749] ~15:51–24:36, tier 5, retrieved 2026-11-27
- notes: the 1-in-163 figure is his weight read; check with tools/craftodds.py on data/mods/Amulets.json before repeating it.

## Campaign money (Spud the King, late 0.5.5)
@ v=0.5.5 vol=volatile conf=single-source date=2026-11-24
Late in the league, campaign drops can fund an endgame item before maps: a level-1 uncut skill gem from the Clearfell abandoned stash sold for 13–14 chaos (~1.4 div) almost instantly, because endgame players buy them for testing; Act 2 jewels have only item-level-1 affix tiers, so a good one is worth the same as an endgame one (he rolled two jewels valued 25–30 div and about 100 div); level-8 uncut skill and spirit gems from area-level-23 zones sold for about 3.3–4 div each, roughly 16 div per hour of farming; Expedition skill-gem stones in Act 4 (Blunder Point) and the Interludes gave gems worth about 23–47 div. In Trial of Chaos he wagered 27 div of exalts at the end of a 10-room run and doubled them. He also lists in divines instead of chaos when that pays more, and prices slow sellers between the best available and best competing ratio.
- src: Spud the King, "MOST Absurd ways to get RICH in POE 2 - Spud to Mageblood" [S750] ~4:29–22:55, tier 5, retrieved 2026-11-27
- notes: matches David's own lesson that low-level gems spike late in a league ([[strategy/league-lifecycle-pricing]]). Interludes are removed in 1.0. The wager matches [[endgame/trial-of-chaos]]. He played Tornado Druid with The Taming ring and says it gave Tornado all three elements ([S750] ~15:35–15:52), the ring route noted in [[builds/storm-shaman]].

## Today vs the video (order books read 2026-11-27)
@ v=0.5.5 vol=volatile conf=single-source date=2026-11-27
David's in-game books on 2026-11-27: Scroll of Wisdom for exalts, best seller 22 and best buyer 22.5 scrolls per exalt (2.3% spread); Orb of Augmentation, best seller 2.30 and best buyer 19 augs per exalt (~730%, both sides resting, i.e. illiquid); Regal Orb, best seller 1.11 and best buyer 2.28 regals per exalt (~105%, a stand-off with thousands on both sides). The early-league scroll margin of ~30% is gone; the wide books are wide because few trades happen, not because the profit is free.
- src: David's Currency Exchange screenshots 2026-11-27 (in-game order book, tier 1 for the live book) → data/prices/2026-11-27_exchange-books.csv
- notes: which unit "Stock" counts on the Competing side is still unconfirmed.
