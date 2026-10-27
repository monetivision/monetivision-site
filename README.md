# monetivision.com
Statik site (HTML/CSS/JS, derleme gerektirmez). Marka: /workspace/monetivision/brand/BRAND_KIT.md (tokens.css + Anton/Oswald/Inter).
- Yazılar: `python3 scripts/build_feed.py` → `data/articles.json` (kaynak https://monetivision.substack.com/feed)
- GitHub Actions (`.github/workflows/update-feed.yml`) 6 saatte bir akışı yeniler.
- Önizleme: `python3 -m http.server` → http://localhost:8000
