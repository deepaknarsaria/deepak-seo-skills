---
name: cannibalization-finder
description: Scan a keyword/positions export and flag queries where more than one URL from the same site ranks, i.e. keyword cannibalization that splits authority. Use when the user uploads a Semrush "Organic Positions" or Google Search Console "Pages + Queries" export and wants to find self-competing pages before consolidating them.
---

# Cannibalization Finder

Find queries where a site competes with itself, the first step before consolidating.

## When to use
- A Semrush Organic Positions or GSC Performance (query + page) export is provided.
- The user mentions cannibalization, duplicate pages, or "two pages ranking for one keyword".

## How to run
1. Run: `python scripts/find_cannibalization.py <export.csv>`
2. Review `cannibalization_report.csv`: each query with 2+ ranking URLs, sorted by combined traffic.
3. For each conflict, pick the canonical winner, 301 the rest, then plan the survivor with fan-out-brief-builder.

## What it flags
- Same query mapped to 2+ URLs (direct conflict).
- Near-duplicate query permutations pointing at different URLs (soft conflict to verify in GSC).

## Human gate
The skill detects and ranks conflicts. A human confirms the winner and approves any redirect.
