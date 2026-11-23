# Flasks

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Slots and types
- Claim: Two flask slots by default: one life flask, one mana flask (more only if something says so). Flasks recover over their duration by default, not instantly.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Flask](https://poe2wiki.net/wiki/Flask), tier 2; [Mobalytics Flasks](https://mobalytics.gg/poe-2/guides/flasks), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: game keywords also define "Utility Flasks" (timed buffs) — [INFERRED] legacy/unused in 0.5.x since both tier-2/3 sources say only life + mana slots; verify in base_items.json.

## Recovery wasted at full
- Claim: By default a flask's effect ends when you reach full unreserved life/mana — leftover recovery is lost. Some uniques override this.
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Flasks](https://mobalytics.gg/poe-2/guides/flasks), tier 3; [poe2wiki Life flask](https://www.poe2wiki.net/wiki/Life_flask) (unique with "Effect is not removed when Unreserved Life is Filled"), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Charges
- Claim: Flasks use charges; kills refill them: Normal = ½ monster Power, Magic = Power, Rare/Unique = 2× Power. Checkpoints and wells fully refill. Flasks only hold charges while equipped (unequipping empties them).
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Flasks", tier 2; [poe2wiki Flask](https://poe2wiki.net/wiki/Flask), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Example bases (life)
- Greater 150 life / 4 s · Grand 260 / 5 s · Giant 340 / 4 s · Colossal 450 / 4 s; each 10 charges per use, 70–75 max.
- Version: 0.5.x
- Source: [poe2wiki List of life flasks](https://www.poe2wiki.net/wiki/List_of_life_flasks), tier 2; [Mobalytics Flasks](https://mobalytics.gg/poe-2/guides/flasks) (Colossal 10/75), tier 3; retrieved 2026-11-17
- Confidence: confirmed (Colossal); single-source others
- Notes: full base list → [[items/bases-implicits]] from base_items.json.

## Charge generation / instant recovery on belts and uniques
- Examples: belts with "Flasks gain X charges per second" (e.g. Fine Belt implicit 0.17/s), "Life Flasks used while on Low Life apply Recovery Instantly", "Life Recovery from Flasks also applies to Energy Shield", Overflowing Chalice buff (+2 charges/s, 30% increased recovery).
- Version: 0.5.x
- Source: [poe2wiki Fine Belt](https://www.poe2wiki.net/wiki/Fine_Belt), [poe2wiki List of unique belts](https://www.poe2wiki.net/wiki/List_of_unique_belts), tier 2; game keywords "Overflowing Chalice"; retrieved 2026-11-17
- Confidence: single-source each
- Notes: Vaal Pact blocks life flask use (Mobalytics). Monster mod "Siphons Flask Charges" removes 3 flask + charm charges every 3 s within 3.6 m (game keywords).
