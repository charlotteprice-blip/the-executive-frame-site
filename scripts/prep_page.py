#!/usr/bin/env python3
"""
prep_page.py — Prepare an HTML page for the Executive Frame™ site.

Usage: python3 scripts/prep_page.py path/to/file.html

Actions performed:
  1. Remove all <style>...</style> blocks from the <head>
  2. Add <link rel="stylesheet" href="[prefix]assets/css/ef-styles.css"> after
     the last <link> tag in the <head>, if not already present
  3. Replace the entire <nav>...</nav> block with <nav id="site-nav"></nav>,
     if a full nav block is present
  4. Add <script src="[prefix]assets/js/nav.js"></script> before </body>,
     if not already present
  5. Write the result back to the same file

The [prefix] is computed from the file's depth relative to the project root
(e.g. "" for root-level files, "../" for files one level deep).
"""

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path('/Users/charlotteberry/Desktop/the-executive-frame-site').resolve()


def asset_prefix(file_path: Path) -> str:
    depth = len(file_path.resolve().parent.relative_to(PROJECT_ROOT).parts)
    return '../' * depth


def prep_page(file_path: str) -> None:
    path = Path(file_path).resolve()
    html = path.read_text(encoding='utf-8')

    prefix = asset_prefix(path)
    css_href = f'{prefix}assets/css/ef-styles.css'
    js_src   = f'{prefix}assets/js/nav.js'

    # 1. Remove all <style>...</style> blocks
    html = re.sub(r'[ \t]*<style[^>]*>.*?</style>[ \t]*\n?', '', html, flags=re.DOTALL)

    # 2. Add stylesheet link after the last <link> in <head>, if not already present
    if 'ef-styles.css' not in html:
        # Isolate the <head> region to avoid matching <link> tags in <body>
        head_match = re.search(r'(<head\b[^>]*>)(.*?)(</head>)', html, re.DOTALL | re.IGNORECASE)
        link_tag = f'<link rel="stylesheet" href="{css_href}">'
        if head_match:
            head_inner = head_match.group(2)
            links = list(re.finditer(r'<link\b[^>]*/?>', head_inner, re.IGNORECASE))
            if links:
                last_end = head_match.start(2) + links[-1].end()
                html = html[:last_end] + '\n' + link_tag + html[last_end:]
            else:
                html = html[:head_match.start(3)] + link_tag + '\n' + html[head_match.start(3):]
        else:
            # No <head> found; insert before </body> as a fallback
            html = html.replace('</body>', link_tag + '\n</body>', 1)

    # 3. Replace full <nav>...</nav> with placeholder if not already a bare placeholder
    if not re.search(r'<nav\s+id="site-nav"\s*>\s*</nav>', html):
        html = re.sub(r'<nav\b.*?</nav>', '<nav id="site-nav"></nav>', html, count=1, flags=re.DOTALL)

    # 4. Add nav.js script before </body> if not already present
    if 'nav.js' not in html:
        html = html.replace('</body>', f'<script src="{js_src}"></script>\n</body>', 1)

    path.write_text(html, encoding='utf-8')
    print(f'prepped: {path.relative_to(PROJECT_ROOT)}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 scripts/prep_page.py path/to/file.html')
        sys.exit(1)
    prep_page(sys.argv[1])
