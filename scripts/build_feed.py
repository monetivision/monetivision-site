#!/usr/bin/env python3
"""Substack RSS -> data/articles.json (yalnız standart kütüphane)."""
import json, re, urllib.request, xml.etree.ElementTree as ET, html, pathlib
FEED = "https://monetivision.substack.com/feed"
out = pathlib.Path(__file__).resolve().parent.parent / "data" / "articles.json"
req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0 monetivision-site"})
root = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())
items = []
for it in root.iter("item"):
    g = lambda t: (it.findtext(t) or "").strip()
    enc = it.find("enclosure")
    desc = re.sub(r"<[^>]+>", "", html.unescape(g("description")))
    items.append({"title": g("title"), "link": g("link"), "date": g("pubDate"),
                  "summary": desc[:220], "image": enc.get("url") if enc is not None else ""})
out.write_text(json.dumps({"feed": FEED, "items": items[:9]}, ensure_ascii=False, indent=1))
print(f"{len(items[:9])} yazı -> {out}")
