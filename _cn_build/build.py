#!/usr/bin/env python3
"""Build the China-mainland edition of the site (yanuclimb.cn) into _site_cn/.

Why this exists instead of Jekyll (CNS window, 2026-09-18): the CN edition needs a rewrite
layer on top of whatever renders the markdown — GitHub-Pages baseurl removal, dropping the
/cn/ prefix, no Google Fonts (unreachable in mainland), 备案号 footer, reset.html API base —
and the Liquid used by the CN pages is three tags plus `relative_url`. One script handles all
of it; the global site stays on GitHub Pages' own Jekyll build, untouched.

Inputs (repo root):
  _layouts/cn.html      page shell ({{ page.title }} / {{ page.description | default: site.description }} / {{ content }})
  cn/*.md               front matter: title / permalink / (description); body = markdown
  cn/index.html         landing page, raw HTML
  reset.html            password-reset page (global copy; API base gets replaced)
  assets/               copied verbatim (minus .DS_Store); CSS gets the same path rewrite
  _cn_build/site.json   company / icp / psb{text,code,icon} / api_base / description / year

Rewrite rules, applied in this order to every HTML/CSS output:
  1. {{ '/cn/x/' | relative_url }}                     -> /x/
  2. <li><a href="/climmate-legal/" …>Global…</a></li> -> removed (a "Global" link that would
                                                          point at the CN home is misleading;
                                                          GitHub Pages is unreachable in mainland)
  3. href/src/url() values starting with /climmate-legal/cn/ -> /
  4. href/src/url() values starting with /climmate-legal/     -> /   (anchored: an absolute
                                                          https://yh382.github.io/climmate-legal/… link is left alone)
  4b. root-relative page links without a trailing slash (href="/about") -> href="/about/"
     (saves the file_server 308 per click)
  5. Google Fonts <link> tags                          -> removed (system font stack in --font-sans)
  6. <!-- cn:copyright -->…<!-- /cn:copyright -->      -> © {year} {company}. 版权所有
     <!-- cn:icp -->…<!-- /cn:icp -->                  -> ICP link (+ 公安 link when psb.text set)
  7. reset.html: var API_BASE = "…"                     -> site.json api_base;
     href="climmate://" (RN global app scheme)           -> site.json app_scheme (CN app = yanu://)
Any leftover `{{` / `{%` / root-relative `/climmate-legal/` / `fonts.googleapis` in the output fails the build.
Markdown: python-markdown with tables + fenced_code + toc (heading ids), so the CN build renders the
same constructs GitHub Pages' kramdown does for the current pages.
"""
from __future__ import annotations

import html
import json
import re
import shutil
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site_cn"
SITE = json.loads((ROOT / "_cn_build" / "site.json").read_text(encoding="utf-8"))

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
RELATIVE_URL = re.compile(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}")
GLOBAL_LINK_LI = re.compile(r'\s*<li><a href="/climmate-legal/"[^>]*>[^<]*</a></li>')
GOOGLE_FONTS = re.compile(r'\s*<link[^>]*(fonts\.googleapis\.com|fonts\.gstatic\.com)[^>]*>')
# root-relative GitHub-Pages paths only: href="/climmate-legal/…", src="/climmate-legal/…", url('/climmate-legal/…')
BASEURL = re.compile(r'((?:href|src)="|url\(\'?)/climmate-legal/(?:cn/)?')
# href="/about" (no trailing slash, no dot/hash/query) -> href="/about/"
PAGE_LINK = re.compile(r'href="/([a-z0-9-]+)"')
MARKER = lambda name: re.compile(rf"<!-- cn:{name} -->.*?<!-- /cn:{name} -->", re.S)


def fail(msg: str) -> None:
    print(f"✗ {msg}", file=sys.stderr)
    sys.exit(1)


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    m = FRONT_MATTER.match(text)
    if not m:
        fail("missing front matter")
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, text[m.end():]


def footer_icp_html() -> str:
    icp = SITE.get("icp", "").strip()
    if not icp:
        return '<span>ICP备案号将在备案完成后展示</span>\n          <a href="https://beian.miit.gov.cn/" rel="noopener">工信部备案系统</a>'
    parts = [f'<a href="https://beian.miit.gov.cn/" rel="noopener" target="_blank">{html.escape(icp)}</a>']
    psb = SITE.get("psb") or {}
    if psb.get("text"):
        icon = f'<img src="{html.escape(psb["icon"])}" alt="" style="width:16px;height:16px;vertical-align:-3px;margin-right:4px;">' if psb.get("icon") else ""
        href = f'https://beian.mps.gov.cn/#/query/webSearch?code={html.escape(psb["code"])}' if psb.get("code") else "https://beian.mps.gov.cn/"
        parts.append(f'<a href="{href}" rel="noopener" target="_blank">{icon}{html.escape(psb["text"])}</a>')
    return "\n          ".join(parts)


def footer_copyright_html() -> str:
    company = SITE.get("company", "").strip()
    year = SITE.get("year", "2026")
    if not company:
        return f"<p>&copy; {year} YANU 岩有. All rights reserved.</p>"
    return f"<p>&copy; {year} {html.escape(company)} 版权所有</p>"


def rewrite(text: str, *, is_page: bool) -> str:
    text = RELATIVE_URL.sub(lambda m: re.sub(r"^/cn(?=/)", "", m.group(1)), text)
    text = GLOBAL_LINK_LI.sub("", text)
    text = BASEURL.sub(lambda m: m.group(1) + "/", text)
    text = PAGE_LINK.sub(r'href="/\1/"', text)
    text = GOOGLE_FONTS.sub("", text)
    if is_page:
        for name, repl in (("copyright", footer_copyright_html()), ("icp", footer_icp_html())):
            pat = MARKER(name)
            if not pat.search(text):
                fail(f"page is missing <!-- cn:{name} --> markers")
            text = pat.sub(lambda _m, r=repl: r, text)
    return text


def check(text: str, where: str) -> None:
    for bad in ("{{", "{%", '="/climmate-legal/', "url('/climmate-legal/", "fonts.googleapis", "fonts.gstatic"):
        if bad in text:
            fail(f"{where}: leftover {bad!r}")


def write(rel: str, text: str) -> None:
    check(text, rel)
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    print(f"  {rel}")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    layout = (ROOT / "_layouts" / "cn.html").read_text(encoding="utf-8")

    # markdown pages
    for md in sorted((ROOT / "cn").glob("*.md")):
        meta, body = parse_front_matter(md.read_text(encoding="utf-8"))
        permalink = meta.get("permalink")
        if not permalink or not permalink.startswith("/cn/"):
            fail(f"{md.name}: permalink must start with /cn/ (got {permalink!r})")
        rel = permalink[len("/cn/"):].strip("/")
        content = markdown.markdown(body, extensions=["tables", "fenced_code", "toc"])
        page = (layout
                .replace("{{ page.title }}", html.escape(meta.get("title", "")))
                .replace("{{ page.description | default: site.description }}",
                         html.escape(meta.get("description") or SITE.get("description", "")))
                .replace("{{ content }}", content))
        write(f"{rel}/index.html" if rel else "index.html", rewrite(page, is_page=True))

    # landing + reset
    write("index.html", rewrite((ROOT / "cn" / "index.html").read_text(encoding="utf-8"), is_page=True))
    reset = (ROOT / "reset.html").read_text(encoding="utf-8")
    reset, n = re.subn(r'var API_BASE = "[^"]+";', f'var API_BASE = "{SITE["api_base"]}";', reset)
    if n != 1:
        fail("reset.html: expected exactly one `var API_BASE = …` line")
    reset, n = re.subn(r'href="climmate://"', f'href="{SITE["app_scheme"]}://"', reset)
    if n < 1:
        fail("reset.html: expected the Open-app links (href=\"climmate://\")")
    write("reset.html", rewrite(reset, is_page=False))

    # assets
    for src in sorted((ROOT / "assets").iterdir()):
        if src.name.startswith("."):
            continue
        if src.suffix == ".css":
            write(f"assets/{src.name}", rewrite(src.read_text(encoding="utf-8"), is_page=False))
        else:
            (OUT / "assets").mkdir(exist_ok=True)
            shutil.copy2(src, OUT / "assets" / src.name)
            print(f"  assets/{src.name}")
    print(f"✓ built {OUT.relative_to(ROOT)}/  (icp={'set' if SITE.get('icp') else 'PLACEHOLDER'}, company={'set' if SITE.get('company') else 'PLACEHOLDER'})")


if __name__ == "__main__":
    main()
