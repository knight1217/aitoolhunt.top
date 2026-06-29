#!/usr/bin/env python3
"""
Generate static HTML pages for every AI tool from tools.json.
Each page has full content visible without JavaScript — critical for Google AdSense.
"""
import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
DATA_FILE = os.path.join(BASE_DIR, 'data', 'tools.json')

# HTML template for a tool detail page
TOOL_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{keywords}">
  <title>{title} Review 2026 — Rating, Pricing & Alternatives | AI Tool Hunt</title>
  <link rel="stylesheet" href="../css/style.css">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
  <script type="application/ld+json">
  {ld_json}
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1693165095863269" crossorigin="anonymous"></script>
</head>
<body>

<header class="header">
  <div class="container header-inner">
    <a href="../index.html" class="logo"><span class="logo-icon">🤖</span>AI Tool Hunt</a>
    <nav class="nav-links">
      <a href="../index.html">Home</a>
      <a href="../index.html#categories">Categories</a>
      <a href="../guide.html">Guide</a>
      <a href="../compare.html">Compare</a>
      <a href="../blog/">Blog</a>
      <a href="../about.html">About</a>
    </nav>
    <button class="mobile-toggle" aria-label="Menu">☰</button>
  </div>
</header>

<main class="section">
<div class="container">
  <!-- Breadcrumb -->
  <nav style="margin-bottom:24px;font-size:0.88rem;color:var(--text-muted)">
    <a href="../index.html" style="color:var(--text-secondary)">Home</a> &rsaquo;
    <a href="../index.html#categories" style="color:var(--text-secondary)">Categories</a> &rsaquo;
    <a href="../category.html?id={category_id}" style="color:var(--text-secondary)">{category_name}</a> &rsaquo;
    <span style="color:var(--text-primary)">{name}</span>
  </nav>

  <article style="max-width:860px;margin:0 auto;line-height:1.85;font-size:1.05rem;">

    <!-- Header -->
    <div style="display:flex;align-items:flex-start;gap:24px;flex-wrap:wrap;margin-bottom:32px">
      <div style="flex:1;min-width:280px">
        <p style="color:var(--accent);font-size:0.88rem;margin-bottom:6px;text-transform:uppercase;letter-spacing:1px">{category_name} Tool</p>
        <h1 style="font-size:2.4rem;margin-bottom:12px;line-height:1.25;color:var(--text-primary)">{name} Review {review_year}</h1>
        <p style="font-size:1.15rem;color:var(--text-secondary);margin-bottom:20px;line-height:1.65">{summary}</p>
        <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;margin-bottom:16px">
          <a href="{url}" target="_blank" rel="nofollow noopener" style="display:inline-block;background:var(--gradient-1);color:#fff;padding:12px 28px;border-radius:10px;text-decoration:none;font-weight:600;font-size:0.95rem;transition:transform 0.2s,box-shadow 0.2s" onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 6px 24px rgba(108,92,231,0.4)'" onmouseout="this.style.transform='';this.style.boxShadow=''">Visit {name} &rarr;</a>
          <span style="background:var(--bg-card);border:1px solid var(--border);padding:6px 14px;border-radius:8px;font-size:0.88rem;color:var(--text-secondary)">{pricing}</span>
        </div>
      </div>
      <div style="text-align:center;min-width:120px">
        <div style="font-size:3.5rem;font-weight:700;background:var(--gradient-1);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">{rating}</div>
        <div style="font-size:0.85rem;color:var(--text-muted);margin-top:4px">Out of 10</div>
        <div style="margin-top:8px;color:var(--warning);font-size:0.95rem">{stars}</div>
      </div>
    </div>

    <!-- Quick Facts -->
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:24px;margin-bottom:32px">
      <h2 style="font-size:1.2rem;margin-bottom:16px;color:var(--text-primary)">📋 Quick Facts</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px">
        <div><strong style="color:var(--text-secondary);font-size:0.85rem">PRICING</strong><br><span style="color:var(--text-primary)">{pricing}</span></div>
        <div><strong style="color:var(--text-secondary);font-size:0.85rem">DETAILS</strong><br><span style="color:var(--text-primary)">{price_detail}</span></div>
        <div><strong style="color:var(--text-secondary);font-size:0.85rem">RATING</strong><br><span style="color:var(--text-primary)">{rating}/10</span></div>
        <div><strong style="color:var(--text-secondary);font-size:0.85rem">BEST FOR</strong><br><span style="color:var(--text-primary)">{best_for}</span></div>
      </div>
    </div>

    <!-- Description -->
    <h2 style="font-size:1.5rem;margin-top:36px;margin-bottom:16px;color:var(--text-primary)">What is {name}?</h2>
    <p style="margin-bottom:20px;color:var(--text-secondary)">{description}</p>

    <!-- Pros & Cons -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:32px">
      <div style="background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.2);border-radius:var(--radius);padding:20px">
        <h3 style="font-size:1.1rem;color:var(--success);margin-bottom:12px">✅ Pros</h3>
        <ul style="list-style:none;padding:0;color:var(--text-secondary);line-height:2">{pros_html}</ul>
      </div>
      <div style="background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.2);border-radius:var(--radius);padding:20px">
        <h3 style="font-size:1.1rem;color:var(--danger);margin-bottom:12px">❌ Cons</h3>
        <ul style="list-style:none;padding:0;color:var(--text-secondary);line-height:2">{cons_html}</ul>
      </div>
    </div>

    <!-- Step-by-Step Tutorial -->
    <h2 style="font-size:1.5rem;margin-top:36px;margin-bottom:16px;color:var(--text-primary)">📖 How to Use {name}</h2>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:24px;margin-bottom:28px">
      {tutorial_html}
    </div>

    <!-- Alternatives -->
    <h2 style="font-size:1.5rem;margin-top:36px;margin-bottom:16px;color:var(--text-primary)">🔄 Alternatives to {name}</h2>
    <p style="color:var(--text-secondary);margin-bottom:16px">If {name} doesn't meet your needs, consider these alternatives we've also reviewed:</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-bottom:28px">
      {alternatives_html}
    </div>

    <!-- Tags -->
    <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:32px">
      {tags_html}
    </div>

    <!-- CTA -->
    <div style="background:linear-gradient(135deg,var(--bg-card),var(--bg-card-hover));border:1px solid var(--border);border-radius:var(--radius-lg);padding:28px;text-align:center;margin-bottom:40px">
      <h2 style="font-size:1.5rem;margin-bottom:12px;color:var(--text-primary)">Ready to try {name}?</h2>
      <p style="color:var(--text-secondary);margin-bottom:20px">Thousands of users rely on {name} every day. See if it's right for you.</p>
      <a href="{url}" target="_blank" rel="nofollow noopener" style="display:inline-block;background:var(--gradient-1);color:#fff;padding:14px 36px;border-radius:10px;text-decoration:none;font-weight:600;font-size:1.05rem;transition:transform 0.2s,box-shadow 0.2s" onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 32px rgba(108,92,231,0.4)'" onmouseout="this.style.transform='';this.style.boxShadow=''">Visit {name} Website &rarr;</a>
    </div>

    <!-- Disclaimer -->
    <p style="font-size:0.8rem;color:var(--text-muted);text-align:center;line-height:1.6;margin-bottom:40px;padding:16px;border-top:1px solid var(--border)">
      <em>Our review is based on hands-on testing of {name} as of {today}. Features and pricing may change. 
      This page may contain affiliate links — we may earn a commission if you sign up through our links, at no extra cost to you. 
      Our ratings and opinions are always independent.</em>
    </p>

  </article>
</div>
</main>

<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <h3>🤖 AI Tool Hunt</h3>
        <p>Hand-tested AI tool reviews. We test every tool ourselves so you don't have to.</p>
      </div>
      <div class="footer-col">
        <h4>Categories</h4>
        <a href="../category.html?id=writing">AI Writing</a>
        <a href="../category.html?id=image">AI Image</a>
        <a href="../category.html?id=video">AI Video</a>
        <a href="../category.html?id=coding">AI Coding</a>
        <a href="../category.html?id=chat">AI Chat</a>
      </div>
      <div class="footer-col">
        <h4>Pages</h4>
        <a href="../index.html">Home</a>
        <a href="../compare.html">Compare Tools</a>
        <a href="../about.html">About</a>
        <a href="../privacy-policy.html">Privacy Policy</a>
        <a href="../contact.html">Contact</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 AI Tool Hunt. All rights reserved.</span>
    </div>
  </div>
</footer>

<script>
// Mobile menu
(function(){
  var t=document.querySelector('.mobile-toggle');
  var n=document.querySelector('.nav-links');
  if(t&&n) t.addEventListener('click',function(){n.classList.toggle('open')});
})();
</script>
</body>
</html>'''

def escape_html(text):
    """Basic HTML escaping."""
    if not text:
        return ''
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def build_tutorial_html(tutorial):
    """Convert tutorial text with step numbers into HTML ordered list."""
    if not tutorial:
        return '<p style="color:var(--text-secondary)">No tutorial available yet.</p>'
    # Split by step numbers (1. 2. 3. etc)
    import re
    parts = re.split(r'(\d+\.\s)', tutorial)
    result = []
    i = 0
    current = ''
    for part in parts:
        if re.match(r'^\d+\.\s$', part):
            if current:
                result.append(current.strip())
            current = ''
        else:
            current += part
    if current:
        result.append(current.strip())
    
    if len(result) <= 1:
        return f'<p style="color:var(--text-secondary);line-height:1.9">{escape_html(tutorial)}</p>'
    
    items = ''.join(
        f'<li style="padding:8px 0;border-bottom:1px solid var(--border);line-height:1.75">{escape_html(step)}</li>'
        for step in result
    )
    return f'<ol style="padding-left:20px;color:var(--text-secondary);line-height:1.9">{items}</ol>'

def build_stars(rating):
    """Convert rating to star display."""
    full = int(rating)
    half = 1 if (rating - full) >= 0.5 else 0
    empty = 10 - full - half
    return '★' * full + ('½' if half else '') + '☆' * empty

def build_alternatives_html(alternatives, all_tools):
    """Generate alternative tool cards."""
    if not alternatives:
        return '<p style="color:var(--text-muted);grid-column:1/-1">No alternatives listed.</p>'
    
    alt_map = {t['id']: t for t in all_tools}
    items = []
    for alt_id in alternatives[:6]:
        t = alt_map.get(alt_id)
        if t:
            items.append(
                f'<a href="{alt_id}.html" style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:16px;text-decoration:none;color:var(--text-primary);transition:all 0.2s;display:block" onmouseover="this.style.borderColor=\'var(--accent)\';this.style.transform=\'translateY(-2px)\'" onmouseout="this.style.borderColor=\'var(--border)\';this.style.transform=\'\'">'
                f'<strong>{escape_html(t["name"])}</strong>'
                f'<span style="float:right;color:var(--accent);font-size:0.9rem">★{t.get("rating","?")}</span>'
                f'<p style="font-size:0.85rem;color:var(--text-muted);margin-top:4px;line-height:1.5">{escape_html(t.get("summary","")[:80])}</p>'
                f'</a>'
            )
    return '\n'.join(items) if items else '<p style="color:var(--text-muted)">No alternatives found.</p>'

def build_tags_html(tags):
    if not tags:
        return ''
    return '\n'.join(
        f'<span style="background:var(--bg-card);border:1px solid var(--border);padding:4px 12px;border-radius:20px;font-size:0.82rem;color:var(--text-secondary)">{escape_html(t)}</span>'
        for t in tags
    )

def build_ld_json(tool, category_name):
    """Generate JSON-LD structured data for SEO."""
    ld = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": tool['name'],
        "description": tool.get('description', tool.get('summary', '')),
        "applicationCategory": "AIApplication",
        "operatingSystem": "Web",
        "offers": {
            "@type": "Offer",
            "price": "0" if 'Free' in tool.get('pricing', '') else tool.get('price_detail', ''),
            "priceCurrency": "USD"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": str(tool.get('rating', 0)),
            "bestRating": "10",
            "worstRating": "1"
        }
    }
    return json.dumps(ld, indent=2, ensure_ascii=False)

def build_meta_desc(tool):
    summary = tool.get('summary', '')
    rating = tool.get('rating', '')
    pricing = tool.get('pricing', '')
    return f"{tool['name']} review: ★{rating}/10. {summary} Pricing: {pricing}. Honest, hands-on review with pros, cons, tutorial, and best alternatives for 2026."

def build_keywords(tool):
    name = tool['name'].lower()
    tags = ', '.join(tool.get('tags', []))
    return f"{name}, {name} review, {name} pricing, {name} alternatives, {tags}, AI tools, best AI tools 2026"

def main():
    # Load data
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    tools = data['tools']
    categories = {c['id']: c for c in data['categories']}
    today = datetime.now().strftime('%B %Y')
    year = datetime.now().year
    
    # Create tools directory
    os.makedirs(TOOLS_DIR, exist_ok=True)
    print(f"Generating {len(tools)} tool pages in {TOOLS_DIR}/")
    
    generated = 0
    for tool in tools:
        cat = categories.get(tool['category'], {})
        cat_name = cat.get('name', tool['category'].title())
        
        # Build rating stars
        rating = tool.get('rating', 0)
        stars = build_stars(rating)
        
        # Build pros/cons HTML
        pros_html = '\n'.join(
            f'<li>✔ {escape_html(p)}</li>' for p in tool.get('pros', [])
        ) or '<li style="color:var(--text-muted)">No pros listed</li>'
        
        cons_html = '\n'.join(
            f'<li>✘ {escape_html(c)}</li>' for c in tool.get('cons', [])
        ) or '<li style="color:var(--text-muted)">No cons listed</li>'
        
        # Build tutorial
        tutorial_html = build_tutorial_html(tool.get('tutorial', ''))
        
        # Build alternatives
        alternatives_html = build_alternatives_html(tool.get('alternatives', []), tools)
        
        # Build tags
        tags_html = build_tags_html(tool.get('tags', []))
        
        # Build JSON-LD
        ld_json = build_ld_json(tool, cat_name)
        
        # Build meta
        meta_desc = build_meta_desc(tool)
        keywords = build_keywords(tool)
        
        # Fill template using replace (avoid .format() conflict with CSS {})
        html = TOOL_TEMPLATE
        html = html.replace('{meta_desc}', escape_html(meta_desc))
        html = html.replace('{keywords}', escape_html(keywords))
        html = html.replace('{title}', escape_html(tool['name']))
        html = html.replace('{ld_json}', ld_json)
        html = html.replace('{category_id}', tool.get('category', ''))
        html = html.replace('{category_name}', escape_html(cat_name))
        html = html.replace('{name}', escape_html(tool['name']))
        html = html.replace('{review_year}', str(year))
        html = html.replace('{summary}', escape_html(tool.get('summary', '')))
        html = html.replace('{url}', tool.get('url', '#'))
        html = html.replace('{pricing}', escape_html(tool.get('pricing', 'Unknown')))
        html = html.replace('{rating}', str(rating))
        html = html.replace('{stars}', stars)
        html = html.replace('{price_detail}', escape_html(tool.get('price_detail', tool.get('pricing', ''))))
        html = html.replace('{best_for}', escape_html(tool.get('best_for', 'General use')))
        html = html.replace('{description}', escape_html(tool.get('description', tool.get('summary', ''))))
        html = html.replace('{pros_html}', pros_html)
        html = html.replace('{cons_html}', cons_html)
        html = html.replace('{tutorial_html}', tutorial_html)
        html = html.replace('{alternatives_html}', alternatives_html)
        html = html.replace('{tags_html}', tags_html)
        html = html.replace('{today}', today)
        html = html.replace('{tool_id}', tool['id'])
        
        # Write file
        filepath = os.path.join(TOOLS_DIR, f"{tool['id']}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        generated += 1
        print(f"  [{generated}/{len(tools)}] {tool['id']}.html")
    
    print(f"\nDone! Generated {generated} tool pages.")
    print(f"Files in: {TOOLS_DIR}/")

if __name__ == '__main__':
    main()
