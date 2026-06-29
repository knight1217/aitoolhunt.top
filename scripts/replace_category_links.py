#!/usr/bin/env python3
"""Replace all category.html?id=XXX links with category-XXX.html"""
import json, glob

BASE = __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))

with open(f'{BASE}/data/tools.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
cat_ids = [c['id'] for c in data['categories']]

files = glob.glob(f'{BASE}/**/*.html', recursive=True) + glob.glob(f'{BASE}/**/*.js', recursive=True)
total = 0
for fp in files:
    with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    orig = content[:]
    for cid in cat_ids:
        old = f'category.html?id={cid}'
        new = f'category-{cid}.html'
        if old in content:
            content = content.replace(old, new)
            total += 1
    if content != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        rel = fp.replace(BASE + '/', '').replace(BASE + '\\', '')
        print(f'  {rel}')
print(f'\nTotal replacements: {total}')
