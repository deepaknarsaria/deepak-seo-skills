---
name: disavow-triage
description: Score a backlink export for toxicity and write a ready-to-submit Google disavow file plus a human review sheet. Use when the user uploads a Semrush or Ahrefs backlink/anchor export and is worried about spam links, a negative-SEO attack, or an algorithmic penalty risk. Never auto-submits.
---

# Disavow Triage

Find toxic referring domains and prepare a disavow file for human review.

## When to use
- A backlink or anchor-text export is provided.
- The user mentions spam links, toxic backlinks, link networks, or negative SEO.

## How to run
1. Run: `python scripts/score_backlinks.py <backlinks.csv>`
2. Review `disavow_review.csv` line by line.
3. Only after review, upload `disavow.txt` in Google Search Console.

## Scoring heuristics
Telegram / t.me anchors, "seo/backlink/link-boost" anchor spam, known junk TLDs,
and exact-match over-optimisation. Each flagged domain shows the reason.

## Human gate (critical)
The skill writes the file. It never submits. A human reviews every domain first,
because disavowing good links is hard to undo.
