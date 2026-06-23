---
name: fan-out-brief-builder
description: Turn one commercial seed keyword into a query fan-out content brief that covers the cluster of related sub-questions an AI engine decomposes a query into. Use when the user wants to plan content for AI Overviews / AI Mode, asks about query fan-out, topical clusters, or wants a brief that wins citations rather than ranking one page for one phrase.
---

# Fan-Out Brief Builder

Plan content for how AI search actually retrieves: across a cluster, not a keyword.

## Why
AI Overviews and AI Mode use query fan-out: one query is decomposed into concurrent
sub-queries, results are merged, and grounded answers cite pages that satisfy the cluster.
This skill maps that cluster and structures a page to be retrieved and cited.

## How to run
1. Run: `python scripts/build_brief.py "data migration consulting"`
2. Open `brief_<seed>.md`.
3. For live People Also Ask expansion, plug a SERP API key where the script notes it.

## Output
A markdown brief: the fan-out sub-questions to answer, recommended H2/H3 structure,
definition-first answer slots, an FAQ block, and schema suggestions.
