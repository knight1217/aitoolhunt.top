#!/usr/bin/env python3
"""更新 blog/index.html — 30篇文章完整版"""

import os

BLOG_INDEX = "C:/Users/MI/WorkBuddy/2026-05-26-19-17-29/aitools-site/blog/index.html"

# 30篇文章数据：slug, title, desc, cat, cat_bg, date, read
ARTICLES = [
  # ---- 14篇旧文章 ----
  ("best-ai-tools-2026", "Best AI Tools 2026: The Ultimate Guide (50+ Tools Reviewed)", "Hand-picked, honestly reviewed. No fluff, no hype — just the tools that actually deliver in 2026.", "🔥 Popular", "var(--accent)", "June 2026", "8 min read"),
  ("chatgpt-vs-claude-vs-gemini-2026", "ChatGPT vs Claude vs Gemini 2026: Which AI Assistant Wins?", "We tested them head-to-head on real tasks. Accuracy, coding, writing, privacy — here's the full breakdown.", "Comparison", "var(--border)", "June 2026", "7 min read"),
  ("ai-image-generation-compared-2026", "Midjourney vs DALL-E vs Stable Diffusion vs Leonardo (2026)", "Four image generators, four philosophies. Find which one fits your creative workflow.", "Comparison", "var(--border)", "June 2026", "7 min read"),
  ("free-ai-tools-2026", "18 Best Free AI Tools in 2026 (No Trials, Actually Free)", "Build a complete AI toolkit for $0/month. No credit cards, no time-limited trials.", "Guide", "var(--border)", "June 2026", "6 min read"),
  ("ai-coding-assistants-compared-2026", "Best AI Coding Assistant 2026: Cursor vs Copilot vs Windsurf vs Claude Code", "Which one actually makes you faster? Tested on real projects with real results.", "Comparison", "var(--border)", "June 2026", "7 min read"),
  ("ai-tools-beginners-guide-2026", "AI Tools for Beginners: Where to Start in 2026", "No tech skills needed. Exactly which tools to use, what to avoid, and your first AI workflow in 10 minutes.", "Beginner", "var(--border)", "June 2026", "6 min read"),
  ("best-ai-video-tools-2026", "Best AI Video Tools 2026 (Free & Paid)", "Text-to-video generators, AI editors, and everything between. Find the right tool for your budget.", "Roundup", "var(--border)", "June 2026", "7 min read"),
  ("best-ai-music-audio-tools-2026", "Best AI Music & Audio Tools 2026 (Create Music Without Skills)", "AI song generators, voice tools, and podcast editors. Make music with zero training.", "Roundup", "var(--border)", "June 2026", "6 min read"),
  ("ai-tools-for-students-2026", "Top AI Tools for Students 2026 (Study Smarter, Not Harder)", "Research, writing, memorization, presentations — the AI toolkit every student needs.", "Guide", "var(--border)", "June 2026", "7 min read"),
  ("ai-tools-small-business-2026", "AI Tools for Small Business Owners 2026 (Do More With Less)", "Marketing, customer service, operations — AI tools that save time without breaking the bank.", "Business", "var(--border)", "June 2026", "7 min read"),
  ("how-to-create-ai-images-guide-2026", "How to Create AI Images: Complete Beginner's Guide 2026", "Step-by-step from zero to pro. Choose tools, write prompts, avoid mistakes.", "Tutorial", "var(--border)", "June 2026", "8 min read"),
  ("leonardo-ai-vs-midjourney-2026", "Leonardo AI vs Midjourney 2026: Which AI Image Generator Wins?", "Quality, pricing, features, and ease of use compared. Find your perfect image generator.", "Comparison", "var(--border)", "June 2026", "7 min read"),
  ("suno-vs-udio-2026", "Suno vs Udio 2026: Best AI Music Generator Compared", "Sound quality, creative control, and pricing head-to-head. Which AI makes better songs?", "Comparison", "var(--border)", "June 2026", "6 min read"),
  ("ai-tools-social-media-2026", "Best AI Tools for Social Media Content 2026 (Save 10+ Hours/Week)", "Graphics, video, copywriting, scheduling — the complete AI social media toolkit.", "Guide", "var(--border)", "June 2026", "6 min read"),
  # ---- 16篇新文章 ----
  ("ai-tools-content-creators-2026", "Best AI Tools for Content Creators 2026 (14 Tools Reviewed)", "The ultimate AI toolkit for YouTubers, bloggers, and influencers. Scripts, thumbnails, music, editing — all AI-powered.", "Guide", "var(--border)", "June 2026", "9 min read"),
  ("make-money-with-ai-tools-2026", "How to Make Money with AI Tools in 2026 (8 Proven Methods)", "Practical, actionable ways to earn income using AI tools — no coding required. Freelancing, content, consulting, and more.", "Guide", "var(--border)", "June 2026", "10 min read"),
  ("ai-non-programmers-coding-2026", "AI Coding for Non-Programmers 2026 (Build Apps Without Code)", "You don't need to learn Python to build with AI. A practical guide to shipping real software without writing a line of code.", "Tutorial", "var(--border)", "June 2026", "9 min read"),
  ("ai-video-generation-workflow-2026", "AI Video Generation Workflow 2026: From Prompt to Publish", "A complete step-by-step workflow for creating publish-ready videos using AI — no camera, no editing skills required.", "Tutorial", "var(--border)", "June 2026", "8 min read"),
  ("ai-productivity-tools-2026", "12 Best AI Productivity Tools 2026 (Tested & Ranked)", "AI tools that actually save time in 2026. Tested 30+ tools — here are the 12 that earned a permanent spot in our workflow.", "Roundup", "var(--border)", "June 2026", "9 min read"),
  ("ai-academic-research-tools-2026", "AI Tools for Researchers & Academics 2026 (Literature to Writing)", "From literature review to citation management to writing — AI tools that accelerate academic research without compromising integrity.", "Guide", "var(--border)", "June 2026", "9 min read"),
  ("ai-presentation-tools-2026", "Best AI Presentation Tools 2026: Create Stunning Slides in Minutes", "Stop wasting hours on PowerPoint. These AI tools generate complete presentations from a text prompt — design, layout, and content included.", "Roundup", "var(--border)", "June 2026", "7 min read"),
  ("ai-voice-cloning-guide-2026", "AI Voice Cloning Guide 2026: ElevenLabs, Murf, and Beyond", "How AI voice cloning works, which tools sound most human, and the ethics & legal landscape in 2026.", "Guide", "var(--border)", "June 2026", "8 min read"),
  ("ai-seo-tools-2026", "AI SEO Tools 2026: Rank Faster with Less Effort", "AI won't replace SEO — but it makes it 10x faster. The best AI tools for keyword research, content optimization, and technical SEO in 2026.", "Guide", "var(--border)", "June 2026", "8 min read"),
  ("ai-freelancers-tools-2026", "AI Tools for Freelancers 2026: Run Your Business on Autopilot", "How solo freelancers use AI to compete with agencies. Client onboarding, project management, invoicing — all AI-assisted.", "Business", "var(--border)", "June 2026", "9 min read"),
  ("ai-data-analysis-tools-2026", "Best AI Data Analysis Tools 2026 (No Coding Required)", "Analyze data, generate insights, and create visualizations — without Excel wizardry or Python. AI makes data analysis accessible to everyone in 2026.", "Roundup", "var(--border)", "June 2026", "8 min read"),
  ("ai-language-learning-2026", "AI Language Learning Tools 2026: Learn Faster with AI Tutors", "AI language tutors are available 24/7, never get impatient, and adapt to your level. The best AI tools for learning languages in 2026.", "Guide", "var(--border)", "June 2026", "7 min read"),
  ("ai-job-hunting-tools-2026", "AI Job Hunting Tools 2026: Resume to Interview to Offer", "Use AI to optimize your resume for ATS systems, write cover letters, practice interviews, and negotiate offers. The complete AI job hunt guide.", "Guide", "var(--border)", "June 2026", "9 min read"),
  ("ai-avatar-generators-2026", "Best AI Avatar Generators 2026 (Profile Pictures & Characters)", "Create stunning AI avatars and profile pictures for LinkedIn, Instagram, or gaming. Compare the top AI avatar generators and learn to create professional portraits.", "Roundup", "var(--border)", "June 2026", "7 min read"),
  ("ai-automation-tools-compared-2026", "AI Automation Tools Compared 2026: Zapier vs Make vs n8n vs LFlow", "Automate repetitive tasks with AI. Compare Zapier, Make, n8n, and LFlow — find the right automation tool for your workflow.", "Comparison", "var(--border)", "June 2026", "8 min read"),
  ("ai-design-tools-compared-2026", "Best AI Design Tools 2026: Canva vs Adobe Firefly vs Figma AI", "AI design tools compared. Canva AI, Adobe Firefly, Figma AI, and Midjourney — which one fits your workflow?", "Comparison", "var(--border)", "June 2026", "8 min read"),
]

# 生成卡片HTML
cards_html = ""
for slug, title, desc, cat, cat_bg, date, read in ARTICLES:
    cards_html += f"""    <a href="{slug}.html" style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:28px;transition:var(--transition);display:block;text-decoration:none;color:inherit;">
      <span style="display:inline-block;background:{cat_bg};color:var(--text-secondary);font-size:0.75rem;padding:4px 10px;border-radius:20px;margin-bottom:12px;">{cat}</span>
      <h3 style="font-size:1.15rem;margin-bottom:8px;line-height:1.4;">{title}</h3>
      <p style="color:var(--text-secondary);font-size:0.9rem;line-height:1.6;margin-bottom:12px;">{desc}</p>
      <span style="color:var(--text-muted);font-size:0.8rem;">📅 {date} · {read}</span>
    </a>
"""

# 完整HTML
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="AI Tool Hunt Blog — honest AI tool reviews, comparisons, guides, and tips. Stay updated on the best AI tools in 2026.">
  <title>Blog — AI Tool Hunt</title>
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
      <a href="../compare.html">Compare</a>
      <a href="index.html" class="active">Blog</a>
      <a href="../about.html">About</a>
      <a href="../contact.html">Contact</a>
    </nav>
    <button class="mobile-toggle" aria-label="Menu">☰</button>
  </div>
</header>

<main class="section">
<div class="container">
  <h1 style="font-size:2rem;margin-bottom:8px;text-align:center;">📝 AI Tool Hunt Blog</h1>
  <p style="text-align:center;color:var(--text-secondary);margin-bottom:40px;">Honest reviews, comparisons, and guides. Updated weekly.</p>

  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
{cards_html}
  </div>

  <div style="text-align:center;margin-top:48px;padding:32px;background:var(--bg-card);border-radius:var(--radius);">
    <p style="color:var(--text-secondary);margin-bottom:8px;">📬 New articles every week. Stay tuned.</p>
    <p style="color:var(--text-muted);font-size:0.85rem;">Got a topic you want us to cover? <a href="../about.html#contact" style="color:var(--accent);">Let us know →</a></p>
  </div>
</div>
</main>

<footer class="footer">
  <div class="container">
    <div class="footer-links" style="margin-bottom:16px">
      <a href="../about.html">About</a><span style="margin:0 8px;color:#666">|</span>
      <a href="../privacy-policy.html">Privacy Policy</a><span style="margin:0 8px;color:#666">|</span>
      <a href="index.html">Blog</a><span style="margin:0 8px;color:#666">|</span>
      <a href="../about.html#contact">Contact</a>
    </div>
    <div class="footer-bottom"><span>&copy; 2026 AI Tool Hunt. All rights reserved.</span></div>
  </div>
</footer>
<script src="../js/data.js"></script>
<script src="../js/main.js"></script>
</body>
</html>"""

with open(BLOG_INDEX, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Done! blog/index.html updated with {len(ARTICLES)} articles.")
