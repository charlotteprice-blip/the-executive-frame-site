#!/usr/bin/env python3
"""
prep_all.py — Run prep_page.py against every HTML file in the project root
and in the pages/ folder, skipping files already prepped (those that contain
id="site-nav").

Usage: python3 scripts/prep_all.py
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path('/Users/charlotteberry/Desktop/the-executive-frame-site').resolve()

sys.path.insert(0, str(PROJECT_ROOT / 'scripts'))
from prep_page import prep_page

SEARCH_DIRS = [
    PROJECT_ROOT,
    PROJECT_ROOT / 'pages',
]


def main():
    targets = []
    for directory in SEARCH_DIRS:
        if directory.is_dir():
            targets.extend(sorted(directory.glob('*.html')))

    skipped = []
    prepped = []

    for html_file in targets:
        content = html_file.read_text(encoding='utf-8')
        if 'id="site-nav"' in content:
            skipped.append(html_file.relative_to(PROJECT_ROOT))
            continue
        prep_page(str(html_file))
        prepped.append(html_file.relative_to(PROJECT_ROOT))

    print(f'\nDone. {len(prepped)} prepped, {len(skipped)} skipped.')
    if skipped:
        print('Skipped (already prepped):')
        for f in skipped:
            print(f'  {f}')


if __name__ == '__main__':
    main()
