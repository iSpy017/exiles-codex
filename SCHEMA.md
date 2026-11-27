# KB schema (v1, 2026-11-27)

The repo is the single source of truth. Everything derived (index, coverage, app JSON) is built by scripts, never hand-written.

## Layout
```
kb/<area>/<topic>.md     one topic per file, no size cap, no -2 splits
sources.yaml             source registry; entries cite [Sxxx]
conflicts.yaml           C001…; both claims kept, never settled silently
CHANGELOG.md             pre-migration history; from 2026-11-27 on, git log
data/                    generated tables (crawl → CSV), prices/ (dated, append-only)
notes/                   non-KB files kept as-is (strategy notes, tool docs, filter, .build)
tools/                   kbschema.py, lint.py, build scripts
legacy/                  frozen Project docs (tag pre-migration), read-only
```

## Topic file
```
---
title: Ignite & Flammability
status: done | partial | todo | needs-1.0-check | retired
defaults: v=0.5.5.9 vol=may-change conf=single-source      # doc-level, inherited by entries
tracker_topic: "Ignite"                                    # coverage tracker row
merged_from: [rune-effects.md, rune-effects-2.md]          # only if merged
---
<doc intro prose>

## <Entry heading>                                         # entry ID = <file>#<slug(heading)>
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17 [fill=v,vol] [missing=src]
<claim, own words>
- src: game keywords "Ignite", tier 2; Mobalytics Ignite [S072], tier 3; poe2db:Ignite, tier 2
- conf: <free text when it says more than the enum>
- v: <raw version text when it says more than the enum>
- notes: <interactions, [[links]]>
```

## Meta line `@`
| key | values | rule |
|---|---|---|
| v | 1.0 · 0.5.5.9 · 0.5.5 · 0.5.x · 0.5.0 · 0.5 | version the claim was true for |
| vol | stable · may-change · volatile · retired | volatile needs `date` |
| conf | confirmed · single-source · inferred · conflict | inferred needs a reason in text |
| date | YYYY-MM-DD | newest retrieval/crawl date of the sources |
| fill | v,vol,conf,src | value inherited from the doc header, not stated by the entry |
| missing | v,vol,conf,src | nothing derivable: on the fix queue. Never guessed. |

## Sources
- `[S123]` → sources.yaml (title, url, tier, last_checked, use, reachable). Link text stays in the entry.
- `poe2db:<Page>` → https://poe2db.tw/us/<Page>, crawl date = `poe2db_crawl` in sources.yaml.

## Lint (tools/lint.py) — errors fail the build
frontmatter title/status · volatile without date · price without date · unknown [Sxxx] · broken [[link]] · `[INFERRED]:` with empty reason · invalid YAML · duplicate conflict ids.
Warnings = fix queue: unknown v/vol/conf, no source, `[INFERRED]` at line end.

## Hard rules kept
Sources on every fact · version tags · dated prices · conflicts logged, not settled · [INFERRED] + reason · paraphrase, don't copy.

## Generated data and tools
| file | built by | use |
|---|---|---|
| data/uniques.csv, data/unique_mods.csv | tools/gen_uniques.py <corpus> <date> | every unique + its mods (Family/Stats from game data) |
| data/poe2db/<Page>.tsv, _refs.csv | tools/gen_poe2db_refs.py <corpus> <date> | table rows of each PoE2DB page the KB cites; lint checks every poe2db: ref |
| data/unique_sources.csv (+ pob_source/pob_league in uniques.csv) | tools/gen_pob_uniques.py <pob_repo> <ref> | Path of Building's unique sources and leagues |
| data/passive_tree_<ver>.csv | tools/gen_pob_tree.py <pob_repo> <ver> <ref> | every passive node: kind, ascendancy, stats |
| site/kb.json, index.jsonl, coverage.json, coverage.html | tools/build_index.py (CI) | app, Claude retrieval, coverage page |
| refresh-worklist.md | tools/crawl_diff.py <old> <new> | 1.0 refresh: entries citing changed pages |
| — | tools/kbsearch.py "q" | BM25 section search (negations kept) |
| — | tools/craftodds.py <class> --target <family> | exalt odds from PoE2DB spawn weights (data/mods) |
| — | tools/copycheck.py <corpus> | paraphrase check: 9-word runs shared with the crawl (stat/name lists are expected hits) |

Docs whose tables duplicate generated data carry `data: [...]` in frontmatter: query those files instead of reading the tables.
