---
name: ai-citation-tracker
description: Track whether a brand is cited in AI answers for a set of priority commercial prompts, since Search Console does not expose AI Mode citations. Use when the user wants to measure GEO/AI visibility, citation share, or whether the brand shows up in ChatGPT / Perplexity / Gemini answers.
---

# AI Citation Tracker

Measure the thing Search Console cannot show you: AI answer citations.

## How to run
1. Put one prompt per line in `prompts.txt` and set your brand name.
2. With an LLM API key set, run: `python scripts/track_citations.py prompts.txt "Kanerika"`
3. Without a key, the script writes a tracking template you can fill manually or wire to an API.

## Output
`citation_log.csv`: prompt, cited (yes/no), notes, date. Append weekly to see the trend.

## Note
This is a Claude-native baseline you control. For full multi-engine coverage,
point the API hook at each engine you want to monitor.
