#!/usr/bin/env python3
"""Log whether a brand is cited in AI answers for priority prompts.

If ANTHROPIC_API_KEY is set and the SDK is installed, it queries the model.
Otherwise it writes a manual tracking template.
"""
import sys, csv, os, datetime

def main(path, brand):
    prompts = [l.strip() for l in open(path) if l.strip()]
    today = datetime.date.today().isoformat()
    rows = []; key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        try:
            import anthropic
            client = anthropic.Anthropic()
            for p in prompts:
                msg = client.messages.create(model="claude-sonnet-4-6", max_tokens=600,
                      messages=[{"role":"user","content":p}])
                text = "".join(b.text for b in msg.content if getattr(b,"type",None)=="text")
                cited = "yes" if brand.lower() in text.lower() else "no"
                rows.append([p, cited, text[:120].replace("\n"," "), today])
        except Exception as e:
            print("API path failed, writing template instead:", e); key = None
    if not key:
        rows = [[p, "", "fill manually or wire an API key", today] for p in prompts]
    with open("citation_log.csv","w",newline="") as f:
        w = csv.writer(f); w.writerow(["prompt","cited","notes","date"]); w.writerows(rows)
    print(f"Wrote citation_log.csv for {len(prompts)} prompts (brand: {brand}).")

if __name__ == "__main__":
    if len(sys.argv) < 3: sys.exit('usage: python track_citations.py prompts.txt "Brand"')
    main(sys.argv[1], sys.argv[2])
