"""Regenerate FYERS_API_v3.md from the live Fyers API docs.

Since 16 Oct 2026 the Fyers API v3 docs live at https://fyers.in/api-docs/v3/
(a Nextra site, server rendered). The old React app at myapi.fyers.in/docsv3
now redirects there and its bundle no longer references an OpenAPI YAML, so
this script reads the HTML pages instead:

1. Start at the first page (Getting Started -> Overview) and follow each
   page's "next" pager link. That walk gives the order of the sidebar.
2. Pages that the pager walk skips but that are linked from a visited page
   are appended at the end, so nothing linked is lost.
3. Each page's <article> is converted to markdown, the page title becomes a
   "##" heading and the page's own headings are demoted under it.

    uv run --with markdownify regenerate_fyers_api_v3.py
    uv run --with markdownify regenerate_fyers_api_v3.py --out other.md

Only the code samples the server renders are kept (Python request and the
JSON response on most pages); the site loads the other languages client side.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import time
import urllib.request
from pathlib import Path

from markdownify import markdownify

SITE = "https://fyers.in"
START = "/api-docs/v3/getting-started/"
PREFIX = "/api-docs/v3/"
OUT = Path(__file__).with_name("FYERS_API_v3.md")
UA = {"User-Agent": "Mozilla/5.0 (docs mirror)"}


def fetch(path: str) -> str:
    req = urllib.request.Request(SITE + path, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def article(html: str) -> str:
    m = re.search(r"<article\b.*?</article>", html, flags=re.S)
    return m.group(0) if m else ""


def next_link(art: str) -> str | None:
    # The pager's "next" anchor is the one pushed right with ms-auto.
    for a in re.findall(r"<a\b[^>]*>", art):
        if "x:ms-auto" in a:
            m = re.search(r'href="([^"]+)"', a)
            if m and m.group(1).startswith(PREFIX):
                return m.group(1)
    return None


def page_links(html: str) -> list[str]:
    links = re.findall(r'href="(%s[^"#?]*/)"' % re.escape(PREFIX), html)
    return [u for u in links if "/_next/" not in u]


def to_markdown(art: str, url: str) -> tuple[str, str, str]:
    """Return (title, body, last_updated) for one page."""
    updated = ""
    m = re.search(r'<time dateTime="([^"]+)"', art)
    if m:
        updated = m.group(1)[:10]
    # Drop the pager and the "Last updated" line; they are navigation.
    art = re.sub(r'<div class="[^"]*x:mb-8 x:flex[^"]*">.*?</div>(?=</article>)', "", art, flags=re.S)
    art = re.sub(r"<(script|style|svg|button)\b[^>]*>.*?</\1>", "", art, flags=re.S)
    md = markdownify(art, heading_style="ATX")
    # Everything before the page's H1 is the breadcrumb and share buttons.
    h1 = re.search(r"^# (.+)$", md, flags=re.M)
    title = h1.group(1).strip() if h1 else url.strip("/").split("/")[-1]
    body = md[h1.end():] if h1 else md
    body = body.split("Last updated on")[0]
    body = re.sub(r"\[Open in GPT[^\n]*\n", "", body)
    # Video tutorial blocks are just YouTube links with durations; keep them short.
    body = re.sub(r"\]\((/api-docs/[^)]*)\)", lambda m: f"]({SITE}{m.group(1)})", body)
    body = re.sub(r"^(#{1,5}) ", lambda m: "#" * (len(m.group(1)) + 1) + " ", body, flags=re.M)
    body = re.sub(r"^#+\s*$", "", body, flags=re.M)  # empty headings (icons only)
    body = re.sub(r"[ \t]+$", "", body, flags=re.M)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return title, body, updated


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--delay", type=float, default=0.3, help="seconds between requests")
    a = ap.parse_args()

    pages: dict[str, tuple[str, str, str]] = {}
    order: list[str] = []
    discovered: list[str] = []

    url: str | None = START
    while url and url not in pages:
        html = fetch(url)
        art = article(html)
        pages[url] = to_markdown(art, url)
        order.append(url)
        discovered += page_links(art)
        url = next_link(art)
        time.sleep(a.delay)

    # Pages linked from content but not on the pager path.
    queue = [u for u in dict.fromkeys(discovered) if u not in pages]
    while queue:
        url = queue.pop(0)
        if url in pages:
            continue
        try:
            html = fetch(url)
        except Exception as e:  # a dead link inside the docs
            print(f"skip {url}: {e}", file=sys.stderr)
            continue
        art = article(html)
        if not art:
            continue
        pages[url] = to_markdown(art, url)
        order.append(url)
        queue += [u for u in page_links(art) if u not in pages and u not in queue]
        time.sleep(a.delay)

    today = dt.date.today().isoformat()
    lines = [
        "# FYERS API v3 Documentation",
        "",
        f"> Generated from the live FYERS API v3 docs at {SITE}{PREFIX} on {today}",
        f"> ({len(order)} pages, in the site's own page order) by `regenerate_fyers_api_v3.py`.",
        "> Re-run that script to refresh this file; do not edit it by hand. Each section",
        "> names its source page and the date Fyers last updated it. Only the code samples",
        "> the server renders are kept (mostly Python and the JSON response).",
        "",
        "## Contents",
        "",
    ]
    for u in order:
        lines.append(f"- {pages[u][0]} (`{u[len(PREFIX):] or '/'}`)")
    for u in order:
        title, body, updated = pages[u]
        lines += ["", f"## {title}", ""]
        meta = f"Source: {SITE}{u}"
        if updated:
            meta += f" (last updated {updated})"
        lines += [f"*{meta}*", "", body]
    doc = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"
    a.out.write_text(doc, encoding="utf-8", newline="\n")
    print(f"wrote {a.out}: {len(order)} pages, {len(doc.splitlines())} lines, {len(doc.encode())} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
