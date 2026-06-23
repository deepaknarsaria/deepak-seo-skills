#!/usr/bin/env python3
"""Fetch URLs as different crawlers and flag bot-challenge / non-200 responses."""
import sys, re
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

AGENTS = {
    "Googlebot": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "GPTBot": "Mozilla/5.0 (compatible; GPTBot/1.0; +https://openai.com/gptbot)",
    "PerplexityBot": "Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/bot)",
}
CHALLENGE = re.compile(r"(bot verification|just a moment|cf-browser-verification|checking your browser|attention required)", re.I)

def check(url, ua):
    try:
        req = Request(url, headers={"User-Agent": ua})
        with urlopen(req, timeout=20) as resp:
            body = resp.read(4000).decode("utf-8","ignore")
            status = resp.status
            m = re.search(r"<title[^>]*>(.*?)</title>", body, re.I|re.S)
            title = (m.group(1).strip()[:60] if m else "")
            flag = "CHALLENGE" if CHALLENGE.search(body) or CHALLENGE.search(title) else "ok"
            return f"{status} {flag:9} {title}"
    except HTTPError as e: return f"{e.code} HTTP-ERROR"
    except URLError as e:  return f"ERR  {e.reason}"

def main(path):
    urls = [l.strip() for l in open(path) if l.strip() and not l.startswith("#")]
    for url in urls:
        print(f"\n{url}")
        for name, ua in AGENTS.items():
            print(f"  {name:14} {check(url, ua)}")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit("usage: python check_crawlers.py urls.txt")
    main(sys.argv[1])
