# KB profile — legacy freeze 2026-11-26

Docs 199 (8 control) · chars 1,163,940 · tokens 417,914 (claude.ai count) · entries 908 · table rows 2,142

## Doc size (IQR, §2.3)
median 5,370 chars · Q1 3,358 · Q3 7,377 · outlier > 13,406 → 6 docs: kb/03-changelog.md, kb/04-conflicts.md, kb/00-index.md, kb/01-coverage-tracker.md, kb/gems/lineage-drop-sources.md, Witchhunter - Level 96 - Unnamed - poe.ninja.build

split part-docs (-N.md): 47 · table-copy docs (≥50% table chars): 39 holding 23% of all chars

By folder (docs / chars / entries / table rows):
| folder | docs | chars | entries | table rows |
|---|---|---|---|---|
| kb/items | 49 | 319,555 | 182 | 904 |
| kb/mechanics | 33 | 143,810 | 235 | 48 |
| kb/gems | 22 | 125,197 | 105 | 511 |
| kb/endgame | 15 | 121,205 | 141 | 143 |
| kb | 8 | 117,290 | 0 | 192 |
| kb/builds | 10 | 69,462 | 40 | 114 |
| kb/crafting | 11 | 59,164 | 58 | 147 |
| kb/campaign | 13 | 45,952 | 41 | 49 |
| kb/strategy | 11 | 44,493 | 47 | 0 |
| kb/classes | 7 | 30,184 | 33 | 14 |
| . | 3 | 29,643 | 0 | 0 |
| kb/economy | 7 | 23,239 | 26 | 0 |
| claude/data | 3 | 15,001 | 0 | 0 |
| claude | 4 | 14,009 | 0 | 20 |
| kb/tools | 3 | 5,736 | 0 | 0 |

Non-control docs with 0 structured entries: 17

## Entry completeness (§2.2 missing values)
- claim: missing 157 (17%)
- version: missing 19 (2%)
- volatility: missing 153 (17%)
- source: missing 115 (13%)
- confidence: missing 128 (14%)
- notes: missing 342 (38%)
- source without URL/PoE2DB ref: 137 · without tier: 133 · without date: 189
- price numbers with no date in entry: 5

## Label consistency (§2.2 inconsistent data)
- version (normalised): 0.5.x 583, 0.5.5.9 166, OTHER 39, 1.0 37, 0.5.5 23, <0.5 19, MISSING 19, 0.5 13, 0.5.0 9
- distinct raw version strings: 124
- volatility: may-change 634, MISSING 153, stable 53, volatile 49, may-change. 14, retired 3, volatile. 2
- confidence (first word): single-source 465, confirmed 265, MISSING 128, inferred 31, single-source. 13, conflict 4, n/a 1, partly 1
- source tier: 2 655, none 133, 3 52, 5 28, 1 25, 4 15

## Integrity
- broken_link 6, inferred_no_reason 1
- exact duplicate table rows across docs: 9
- near-duplicate claims across docs (TF-IDF cosine ≥0.75): 0