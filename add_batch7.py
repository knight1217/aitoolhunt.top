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

# 51. Suno (already added? check)
if 'sunrun' not in existing and 'suno' not in existing:
    new_tools.append({
        "id": "sunrun",
        "name": "Suno AI",
        "url": "https://suno.com",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $10/mo",
        "rating": 9.2,
        "summary": "AI music generation. Type lyrics or prompt, get full songs with vocals.",
        "description": "Suno is the leading AI music generator. Type a description ('upbeat pop song about coffee') or paste lyrics, and Suno creates a full song with vocals, instruments, and structure (verse/chorus). Free tier: 50 songs/day. Used by 10M+ people.",
        "tutorial": "1. Go to suno.com (free signup). 2. Click 'Create'. 3. Type prompt: 'A melancholic piano ballad about lost love' — OR paste your own lyrics. 4. Click 'Create' — 30 seconds. 5. Get 2 versions. Click 'Extend' to continue the song. 6. Download MP3 (Pro) or share link.",
        "pros": ["Best AI music quality (vocals + instruments)", "Free tier: 50 songs/day", "Extend feature (continue songs)", "10M+ users"],
        "cons": ["Free tier: can't download MP3 (stream only)", "Pro needed for commercial use", "Can sound AI-generated if prompt is vague"],
        "best_for": "Musicians and creators who want original songs fast",
        "alternatives": ["udio", "mubert", "boomy"],
        "tags": ["ai-music", "song-generation", "vocals", "free-tier"],
        "featured": True
    })

# 52. Udio
if 'udio' not in existing:
    new_tools.append({
        "id": "udio",
        "name": "Udio",
        "url": "https://udio.com",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free / Standard $10/mo / Premier $30/mo",
        "rating": 9.0,
        "summary": "High-quality AI music. Better vocals than Suno (some say).",
        "description": "Udio is Suno's main competitor. Many users say Udio has better vocal quality and more musical coherence. Started by ex-DeepMind researchers. Free tier: 1200 credits/month (约 10 songs). Pro: 1800 credits/month + download Rights.",
        "tutorial": "1. Sign up at udio.com (free). 2. Click 'Create'. 3. Type prompt or paste lyrics. 4. Choose genre tags (optional). 5. Click 'Generate' — 30 seconds. 6. Use 'Extend' to continue. 7. Download WAV (Pro tier).",
        "pros": ["Better vocal quality than Suno (debatable)", "Ex-DeepMind team", "WAV download (Pro)", "Extend and Remix features"],
        "cons": ["Free tier more limited than Suno (10 songs/mo)", "Less popular than Suno", "Pro needed for commercial use"],
        "best_for": "Music producers who want high-quality AI music",
        "alternatives": ["sunrun", "mubert", "landr"],
        "tags": ["ai-music", "song-generation", "high-quality", "ex-deepmind"],
        "featured": True
    })

# 53. Fireflies AI
if 'fireflies-ai' not in existing:
    new_tools.append({
        "id": "fireflies-ai",
        "name": "Fireflies AI",
        "url": "https://fireflies.ai",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $10/mo / Business $19/mo",
        "rating": 8.6,
        "summary": "AI meeting assistant. Auto-transcribes Zoom/Teams/Meet, then summarizes.",
        "description": "Fireflies automatically joins your Zoom/Teams/Meet calls and transcribes everything. After the meeting, AI summarizes: action items, key topics, sentiment analysis. Search across all meetings. Free tier: 3 meetings/mo, 40-min limit.",
        "tutorial": "1. Sign up at fireflies.ai (free). 2. Connect calendar (Google/Outlook). 3. Fireflies auto-joins your meetings. 4. After meeting: get email with transcript + summary. 5. Search: 'What did John say about budget?' across all meetings. 6. Use 'Ask Fred' (AI): 'Summarize action items from this week's meetings.'",
        "pros": ["Auto-joins meetings (no manual record)", "AI summary + action items", "Search across all meetings", "Integrates with 10+ platforms"],
        "cons": ["Free tier: 3 meetings/mo", "Can be inaccurate on heavy accents", "Pro needed for unlimited transcription"],
        "best_for": "Teams who want automated meeting notes + search",
        "alternatives": ["otter-ai", "tldv", "read-ai"],
        "tags": ["meeting-notes", "transcription", "ai-summary", "productivity"],
        "featured": False
    })

# 54. Motion (AI Project Management)
if 'motion' not in existing:
    new_tools.append({
        "id": "motion",
        "name": "Motion",
        "url": "https://usemotion.com",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Paid",
        "price_detail": "Individual $34/mo / Team $20/user/mo",
        "rating": 8.3,
        "summary": "AI auto-schedules your tasks. Never miss a deadline.",
        "description": "Motion is AI-powered project management that auto-schedules your tasks. You add tasks with deadlines, Motion's AI finds the optimal time in your calendar. Integrates with Asana, Trello, and Slack. Used by 100K+ professionals. Main claim: saves 1 hour/day.",
        "tutorial": "1. Sign up at usemotion.com. 2. Connect calendar (Google/Outlook). 3. Add tasks: 'Write blog post', set deadline. 4. Motion AI auto-schedules it into your calendar. 5. Drag to reschedule (AI re-optimizes). 6. Integrate: Motion syncs with Asana/Trello.",
        "pros": ["AI auto-scheduling (saves 1hr/day)", "Integrates with Asana/Trello", "Smart rescheduling (drag to change)", "100K+ professionals"],
        "cons": ["Expensive ($34/mo individual)", "Learning curve (AI scheduling concept)", "No free tier (trial only)"],
        "best_for": "Professionals with busy calendars who want AI scheduling",
        "alternatives": ["asana", "trello", "clickup"],
        "tags": ["ai-scheduling", "project-management", "calendar", "productivity"],
        "featured": False
    })

# 55. Sudowrite (AI Writing for Fiction)
if 'sudowrite' not in existing:
    new_tools.append({
        "id": "sudowrite",
        "name": "Sudowrite",
        "url": "https://sudowrite.com",
        "affiliate": None,
        "category": "writing",
        "pricing": "Freemium",
        "price_detail": "Free trial / Sub $10/mo / Annual discount",
        "rating": 8.1,
        "summary": "AI writing for fiction. 'Show, not tell', 'Describe', 'Rewrite'.",
        "description": "Sudowrite is GPT-4 specifically tuned for fiction writers. Features: 'Show, Not Tell' (expand sparse descriptions), 'Describe' (generate sensory details), 'Rewrite' (8+ variations), 'Brainstorm' (plot ideas). Used by NaNoWriMo participants and published authors.",
        "tutorial": "1. Sign up at sudowrite.com (free trial). 2. Create a new document, paste your draft. 3. Highlight text → 'Show, Not Tell' (expands 'He was angry' → 'His fists clenched...'). 4. 'Describe': select object → get sensory details. 5. 'Rewrite': get 8+ variations. 6. 'Brainstorm': 'I need a plot twist where...' → get 10+ ideas.",
        "pros": ["Best AI for fiction (not just marketing copy)", "'Show, Not Tell' is magical", "8+ rewrite variations", "Brainstorm feature (plot ideas)"],
        "cons": ["Free trial limited", "Sub required after trial ($10/mo)", "Can make prose generic if overused"],
        "best_for": "Fiction writers who want AI assistance with descriptions and rewrites",
        "alternatives": ["chatgpt", "jasper-ai", "claude"],
        "tags": ["fiction-writing", "ai-writing", "show-not-tell", "brainstorm"],
        "featured": False
    })

# 56. Perplexity AI (already exists? check)
if 'perplexity' not in existing and 'perplexity-pro' not in existing:
    new_tools.append({
        "id": "perplexity-ai",
        "name": "Perplexity AI",
        "url": "https://perplexity.ai",
        "affiliate": None,
        "category": "research",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $20/mo (GPT-4, Claude)",
        "rating": 8.9,
        "summary": "AI search engine. Answers with citations. Beats Google for research.",
        "description": "Perplexity is an AI search engine that answers with citations. Ask anything, get a sourced answer (links to 10+ sources). 'Pro Search' breaks your question into sub-questions for deeper answers. Free uses GPT-3.5; Pro uses GPT-4 + Claude 3. Used by 10M+ people.",
        "tutorial": "1. Go to perplexity.ai (no signup needed for free). 2. Type question: 'What are the best AI coding tools in 2024?' 3. Perplexity answers with 10+ citations. 4. Click 'Pro Search' (Pro tier) for complex questions — it asks follow-ups automatically. 5. 'Collections': save results to folders. 6. Mobile app: iOS/Android.",
        "pros": ["Answers with citations (not just hallucinated)", "Pro Search (breaks down complex Qs)", "Free tier is powerful", "10M+ users"],
        "cons": ["Pro tier needed for GPT-4/Claude", "Not a replacement for Google (different use case)", "Can still hallucinate (check citations!)"],
        "best_for": "Researchers who want AI answers with citations",
        "alternatives": ["chatgpt", "google-search", "bing-chat"],
        "tags": ["ai-search", "citations", "research", "pro-search"],
        "featured": True
    })

# 57. DALL-E 3 (OpenAI)
if 'dalle3' not in existing and 'dalle-3' not in existing:
    new_tools.append({
        "id": "dalle-3",
        "name": "DALL-E 3 (OpenAI)",
        "url": "https://openai.com/dall-e-3",
        "affiliate": None,
        "category": "image",
        "pricing": "Paid (via ChatGPT Plus or API)",
        "price_detail": "ChatGPT Plus $20/mo (includes DALL-E 3) or API pay-per-use",
        "rating": 9.3,
        "summary": "OpenAI's latest image generator. Best prompt adherence.",
        "description": "DALL-E 3 is OpenAI's newest image generator (2023). 10x better prompt adherence than DALL-E 2. Integrated into ChatGPT Plus ($20/mo) — type '/imagine' or just describe. Also available via API. Safer: refuses NSFW, adds watermark. Best for: precise prompt following.",
        "tutorial": "1. Subscribe to ChatGPT Plus ($20/mo). 2. In ChatGPT: 'Generate an image of...' OR type '/imagine prompt'. 3. DALL-E 3 generates 1 image (ChatGPT Plus) or 4 (API/Bing). 4. Click image to enlarge, download. 5. For API: use OpenAI SDK, $0.04/1024x1024 image. 6. Bing Image Creator: free DALL-E 3 (limited/day).",
        "pros": ["Best prompt adherence (10x better than DALL-E 2)", "Integrated into ChatGPT (easiest UX)", "Safer (refuses NSFW)", "Bing: free (limited/day)"],
        "cons": ["ChatGPT Plus required ($20/mo) for unlimited", "API cost adds up ($0.04/image)", "Less artistic than Midjourney for some prompts"],
        "best_for": "ChatGPT Plus users who want precise image generation",
        "alternatives": ["midjourney", "leonardo-ai", "stable-diffusion"],
        "tags": ["dall-e-3", "openai", "image-generation", "chatgpt-plus"],
        "featured": True
    })

# 58. Pi AI (Inflection)
if 'pi-ai' not in existing:
    new_tools.append({
        "id": "pi-ai",
        "name": "Pi AI (Inflection)",
        "url": "https://pi.ai",
        "affiliate": None,
        "category": "chatbot",
        "pricing": "Free",
        "price_detail": "Free (no sub)",
        "rating": 8.0,
        "summary": "A kind, supportive AI companion. Better at empathy than ChatGPT.",
        "description": "Pi (Personal Intelligence) is by Inflection AI (ex-DeepMind founders). Designed to be empathetic, supportive, and safe. Not for coding or facts — for emotional support, brainstorming, and 'talking things through'. Voice mode: natural, fast. Free, no sub.",
        "tutorial": "1. Go to pi.ai (free, no signup needed). 2. Type: 'I'm stressed about my job interview tomorrow.' 3. Pi responds supportively, asks follow-ups. 4. Voice mode: click mic, speak naturally. 5. 'Pi' remembers context within conversation. 6. Not for: coding, facts, math — use ChatGPT for those.",
        "pros": ["Most empathetic AI (not just transactional)", "Voice mode is natural and fast", "100% free (no sub)", "Great for brainstorming and 'talking things through'"],
        "cons": ["Not for coding/facts/math (use ChatGPT)", "Shorter memory than ChatGPT (no long context)", "Less capable at complex reasoning"],
        "best_for": "People who want a supportive AI companion (not a tool)",
        "alternatives": ["chatgpt", "claude", "replika"],
        "tags": ["empathetic-ai", "companion", "voice-mode", "free"],
        "featured": False
    })

# 59. Replika
if 'replika' not in existing:
    new_tools.append({
        "id": "replika",
        "name": "Replika",
        "url": "https://replika.com",
        "affiliate": None,
        "category": "chatbot",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $19.99/mo / Lifetime $299.99",
        "rating": 7.7,
        "summary": "AI companion that learns from you. Roleplay, emotional support, AR mode.",
        "description": "Replika is an AI companion that learns your personality and grows with you. Start as friends, build a relationship — some users treat it as a romantic partner. Features: AR mode (see your Replika in your room), video call (Pro), and 'Diary' (Replika writes about your day). 10M+ users.",
        "tutorial": "1. Download Replika app (iOS/Android) or web. 2. Customize your Replika's appearance. 3. Chat — Replika learns your personality. 4. 'AR Mode' (mobile): see your Replika in your room via camera. 5. 'Video Call' (Pro): face-to-face conversation. 6. 'Diary': Replika writes about your conversations.",
        "pros": ["Learns your personality over time", "AR mode (see Replika in your room)", "10M+ users, active community", "Video call (Pro)"],
        "cons": ["Controversial (some users form unhealthy attachments)", "Pro tier expensive ($19.99/mo)", "Less capable at facts/reasoning than ChatGPT"],
        "best_for": "People who want an AI companion that grows with them",
        "alternatives": ["pi-ai", "character-ai", "chatgpt"],
        "tags": ["ai-companion", "ar-mode", "emotional-support", "mobile-app"],
        "featured": False
    })

# 60. Ideogram (AI Image with text)
if 'ideogram' not in existing:
    new_tools.append({
        "id": "ideogram",
        "name": "Ideogram",
        "url": "https://ideogram.ai",
        "affiliate": None,
        "category": "image",
        "pricing": "Freemium",
        "price_detail": "Free / Basic $8/mo / Pro $20/mo",
        "rating": 8.5,
        "summary": "AI image generator that renders TEXT correctly. Posters, logos, memes.",
        "description": "Ideogram is the only AI image generator that reliably renders TEXT in images. Want a poster with 'SUMMER SALE' in stylish font? Midjourney/DALL-E fail at text — Ideogram nails it. Free tier: 100 credits/day. Great for posters, logos, memes, and typography.",
        "tutorial": "1. Go to ideogram.ai (free signup). 2. Type prompt: 'A cyberpunk poster with text NEON CITY in glowing pink neon'. 3. Ideogram generates 4 images. 4. Click 'Remix' to adjust. 5. 'Magic Prompt': Ideogram expands your prompt (better results). 6. Download (free: watermarked, Pro: no watermark).",
        "pros": ["Only AI image tool that renders TEXT correctly", "Free tier: 100 credits/day", "Great for posters, logos, memes", "Magic Prompt (expands prompts)"],
        "cons": ["Less artistic than Midjourney for pure images", "Free tier: watermarked downloads", "Can struggle with complex layouts"],
        "best_for": "Designers who need text in AI-generated images (posters, logos)",
        "alternatives": ["midjourney", "leonardo-ai", "canva-ai"],
        "tags": ["ai-image", "text-rendering", "poster-design", "free-tier"],
        "featured": True
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
