#!/usr/bin/env python3
"""Add CloudCannon source editable regions to Executive Frame HTML pages.

Convention (matches the regions already live on the site):
    data-editable="source" data-path="/<file>.html" data-key="<type>-<n>"

Headings containing an <em> accent are split into protected sub-regions
(<span> -> -t1, <em> -> -e1) so the italic styling survives a rewording.

Locked and never touched: nav, footer, svg, form, script, style, head,
HTML comments, skip links, the nine assessment pages, and any element
whose inner content is not plain text.

Usage:  python3 add_editable_regions.py [--apply] [file ...]
"""
import re, sys, os, glob

EXCLUDE_FILES = {
    'ef-assessment-consulting.html', 'ef-assessment-corporate.html',
    'ef-assessment-education.html', 'ef-assessment-elite.html',
    'ef-assessment-family.html', 'ef-assessment-health.html',
    'ef-assessment-law.html', 'ef-assessment-neurodiversity.html',
    'ef-assessment-women.html', 'TEMP-upload-test.html',
}

MASK_RE = re.compile(r'<(nav|footer|svg|form|script|style|head)\b.*?</\1\s*>', re.S | re.I)
COMMENT_RE = re.compile(r'<!--.*?-->', re.S)
OPEN_RE = re.compile(r'<(div|p|h1|h2|h3|h4|a|summary)\b([^>]*)>', re.I)
CLASS_RE = re.compile(r'class="([^"]*)"', re.I)
KEYNUM_RE = re.compile(r'data-key="([a-z-]+?)-(\d+)(?:-[te]\d+)?"')


def key_type(tag, cls):
    c = cls.split()
    if tag == 'h1':
        return 'page-title'
    if tag == 'h2':
        return 'section-title'
    if tag == 'h3':
        return 'card-title'
    if tag == 'h4':
        return 'sub-title'
    if tag == 'summary':
        return 'faq-q'
    if tag == 'p':
        if any(x == 'lead' or x.startswith('lead') for x in c):
            return 'lead-text'
        if 's-body' in c:
            return 'body-text'
        return 'text'
    if tag == 'div':
        if any('eyebrow' in x for x in c):
            return 'eyebrow'
        if 'ce' in c or any('tag' in x for x in c):
            return 'card-tag'
        if 'q' in c:
            return 'faq-q'
        return None
    if tag == 'a':
        if 'skip' in c:
            return None
        if any(x.endswith('btn') or x == 'btn' for x in c) or any('btn' in x for x in c):
            return 'button-label'
        return None
    return None


def masked_spans(text):
    spans = [m.span() for m in MASK_RE.finditer(text)]
    spans += [m.span() for m in COMMENT_RE.finditer(text)]
    return spans


def in_spans(pos, spans):
    return any(a <= pos < b for a, b in spans)


def find_close(text, tag, start):
    """Return (inner_start, inner_end, close_end) for the element opened at start."""
    depth = 1
    pos = start
    pat = re.compile(r'<(/?)' + tag + r'\b[^>]*>', re.I)
    while True:
        m = pat.search(text, pos)
        if not m:
            return None
        if m.group(1):
            depth -= 1
            if depth == 0:
                return m.start(), m.end()
        else:
            depth += 1
        pos = m.end()


EM_SPLIT_RE = re.compile(r'(<em\b[^>]*>.*?</em>)', re.S | re.I)


def process(path, apply_changes):
    text = open(path, encoding='utf-8').read()
    original = text
    spans = masked_spans(text)
    counters = {}
    for m in KEYNUM_RE.finditer(text):
        t, n = m.group(1), int(m.group(2))
        counters[t] = max(counters.get(t, 0), n)

    edits = []          # (start, end, replacement)
    added = 0

    for m in OPEN_RE.finditer(text):
        tag = m.group(1).lower()
        attrs = m.group(2)
        if in_spans(m.start(), spans):
            continue
        if 'data-editable' in attrs:
            continue
        cls_m = CLASS_RE.search(attrs)
        cls = cls_m.group(1) if cls_m else ''
        ktype = key_type(tag, cls)
        if not ktype:
            continue
        close = find_close(text, tag, m.end())
        if not close:
            continue
        inner_start, close_end = m.end(), close[0]
        inner = text[inner_start:close_end]
        if not inner.strip():
            continue

        def attr(key):
            return ' data-editable="source" data-path="/%s" data-key="%s"' % (os.path.basename(path), key)

        if tag in ('h1', 'h2') and re.search(r'<em\b', inner, re.I):
            parts = EM_SPLIT_RE.split(inner)
            if any(re.search(r'<(?!/?em\b)', p) for p in parts):
                continue
            counters[ktype] = counters.get(ktype, 0) + 1
            base = '%s-%d' % (ktype, counters[ktype])
            out, ti, ei, ok = [], 0, 0, True
            for p in parts:
                if not p:
                    continue
                if p.lower().startswith('<em'):
                    em = re.match(r'<em\b([^>]*)>(.*?)</em>', p, re.S | re.I)
                    if not em or re.search(r'<', em.group(2)):
                        ok = False
                        break
                    ei += 1
                    out.append('<em%s%s>%s</em>' % (em.group(1), attr('%s-e%d' % (base, ei)), em.group(2)))
                elif p.strip():
                    ti += 1
                    out.append('<span%s>%s</span>' % (attr('%s-t%d' % (base, ti)), p))
                else:
                    out.append(p)
            if not ok:
                counters[ktype] -= 1
                continue
            edits.append((inner_start, close_end, ''.join(out)))
            added += ti + ei
            continue

        if re.search(r'<', inner):
            continue
        counters[ktype] = counters.get(ktype, 0) + 1
        key = '%s-%d' % (ktype, counters[ktype])
        insert_at = m.end() - 1
        if text[insert_at - 1] == '/':
            insert_at -= 1
        edits.append((insert_at, insert_at, attr(key)))
        added += 1

    for start, end, repl in sorted(edits, key=lambda e: -e[0]):
        text = text[:start] + repl + text[end:]

    if apply_changes and text != original:
        open(path, 'w', encoding='utf-8').write(text)
    return added, len(re.findall(r'data-editable="source"', text))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    apply_changes = '--apply' in sys.argv
    files = args or sorted(f for f in glob.glob('*.html') if f not in EXCLUDE_FILES)
    total_added = total_now = 0
    for f in files:
        if os.path.basename(f) in EXCLUDE_FILES:
            continue
        added, now = process(f, apply_changes)
        total_added += added
        total_now += now
        print('%-38s +%-5d %d' % (f, added, now))
    print('-' * 52)
    print('%-38s +%-5d %d' % ('TOTAL', total_added, total_now))
    print('mode:', 'APPLIED' if apply_changes else 'dry run')


if __name__ == '__main__':
    main()
