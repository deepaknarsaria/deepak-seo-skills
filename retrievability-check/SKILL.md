---
name: retrievability-check
description: Fetch a list of priority URLs as Googlebot, GPTBot and PerplexityBot and flag any that return a bot-challenge or non-200, so pages stay retrievable (and groundable in AI answers). Use when the user suspects a WAF or CDN is blocking crawlers, sees "Bot Verification" or "Just a moment" titles, or wants to confirm key pages are crawlable.
---

# Retrievability Check

Confirm priority URLs are reachable by search and AI crawlers.

## When to use
- Pages show "Bot Verification" / "Just a moment" in the index.
- After changing CDN/WAF rules, to verify crawlers are allowlisted.

## How to run
1. Put one URL per line in `urls.txt`.
2. Run: `python scripts/check_crawlers.py urls.txt`
3. Read the table; anything marked CHALLENGE or non-200 needs a WAF fix.

## Note
Run this from a normal network (not a sandbox). It only reads pages, it changes nothing.
Pair the findings with Search Console URL Inspection (live test) to confirm Googlebot's view.
