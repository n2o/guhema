"""Compare a page of the old Django site with the Astro build (until cutover; delete with Django).

Usage:
  uv run python manage.py runserver 8765 &      # old site, prod DB copy in db.sqlite3
  npx astro build                               # new site in dist/ (or: ASTRO_URL=http://localhost:4321 with `npx astro dev`)
  python3 tools/compare.py /produkte/lochsagen/ [/other/path/ ...] [--lang de|en|ru|all] [--old-only] [--structure]

Compares the content of <div id="main"> as a token stream: text, table cell/row boundaries,
img alt texts and link targets (language prefix and image file names normalized). Exit 1 on differences.
"""
import difflib
import os
import re
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

DJANGO = "http://127.0.0.1:8765"
DIST = Path(__file__).resolve().parent.parent / "dist"
ASTRO_URL = os.environ.get("ASTRO_URL")
IMG = re.compile(r"\.(png|jpe?g|gif|webp)(\?.*)?$", re.I)


class Tokens(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0  # >0 while inside #main
        self.out = []
        self.skip = 0  # inside <script>/<style>

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.depth:
            if tag not in VOID:
                self.depth += 1
        elif tag == "div" and a.get("id") == "main":
            self.depth = 1
            return
        if not self.depth:
            return
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("tr", "td", "th", "table", "h1", "h2", "h3", "h4", "li", "p"):
            self.out.append(f"<{tag}>")
        if tag == "img":
            self.out.append(f"[img alt={a.get('alt', '')!r}]")
        if tag == "a" and a.get("href"):
            href = re.sub(r"^/(en|ru)(?=/)", "", a["href"])
            if IMG.search(href):
                href = "IMAGE"
            href = re.sub(r"/empfehlungen$", "/empfehlungen/", href)  # Django had no trailing slash here
            self.out.append(f"[a {href}]")

    def handle_endtag(self, tag):
        if not self.depth or tag in VOID:
            return
        if tag in ("script", "style"):
            self.skip -= 1
        self.depth -= 1

    def handle_data(self, data):
        if self.depth and not self.skip:
            text = " ".join(data.split())
            if text:
                self.out.append(text)


VOID = {"img", "br", "hr", "input", "meta", "link", "source", "wbr"}


def structure(toks):
    return [re.sub(r"alt=.*", "alt]", t) for t in toks if t.startswith(("<", "[img", "[a "))]


def tokens(html):
    p = Tokens()
    p.feed(html)
    return p.out


def fetch(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req) as r:
            return r.read().decode()
    except urllib.error.HTTPError as e:
        return f"<div id='main'>HTTP {e.code}</div>"


def old(path, lang):
    path = re.sub(r"/empfehlungen/$", "/empfehlungen", path)
    return fetch(DJANGO + path, {"Cookie": f"django_language={lang}"})


def new(path, lang):
    if ASTRO_URL:
        return fetch(ASTRO_URL + ("" if lang == "de" else f"/{lang}") + path)
    f = DIST / (path.strip("/") if lang == "de" else f"{lang}/{path.strip('/')}") / "index.html"
    return f.read_text() if f.exists() else "<div id='main'>MISSING in dist</div>"


def main():
    args = sys.argv[1:]
    lang = args[args.index("--lang") + 1] if "--lang" in args else "all"
    paths = [a for a in args if a.startswith("/")]
    langs = ["de", "en", "ru"] if lang == "all" else [lang]
    failed = False
    for path in paths:
        for lg in langs:
            a, b = tokens(old(path, lg)), tokens(new(path, lg))
            if "--structure" in args:  # markup only: for re-translated texts
                a, b = structure(a), structure(b)
            if "--old-only" in args:
                print("\n".join(a))
                continue
            diff = list(difflib.unified_diff(a, b, f"django {lg} {path}", f"astro {lg} {path}", n=2, lineterm=""))
            print(f"{'DIFF' if diff else 'OK  '} {lg} {path}")
            if diff:
                failed = True
                print("\n".join(diff[:80]) + ("\n..." if len(diff) > 80 else ""))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
