#!/usr/bin/env python3
"""Generate sitemap.xml from all HTML files in the site."""
import os, glob
from datetime import date

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
today = date.today().isoformat()

# All HTML files under BASE (skip scripts/)
files = []
for root, dirs, filenames in os.walk(BASE):
    # Skip hidden dirs and scripts
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('scripts',)]
    for f in filenames:
        if f.endswith('.html'):
            full = os.path.join(root, f)
            rel = os.path.relpath(full, BASE).replace('\\', '/')
            files.append(rel)

# Sort and classify
static_pages = []
tool_pages = []
blog_pages = []
compare_pages = []

for f in sorted(files):
    if f.startswith('blog/'):
        blog_pages.append(f)
    elif f.startswith('compare/'):
        compare_pages.append(f)
    elif f.startswith('tools/'):
        tool_pages.append(f)
    else:
        static_pages.append(f)

def url_entry(path, priority, changefreq='monthly'):
    return f'  <url><loc>https://aitoolhunt.top/{path}</loc><lastmod>{today}</lastmod><changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>'

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
         '',
         '  <!-- Static Pages -->']

for p in static_pages:
    if p == 'index.html':
        lines.append(url_entry('', '1.0', 'weekly'))
    elif p in ('guide.html', 'compare.html', 'automation.html', 'videos.html', 'student.html', 'make-money.html'):
        lines.append(url_entry(p, '0.8', 'weekly'))
    elif p in ('blog/index.html',):
        lines.append(url_entry('blog/', '0.9', 'weekly'))
    elif p in ('about.html', 'contact.html'):
        lines.append(url_entry(p, '0.5'))
    else:
        lines.append(url_entry(p, '0.4'))

lines.append('')
lines.append('  <!-- Tool Review Pages -->')
for p in tool_pages:
    lines.append(url_entry(p, '0.8'))

lines.append('')
lines.append('  <!-- Blog Posts -->')
for p in blog_pages:
    lines.append(url_entry(p, '0.7'))

lines.append('')
lines.append('  <!-- Comparison Pages -->')
for p in compare_pages:
    lines.append(url_entry(p, '0.7'))

lines.append('')
lines.append('</urlset>')

sitemap = '\n'.join(lines) + '\n'
path = os.path.join(BASE, 'sitemap.xml')
with open(path, 'w', encoding='utf-8') as f:
    f.write(sitemap)

print(f'Sitemap generated: {path}')
print(f'  Static: {len(static_pages)}')
print(f'  Tools: {len(tool_pages)}')
print(f'  Blog: {len(blog_pages)}')
print(f'  Compare: {len(compare_pages)}')
print(f'  Total: {len(static_pages) + len(tool_pages) + len(blog_pages) + len(compare_pages)} URLs')
