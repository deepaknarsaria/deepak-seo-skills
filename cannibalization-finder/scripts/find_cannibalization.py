#!/usr/bin/env python3
"""Flag keyword cannibalization: one query ranking with more than one URL."""
import csv, sys, re
from collections import defaultdict

def pick(headers, *cands):
    for c in cands:
        for h in headers:
            if c.lower() in h.lower(): return h
    return None

def norm(q):
    return re.sub(r"\s+", " ", (q or "").strip().lower())

def main(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows: print("Empty file."); return
    h = rows[0].keys()
    qcol = pick(h, "keyword", "query")
    ucol = pick(h, "url", "page", "landing")
    tcol = pick(h, "traffic", "clicks")
    if not qcol or not ucol:
        sys.exit("Need a query column and a URL/page column in the export.")
    by_q = defaultdict(lambda: defaultdict(float))
    for r in rows:
        q = norm(r.get(qcol)); u = (r.get(ucol) or "").strip()
        if not q or not u: continue
        try: t = float(str(r.get(tcol, 0)).replace("%","").replace(",","") or 0)
        except ValueError: t = 0.0
        by_q[q][u] += t
    conflicts = {q: urls for q, urls in by_q.items() if len(urls) > 1}
    rows_out = []
    for q, urls in conflicts.items():
        combined = sum(urls.values())
        rows_out.append((q, len(urls), round(combined, 2), " | ".join(sorted(urls))))
    rows_out.sort(key=lambda x: -x[2])
    with open("cannibalization_report.csv", "w", newline="") as out:
        w = csv.writer(out)
        w.writerow(["query", "competing_urls", "combined_traffic", "urls"])
        w.writerows(rows_out)
    print(f"Found {len(conflicts)} queries with 2+ ranking URLs -> cannibalization_report.csv")
    for q, n, t, _ in rows_out[:5]:
        print(f"  {q!r}: {n} URLs, combined traffic {t}")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit("usage: python find_cannibalization.py <export.csv>")
    main(sys.argv[1])
