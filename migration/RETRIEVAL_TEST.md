# Retrieval test — old Project docs vs repo KB

Same BM25 ranking both sides; OLD reads whole docs, NEW reads one section. Hit = unit from a gold doc containing the answer string.
OLD models project_search → project_read (approximation: the real Project search is a RAG snippet index, not BM25).

## dev (10 questions)
| store | recall@1 | recall@3 | recall@5 | precision@5 | F1@5 | MRR | median tokens read to answer | mean tokens |
|---|---|---|---|---|---|---|---|---|
| OLD docs | 0.70 | 0.90 | 1.00 | 0.24 | 0.39 | 0.82 | 1,244 | 1,881 |
| NEW sections | 0.60 | 1.00 | 1.00 | 0.36 | 0.53 | 0.78 | 365 | 347 |

## test (20 questions)
| store | recall@1 | recall@3 | recall@5 | precision@5 | F1@5 | MRR | median tokens read to answer | mean tokens |
|---|---|---|---|---|---|---|---|---|
| OLD docs | 0.80 | 0.90 | 0.95 | 0.25 | 0.40 | 0.86 | 2,650 | 3,237 |
| NEW sections | 0.80 | 0.90 | 0.90 | 0.44 | 0.59 | 0.84 | 261 | 766 |

## Per test question (rank of first hit, tokens read: OLD → NEW)
- evasion chance cap: 1 / 987 → 1 / 159
- maximum block chance: miss / 11,872 → miss / 8,148
- how does the currency exchange order book work: 1 / 1,749 → 1 / 224
- what does a gemcutter prism do: 1 / 1,540 → 3 / 796
- armour damage reduction formula: 1 / 1,156 → 1 / 237
- Xesht breachstone boss: 1 / 3,181 → 1 / 145
- ritual reroll and defer rewards: 1 / 3,643 → 1 / 205
- perfect essence removes a mod and adds one: 1 / 3,317 → 1 / 251
- omens that change exalted orb outcome: 5 / 8,330 → 2 / 499
- desecration well of souls choose one of three mods: 1 / 2,939 → 1 / 249
- expedition logbooks: 1 / 3,887 → 1 / 272
- storm shaman tornado flame wall: 1 / 2,842 → 1 / 505
- the 5 div T15 test before investing: 1 / 2,092 → 1 / 100
- unique monster life multiplier boss: 1 / 2,563 → 1 / 332
- freeze buildup threshold on monsters: 1 / 2,737 → 1 / 352
- life leech cap and recoup duration: 1 / 1,889 → 1 / 87
- how many charm slots: 2 / 3,624 → 1 / 200
- how many zones and bosses in act 5 and 6: 2 / 2,032 → miss / 1,728
- thunderstorm drench enemy level cap: 1 / 2,131 → 1 / 488
- when does crit chance leave the passive tree in 1.0: 1 / 2,231 → 1 / 344

## Notes
- Dev tuning (allowed on dev only): question words (how/what/does/…) added to the stopword list; negations stay. One dev label corrected after the run: gold doc says "can't be traded", label had "untradeable". Test labels untouched.
- Result on test: same recall@1/@3, precision@5 0.25 → 0.44, median tokens to answer ~2,650 → ~260 (≈10×). Recall@5 0.95 → 0.90: one question whose answer sits in a different section than the best-matching one.
- Rule that follows: search sections first; if no section answers, read the top doc whole (old cost, only on misses).
