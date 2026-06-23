# Deepak SEO Skills

A small, human-in-the-loop library of Agent Skills for running SEO and GEO
operations (built and demonstrated on kanerika.com). Each skill automates the repeatable work and leaves
every irreversible decision (disavow submission above all) to a human.

Built on the open Agent Skills standard: https://github.com/agentskills/agentskills

## Skills
| Skill | What it does | Human gate |
|-------|--------------|-----------|
| keyword-intent-triage | Classifies keywords/URLs by intent and funnel stage; flags high-traffic, zero-commercial pages | You approve what gets pruned |
| disavow-triage | Scores referring domains for toxicity; writes a ready-to-submit disavow.txt | You review before uploading to GSC |
| retrievability-check | Fetches priority URLs as Googlebot/GPTBot/PerplexityBot; flags bot-challenge pages | Reports only, no changes |
| fan-out-brief-builder | Turns one commercial keyword into a query fan-out content brief | You edit before writing |
| ai-citation-tracker | Logs whether the brand is cited across AI answers for priority prompts | Reporting only |

## Install (Claude Code / any Agent Skills runtime)
Clone into your skills directory, or:
```
npx openskills install deepaknarsaria/deepak-seo-skills
```
Each skill is a folder with a SKILL.md plus scripts. See each folder for usage.

Author: Deepak Narsaria · deepaknarsaria.com
