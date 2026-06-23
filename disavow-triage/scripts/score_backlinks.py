#!/usr/bin/env python3
"""Score referring domains for toxicity and emit a disavow.txt for review."""
import csv, sys, re
from urllib.parse import urlparse

SPAM_ANCHOR = re.compile(r"(t\.me|telegram|seo backlinks?|bulk link|link posting|black.?links?|traffic boost|link indexing|@\w+)", re.I)
JUNK_TLD = re.compile(r"\.(biz|xyz|top|click|loan|work|ru|cn)$", re.I)
JUNK_HINT = re.compile(r"(seocheck|bestcss|directory|backlink|linkbuild|catalog)", re.I)

def pick(headers, *cands):
    for c in cands:
        for hh in headers:
            if c.lower() in hh.lower(): return hh
    return None

def domain(u):
    if not u: return ""
    if "://" not in u: u = "http://" + u
    return (urlparse(u).netloc or "").lower().replace("www.","")

def main(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows: print("Empty file."); return
    h = rows[0].keys()
    dcol = pick(h,"referring domain","source url","source","domain","url")
    acol = pick(h,"anchor")
    flagged = {}
    for r in rows:
        dom = domain(r.get(dcol,"")); anchor = (r.get(acol,"") or "")
        if not dom: continue
        reasons = []
        if SPAM_ANCHOR.search(anchor): reasons.append("spam anchor")
        if JUNK_TLD.search(dom): reasons.append("junk TLD")
        if JUNK_HINT.search(dom): reasons.append("link-network domain")
        if reasons:
            flagged.setdefault(dom, set()).update(reasons)
    with open("disavow.txt","w") as d, open("disavow_review.csv","w",newline="") as rv:
        w = csv.writer(rv); w.writerow(["domain","reasons"])
        d.write("# Disavow file - REVIEW BEFORE SUBMITTING IN SEARCH CONSOLE\n")
        for dom, reasons in sorted(flagged.items()):
            d.write(f"domain:{dom}\n"); w.writerow([dom, ", ".join(sorted(reasons))])
    print(f"Flagged {len(flagged)} toxic domains -> disavow.txt + disavow_review.csv")
    print("Review every line before uploading to Google Search Console.")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit("usage: python score_backlinks.py <backlinks.csv>")
    main(sys.argv[1])
