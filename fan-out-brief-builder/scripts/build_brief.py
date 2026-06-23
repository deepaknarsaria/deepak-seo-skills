#!/usr/bin/env python3
"""Generate a query fan-out content brief from one seed keyword.

Offline by design: produces a strong brief scaffold from fan-out patterns.
To expand with live People Also Ask data, add a SERP API call where marked.
"""
import sys, re

PATTERNS = [
    "what is {s}", "how does {s} work", "{s} process step by step",
    "best {s} companies", "{s} vs in-house", "{s} pricing and cost",
    "{s} for financial services", "{s} for healthcare", "{s} for retail",
    "{s} benefits and risks", "how to choose a {s} partner", "{s} examples and case studies",
]
SCHEMA = ["Organization", "Service", "FAQPage", "BreadcrumbList"]

def build(seed):
    s = seed.strip().lower(); slug = re.sub(r"[^a-z0-9]+","-",s).strip("-")
    subs = [p.format(s=s) for p in PATTERNS]
    # --- SERP API hook: replace `subs` with live PAA + related searches here ---
    lines = [f"# Content Brief: {seed}", "",
             "## Target", f"Primary commercial intent: **{seed}**", "",
             "## Query fan-out cluster (answer all of these on one strong page)"]
    lines += [f"- {q}" for q in subs]
    lines += ["", "## Recommended structure",
              f"- H1: {seed.title()} (definition-first answer in the first 100 words)",
              "- H2: How it works  (extractable, step-by-step)",
              "- H2: When to use a partner vs in-house",
              "- H2: Industry applications (one H3 per vertical above)",
              "- H2: How to choose a partner (criteria checklist)",
              "- H2: Case studies with named outcomes and numbers (experience signal)",
              "- H2: FAQ (use the cluster questions verbatim as Q&A)", "",
              "## Extractability checklist",
              "- [ ] One-sentence definition answer near the top",
              "- [ ] Each H2 answers a distinct sub-query",
              "- [ ] FAQ block mirrors the fan-out questions",
              "- [ ] Original data or a named client result included", "",
              "## Schema to add", ", ".join(SCHEMA)]
    out = f"brief_{slug}.md"
    open(out,"w").write("\n".join(lines))
    print(f"Wrote {out} with {len(subs)} fan-out sub-questions.")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit('usage: python build_brief.py "seed keyword"')
    build(sys.argv[1])
