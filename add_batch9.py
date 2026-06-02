import re, json

with open('js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'window\.__TOOLS_DATA__\s*=\s*(\{.*\})\s*;', content, re.DOTALL)
if not m:
    print("ERROR: could not extract JSON")
    exit(1)

data = json.loads(m.group(1))
existing = set(t['id'] for t in data['tools'])
print(f"Existing tools: {len(existing)}")

new_tools = []

# 65. ElevenLabs (text-to-speech)
if 'elevenlabs' not in existing:
    new_tools.append({
        "id": "elevenlabs",
        "name": "ElevenLabs",
        "url": "https://elevenlabs.io",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free / Starter $5/mo / Creator $22/mo",
        "rating": 9.3,
        "summary": "Best AI text-to-speech. Clone your voice, 29 languages.",
        "description": "ElevenLabs is the leading AI voice generator. Type text, get ultra-realistic speech (29 languages, 100+ voices). 'Voice Clone': upload 1 min audio, clone YOUR voice. Used by NYT, The Guardian, and 1M+ creators. Free tier: 10k chars/mo.",
        "tutorial": "1. Sign up at elevenlabs.io (free). 2. Type text, pick voice. 3. Click 'Generate' — 5 seconds. 4. 'Voice Clone' (Pro): upload 1 min audio, clone your voice. 5. 'Projects': long-form (audiobooks). 6. API: integrate into your app.",
        "pros": ["Best AI voice quality (indistinguishable from human)", "Voice cloning (1 min sample)", "29 languages, 100+ voices", "API available"],
        "cons": ["Free tier limited (10k chars/mo)", "Pro needed for commercial use ($22/mo)", "Can be misused (deepfakes)"],
        "best_for": "Content creators who need ultra-realistic AI voices",
        "alternatives": ["playht", "murf", "resemble-ai"],
        "tags": ["ai-voice", "text-to-speech", "voice-clone", "audiobook"],
        "featured": True
    })

# 66. PlayHT
if 'playht' not in existing:
    new_tools.append({
        "id": "playht",
        "name": "PlayHT",
        "url": "https://play.ht",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free / Personal $14.25/mo / Enterprise custom",
        "rating": 8.4,
        "summary": "AI voice generation. 600+ voices, 60+ languages. API available.",
        "description": "PlayHT offers 600+ AI voices in 60+ languages. 'Voice Cloning' creates a digital twin of your voice. API for developers. Great alternative to ElevenLabs with different voice styles.",
        "tutorial": "1. Sign up at play.ht (free). 2. Type text, choose voice (600+). 3. Click 'Generate'. 4. 'Voice Clone': upload audio, clone voice. 5. API: docs.play.ht. 6. 'Pronunciation Library': customize how words are said.",
        "pros": ["600+ voices (more than ElevenLabs)", "Voice cloning available", "API for developers", "Pronunciation customization"],
        "cons": ["Voice quality slightly below ElevenLabs", "Free tier watermarked", "UI less polished than ElevenLabs"],
        "best_for": "Developers who need AI voice API",
        "alternatives": ["elevenlabs", "murf", "resemble-ai"],
        "tags": ["ai-voice", "text-to-speech", "api", "voice-clone"],
        "featured": False
    })

# 67. Murf AI
if 'murf' not in existing:
    new_tools.append({
        "id": "murf",
        "name": "Murf AI",
        "url": "https://murf.ai",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free / Basic $19/mo / Pro $39/mo",
        "rating": 8.2,
        "summary": "AI voiceover for videos and presentations. 120+ voices, 20+ languages.",
        "description": "Murf is an AI voice generator for voiceovers — videos, presentations, ads. 120+ voices, 20+ languages. 'Voice Changer': upload recording, convert to AI voice. Great for YouTubers and marketers.",
        "tutorial": "1. Sign up at murf.ai (free). 2. Click 'Create Project'. 3. Type script, pick voice (120+). 4. Adjust pitch, speed, emphasis. 5. 'Voice Changer': upload recording → convert to AI voice. 6. Export: MP3 or integrate with Canva/PowerPoint.",
        "pros": ["120+ voices, 20+ languages", "Voice Changer (upload → AI voice)", "Integrates with Canva/PowerPoint", "Great for YouTube voiceovers"],
        "cons": ["Free tier very limited (10 mins)", "Pro tier expensive ($39/mo)", "Less natural than ElevenLabs for some voices"],
        "best_for": "YouTubers and marketers who need voiceovers",
        "alternatives": ["elevenlabs", "playht", "resemble-ai"],
        "tags": ["ai-voice", "voiceover", "video", "youtube"],
        "featured": False
    })

# 68. Remove.bg (AI background removal)
if 'remove-bg' not in existing:
    new_tools.append({
        "id": "remove-bg",
        "name": "Remove.bg",
        "url": "https://remove.bg",
        "affiliate": None,
        "category": "image",
        "pricing": "Freemium",
        "price_detail": "Free (low-res) / Pro $9/mo / API pay-per-use",
        "rating": 8.7,
        "summary": "AI background removal. 1-click, no skills needed. API available.",
        "description": "Remove.bg removes image backgrounds in 1 click using AI. 100% automatic — no manual selection. Free tier: low-res preview. Pro: high-res, batch processing, API. Used by 500K+ photographers and e-commerce sellers.",
        "tutorial": "1. Go to remove.bg (no signup needed for 1 free try). 2. Upload image (PNG/JPG). 3. Wait 5 seconds — background removed! 4. Download (free: low-res, Pro: high-res). 5. For batch: upload 50+ images, process all. 6. API: integrate into your app (pay-per-use).",
        "pros": ["1-click, 100% automatic", "High-res (Pro)", "Batch processing (50+ images)", "API available"],
        "cons": ["Free tier low-res only", "Pro needed for transparent BG", "Struggles with complex edges (hair, fur)"],
        "best_for": "E-commerce sellers and photographers who need quick BG removal",
        "alternatives": ["canva-ai", "photoshop-ai", "clipdrop"],
        "tags": ["background-removal", "ai-image", "e-commerce", "api"],
        "featured": True
    })

# 69. Clipdrop (by Stability AI)
if 'clipdrop' not in existing:
    new_tools.append({
        "id": "clipdrop",
        "name": "Clipdrop (Stability AI)",
        "url": "https://clipdrop.co",
        "affiliate": None,
        "category": "image",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $9/mo / API pay-per-use",
        "rating": 8.5,
        "summary": "AI image tools: relight, upscale, background replace, sketch-to-image.",
        "description": "Clipdrop (by Stability AI) is a suite of AI image tools: Relight (adjust lighting), Upscale (2x/4x), Background Replacement, Sketch-to-Image, and Text-to-Image. Mobile app + web. API available.",
        "tutorial": "1. Go to clipdrop.co or download app. 2. Pick tool: 'Relight', 'Upscale', 'Replace Background', etc. 3. Upload image. 4. Adjust settings (e.g., light direction for Relight). 5. Download result. 6. API: integrate into your app.",
        "pros": ["Suite of 10+ AI image tools", "Relight (adjust lighting after shooting)", "Upscale 2x/4x", "Mobile app + API"],
        "cons": ["Free tier limited (5 uses/day)", "Pro needed for bulk", "Some tools less powerful than standalone tools"],
        "best_for": "Photographers who want AI image editing tools",
        "alternatives": ["remove-bg", "leonardo-ai", "canva-ai"],
        "tags": ["ai-image", "relight", "upscale", "background-replacement"],
        "featured": False
    })

# 70. Microsoft Designer (Bing Image Creator)
if 'microsoft-designer' not in existing:
    new_tools.append({
        "id": "microsoft-designer",
        "name": "Microsoft Designer / Bing Image Creator",
        "url": "https://designer.microsoft.com",
        "affiliate": None,
        "category": "image",
        "pricing": "Free",
        "price_detail": "Free (Bing Image Creator uses DALL-E 3)",
        "rating": 8.1,
        "summary": "Free AI image generation (DALL-E 3). Integrated into Microsoft 365.",
        "description": "Microsoft Designer (and Bing Image Creator) uses DALL-E 3 for free AI image generation. 10-20 images/day free. Integrated into Microsoft 365 (Word, PowerPoint). 'Designer' also offers templates for social media posts.",
        "tutorial": "1. Go to bing.com/images/create OR designer.microsoft.com. 2. Sign in with Microsoft account (free). 3. Type prompt, click 'Create'. 4. Bing: 4 images per prompt, 20 prompts/day. 5. Designer: also offers templates (social media, presentations). 6. Download: PNG, free, no watermark.",
        "pros": ["100% free (DALL-E 3 powered)", "Integrated into Microsoft 365", "20 prompts/day (Bing)", "No watermark on downloads"],
        "cons": ["Limited daily uses (20/day)", "Less control than Midjourney/Leonardo", "Requires Microsoft account"],
        "best_for": "Microsoft users who want free AI image generation",
        "alternatives": ["dalle-3", "midjourney", "leonardo-ai"],
        "tags": ["dalle-3", "free", "microsoft", "bing"],
        "featured": True
    })

# 71. Craiyon (formerly DALL-E mini)
if 'craiyon' not in existing:
    new_tools.append({
        "id": "craiyon",
        "name": "Craiyon",
        "url": "https://craiyon.com",
        "affiliate": None,
        "category": "image",
        "pricing": "Freemium",
        "price_detail": "Free (watermark) / Supporter $6/mo / Professional $24/mo",
        "rating": 7.8,
        "summary": "Free AI image generation. No signup needed. Lower quality than DALL-E.",
        "description": "Craiyon (formerly DALL-E mini) is a free AI image generator. No signup needed. Lower quality than DALL-E/Midjourney, but 100% free (with watermark). Great for experimentation. 9 images per prompt.",
        "tutorial": "1. Go to craiyon.com (no signup needed). 2. Type prompt. 3. Get 9 images (2-3 mins). 4. Click image to enlarge. 5. Download (free: watermarked). 6. Pro: no watermark, faster (45 seconds).",
        "pros": ["100% free (no signup)", "9 images per prompt", "No credit card needed", "Great for experimentation"],
        "cons": ["Lower quality than DALL-E/Midjourney", "Free: watermarked", "Slow (2-3 mins per prompt)"],
        "best_for": "People who want to try AI image generation for free",
        "alternatives": ["dalle-3", "midjourney", "leonardo-ai"],
        "tags": ["free", "ai-image", "no-signup", "experimental"],
        "featured": False
    })

# 72. Galileo AI (UI generation)
if 'galileo-ai' not in existing:
    new_tools.append({
        "id": "galileo-ai",
        "name": "Galileo AI",
        "url": "https://www.usegalileo.ai",
        "affiliate": None,
        "category": "design",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $24/mo",
        "rating": 8.3,
        "summary": "AI UI generation. Screenshot → editable UI (Figma). Prompt → UI.",
        "description": "Galileo AI generates UI designs from text prompts OR screenshots. Upload a screenshot → Galileo converts to editable Figma design. Also: prompt → full UI. Great for designers who want to speed up workflow.",
        "tutorial": "1. Sign up at usegalileo.ai (free). 2. 'Text to UI': type prompt ('A login page with Google sign-in'). 3. Galileo generates UI. 4. 'Screenshot to UI': upload screenshot → editable Figma. 5. Export to Figma (free). 6. Pro: more generations, higher quality.",
        "pros": ["Screenshot → editable Figma (unique!)", "Prompt → full UI", "Export to Figma (free)", "Great for design workflow"],
        "cons": ["Free tier limited (5 generations/mo)", "Pro needed for high quality", "Can be inaccurate on complex UIs"],
        "best_for": "UI/UX designers who want to speed up workflow",
        "alternatives": ["v0-dev", "uizard", "figma-ai"],
        "tags": ["ai-ui", "figma", "screenshot-to-ui", "design"],
        "featured": False
    })

# 73. Uizard (UI design for non-designers)
if 'uizard' not in existing:
    new_tools.append({
        "id": "uizard",
        "name": "Uizard",
        "url": "https://uizard.io",
        "affiliate": None,
        "category": "design",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $29/mo / Business custom",
        "rating": 8.0,
        "summary": "AI UI design for non-designers. Screenshot → editable UI. Prompt → UI.",
        "description": "Uizard lets non-designers create UI designs using AI. 'Screenshot to UI': upload screenshot → editable design. 'Text to UI': type prompt → full UI. Also: drag-and-drop editor. Great for founders who need quick prototypes.",
        "tutorial": "1. Sign up at uizard.io (free). 2. 'Screenshot to UI': upload screenshot → Uizard converts to editable design. 3. 'Text to UI': type prompt → UI. 4. Edit: drag-and-drop. 5. Export: Figma, PNG, or handoff to dev. 6. 'Autodesigner': type description → full app prototype.",
        "pros": ["Screenshot → editable UI", "Text to UI", "Drag-and-drop editor (no design skills needed)", "Great for quick prototypes"],
        "cons": ["Free tier limited (1 project)", "Pro expensive ($29/mo)", "Output can be generic"],
        "best_for": "Founders and PMs who need quick UI prototypes",
        "alternatives": ["galileo-ai", "v0-dev", "figma-ai"],
        "tags": ["ai-ui", "prototype", "non-designer", "screenshot-to-ui"],
        "featured": False
    })

# 74. tl;dv (meeting notes)
if 'tldv' not in existing:
    new_tools.append({
        "id": "tldv",
        "name": "tl;dv",
        "url": "https://tldv.io",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $12/mo / Business $24/mo",
        "rating": 8.1,
        "summary": "AI meeting notes. Auto-transcribes Zoom/Meet/Teams. Summaries + timestamps.",
        "description": "tl;dv (too long; didn't view) auto-transcribes Zoom, Google Meet, and Teams meetings. AI summarizes: key moments, action items, decisions. Timestamps: jump to exact moment in recording. Free tier: 10 meetings/mo.",
        "tutorial": "1. Sign up at tldv.io (free). 2. Install Chrome extension OR connect calendar. 3. Join meeting — tl;dv auto-records + transcribes. 4. After meeting: get email with summary + timestamps. 5. Search: 'What did John say about budget?' across all meetings. 6. 'Clipper': share specific moment (timestamped link).",
        "pros": ["Auto-transcribes (10+ languages)", "AI summary + action items", "Timestamps (jump to moment)", "Free tier (10 meetings/mo)"],
        "cons": ["Free tier limited (10 meetings/mo)", "Pro needed for unlimited", "Can be inaccurate on heavy accents"],
        "best_for": "Teams who want searchable meeting notes + timestamps",
        "alternatives": ["fireflies-ai", "otter-ai", "read-ai"],
        "tags": ["meeting-notes", "transcription", "ai-summary", "timestamps"],
        "featured": False
    })

# 75. Read.ai (meeting insights)
if 'read-ai' not in existing:
    new_tools.append({
        "id": "read-ai",
        "name": "Read.ai",
        "url": "https://read.ai",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $16/mo / Enterprise custom",
        "rating": 8.2,
        "summary": "AI meeting assistant. Real-time insights, sentiment analysis, engagement score.",
        "description": "Read.ai provides real-time meeting insights: sentiment analysis, engagement score, and talking speed. After meeting: AI summary + action items. Integrates with Zoom, Meet, Teams, and Webex. Free tier: 10 meetings/mo.",
        "tutorial": "1. Sign up at read.ai (free). 2. Install app (Zoom/Meet/Teams/Webex). 3. During meeting: see real-time insights (sentiment, engagement). 4. After meeting: get AI summary + action items. 5. 'Engagement Score': see who was most/least engaged. 6. 'Question Detector': see who asked questions (did they get answered?).",
        "pros": ["Real-time insights (during meeting!)", "Sentiment analysis + engagement score", "Question Detector (unique)", "Integrates with 10+ platforms"],
        "cons": ["Free tier limited (10 meetings/mo)", "Pro needed for full insights", "Can feel surveillance-heavy"],
        "best_for": "Managers who want to understand meeting dynamics",
        "alternatives": ["fireflies-ai", "tldv", "otter-ai"],
        "tags": ["meeting-insights", "sentiment-analysis", "engagement-score", "real-time"],
        "featured": False
    })

print(f"\nAdding {len(new_tools)} more tools...")
data['tools'].extend(new_tools)

# Write back
new_json = json.dumps(data, indent=2, ensure_ascii=False)
# Convert 2-space indent to 4-space to match original format
new_json = new_json.replace('  ', '    ')

new_content = f"// Auto-generated from tools.json -- embedded for file:// compatibility\nwindow.__TOOLS_DATA__ = {new_json};\n"

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Done! Total tools: {len(data['tools'])}")
