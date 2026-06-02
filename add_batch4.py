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

# 31. Luma Dream Machine — already exists as luma-dream-machine, intentionally skipped

# 32. CapCut AI
if 'capcut-ai' not in existing:
    new_tools.append({
        "id": "capcut-ai",
        "name": "CapCut AI",
        "url": "https://capcut.com",
        "affiliate": None,
        "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $7.99/mo",
        "rating": 8.3,
        "summary": "TikTok's official video editor. AI features: auto-captions, background remover, magic resize.",
        "description": "CapCut is ByteDance's (TikTok's parent) free video editor, packed with AI features. Auto-captions (99% accuracy), background remover, magic resize (for TikTok/Reels/Shorts), and AI-powered effects. The desktop version is even more powerful.",
        "tutorial": "1. Download CapCut (mobile or desktop). 2. Import your video. 3. Click 'Auto-captions' — gets 99% accuracy in seconds. 4. Try 'Magic Resize' to convert 16:9 to 9:16 for TikTok. 5. Use 'Background Remover' (free, 5 credits/day). 6. Export: 4K, no watermark (free).",
        "pros": ["Free, no watermark", "Best auto-captions (99% accuracy)", "Magic Resize for social media", "TikTok integration"],
        "cons": ["Less powerful than Premiere", "Some AI features are Pro-only", "Mobile version is limited"],
        "best_for": "TikTok/Reels/Shorts creators who want free, fast video editing",
        "alternatives": ["descript", "wondershare-filmora", "adobe-premiere"],
        "tags": ["video-editing", "ai-captions", "tiktok", "free"],
        "featured": True
    })

# 33. Descript
if 'descript' not in existing:
    new_tools.append({
        "id": "descript",
        "name": "Descript",
        "url": "https://descript.com",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free / Creator $12/mo / Pro $24/mo",
        "rating": 8.7,
        "summary": "Edit video/audio by editing text. Like Google Docs for media.",
        "description": "Descript lets you edit video and audio by editing text — like Google Docs for media. Delete a word in the transcript, and it's gone from the audio. Overdub creates an AI clone of your voice. Studio Sound removes background noise magically. Used by podcasters, video creators, and product teams.",
        "tutorial": "1. Download Descript (Mac/Windows). 2. Create a new project, drag in your video/audio. 3. Wait for transcription. 4. Edit the text — deleting words deletes them from audio. 5. Use 'Studio Sound' to remove noise. 6. Try 'Overdub' (Pro): type text, it speaks in your voice.",
        "pros": ["Edit audio/video by editing text", "Studio Sound (noise removal) is magic", "Overdub (AI voice clone)", "Great for podcasts"],
        "cons": ["Learning curve for non-editors", "Pro tier needed for best features", "Can be slow on large files"],
        "best_for": "Podcasters and video creators who hate timeline editing",
        "alternatives": ["capcut-ai", "adobe-audition", "garageband"],
        "tags": ["video-editing", "audio-editing", "ai-transcription", "overdub"],
        "featured": True
    })

# 34. WonderShare Filmora
if 'wondershare-filmora' not in existing:
    new_tools.append({
        "id": "wondershare-filmora",
        "name": "WonderShare Filmora",
        "url": "https://filmora.wondershare.com",
        "affiliate": None,
        "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free (watermark) / Sub $49.99/yr",
        "rating": 7.9,
        "summary": "Easy video editing with AI features. Great for beginners.",
        "description": "Filmora is a beginner-friendly video editor with AI features: auto-reframe, AI portrait (background removal), speed ramping, and 1000+ effects. Less complex than Premiere but more powerful than CapCut desktop. Great for YouTube, TikTok, and family videos.",
        "tutorial": "1. Download Filmora (Windows/Mac). 2. Start a new project, import media. 3. Drag clips to timeline. 4. Try AI features: right-click clip → 'AI Portrait' (removes background). 5. Add effects: Effects tab → drag to timeline. 6. Export: 4K, no watermark with paid plan.",
        "pros": ["Beginner-friendly", "AI features (portrait, reframe)", "1000+ effects/templates", "One-time purchase available"],
        "cons": ["Watermark on free export", "Less powerful than Premiere/DaVinci", "Some effects feel cheesy"],
        "best_for": "Beginners who want easy video editing with AI features",
        "alternatives": ["capcut-ai", "descript", "davinci-resolve"],
        "tags": ["video-editing", "beginner-friendly", "ai-effects", "freemium"],
        "featured": False
    })

# 35. Mubert
if 'mubert' not in existing:
    new_tools.append({
        "id": "mubert",
        "name": "Mubert",
        "url": "https://mubert.com",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $14/mo / Business custom",
        "rating": 8.1,
        "summary": "AI-generated music that's royalty-free. Streams, videos, podcasts.",
        "description": "Mubert generates royalty-free AI music in real-time. Pick a genre (Lo-Fi, Electronic, Ambient, etc.), set duration, and Mubert creates a unique track. Great for YouTube videos, podcasts, Twitch streams, and games. 100% royalty-free — no copyright strikes.",
        "tutorial": "1. Go to mubert.com, sign up (free). 2. Click 'Generate Track'. 3. Pick genre, mood, duration. 4. Click 'Generate' — wait 10-30 seconds. 5. Preview, then download (free: MP3 320kbps, Pro: WAV). 6. For continuous music: use Mubert API (Pro) for live streams.",
        "pros": ["Royalty-free AI music", "Real-time generation", "API for developers", "Great for content creators"],
        "cons": ["Free tier has limits (10 tracks/mo)", "Not for professional music production", "Can sound repetitive"],
        "best_for": "Content creators who need royalty-free background music",
        "alternatives": ["suno", "udio", "epidemic-sound"],
        "tags": ["ai-music", "royalty-free", "streaming", "content-creation"],
        "featured": False
    })

# 36. Boomy
if 'boomy' not in existing:
    new_tools.append({
        "id": "boomy",
        "name": "Boomy",
        "url": "https://boomy.com",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free / Sub $9.99/mo",
        "rating": 7.5,
        "summary": "AI music creation for non-musicians. Create songs, distribute to Spotify.",
        "description": "Boomy lets anyone create original songs in seconds — no musical experience needed. Pick a style, click 'Create', and Boomy generates a full song. You can then distribute to Spotify, Apple Music, TikTok, and earn royalties. Great for non-musicians who want to release music.",
        "tutorial": "1. Sign up at boomy.com (free). 2. Click 'New Song', pick a style (Lo-Fi, Trap, Pop, etc.). 3. Click 'Create' — Boomy generates a song in 30 seconds. 4. Edit: adjust instruments, tempo, melody. 5. Save and release: distribute to Spotify/Apple (Pro tier). 6. Earn royalties when people stream your songs.",
        "pros": ["Create songs in 30 seconds", "Distribute to Spotify/Apple", "Earn royalties", "Great for non-musicians"],
        "cons": ["Song quality is hit-or-miss", "Free tier very limited", "Competition is fierce (millions of Boomy songs on Spotify)"],
        "best_for": "Non-musicians who want to release music to streaming platforms",
        "alternatives": ["suno", "mubert", "landr"],
        "tags": ["ai-music", "music-distribution", "non-musician", "royalty"],
        "featured": False
    })

# 37. LANDR
if 'landr' not in existing:
    new_tools.append({
        "id": "landr",
        "name": "LANDR",
        "url": "https://landr.com",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $19.99/mo / Studio $99.99/mo",
        "rating": 8.4,
        "summary": "AI mastering for music. Studio-quality results in minutes, not hours.",
        "description": "LANDR is AI-powered music mastering. Upload your raw mix, and LANDR analyzes it and applies professional mastering — EQ, compression, stereo widening, and loudness optimization. Used by 2M+ musicians. Also offers AI mixing, samples, and distribution to Spotify.",
        "tutorial": "1. Sign up at landr.com (free). 2. Upload your track (WAV/MP3, up to 1GB). 3. Choose a mastering style: Warm, Balanced, or Open. 4. LANDR processes in 2-5 minutes. 5. Preview: compare before/after. 6. Download (free: MP3, Pro: WAV). 7. For distribution: LANDR distributes to Spotify/Apple (Pro tier).",
        "pros": ["Studio-quality AI mastering", "Fast (2-5 minutes)", "Distribution to Spotify/Apple", "Used by 2M+ musicians"],
        "cons": ["Not as good as human mastering for complex tracks", "Pro tier needed for WAV", "Distribution is competitive (many artists)"],
        "best_for": "Musicians who want affordable, fast mastering",
        "alternatives": ["boomy", "suno", "abelton-live"],
        "tags": ["ai-mastering", "music-production", "distribution", "pro-audio"],
        "featured": False
    })

# 38. Looka
if 'looka' not in existing:
    new_tools.append({
        "id": "looka",
        "name": "Looka",
        "url": "https://looka.com",
        "affiliate": None,
        "category": "design",
        "pricing": "Paid",
        "price_detail": "One-time $20-$80 (no subscription)",
        "rating": 8.2,
        "summary": "AI logo maker + brand kit. Professional logos in minutes.",
        "description": "Looka uses AI to generate professional logos in minutes. Enter your company name, pick colors/styles, and Looka generates 100+ logo options. Unlike subscription-only tools, Looka offers one-time purchases ($20 for PNG, $65 for full brand kit). Also generates business cards, social media kits, and brand guidelines.",
        "tutorial": "1. Go to looka.com, enter company name. 2. Pick 3-5 colors and 3-5 symbols. 3. Looka generates 100+ logos — pick one. 4. Customize: change font, color, layout. 5. Purchase: $20 for PNG (no bg), $65 for full brand kit (SVG, EPS, social media templates). 6. Download instantly.",
        "pros": ["Professional logos in minutes", "One-time purchase (no subscription)", "Full brand kit included", "No design skills needed"],
        "cons": ["Less customizable than hiring a designer", "Logos can look similar to others", "No free download (must pay)"],
        "best_for": "Small businesses and startups who need a professional logo fast and cheap",
        "alternatives": ["brandmark", "namelix", "canva-ai"],
        "tags": ["logo-maker", "branding", "ai-design", "one-time-purchase"],
        "featured": False
    })

# 39. Brandmark
if 'brandmark' not in existing:
    new_tools.append({
        "id": "brandmark",
        "name": "Brandmark",
        "url": "https://brandmark.io",
        "affiliate": None,
        "category": "design",
        "pricing": "Freemium",
        "price_detail": "Free (low-res) / Pro $25-$175",
        "rating": 7.8,
        "summary": "AI logo + brand design. Higher-res outputs than Looka (free preview).",
        "description": "Brandmark is an AI logo generator that also creates full brand packages — business cards, social media banners, favicons, and brand guidelines. The free tier lets you preview (watermarked), and Pro tiers give high-res SVG/EPS. Good alternative to Looka with more customization.",
        "tutorial": "1. Go to brandmark.io, enter company name. 2. Pick colors and 3+ keywords (e.g., 'modern', 'bold'). 3. Brandmark generates logos — click to customize. 4. customize: change font, icon, layout. 5. Free: preview only (watermarked). 6. Pro: $25 for high-res PNG, $175 for full brand kit (SVG, EPS, business cards, social media).",
        "pros": ["Full brand kit (not just logo)", "More customization than Looka", "Free preview (watermarked)", "Good for experimentation"],
        "cons": ["Free tier is low-res (preview only)", "Less known than Looka", "Some logos look generic"],
        "best_for": "Startups who want to experiment with logo ideas before buying",
        "alternatives": ["looka", "namelix", "canva-ai"],
        "tags": ["logo-maker", "branding", "ai-design", "freemium"],
        "featured": False
    })

# 40. Namelix
if 'namelix' not in existing:
    new_tools.append({
        "id": "namelix",
        "name": "Namelix",
        "url": "https://namelix.com",
        "affiliate": None,
        "category": "design",
        "pricing": "Free",
        "price_detail": "Free (open-source)",
        "rating": 7.6,
        "summary": "AI business name generator. Get 100+ name ideas with matching domains.",
        "description": "Namelix generates business name ideas using AI. Enter keywords (e.g., 'coffee shop', 'tech startup'), and Namelix suggests 100+ names with matching .com domains (via Namecheap integration). Also generates logo concepts. 100% free and open-source.",
        "tutorial": "1. Go to namelix.com. 2. Enter keywords (e.g., 'sustainable fashion'). 3. Pick name style: Brandable, Compound, Misspelled, etc. 4. Namelix shows 100+ names with available .com domains. 5. Click a name to see logo options. 6. Register domain via Namecheap (integrated).",
        "pros": ["100% free", "Shows available .com domains", "Generates logo concepts", "Open-source"],
        "cons": ["Domain prices not included (must pay Namecheap)", "Some names feel generic", "No trademark check"],
        "best_for": "Entrepreneurs brainstorming business names",
        "alternatives": ["looka", "brandmark", "shopify-business-name-generator"],
        "tags": ["business-name", "domain-search", "free", "branding"],
        "featured": False
    })

print(f"\nAdding {len(new_tools)} more tools...")
data['tools'].extend(new_tools)

# Write back
new_json = json.dumps(data, indent=2, ensure_ascii=False)
new_json = new_json.replace('  ', '    ')

new_content = f"// Auto-generated from tools.json -- embedded for file:// compatibility\nwindow.__TOOLS_DATA__ = {new_json};\n"

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Done! Total tools: {len(data['tools'])}")
