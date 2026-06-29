#!/usr/bin/env python3
"""
Generate static category pages from tools.json.
Each category gets its own HTML page with all tools listed + rich content.
"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(f'{BASE}/data/tools.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

CAT_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{meta_desc}">
  <title>Best {cat_name} Tools 2026 — Reviews, Pricing & Comparisons | AI Tool Hunt</title>
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
      <a href="../categories.html">Categories</a>
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
    <a href="../categories.html" style="color:var(--text-secondary)">Categories</a> &rsaquo;
    <span style="color:var(--text-primary)">{cat_name}</span>
  </nav>

  <div style="text-align:center;margin-bottom:40px">
    <div style="font-size:3rem;margin-bottom:12px">{icon}</div>
    <h1 style="font-size:2.5rem;margin-bottom:12px">Best {cat_name} Tools in 2026</h1>
    <p style="font-size:1.15rem;color:var(--text-secondary);max-width:680px;margin:0 auto;line-height:1.7">{cat_desc}</p>
    <p style="color:var(--text-muted);margin-top:8px;font-size:0.9rem">{count} tools reviewed &bull; Updated June 2026</p>
  </div>

  <!-- Tool Grid -->
  <div class="tool-grid" style="margin-bottom:48px">
    {tool_cards}
  </div>

  <!-- Category Info -->
  <article style="max-width:800px;margin:0 auto 48px;line-height:1.85;color:var(--text-secondary)">
    <h2 style="font-size:1.5rem;color:var(--text-primary);margin-bottom:16px">How to Choose the Right {cat_name} Tool</h2>
    {how_to_choose}
    
    <h2 style="font-size:1.5rem;color:var(--text-primary);margin-top:36px;margin-bottom:16px">Frequently Asked Questions</h2>
    {faq}
  </article>

  <!-- Other Categories -->
  <div style="text-align:center;padding:32px;border-top:1px solid var(--border)">
    <h3 style="font-size:1.2rem;color:var(--text-primary);margin-bottom:16px">Explore More Categories</h3>
    <div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center">
      {other_cats}
    </div>
  </div>

</div>
</main>

<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <h3>🤖 AI Tool Hunt</h3>
        <p>Hand-tested AI tool reviews. 67 tools across 11 categories.</p>
      </div>
      <div class="footer-col">
        <h4>Popular</h4>
        <a href="../category-chat.html">AI Chat</a>
        <a href="../category-image.html">AI Image</a>
        <a href="../category-video.html">AI Video</a>
        <a href="../category-coding.html">AI Coding</a>
        <a href="../category-app-builder.html">AI App Builders</a>
      </div>
      <div class="footer-col">
        <h4>Pages</h4>
        <a href="../index.html">Home</a>
        <a href="../categories.html">All Categories</a>
        <a href="../compare.html">Compare Tools</a>
        <a href="../privacy-policy.html">Privacy Policy</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 AI Tool Hunt. All rights reserved.</span>
    </div>
  </div>
</footer>

<script>
(function(){var t=document.querySelector('.mobile-toggle');var n=document.querySelector('.nav-links');if(t&&n)t.addEventListener('click',function(){n.classList.toggle('open')});})();
</script>
</body>
</html>'''

CATEGORIES_META = {
    'chat': {
        'desc': 'Compare the best AI chatbot and conversational AI tools. ChatGPT, Claude, Gemini, Grok, DeepSeek, and Perplexity — tested and rated.',
        'how_to_choose': '<p>AI chatbots have evolved from simple Q&amp;A machines into full-featured assistants capable of writing code, analyzing documents, generating images, and browsing the web. When choosing a chatbot, consider these key factors:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>Use case:</strong> ChatGPT excels at versatility, Claude at deep reasoning, Gemini at Google integration, Grok at real-time news.</li><li><strong>Context window:</strong> Gemini leads with 1M+ tokens for analyzing entire books; Claude and ChatGPT offer 200K-500K.</li><li><strong>Pricing:</strong> Free tiers are available for all major chatbots. Paid plans ($7.99-$200/mo) unlock advanced models and features.</li><li><strong>Multimodal capabilities:</strong> Most now support image input, file upload, and web browsing. Some include image/video generation.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Which is better, ChatGPT or Claude?</strong><p>A: Both are excellent but serve different strengths. ChatGPT is more versatile with broader integrations (DALL-E, browsing, GPTs). Claude excels at long-form writing, nuanced analysis, and complex reasoning tasks. Many users subscribe to both.</p></div><div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Is there a free AI chatbot?</strong><p>A: Yes! ChatGPT, Claude, Gemini, Grok, DeepSeek, and Perplexity all offer robust free tiers. The free versions use slightly less powerful models but are perfectly capable for most everyday tasks.</p></div><div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: What does $20/month get you?</strong><p>A: ChatGPT Plus ($20) unlocks GPT-5.5, image generation, and advanced data analysis. Claude Pro ($20) gives you more Opus usage and higher limits. Choose based on which AI\'s personality and capabilities match your workflow.</p></div>',
    },
    'image': {
        'desc': 'Find the best AI image generators. Midjourney, DALL-E 3, Stable Diffusion, Leonardo AI, Adobe Firefly, and Ideogram — compared.',
        'how_to_choose': '<p>AI image generation has matured dramatically in 2026. Here\'s how to pick the right tool:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>Quality vs cost:</strong> Midjourney V7 produces the most artistic results ($10-120/mo). Stable Diffusion SD3.5 is completely free if you have a GPU.</li><li><strong>Ease of use:</strong> DALL-E (inside ChatGPT) is the simplest — just describe what you want. Midjourney requires Discord or web app. Stable Diffusion needs technical setup.</li><li><strong>Control:</strong> Stable Diffusion + ControlNet gives professional-grade control. Midjourney is more about aesthetic exploration.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Is there a free AI image generator?</strong><p>A: Yes! Stable Diffusion is free and open-source. DALL-E has free access through ChatGPT. Adobe Firefly offers free credits. Leonardo AI gives 150 free tokens daily.</p></div><div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Midjourney vs DALL-E vs Stable Diffusion?</strong><p>A: Midjourney = best artistic quality. DALL-E = easiest to use (text in ChatGPT). Stable Diffusion = most control + free + open source. Many creators use all three for different purposes.</p></div>',
    },
    'video': {
        'desc': 'Best AI video generators and editors: Sora 2, Runway, Kling, Luma, Pika, CapCut, Synthesia, HeyGen — reviewed and compared.',
        'how_to_choose': '<p>The AI video space exploded in 2025-2026. Pick based on your use case:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>Narrative filmmaking:</strong> Sora 2 produces the most realistic narrative videos. Best for cinematic storytelling.</li><li><strong>Quick social content:</strong> CapCut is free, fast, and TikTok-native. Opus Clip auto-extracts viral moments from long videos.</li><li><strong>Avatar/talking-head:</strong> Synthesia and HeyGen create professional AI-avatar videos in 140+ languages.</li><li><strong>Artistic/cinematic:</strong> Runway Gen-4.5 and Luma Dream Machine excel at creative video generation.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Is Sora 2 free?</strong><p>A: Sora 2 is included with ChatGPT Plus ($20/mo) with limited credits, or unlimited with ChatGPT Pro ($200/mo).</p></div><div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: What\'s the best free AI video editor?</strong><p>A: CapCut is completely free with no watermark, 4K export, auto-captions, and trending templates. It\'s the most popular choice for TikTok and Reels creators.</p></div>',
    },
    'coding': {
        'desc': 'Best AI coding assistants: Claude Code, Cursor, GitHub Copilot, Windsurf, Replit AI — tested and compared for 2026.',
        'how_to_choose': '<p>AI coding tools have evolved from autocomplete to autonomous agents:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>Agentic coding:</strong> Claude Code and Cursor can autonomously implement features across multiple files. Best for experienced devs.</li><li><strong>IDE integration:</strong> GitHub Copilot supports 30+ IDEs including JetBrains. Cursor/Windsurf are VS Code-only.</li><li><strong>Budget:</strong> Windsurf offers unlimited free completions. Claude Code is free CLI (API costs). Cursor is $20/mo for full agentic features.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Which AI coding tool is best in 2026?</strong><p>A: Claude Code leads in autonomous capability (SWE-bench 80.8%). Cursor leads in productivity and UX. Windsurf is the best free option. GitHub Copilot is the enterprise default.</p></div>',
    },
    'audio': {
        'desc': 'Best AI audio and music tools: ElevenLabs, Suno, Udio, Descript, and more — voice cloning, music generation, podcast editing.',
        'how_to_choose': '<p>AI audio tools cover voice synthesis, music generation, and audio editing:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>Voice generation:</strong> ElevenLabs is the industry standard with 70+ languages and voice cloning.</li><li><strong>Music creation:</strong> Suno and Udio generate full songs from text prompts. Mureka offers commercial licensing.</li><li><strong>Podcast editing:</strong> Descript revolutionizes audio editing with transcript-based workflow and AI voice correction.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Can AI really generate music?</strong><p>A: Yes! Suno and Udio can generate complete songs with vocals and instruments from a simple text prompt. The quality is surprisingly good for demos and content creation, though not yet professional-studio level.</p></div>',
    },
    'writing': {
        'desc': 'Best AI writing tools: Jasper, Grammarly, Copy.ai, Writesonic — content creation, grammar checking, and marketing copy.',
        'how_to_choose': '<p>AI writing tools range from grammar checkers to full content generators:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>Grammar &amp; style:</strong> Grammarly is the gold standard for real-time writing improvement across all platforms.</li><li><strong>Marketing content:</strong> Jasper and Copy.ai specialize in brand-controlled marketing copy at scale.</li><li><strong>SEO content:</strong> Writesonic optimizes for both human readers and AI search engines.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Do I need a dedicated AI writing tool when I have ChatGPT?</strong><p>A: For casual writing, ChatGPT works great. Dedicated tools like Jasper offer brand voice control, templates, team workflows, and SEO optimization that general chatbots don\'t provide.</p></div>',
    },
    'design': {
        'desc': 'Best AI design tools: Canva AI, Figma AI, Gamma, Looka — graphic design, presentations, logos, and brand kits.',
        'how_to_choose': '<p>AI design tools make professional design accessible to everyone:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>General design:</strong> Canva AI is the easiest for non-designers. Figma AI integrates into professional design workflows.</li><li><strong>Presentations:</strong> Gamma creates stunning slide decks from a single prompt.</li><li><strong>Logos &amp; branding:</strong> Looka generates complete brand identities including logos, business cards, and social media kits.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Can AI replace graphic designers?</strong><p>A: AI design tools are excellent for quick graphics, social media posts, and presentations. For complex brand strategy and custom illustration, professional designers still add significant value. AI is best seen as a force multiplier for designers and a democratizer for non-designers.</p></div>',
    },
    'app-builder': {
        'desc': 'Best AI app builders: Lovable, Bolt.new, v0 — build full-stack apps, websites, and UI components without coding.',
        'how_to_choose': '<p>AI app builders are 2026\'s hottest category — turning anyone into a developer:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>Full-stack apps:</strong> Lovable generates complete React + Supabase apps with database, auth, and deployment from a text description.</li><li><strong>Developer control:</strong> Bolt.new gives you a real browser-based IDE with terminal access — best of AI speed + dev control.</li><li><strong>UI components:</strong> v0 by Vercel generates production-ready React/Tailwind components — best for frontend developers.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Can I really build an app without coding?</strong><p>A: Yes! Lovable, Bolt.new, and v0 have collectively enabled thousands of non-technical founders to build and launch MVPs. The apps are production-ready for simple to medium complexity. Complex apps may still need developer refinement.</p></div>',
    },
    'productivity': {
        'desc': 'Best AI productivity tools: NotebookLM, Notion AI, Reclaim.ai, Clockwise, Read.ai — work smarter with AI.',
        'how_to_choose': '<p>AI productivity tools automate the tedious parts of work:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>Research &amp; notes:</strong> NotebookLM (free) turns your documents into an interactive AI research assistant. Notion AI integrates AI into your workspace.</li><li><strong>Calendar &amp; scheduling:</strong> Reclaim.ai, Motion, and Clockwise auto-optimize your schedule for focus time.</li><li><strong>Meeting intelligence:</strong> Read.ai, Fireflies, tl;dv, and Otter.ai capture and summarize your meetings.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: What\'s the single best AI productivity tool?</strong><p>A: NotebookLM is arguably the most impactful — it\'s completely free, works with your own documents, and generates genuinely useful summaries, FAQs, and even podcast-style audio overviews of your content.</p></div>',
    },
    'education': {
        'desc': 'Best AI tools for education and learning: Khanmigo, Quizlet AI, Duolingo Max, Consensus, Elicit — learn faster with AI.',
        'how_to_choose': '<p>AI is transforming education — here\'s how to pick the right tools:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>Tutoring:</strong> Khanmigo (Khan Academy) and Socratic (Google) provide AI tutoring across subjects.</li><li><strong>Study tools:</strong> Quizlet AI and Duolingo Max use AI for personalized learning.</li><li><strong>Academic research:</strong> Consensus and Elicit search 200M+ papers, extract data, and build literature reviews.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Are AI study tools actually effective?</strong><p>A: Yes, when used correctly. AI tutors like Khanmigo guide students through problems rather than giving answers. Research tools like Consensus help find and synthesize academic papers faster than traditional methods.</p></div>',
    },
    'marketing': {
        'desc': 'Best AI marketing tools: HubSpot AI, Writesonic, Surfer SEO, AdCreative AI — automate and optimize your marketing.',
        'how_to_choose': '<p>AI marketing tools help you create, optimize, and measure campaigns:</p><ul style="padding-left:20px;margin:12px 0"><li><strong>All-in-one:</strong> HubSpot AI integrates AI across CRM, email, content, and analytics.</li><li><strong>Content &amp; SEO:</strong> Writesonic and Surfer SEO generate and optimize content for both readers and AI search engines.</li><li><strong>Ad creative:</strong> AdCreative AI generates high-converting ad visuals and copy.</li></ul>',
        'faq': '<div style="margin-bottom:20px"><strong style="color:var(--text-primary)">Q: Can AI write better marketing copy than humans?</strong><p>A: AI excels at generating variations, A/B testing ideas, and following proven frameworks. For deeply creative, emotional, or brand-defining campaigns, human marketers still lead. The best approach is AI-assisted human creativity.</p></div>',
    },
}

def build_tool_card(tool):
    rating = tool.get('rating', 0)
    stars = '★' * int(rating) + ('½' if rating - int(rating) >= 0.5 else '') + '☆' * (10 - int(rating) - (1 if rating - int(rating) >= 0.5 else 0))
    tags = ' '.join(f'<span class="tool-tag">{t}</span>' for t in (tool.get('tags', [])[:3]))
    name_esc = tool['name'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    summary_esc = tool.get('summary', '')[:100].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    pricing_esc = tool.get('pricing', '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    
    featured = tool.get('featured', False)
    
    return f'''    <a href="../tools/{tool['id']}.html" class="tool-card{(' featured' if featured else '')}">
      <div class="tool-card-header">
        <div class="tool-card-icon">{get_icon(tool['category'])}</div>
        <div class="tool-card-meta">
          <div class="tool-card-name">{name_esc}</div>
          <div class="tool-card-pricing">{pricing_esc}</div>
        </div>
      </div>
      <p class="tool-card-summary">{summary_esc}...</p>
      <div class="tool-card-footer">
        <div class="tool-rating">
          <span class="stars">{stars}</span>
          <span class="score">{rating}</span>
        </div>
        <div class="tool-card-tags">{tags}</div>
      </div>
    </a>'''

def get_icon(cat):
    icons = {'chat': '💬', 'image': '🎨', 'video': '🎬', 'coding': '💻', 'audio': '🎵',
             'writing': '📝', 'design': '🎯', 'app-builder': '🏗️', 'productivity': '⚡',
             'education': '📚', 'marketing': '📊'}
    return icons.get(cat, '🤖')

def build_ld(cat_name, cat_desc, tools):
    items = []
    for t in tools:
        items.append({
            "@type": "SoftwareApplication",
            "name": t['name'],
            "description": t.get('summary', ''),
            "applicationCategory": "AIApplication",
            "aggregateRating": {"@type": "AggregateRating", "ratingValue": str(t.get('rating', 0)), "bestRating": "10"}
        })
    return json.dumps({"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i+1, "item": item} for i, item in enumerate(items)]}, indent=2, ensure_ascii=False)

# Group tools by category
cats = {}
for t in data['tools']:
    c = t['category']
    cats.setdefault(c, []).append(t)

# Sort tools by rating within each category
for c in cats:
    cats[c].sort(key=lambda x: x.get('rating', 0), reverse=True)

# Get all category defs
all_cat_defs = {c['id']: c for c in data['categories']}

total = 0
for cat_id, tools in cats.items():
    cat_def = all_cat_defs.get(cat_id, {})
    cat_name = cat_def.get('name', cat_id.title())
    cat_icon = get_icon(cat_id)
    cat_desc = CATEGORIES_META.get(cat_id, {}).get('desc', f'Best {cat_name} AI tools reviewed and compared.')
    how_to = CATEGORIES_META.get(cat_id, {}).get('how_to_choose', '<p>Explore our curated list of the best {cat_name} AI tools.</p>'.format(cat_name=cat_name))
    faq = CATEGORIES_META.get(cat_id, {}).get('faq', '')
    
    meta_desc = f"Best {cat_name} AI tools of 2026 — {len(tools)} tools reviewed with ratings, pricing, pros/cons, and tutorials. Honest, hands-on testing."
    
    cards = '\n'.join(build_tool_card(t) for t in tools)
    
    other_cats = '\n'.join(
        f'<a href="../category-{cid}.html" style="background:var(--bg-card);border:1px solid var(--border);padding:10px 18px;border-radius:10px;text-decoration:none;color:var(--text-primary);font-size:0.9rem;transition:all 0.2s" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'var(--border)\'">{get_icon(cid)} {all_cat_defs[cid]['name']}</a>'
        for cid in cats if cid != cat_id
    )
    
    ld = build_ld(cat_name, cat_desc, tools)
    
    html = CAT_TEMPLATE
    html = html.replace('{meta_desc}', meta_desc.replace('"', '&quot;'))
    html = html.replace('{cat_name}', cat_name)
    html = html.replace('{count}', str(len(tools)))
    html = html.replace('{icon}', cat_icon)
    html = html.replace('{cat_desc}', cat_desc)
    html = html.replace('{how_to_choose}', how_to)
    html = html.replace('{faq}', faq)
    html = html.replace('{tool_cards}', cards)
    html = html.replace('{other_cats}', other_cats)
    html = html.replace('{ld_json}', ld)
    
    fname = f'category-{cat_id}.html'
    with open(f'{BASE}/{fname}', 'w', encoding='utf-8') as f:
        f.write(html)
    total += 1
    print(f'  [{total}] {fname} ({len(tools)} tools, {len(html)} bytes)')

print(f'\nGenerated {total} category pages.')
