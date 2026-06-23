#!/usr/bin/env python3
"""Classify a keyword export by intent and flag commercially empty traffic."""
import csv, sys, re

INFO = re.compile(r"\b(what|how|why|guide|examples?|vs|tutorial|meaning|definition|trends?|developments?)\b", re.I)
COMM = re.compile(r"\b(best|top|companies|company|services?|consulting|consultants?|providers?|solutions?|software|platforms?|tools?)\b", re.I)
TRAN = re.compile(r"\b(buy|pricing|price|cost|quote|demo|trial|contact|hire|near me)\b", re.I)

def classify(kw):
    if TRAN.search(kw): return "transactional"
    if COMM.search(kw): return "commercial"
    if INFO.search(kw): return "informational"
    return "navigational"

def pick(headers, *cands):
    for c in cands:
        for h in headers:
            if c.lower() in h.lower(): return h
    return None

def main(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("Empty file."); return
    h = rows[0].keys()
    kcol = pick(h, "keyword", "query"); tcol = pick(h, "traffic", "clicks"); pcol = pick(h, "position", "pos")
    buckets = {k: {"kw": 0, "traffic": 0.0} for k in ["informational","commercial","transactional","navigational"]}
    flagged = []
    for r in rows:
        kw = (r.get(kcol) or "").strip()
        if not kw: continue
        try: traffic = float(str(r.get(tcol, 0)).replace("%","").replace(",","") or 0)
        except ValueError: traffic = 0.0
        intent = classify(kw)
        buckets[intent]["kw"] += 1; buckets[intent]["traffic"] += traffic
        if intent == "informational" and traffic >= 1.0:
            flagged.append((kw, r.get(pcol,""), traffic))
    total_t = sum(b["traffic"] for b in buckets.values()) or 1
    print("\nINTENT SPLIT (by traffic share)")
    for k,v in buckets.items():
        print(f"  {k:15} {v['kw']:5} kw   {v['traffic']/total_t*100:5.1f}% traffic")
    flagged.sort(key=lambda x: -x[2])
    with open("intent_triage_report.csv","w",newline="") as out:
        w = csv.writer(out); w.writerow(["keyword","position","traffic_share","recommendation"])
        for kw,pos,tr in flagged:
            w.writerow([kw,pos,tr,"informational high-traffic: prune / repurpose / interlink to commercial page"])
    print(f"\nFlagged {len(flagged)} high-traffic informational keywords -> intent_triage_report.csv")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit("usage: python triage.py <export.csv>")
    main(sys.argv[1])
