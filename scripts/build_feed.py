#!/usr/bin/env python3
"""Substack RSS -> data/articles.json (yalnız standart kütüphane)."""
import json, re, sys, urllib.error, urllib.request, xml.etree.ElementTree as ET, html, pathlib
FEED = "https://monetivision.substack.com/feed"
out = pathlib.Path(__file__).resolve().parent.parent / "data" / "articles.json"
req = urllib.request.Request(
    FEED,
    headers={
        "User-Agent": "Mozilla/5.0 (compatible; MonetivisionSite/1.0; +https://www.monetivision.com)",
        "Accept": "application/rss+xml, application/xml, text/xml, */*",
    },
)
try:
    raw = urllib.request.urlopen(req, timeout=30).read()
except urllib.error.HTTPError as e:
    print(f"feed fetch failed: HTTP {e.code} {e.reason}; keeping existing {out}", file=sys.stderr)
    raise SystemExit(0)
except Exception as e:
    print(f"feed fetch failed: {e}; keeping existing {out}", file=sys.stderr)
    raise SystemExit(0)
root = ET.fromstring(raw)
items = []
for it in root.iter("item"):
    g = lambda t: (it.findtext(t) or "").strip()
    enc = it.find("enclosure")
    desc = re.sub(r"<[^>]+>", "", html.unescape(g("description")))
    items.append({"title": g("title"), "link": g("link"), "date": g("pubDate"),
                  "summary": desc[:220], "image": enc.get("url") if enc is not None else ""})
out.write_text(json.dumps({"feed": FEED, "items": items[:9]}, ensure_ascii=False, indent=1))
print(f"{len(items[:9])} yazı -> {out}")
