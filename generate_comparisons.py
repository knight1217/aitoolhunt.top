#!/usr/bin/env python3
"""生成新比较页面到 compare/ 目录"""

import os

CMP = "C:/Users/MI/WorkBuddy/2026-05-26-19-17-29/aitools-site/compare"

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{desc}">
  <title>{title} | AI Tool Hunt</title>
  <link rel="stylesheet" href="../css/style.css">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
</head>
<body>

<header class="header">
  <div class="container header-inner">
    <a href="../index.html" class="logo"><span class="logo-icon">🤖</span>AI Tool Hunt</a>
    <nav class="nav-links">
      <a href="../index.html">Home</a>
      <a href="../index.html#categories">Categories</a>
      <a href="../guide.html">Guide</a>
      <a href="../compare.html" class="active">Compare</a>
      <a href="../blog/index.html">Blog</a>
      <a href="../about.html">About</a>
    </nav>
    <button class="mobile-toggle" aria-label="Menu">☰</button>
  </div>
</header>

<main class="section">
<div class="container">
<article style="max-width:900px;margin:0 auto;line-height:1.85;font-size:1.05rem;color:var(--text-primary);">
  <p style="color:var(--accent);font-size:0.9rem;margin-bottom:8px;">📅 June 2026 · Comparison</p>
  <h1 style="font-size:2.2rem;margin-bottom:16px;line-height:1.3;">{title}</h1>
  <p style="color:var(--text-secondary);font-size:1.1rem;margin-bottom:32px;">{desc}</p>
{body}
  <p style="margin-top:40px;padding:20px;background:var(--bg-card);border-radius:var(--radius);text-align:center;color:var(--text-secondary);">
    🔍 <a href="../compare.html" style="color:var(--accent);">Browse all comparisons →</a>
  </p>
</article>
</div>
</main>

<footer class="footer">
  <div class="container">
    <div class="footer-links" style="margin-bottom:16px;">
      <a href="../about.html">About</a>
      <span style="margin:0 8px;color:#666;">|</span>
      <a href="../privacy-policy.html">Privacy Policy</a>
      <span style="margin:0 8px;color:#666;">|</span>
      <a href="../about.html#contact">Contact</a>
    </div>
    <p style="color:var(--text-muted);font-size:0.85rem;">© 2026 AI Tool Hunt. All rights reserved.</p>
  </div>
</footer>
<script src="../js/main.js"></script>
</body>
</html>"""

ARTICLES = [
  {
    "slug": "notion-ai-vs-obsidian-ai-2026",
    "title": "Notion AI vs. Obsidian AI 2026: Best AI Note-Taking Tool?",
    "desc": "We compare the two most popular AI-enhanced note-taking apps on features, AI quality, pricing, and privacy.",
    "body": """  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:32px;">
    <div style="background:var(--bg-card);border:1px solid var(--accent);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">🏆 Notion AI</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">AI built natively into your workspace. Summarize pages, draft content, translate — all without leaving Notion.</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 $10/mo add-on (requires Notion plan)</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">📝 Obsidian + AI</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">Local-first, plugin-based AI. Use your own API key (ChatGPT/Claude). Maximum privacy, more setup.</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 Free (BYO API key) / $10/mo Obsidian Sync</p>
    </div>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🤖 AI Feature Comparison</h2>
  <div style="overflow-x:auto;margin-bottom:32px;">
  <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
    <thead><tr style="background:var(--bg-card);"><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">Feature</th><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">Notion AI</th><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">Obsidian AI</th></tr></thead>
    <tbody>
      <tr><td style="padding:10px;border-bottom:1px solid var(--border);">AI Summarization</td><td style="padding:10px;border-bottom:1px solid var(--border);">✅ Native</td><td style="padding:10px;border-bottom:1px solid var(--border);">✅ Via plugin</td></tr>
      <tr><td style="padding:10px;border-bottom:1px solid var(--border);">Privacy</td><td style="padding:10px;border-bottom:1px solid var(--border);">⚠️ Cloud</td><td style="padding:10px;border-bottom:1px solid var(--border);">✅ Local</td></tr>
      <tr><td style="padding:10px;">Offline Use</td><td style="padding:10px;">❌ No</td><td style="padding:10px;">✅ Yes</td></tr>
    </tbody>
  </table>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🔮 Bottom Line</h2>
  <p><strong>Choose Notion AI</strong> if you want an all-in-one workspace with zero setup. <strong>Choose Obsidian AI</strong> if privacy and local-first workflow matter more.</p>"""
  },
  {
    "slug": "github-copilot-vs-codewhisperer-2026",
    "title": "GitHub Copilot vs. Amazon CodeWhisperer 2026: AI Code Review",
    "desc": "Two AI coding assistants backed by tech giants. We compare code quality, IDE support, pricing, and security features.",
    "body": """  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:32px;">
    <div style="background:var(--bg-card);border:1px solid var(--accent);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">🤖 GitHub Copilot</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">Powered by OpenAI (GPT-4). Industry-standard AI pair programmer. Tightest IDE integration.</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 $10/mo (Pro) / $21/mo (Business)</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">🛠️ Amazon CodeWhisperer</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">AWS-optimized AI coding assistant. Free tier is generous. Strong on security scanning.</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 Free (Individual) / $19/mo (Professional)</p>
    </div>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">📊 Head-to-Head Comparison</h2>
  <div style="overflow-x:auto;margin-bottom:32px;">
  <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
    <thead><tr style="background:var(--bg-card);"><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">Metric</th><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">Copilot</th><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">CodeWhisperer</th></tr></thead>
    <tbody>
      <tr><td style="padding:10px;border-bottom:1px solid var(--border);">Code Quality</td><td style="padding:10px;border-bottom:1px solid var(--border);">⭐⭐⭐⭐⭐</td><td style="padding:10px;border-bottom:1px solid var(--border);">⭐⭐⭐⭐</td></tr>
      <tr><td style="padding:10px;border-bottom:1px solid var(--border);">IDE Support</td><td style="padding:10px;border-bottom:1px solid var(--border);">VS Code, JetBrains, Neovim</td><td style="padding:10px;border-bottom:1px solid var(--border);">VS Code, JetBrains</td></tr>
      <tr><td style="padding:10px;">Free Tier</td><td style="padding:10px;">❌ No (students free)</td><td style="padding:10px;">✅ Yes</td></tr>
    </tbody>
  </table>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🔮 Bottom Line</h2>
  <p><strong>Choose Copilot</strong> for best-in-class code completion and multi-language support. <strong>Choose CodeWhisperer</strong> if you're deep in AWS and want a free tier.</p>"""
  },
  {
    "slug": "grammarly-vs-prowritingaid-2026",
    "title": "Grammarly vs. ProWritingAid 2026: Best AI Writing Assistant?",
    "desc": "Deep-dive comparison of the two leading AI writing tools. Which one actually makes you a better writer?",
    "body": """  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:32px;">
    <div style="background:var(--bg-card);border:1px solid var(--accent);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">✍️ Grammarly</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">Best-in-class grammar and spelling checker. AI suggestions are context-aware. Works everywhere (browser, MS Office, mobile).</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 Free / Premium $12/mo</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">📚 ProWritingAid</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">Deep writing analysis: overused words, sentence length variety, pacing. Built for novelists and long-form writers.</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 Free / Premium $10/mo (annual)</p>
    </div>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🎯 Who Should Use Which?</h2>
  <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:20px;">
    <p style="margin:4px 0;"><strong>Grammarly is better for:</strong> Business writing, emails, daily communication, non-native English speakers.</p>
    <p style="margin:4px 0;"><strong>ProWritingAid is better for:</strong> Novelists, creative writers, academics writing long manuscripts.</p>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🔮 Bottom Line</h2>
  <p>Grammarly for daily use and business. ProWritingAid for serious creative writing. Both have free tiers — try both before paying.</p>"""
  },
  {
    "slug": "synesia-vs-heygen-2026",
    "title": "Synthesia vs. HeyGen 2026: Best AI Video Avatar Tool?",
    "desc": "Create professional AI avatar videos without a camera or crew. We compare quality, pricing, and customization.",
    "body": """  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:32px;">
    <div style="background:var(--bg-card);border:1px solid var(--accent);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">🎬 Synthesia</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">Enterprise-grade AI avatars. 140+ languages, custom avatar creation, strong governance features. Used by 60% of Fortune 500.</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 $22/mo (Starter) / Custom Enterprise</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">🎥 HeyGen</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">Fast-growing challenger. Better avatar realism, faster rendering, more generous free tier. Strong on social media use cases.</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 Free (3 videos/mo) / $24/mo (Creator)</p>
    </div>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🎥 Video Quality Comparison</h2>
  <div style="overflow-x:auto;margin-bottom:32px;">
  <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
    <thead><tr style="background:var(--bg-card);"><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">Feature</th><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">Synthesia</th><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">HeyGen</th></tr></thead>
    <tbody>
      <tr><td style="padding:10px;border-bottom:1px solid var(--border);">Avatar Realism</td><td style="padding:10px;border-bottom:1px solid var(--border);">⭐⭐⭐⭐</td><td style="padding:10px;border-bottom:1px solid var(--border);">⭐⭐⭐⭐⭐</td></tr>
      <tr><td style="padding:10px;border-bottom:1px solid var(--border);">Free Tier</td><td style="padding:10px;border-bottom:1px solid var(--border);">❌ No</td><td style="padding:10px;border-bottom:1px solid var(--border);">✅ Yes (3 videos/mo)</td></tr>
      <tr><td style="padding:10px;">Enterprise Features</td><td style="padding:10px;">✅ Strong</td><td style="padding:10px;">⚠️ Growing</td></tr>
    </tbody>
  </table>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🔮 Bottom Line</h2>
  <p><strong>Choose Synthesia</strong> for enterprise training videos and corporate communications. <strong>Choose HeyGen</strong> for social media, marketing, and if you want a free tier to test.</p>"""
  },
  {
    "slug": "jasper-vs-copyai-2026",
    "title": "Jasper vs. Copy.ai 2026: Best AI Writing Tool for Marketing?",
    "desc": "Both tools target marketers and agencies. We compare output quality, workflow features, pricing, and team collaboration.",
    "body": """  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:32px;">
    <div style="background:var(--bg-card);border:1px solid var(--accent);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">📝 Jasper AI</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">The OG AI marketing writer. Brand Voice feature, 50+ templates, strong on long-form content. Higher price point but more features.</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 $39/mo (Creator) / $59/mo (Pro)</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">✨ Copy.ai</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">Workflow-first AI writing. "Workflows" automate multi-step content pipelines. Strong on sales and GTM content. More affordable.</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 Free / $36/mo (Pro)</p>
    </div>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🏢 Team & Collaboration Features</h2>
  <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:20px;">
    <p style="margin:4px 0;"><strong>Jasper:</strong> Brand Voice (consistent tone), Jasper Chat, team templates, API access on higher tiers.</p>
    <p style="margin:4px 0;"><strong>Copy.ai:</strong> Workflows (visual automation builder), Go-to-Market workflows, simpler UI for non-writers.</p>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🔮 Bottom Line</h2>
  <p><strong>Choose Jasper</strong> if brand consistency and long-form content matter most. <strong>Choose Copy.ai</strong> if you want to automate multi-step content workflows and save money.</p>"""
  },
  {
    "slug": "runway-vs-pika-2026",
    "title": "Runway ML vs. Pika 2026: Best AI Video Generation Tool?",
    "desc": "Text-to-video is exploding. Runway Gen-4 vs. Pika 2.0 — which one should you use for AI video creation?",
    "body": """  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:32px;">
    <div style="background:var(--bg-card);border:1px solid var(--accent);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">🎬 Runway ML (Gen-4)</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">Professional-grade AI video. Gen-4 delivers cinematic quality, precise motion control, and advanced editing features (Inpainting, Motion Brush).</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 $12/mo (Standard) / $76/mo (Unlimited)</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;">
      <h2 style="font-size:1.3rem;margin-bottom:12px;">⚡ Pika 2.0</h2>
      <p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:16px;">Fast, fun, and accessible. Pika 2.0 focuses on speed and ease of use. "Pikaffects" let you animate any image. Strong community.</p>
      <p style="font-size:0.9rem;color:var(--text-muted);">💰 Free (30 credits/mo) / $8/mo (Standard)</p>
    </div>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🎥 Video Quality & Features</h2>
  <div style="overflow-x:auto;margin-bottom:32px;">
  <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
    <thead><tr style="background:var(--bg-card);"><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">Feature</th><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">Runway</th><th style="padding:12px;text-align:left;border-bottom:1px solid var(--border);">Pika</th></tr></thead>
    <tbody>
      <tr><td style="padding:10px;border-bottom:1px solid var(--border);">Video Quality</td><td style="padding:10px;border-bottom:1px solid var(--border);">⭐⭐⭐⭐⭐</td><td style="padding:10px;border-bottom:1px solid var(--border);">⭐⭐⭐⭐</td></tr>
      <tr><td style="padding:10px;border-bottom:1px solid var(--border);">Motion Control</td><td style="padding:10px;border-bottom:1px solid var(--border);">✅ Advanced (Motion Brush)</td><td style="padding:10px;border-bottom:1px solid var(--border);">⚠️ Basic</td></tr>
      <tr><td style="padding:10px;">Free Tier</td><td style="padding:10px;">❌ No</td><td style="padding:10px;">✅ Yes</td></tr>
    </tbody>
  </table>
  </div>
  <h2 style="font-size:1.5rem;margin-top:40px;margin-bottom:16px;">🔮 Bottom Line</h2>
  <p><strong>Choose Runway</strong> for professional video production and cinematic quality. <strong>Choose Pika</strong> for quick social media clips, animating images, and if you want a free tier.</p>"""
  },
]

def main():
    import os
    os.makedirs(CMP, exist_ok=True)
    for a in ARTICLES:
        html = HEADER.format(
            desc=a["desc"],
            title=a["title"],
            body=a["body"]
        )
        path = os.path.join(CMP, a["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Written: " + a["slug"] + ".html")

    # 打印compare.html的新卡片
    print("\n" + "="*60)
    print("COMPARE.HTML CARDS (add to compare.html):")
    print("="*60)
    for a in ARTICLES:
        lines = []
        lines.append('    <a href="' + a["slug"] + '.html" style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:28px;transition:var(--transition);display:block;text-decoration:none;color:inherit;">')
        lines.append('      <span style="display:inline-block;background:var(--border);color:var(--text-secondary);font-size:0.75rem;padding:4px 10px;border-radius:20px;margin-bottom:12px;">Comparison</span>')
        lines.append('      <h3 style="font-size:1.15rem;margin-bottom:8px;line-height:1.4;">' + a["title"] + '</h3>')
        lines.append('      <p style="color:var(--text-secondary);font-size:0.9rem;line-height:1.6;margin-bottom:12px;">' + a["desc"] + '</p>')
        lines.append('      <span style="color:var(--text-muted);font-size:0.8rem;">📅 June 2026 · Comparison</span>')
        lines.append('    </a>')
        print('\n'.join(lines))
        print()

if __name__ == "__main__":
    main()
