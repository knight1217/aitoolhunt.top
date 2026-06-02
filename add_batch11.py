import re, json
from collections import Counter

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

# 91. CodeT5+ (AI Coding - open source)
if 'codet5' not in existing:
    new_tools.append({
        "id": "codet5",
        "name": "CodeT5+ (Salesforce)",
        "url": "https://github.com/salesforce/CodeT5",
        "affiliate": None,
        "category": "coding",
        "pricing": "Free",
        "price_detail": "Open-source (free)",
        "rating": 8.1,
        "summary": "Open-source code LLM by Salesforce. 220M-16B params.",
        "description": "CodeT5+ is Salesforce's open-source code LLM. 220M to 16B parameters. Supports code completion, summarization, translation (Java→Python, etc.). Completely free, self-host or API. Competes with Codex/CodeLlama.",
        "tutorial": "1. Go to github.com/salesforce/CodeT5. 2. 'pip install transformers' (Hugging Face). 3. Load model: 'Salesforce/codet5p-16b'. 4. Use: code completion, translation. 5. 'CodeT5+ Playground': Hugging Face Spaces (free, no install). 6. Fine-tune on your codebase (advanced).",
        "pros": ["Open-source (free)", "Code translation (Java→Python, etc.)", "Multiple sizes (220M-16B)", "Salesforce research (trusted)"],
        "cons": ["Requires GPU for self-hosting (16B model)", "Less capable than GPT-4/Claude for complex tasks", "No managed API (self-host or Hugging Face)"],
        "best_for": "Developers who want open-source code LLM (free alternative to GitHub Copilot)",
        "alternatives": ["codellama", "starcoder", "github-copilot"],
        "tags": ["open-source", "code-llm", "salesforce", "free"],
        "featured": False
    })

# 92. StarCoder (Hugging Face + BigCode)
if 'starcoder' not in existing:
    new_tools.append({
        "id": "starcoder",
        "name": "StarCoder (BigCode)",
        "url": "https://huggingface.co/bigcode/starcoder",
        "affiliate": None,
        "category": "coding",
        "pricing": "Free",
        "price_detail": "Open-source (free)",
        "rating": 8.3,
        "summary": "15B param code LLM. Trained on 80+ languages. Open-source.",
        "description": "StarCoder is a 15B parameter LLM trained on 80+ programming languages. By BigCode (Hugging Face + Intel). Completely open-source. Use via Hugging Face Inference API (free tier) or self-host. Competes with Codex/GitHub Copilot.",
        "tutorial": "1. Go to huggingface.co/bigcode/starcoder. 2. 'Use in Inference API' (free tier, rate-limited). 3. Or 'pip install transformers' → load locally (needs GPU). 4. 'StarCoder Playground': Hugging Face Spaces (free). 5. Fine-tune: use your codebase (advanced). 6. 'StarCoder2' (16B, newer): huggingface.co/bigcode/starcoder2-15b.",
        "pros": ["15B params (powerful for open-source)", "80+ programming languages", "Completely free (open-source)", "Hugging Face Inference API (no install)"],
        "cons": ["Needs GPU for self-hosting (15B model)", "Less capable than GPT-4/Claude for complex reasoning", "Inference API has rate limits (free tier)"],
        "best_for": "Developers who want free, open-source code LLM (alternative to GitHub Copilot)",
        "alternatives": ["codellama", "codet5", "github-copilot"],
        "tags": ["open-source", "code-llm", "huggingface", "free"],
        "featured": False
    })

# 93. AIVA (AI Music Composition)
if 'aiva' not in existing:
    new_tools.append({
        "id": "aiva",
        "name": "AIVA",
        "url": "https://www.aiva.ai",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free / Standard €14.99/mo / Pro €49.99/mo",
        "rating": 7.7,
        "summary": "AI music composer. Create soundtracks for videos, games, podcasts.",
        "description": "AIVA composes original music using AI. Choose genre (epic, jazz, pop, etc.), mood, length. Free: download MP3 (non-commercial). Paid: WAV + commercial license. Used by 1M+ creators.",
        "tutorial": "1. Sign up at aiva.ai (free). 2. 'Create Track': pick genre, mood, length. 3. AIVA generates 3 variations. 4. Edit: change instruments, tempo, structure. 5. Download: MP3 (free, non-commercial) or WAV (Pro, commercial license). 6. 'Upload Influence Track': influence AIVA's style (Pro).",
        "pros": ["Original compositions (not samples)", "Free tier (MP3, non-commercial)", "Edit instruments, tempo, structure", "1M+ creators"],
        "cons": ["Free = non-commercial (no license)", "Less control than manual composition", "Can sound 'AI-generated' (uncanny for some genres)"],
        "best_for": "Content creators who need original background music (podcasts, videos, games)",
        "alternatives": ["mubert", "boomy", "soundraw"],
        "tags": ["ai-music", "composition", "soundtrack", "commercial-license"],
        "featured": False
    })

# 94. Soundraw (AI Music Generator)
if 'soundraw' not in existing:
    new_tools.append({
        "id": "soundraw",
        "name": "Soundraw",
        "url": "https://soundraw.io",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free (limited) / Pro $29.99/mo (commercial license)",
        "rating": 8.0,
        "summary": "AI music generator with fine-grained control. Commercial license included.",
        "description": "Soundraw generates AI music with more control than AIVA/Mubert. Pick genre, mood, length, tempo, instruments. Edit: rearrange sections, change melody. Pro: unlimited downloads + commercial license. Used by 500K+ creators.",
        "tutorial": "1. Sign up at soundraw.io (free trial). 2. 'Create Music': genre, mood, length, tempo. 3. Soundraw generates 15+ tracks. 4. 'Edit': rearrange sections, change melody, swap instruments. 5. Download: MP3 (free: watermarked) or WAV (Pro: commercial license). 6. 'Playlist': create full album (Pro).",
        "pros": ["More control than AIVA/Mubert (edit sections, melody)", "Commercial license included (Pro)", "500K+ creators", "No copyright issues (original compositions)"],
        "cons": ["Free = watermarked (not usable)", "Pro is expensive ($29.99/mo)", "Still 'AI-generated' sound (not human composer)"],
        "best_for": "Content creators who want customizable AI music with commercial license",
        "alternatives": ["aiva", "mubert", "boomy"],
        "tags": ["ai-music", "commercial-license", "customizable", "soundtrack"],
        "featured": False
    })

# 95. Mem (AI Note-Taking)
if 'mem' not in existing:
    new_tools.append({
        "id": "mem",
        "name": "Mem",
        "url": "https://www.mem.ai",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free / Mem Prime $14.99/mo",
        "rating": 8.2,
        "summary": "AI note-taking. Auto-links related notes. Chat with your notes.",
        "description": "Mem is AI-powered note-taking. Auto-links related notes (like Obsidian but automatic). 'Mem Chat': ask questions across all notes. 'Smart Merge': combines duplicate notes. Free: unlimited notes. Prime: AI features + collaboration.",
        "tutorial": "1. Sign up at mem.ai (free). 2. 'Create Mem': write note (like Google Keep). 3. Mem auto-links related notes (no manual tagging). 4. 'Mem Chat': ask 'What did I write about AI tools?' — searches all notes. 5. 'Smart Merge': Mem suggests merging duplicate notes. 6. Prime ($14.99/mo): AI summarization, collaboration.",
        "pros": ["Auto-links related notes (no manual tagging)", "Mem Chat (search across all notes)", "Free: unlimited notes", "Smart Merge (reduces duplicates)"],
        "cons": ["Prime needed for AI features ($14.99/mo)", "Less features than Notion/Obsidian (pure note-taking)", "Can feel 'magical' but sometimes links unrelated notes"],
        "best_for": "People who take lots of notes and want AI to auto-organize them",
        "alternatives": ["notion-ai", "obsidian", "roam-research"],
        "tags": ["ai-notes", "auto-linking", "chat-with-notes", "productivity"],
        "featured": False
    })

# 96. Rewind (AI Personal Search)
if 'rewind' not in existing:
    new_tools.append({
        "id": "rewind",
        "name": "Rewind",
        "url": "https://www.rewind.ai",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free (limited) / Pro $29/mo",
        "rating": 8.5,
        "summary": "Records everything you see/type. AI search across your history.",
        "description": "Rewind records your screen, microphone, camera (opt-in). 'Ask Rewind': 'What did John say in our Zoom call?' — Rewind finds it. Mac only (for now). Free: 50 recordings/mo. Pro: unlimited + AI chat.",
        "tutorial": "1. Download Rewind (Mac only). 2. Grant permissions (screen recording, microphone). 3. Rewind records everything (you can pause). 4. 'Ask Rewind': 'Find the spreadsheet John sent' — Rewind searches OCR + audio transcript. 5. 'Rewind Chat': chat with your history ('Summarize my day'). 6. Privacy: all data stored locally (not in cloud).",
        "pros": ["Records everything (never lose info again)", "Ask Rewind (AI search across history)", "Data stored locally (privacy)", "Mac only (optimized for Apple Silicon)"],
        "cons": ["Mac only (no Windows/Linux)", "Pro is expensive ($29/mo)", "Can feel surveillance-heavy (records everything)"],
        "best_for": "Mac users who want 'total recall' of everything they've seen/typed",
        "alternatives": ["mem", "notion-ai", "obsidian"],
        "tags": ["ai-search", "screen-recording", "productivity", "mac-only"],
        "featured": False
    })

# 97. Reclaim.ai (AI Calendar Assistant)
if 'reclaim-ai' not in existing:
    new_tools.append({
        "id": "reclaim-ai",
        "name": "Reclaim.ai",
        "url": "https://reclaim.ai",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free (limited) / Premium $8/mo / Business $12/mo",
        "rating": 8.4,
        "summary": "AI calendar assistant. Auto-schedules tasks, meetings, habits.",
        "description": "Reclaim.ai connects to Google Calendar. 'Tasks': auto-schedule deadlines. 'Habits': auto-schedule gym, deep work, etc. 'Meeting Scheduling': auto-finds mutual free time. Free: 1 calendar, 10 tasks/mo. Premium: unlimited.",
        "tutorial": "1. Sign up at reclaim.ai (free). 2. Connect Google Calendar. 3. 'Add Task': 'Write blog post', deadline Friday. Reclaim auto-schedules it. 4. 'Add Habit': 'Gym', 3x/week, 1 hour. Reclaim auto-blocks time. 5. 'Scheduling Link': share with others to book meetings (auto-finds mutual free time). 6. 'Analytics': see how you spend time.",
        "pros": ["Auto-schedules tasks + habits (no manual time-blocking)", "Scheduling Links (like Calendly but smarter)", "Free tier (1 calendar, 10 tasks/mo)", "Google Calendar integration (seamless)"],
        "cons": ["Google Calendar only (no Outlook)", "Free tier limited (10 tasks/mo)", "Can feel 'rigid' if you prefer flexible scheduling"],
        "best_for": "People who want AI to auto-manage their calendar (tasks, habits, meetings)",
        "alternatives": ["calendly", "motion", "clockwise"],
        "tags": ["ai-calendar", "scheduling", "habits", "google-calendar"],
        "featured": False
    })

# 98. Clockwise (AI Calendar Optimizer)
if 'clockwise' not in existing:
    new_tools.append({
        "id": "clockwise",
        "name": "Clockwise",
        "url": "https://www.clockwise.com",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free / Premium $12/user/mo / Enterprise custom",
        "rating": 7.9,
        "summary": "AI calendar optimizer. Creates 'Focus Time' by rearranging meetings.",
        "description": "Clockwise optimizes your Google Calendar. 'Focus Time': auto-creates 2-hour blocks for deep work. 'Meeting Compression': shortens meetings to create buffer time. 'Smart Meeting Scheduling': finds optimal time for all attendees. Free: 1 calendar. Premium: teams.",
        "tutorial": "1. Sign up at clockwise.com (free). 2. Connect Google Calendar. 3. 'Focus Time': set preference (e.g., '2 hours daily, mornings'). Clockwise auto-creates blocks. 4. 'Meeting Compression': Clockwise shortens 1-hour meetings to 45 min (auto-adjusts attendees' calendars). 5. 'Analytics': see 'Focus Score' (how much deep work time you have). 6. Premium: team features (sync focus time across team).",
        "pros": ["Creates 'Focus Time' automatically (deep work blocks)", "Meeting Compression (creates buffer time)", "Free tier (1 calendar)", "Google Calendar integration"],
        "cons": ["Google Calendar only (no Outlook)", "Can feel aggressive (moves meetings around)", "Premium needed for teams"],
        "best_for": "People who want AI to optimize their calendar for deep work (focus time)",
        "alternatives": ["reclaim-ai", "motion", "calendly"],
        "tags": ["ai-calendar", "focus-time", "meeting-optimization", "productivity"],
        "featured": False
    })

# 99. HubSpot AI (CRM + Marketing AI)
if 'hubspot-ai' not in existing:
    new_tools.append({
        "id": "hubspot-ai",
        "name": "HubSpot AI",
        "url": "https://www.hubspot.com/ai",
        "affiliate": None,
        "category": "marketing",
        "pricing": "Freemium",
        "price_detail": "Free (in HubSpot CRM) / Premium features in paid plans",
        "rating": 8.3,
        "summary": "AI for CRM, marketing, sales. Content generation, lead scoring, chatbots.",
        "description": "HubSpot AI is built into HubSpot CRM. 'Content Assistant': generates blog posts, emails, landing pages. 'ChatSpot': chat to manage CRM ( 'Show deals closing this month'). 'AI Lead Scoring': prioritizes hottest leads. Free in HubSpot CRM (paid plans unlock advanced features).",
        "tutorial": "1. Sign up at hubspot.com (free CRM). 2. 'Content Assistant': 'Generate blog post about AI tools' — HubSpot writes draft. 3. 'ChatSpot': 'Show me leads who visited pricing page 3x' — AI queries CRM. 4. 'AI Lead Scoring': HubSpot auto-scores leads (you prioritize follow-up). 5. 'AI Chatbot Builder': no-code, drag-and-drop. 6. Premium: $20/mo+ (advanced AI features).",
        "pros": ["Built into HubSpot CRM (free to start)", "Content Assistant (blog, emails, landing pages)", "ChatSpot (chat to manage CRM)", "AI Lead Scoring (prioritize hottest leads)"],
        "cons": ["Advanced AI features need paid plans ($20/mo+)", "Learning curve (HubSpot is full CRM, not just AI tool)", "Less capable than Jasper/Copy.ai for pure content generation"],
        "best_for": "Businesses already using HubSpot CRM who want AI features built-in",
        "alternatives": ["salesforce-einstein", "jasper-ai", "copy-ai"],
        "tags": ["crm", "marketing-ai", "lead-scoring", "content-assistant"],
        "featured": False
    })

# 100. Salesforce Einstein (AI CRM)
if 'salesforce-einstein' not in existing:
    new_tools.append({
        "id": "salesforce-einstein",
        "name": "Salesforce Einstein",
        "url": "https://www.salesforce.com/products/einstein/",
        "affiliate": None,
        "category": "marketing",
        "pricing": "Paid",
        "price_detail": "Included in Salesforce Enterprise ($150/user/mo+)",
        "rating": 8.1,
        "summary": "AI built into Salesforce CRM. Predicts outcomes, automates tasks, generates content.",
        "description": "Einstein is Salesforce's AI layer. 'Einstein GPT': generates emails, case summaries, product descriptions. 'Predictive AI': forecasts which leads will convert. 'Einstein Bots': AI chatbots for customer service. Included in Salesforce Enterprise ($150/user/mo+).",
        "tutorial": "1. Have Salesforce Enterprise (or higher). 2. 'Einstein GPT': 'Generate follow-up email to lead' — Einstein writes it. 3. 'Predictive AI': Einstein scores leads, forecasts pipeline. 4. 'Einstein Bots': build AI chatbots (no-code). 5. 'Einstein Activity Capture': auto-logs emails/meetings to CRM. 6. 'Tableau Einstein': AI insights in dashboards.",
        "pros": ["Built into Salesforce (no separate tool)", "Einstein GPT (content generation)", "Predictive AI (lead scoring, forecasting)", "Einstein Bots (AI chatbots)"],
        "cons": ["Expensive (Salesforce Enterprise $150/user/mo+)", "Learning curve (Salesforce is complex)", "Less capable than standalone AI tools (Jasper, Copy.ai) for pure content"],
        "best_for": "Enterprises already on Salesforce who want AI features built-in",
        "alternatives": ["hubspot-ai", "zoho-zia", "microsoft-viva-sales"],
        "tags": ["crm", "salesforce", "predictive-ai", "einstein-gpt"],
        "featured": False
    })

# 101. Stable Diffusion XL (SDXL)
if 'sdxl' not in existing:
    new_tools.append({
        "id": "sdxl",
        "name": "Stable Diffusion XL (SDXL)",
        "url": "https://stability.ai/stable-diffusion",
        "affiliate": None,
        "category": "image",
        "pricing": "Free",
        "price_detail": "Open-source (free) / API $18/1M tokens",
        "rating": 9.0,
        "summary": "Most advanced open-source image generator. 1024x1024, photorealistic.",
        "description": "SDXL is Stability AI's most advanced open-source image generator. 1024x1024 base resolution (up to 4K with upscaling). Photorealistic, artistic, anime — all styles. Completely open-source (download + run locally). API: $18/1M tokens (~1000 images).",
        "tutorial": "1. Go to stability.ai/stable-diffusion (download SDXL). 2. 'Local install': needs GPU (RTX 3060+). Use Automatic1111 web UI. 3. 'Online': DreamStudio (stability.ai/dreamstudio) — $18/1M tokens. 4. 'Prompt': 'Photorealistic portrait of...' — SDXL understands complex prompts. 5. 'Negative prompt': tell it what to avoid ('blurry, deformed'). 6. 'Upscale': 2x, 4x (get 4K images).",
        "pros": ["Open-source (free, download + run locally)", "1024x1024 base (up to 4K)", "Understands complex prompts", "API available ($18/1M tokens)"],
        "cons": ["Needs powerful GPU for local install (RTX 3060+)", "Can generate inappropriate content (no built-in filter)", "Less 'curated' than Midjourney (more manual tweaking)"],
        "best_for": "Artists/developers who want open-source, customizable image generation (not locked into Midjourney)",
        "alternatives": ["midjourney", "dalle-3", "leonardo-ai"],
        "tags": ["open-source", "image-generation", "stability-ai", "photorealistic"],
        "featured": True
    })

# 102. Ideogram v2 (AI Image with Text)
if 'ideogram' not in existing:
    new_tools.append({
        "id": "ideogram",
        "name": "Ideogram v2",
        "url": "https://ideogram.ai",
        "affiliate": None,
        "category": "image",
        "pricing": "Freemium",
        "price_detail": "Free (slow) / Basic $8/mo / Pro $20/mo",
        "rating": 8.7,
        "summary": "AI image generator that renders TEXT correctly. Logos, posters, memes.",
        "description": "Ideogram is the ONLY AI image generator that renders text correctly. 'Make a poster saying SALE 50% OFF' — Ideogram nails it. Midjourney/DALL-E struggle with text. Free: slow queue. Basic: $8/mo (faster). Used by 2M+ users.",
        "tutorial": "1. Sign up at ideogram.ai (free). 2. 'Text Prompt': 'A neon sign saying OPEN 24H' — Ideogram renders text perfectly. 3. 'Style': realistic, 3D, anime, watercolor. 4. 'Aspect Ratio': 1:1, 16:9, 9:16. 5. Free: slow queue (5 min). Basic ($8/mo): faster. 6. 'Remix': upload image → Ideogram modifies it (changes text, style).",
        "pros": ["ONLY tool that renders text correctly (unique)", "Logos, posters, memes (text-heavy images)", "Free tier (slow but usable)", "2M+ users"],
        "cons": ["Free = slow queue (5 min wait)", "Less photorealistic than Midjourney/SDXL", "Style control less fine-grained than Midjourney"],
        "best_for": "Designers who need AI images WITH TEXT (logos, posters, memes, social media graphics)",
        "alternatives": ["midjourney", "dalle-3", "leonardo-ai"],
        "tags": ["text-rendering", "image-generation", "logos", "posters"],
        "featured": True
    })

# 103. Photoroom (AI Product Photography)
if 'photoroom' not in existing:
    new_tools.append({
        "id": "photoroom",
        "name": "Photoroom",
        "url": "https://www.photoroom.com",
        "affiliate": None,
        "category": "design",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $12.99/mo / Team $29.99/mo",
        "rating": 8.6,
        "summary": "AI product photography. Remove background, add realistic shadows, change backdrop.",
        "description": "Photoroom is AI for product photography. 'Remove Background': one click. 'AI Shadows': adds realistic drop shadow. 'Backdrop Changer': replace white background with office, outdoors, etc. Used by 10M+ sellers (eBay, Etsy, Amazon). Free: watermarked. Pro: $12.99/mo.",
        "tutorial": "1. Sign up at photoroom.com (free). 2. Upload product photo. 3. 'Remove Background': one click (perfect cutout). 4. 'AI Shadows': adds realistic shadow (makes it look real, not Photoshopped). 5. 'Backdrop Changer': replace white background with 'Office', 'Outdoor', 'Studio', etc. 6. 'Batch Mode': process 50 products at once (Pro).",
        "pros": ["Remove background + AI shadows (looks real)", "Backdrop Changer (office, outdoor, etc.)", "Batch Mode (50 products at once)", "10M+ sellers (eBay, Etsy, Amazon)"],
        "cons": ["Free = watermarked (not usable for sales)", "Pro needed for high-res ($12.99/mo)", "Less control than manual Photoshop (but 10x faster)"],
        "best_for": "E-commerce sellers who need professional product photos (no Photoshop skills)",
        "alternatives": ["remove-bg", "canva-ai", "clipdrop"],
        "tags": ["product-photography", "background-removal", "ai-shadows", "ecommerce"],
        "featured": True
    })

# 104. Looka (AI Logo + Brand Kit)
if 'looka' not in existing:
    new_tools.append({
        "id": "looka",
        "name": "Looka",
        "url": "https://looka.com",
        "affiliate": None,
        "category": "design",
        "pricing": "Paid",
        "price_detail": "$20 (logo) / $65 (brand kit) / $195 (full package)",
        "rating": 8.0,
        "summary": "AI logo generator + full brand kit. Logo, business cards, social media templates.",
        "description": "Looka generates AI logos in seconds. Pick 5+ styles, colors, symbols. Get 100+ logo variations. '$20': high-res PNG. '$65': brand kit (logo + business card + social templates). '$195': full package (everything + vector files). Used by 20M+ businesses.",
        "tutorial": "1. Go to looka.com. 2. Enter company name + industry. 3. Pick 5+ styles, colors, symbols. 4. Looka generates 100+ logos. 5. Pick favorite → customize (font, color, layout). 6. '$20': high-res PNG. '$65': brand kit (business card, social templates). '$195': full package (vector files, unlimited revisions).",
        "pros": ["100+ logo variations in seconds", "Full brand kit ($65: logo + business card + social)", "$20 for basic logo (cheap)", "20M+ businesses"],
        "cons": ["Not unique (AI-generated, others may have similar logos)", "$20 = PNG only (no vector)", "Less control than human designer (but 100x cheaper)"],
        "best_for": "Small businesses who need a logo + brand kit FAST and CHEAP ($20 vs $500 for human)",
        "alternatives": ["brandmark", "namelix", "hatchful-shopify"],
        "tags": ["ai-logo", "brand-kit", "business-card", "cheap"],
        "featured": False
    })

# 105. Brandmark (AI Logo Generator)
if 'brandmark' not in existing:
    new_tools.append({
        "id": "brandmark",
        "name": "Brandmark",
        "url": "https://brandmark.io",
        "affiliate": None,
        "category": "design",
        "pricing": "Paid",
        "price_detail": "$25 (basic) / $65 (pro) / $175 (enterprise)",
        "rating": 7.8,
        "summary": "AI logo generator. More customization than Looka. Full brand kit.",
        "description": "Brandmark is like Looka but with more customization. Generate logo → customize colors, fonts, layouts. '$25': basic (low-res). '$65': pro (high-res + brand kit). '$175': enterprise (vector + unlimited revisions). Used by 10M+ businesses.",
        "tutorial": "1. Go to brandmark.io. 2. Enter company name + slogan (optional). 3. Pick colors, fonts, icons. 4. Brandmark generates 100+ logos. 5. Customize: change font, color, layout, icon position. 6. '$25': low-res PNG. '$65': high-res + brand kit. '$175': vector + unlimited revisions.",
        "pros": ["More customization than Looka (font, layout, icon position)", "Full brand kit ($65)", "$25 for basic (cheap)", "10M+ businesses"],
        "cons": ["Not unique (AI-generated)", "$25 = low-res (not usable for print)", "Less control than human designer"],
        "best_for": "Small businesses who want customizable AI logo (more options than Looka)",
        "alternatives": ["looka", "namelix", "hatchful-shopify"],
        "tags": ["ai-logo", "brand-kit", "customizable", "cheap"],
        "featured": False
    })

print(f"\nAdding {len(new_tools)} more tools...")

# Remove duplicates (double-check)
final_new = []
for t in new_tools:
    if t['id'] not in existing:
        final_new.append(t)
        existing.add(t['id'])

if len(final_new) < len(new_tools):
    print(f"Filtered {len(new_tools) - len(final_new)} duplicates")

data['tools'].extend(final_new)

# Write back
new_json = json.dumps(data, indent=2, ensure_ascii=False)
# Convert 2-space indent to 4-space to match original
new_json = new_json.replace('  ', '    ')

new_content = f"// Auto-generated from tools.json -- embedded for file:// compatibility\nwindow.__TOOLS_DATA__ = {new_json};\n"

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Done! Total tools: {len(data['tools'])}")
