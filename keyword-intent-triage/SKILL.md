---
name: keyword-intent-triage
description: Classify a keyword or URL export by search intent and funnel stage, and flag high-traffic pages that carry no commercial value. Use when the user uploads a Semrush or Google Search Console keyword/positions export and wants to know which traffic actually feeds pipeline and which pages to prune or repurpose.
---

# Keyword Intent Triage

Turn a raw keyword export into a prioritised action sheet.

## When to use
- A Semrush "Organic Positions" or GSC "Queries" CSV is provided.
- The user asks "which traffic is commercial", "what should we prune", or "why does traffic not convert".

## How to run
1. Confirm the CSV has columns for the keyword, position, volume and traffic (the script auto-detects common Semrush/GSC headers).
2. Run: `python scripts/triage.py <export.csv>`
3. Review `intent_triage_report.csv` and the printed summary.

## Output
- Intent split (informational / commercial / transactional / navigational) by keyword count and traffic share.
- A flagged list of high-traffic, low-commercial keywords that are candidates to prune, redirect, or interlink upward into commercial pages.

## Human gate
The skill recommends. The user decides what gets cut or kept.
