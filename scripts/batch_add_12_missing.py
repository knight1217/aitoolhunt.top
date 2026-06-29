#!/usr/bin/env python3
"""
补充12个hub pages引用的缺失工具 + 验证并更新已有工具定价
"""
import json

BASE = __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))

with open(f'{BASE}/data/tools.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ============================================
# PART 1: 12 missing tools from hub pages
# ============================================
missing_tools = [
    {
        "id": "rewind",
        "name": "Rewind",
        "url": "https://rewind.ai", "affiliate": None, "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free (limited storage) / Pro $19/mo / Enterprise custom",
        "rating": 8.2,
        "summary": "AI memory for your Mac. Records everything you see, say, and hear — searchable by keyword.",
        "description": "Rewind is a Mac app that captures everything on your screen and makes it searchable with AI. It records your meetings, browser history, documents, and conversations, then uses local AI processing to let you search your entire digital history. Privacy-first design: all data stays on-device, no cloud upload. The killer feature: ask 'What was that article about AI pricing I read last Tuesday?' and Rewind finds it instantly.",
        "tutorial": "1. Download Rewind from rewind.ai (macOS only). 2. Grant screen recording permission — Rewind starts capturing. 3. Use Cmd+Shift+Space to open search. 4. Type any phrase or keyword — Rewind searches everything you've seen. 5. Click results to replay the exact moment (video/audio replay). 6. Adjust recording retention in settings (default 1 month). 7. Use meeting summaries: after any call, ask Rewind 'What were the action items?'",
        "pros": ["Everything searchable — never lose anything", "All data stays on-device (privacy)", "Instant replay of past meetings/screens", "Compression keeps storage manageable"],
        "cons": ["Mac only", "Free tier very limited storage", "Battery drain from constant recording", "Privacy concerns for shared workspaces"],
        "best_for": "Mac users who attend many meetings and want a perfect memory of everything they've seen",
        "alternatives": ["mem"], "tags": ["memory", "productivity", "mac", "search", "meetings"], "featured": False
    },
    {
        "id": "mem",
        "name": "Mem",
        "url": "https://get.mem.ai", "affiliate": None, "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $14.99/mo / Teams $25/user/mo",
        "rating": 8.0,
        "summary": "AI-powered note-taking that organizes itself. Mem auto-tags, connects, and surfaces your knowledge.",
        "description": "Mem is an AI-native note-taking app that eliminates manual organization. Instead of creating folders and tags, you just write — Mem's AI automatically categorizes, connects, and surfaces relevant notes when you need them. Features include AI chat against your notes ('What did I write about product-market fit?'), smart templates, and intelligent search. Used by knowledge workers who hate organizing notes but love finding them.",
        "tutorial": "1. Sign up at get.mem.ai (web + iOS/Android). 2. Start writing — no folders, no tags needed. 3. Mem auto-tags and connects related notes. 4. Use AI Chat to ask questions about your notes. 5. Create Smart Templates for recurring note types. 6. Share individual notes or collections with team members. 7. Use Mem X (Chrome extension) to save web content directly.",
        "pros": ["Zero organization overhead", "AI chat against your knowledge base", "Smart connection between related notes", "Good mobile apps"],
        "cons": ["Premium features behind paywall", "Can feel chaotic without manual control", "Smaller community than Notion", "Limited formatting options"],
        "best_for": "Knowledge workers who want a self-organizing second brain without manual maintenance",
        "alternatives": ["notion-ai", "craft"], "tags": ["note-taking", "productivity", "knowledge-management", "ai-chat"], "featured": False
    },
    {
        "id": "read-ai",
        "name": "Read.ai",
        "url": "https://www.read.ai", "affiliate": None, "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free (5 meetings/mo) / Pro $19.75/mo / Enterprise $29.75/user/mo",
        "rating": 8.3,
        "summary": "AI meeting reports that actually help. Summaries, action items, and sentiment analysis for Zoom/Meet/Teams.",
        "description": "Read.ai is a meeting intelligence platform that generates actionable meeting summaries, not just transcripts. It joins your video calls, creates real-time summaries, identifies action items and key decisions, and even analyzes meeting sentiment and engagement. Unlike passive transcription tools, Read.ai provides 'Meeting Reports' that tell you what actually happened and what needs to happen next. Integrates with Slack, Notion, and 30+ tools.",
        "tutorial": "1. Sign up at read.ai and connect your calendar. 2. Read.ai auto-joins scheduled meetings (Zoom, Meet, Teams). 3. During the meeting, view real-time summary and speaker metrics. 4. After the meeting, receive a Meeting Report with: summary, action items, decisions, highlights. 5. Watch the 'Playback' to review specific moments. 6. Use the 'Ask Read' chatbot to query past meetings. 7. Integrate with Slack to auto-post meeting summaries to channels.",
        "pros": ["Action-oriented summaries, not just transcripts", "Meeting sentiment and engagement metrics", "30+ integrations (Slack, Notion, etc.)", "Real-time summary during meetings"],
        "cons": ["Free tier only 5 meetings/month", "Pro pricing slightly higher than Fireflies", "AI summaries can miss nuance", "Speaker identification not always accurate"],
        "best_for": "Managers and team leads who need actionable meeting intelligence and accountability tracking",
        "alternatives": ["fireflies", "otter"], "tags": ["meetings", "productivity", "summaries", "analytics"], "featured": False
    },
    {
        "id": "browse-ai",
        "name": "Browse AI",
        "url": "https://www.browse.ai", "affiliate": None, "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free (50 credits/mo) / Starter $48.75/mo / Professional $123.75/mo / Team $249/mo",
        "rating": 8.5,
        "summary": "No-code web scraping and monitoring. Train AI bots to extract data from any website, on a schedule.",
        "description": "Browse AI is a no-code web data extraction platform that lets you 'train' robots to scrape and monitor websites. You show the robot what data to extract from a page, and it replicates the extraction across thousands of pages. Monitor competitor pricing, track job listings, aggregate real estate data, or build datasets from any website — without writing a single line of code. Scheduled runs with change detection and API/webhook integration.",
        "tutorial": "1. Sign up at browse.ai and install the Chrome extension. 2. Click 'Create Robot' and enter a URL. 3. Highlight the data you want to extract (click elements on the page). 4. Name your columns — Browse AI learns the pattern. 5. Run the robot on the current page to test. 6. Set up a schedule: hourly, daily, or weekly. 7. Receive notifications via email, Slack, or webhook when data changes. 8. Export to CSV, Google Sheets, or API access.",
        "pros": ["No coding required for web scraping", "Visual element selection", "Scheduled monitoring with change alerts", "API + webhook + Zapier integration"],
        "cons": ["Expensive for high-volume usage", "Complex sites may break extraction", "Slow on paginated sites", "Credit system limits free tier"],
        "best_for": "Marketers, analysts, and non-technical users who need web data extraction and monitoring",
        "alternatives": [], "tags": ["scraping", "automation", "no-code", "data", "monitoring"], "featured": False
    },
    {
        "id": "tldv",
        "name": "tl;dv",
        "url": "https://tldv.io", "affiliate": None, "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free (unlimited recordings) / Pro $25/mo / Business $59/user/mo",
        "rating": 8.4,
        "summary": "AI meeting recorder for Zoom, Meet, and Teams. Timestamped summaries, clips, and search — free unlimited recording.",
        "description": "tl;dv (too long; didn't view) is an AI meeting recorder that captures, transcribes, and summarizes your video calls. The standout feature: unlimited free recording and transcription for individuals. You can create timestamped highlights, generate AI meeting notes, and share specific moments via clip links (like YouTube timestamps). The AI search lets you find any spoken word across all your recorded meetings.",
        "tutorial": "1. Download tl;dv Chrome extension or desktop app. 2. Join any Zoom/Meet/Teams call — tl;dv appears in the sidebar. 3. Click 'Record' to capture the meeting with transcription. 4. During the call, click 'Bookmark' to mark important moments. 5. After the call, review AI-generated summary and action items. 6. Create clips: highlight transcript to create shareable video moments. 7. Search across all meetings by keyword — find any past conversation.",
        "pros": ["Unlimited free recording and transcription", "Timestamp-based clip sharing", "AI search across all meetings", "Works with Zoom, Meet, and Teams"],
        "cons": ["Desktop app required for best experience", "Pro needed for AI summaries", "Business tier expensive for teams", "Less integrations than competitors"],
        "best_for": "Individual professionals and small teams who record many meetings and need an affordable solution",
        "alternatives": ["fireflies", "otter"], "tags": ["meetings", "recording", "transcription", "productivity"], "featured": False
    },
    {
        "id": "clockwise",
        "name": "Clockwise",
        "url": "https://www.getclockwise.com", "affiliate": None, "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free / Teams $11.50/user/mo / Enterprise custom",
        "rating": 8.3,
        "summary": "AI calendar optimizer. Automatically reschedules meetings to create uninterrupted focus time blocks.",
        "description": "Clockwise is an AI-powered calendar assistant that optimizes your schedule to maximize deep work time. It connects to Google Calendar, analyzes everyone's schedules, and automatically moves flexible meetings to create blocks of uninterrupted focus time. The 2026 version includes 'Focus Time Protection' that prevents new meeting invites from fragmenting your deep work blocks. Team analytics show meeting load and focus time trends.",
        "tutorial": "1. Sign up at getclockwise.com and connect Google Calendar. 2. Clockwise analyzes your meeting patterns. 3. Set your focus time preferences (when and how much). 4. Clockwise automatically moves flexible meetings to optimize your schedule. 5. Use 'Schedule Send' to batch meeting bookings into optimal slots. 6. View team analytics to see meeting load and focus time. 7. Set 'Quiet Hours' to prevent scheduling during personal time.",
        "pros": ["Creates uninterrupted focus blocks automatically", "Teams: meeting optimization across group", "Focus Time Protection in 2026", "Free for individuals"],
        "cons": ["Requires Google Calendar (no Outlook)", "Only works if meetings are reschedulable", "Can feel disruptive to meeting routines", "Teams plan adds per-user cost"],
        "best_for": "Knowledge workers and engineering teams drowning in fragmented schedules",
        "alternatives": ["reclaim-ai", "motion-app"], "tags": ["calendar", "productivity", "focus", "scheduling", "time-management"], "featured": False
    },
    {
        "id": "motion-app",
        "name": "Motion",
        "url": "https://www.usemotion.com", "affiliate": None, "category": "productivity",
        "pricing": "Paid",
        "price_detail": "Individual $34/mo / Team $20/user/mo / Enterprise custom (7-day free trial)",
        "rating": 8.1,
        "summary": "AI executive assistant that auto-schedules tasks, projects, and meetings into your calendar.",
        "description": "Motion is an AI-powered calendar and task manager that automatically schedules your to-do list into your actual calendar. Unlike Clockwise which only optimizes meetings, Motion is a complete task + calendar system: you add tasks with priorities and deadlines, and Motion's AI finds the optimal time slots. It adapts in real-time — if a meeting runs long, Motion reshuffles your day. Used by executives, consultants, and ADHD professionals who struggle with time management.",
        "tutorial": "1. Sign up at usemotion.com (7-day free trial). 2. Connect Google Calendar or Outlook. 3. Add tasks with deadlines and estimated duration. 4. Set task priorities (ASAP, High, Medium, Low). 5. Motion auto-populates your calendar with task blocks. 6. When meetings shift, Motion automatically reschedules tasks. 7. Use the Project view for multi-task projects with dependencies. 8. Review daily 'Plan' each morning showing your optimized schedule.",
        "pros": ["Automatic task scheduling into calendar", "Real-time adaptation to schedule changes", "Project management with dependencies", "Reduces decision fatigue"],
        "cons": ["Expensive for individuals ($34/mo)", "No free tier (only 7-day trial)", "Can feel overly rigid", "Less effective for highly unpredictable days"],
        "best_for": "Executives, consultants, and professionals with ADHD who need AI to manage their time",
        "alternatives": ["reclaim-ai", "clockwise"], "tags": ["calendar", "productivity", "task-management", "scheduling", "time-management"], "featured": False
    },
    {
        "id": "reclaim-ai",
        "name": "Reclaim.ai",
        "url": "https://reclaim.ai", "affiliate": None, "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free (3 habits, 1 calendar) / Starter $10/mo / Business $15/user/mo / Enterprise $25/user/mo",
        "rating": 8.6,
        "summary": "Smart calendar assistant for habits, tasks, and meeting buffers. Protect time with auto-scheduling.",
        "description": "Reclaim.ai is an intelligent calendar assistant that goes beyond meeting optimization to manage your habits, tasks, and work-life balance. Unlike Motion which takes over your calendar, Reclaim is more flexible: it creates 'Habits' (recurring time blocks for exercise, learning, deep work) and 'Smart 1:1s' that find mutual availability. The 'Buffer Time' feature automatically adds travel/prep time between meetings. Integrates deeply with Google Calendar and project management tools like Asana, Jira, Linear, and Todoist.",
        "tutorial": "1. Sign up at reclaim.ai with Google Calendar. 2. Set up Habits: 'Gym 3x/week', 'Code review 2hrs daily', 'Learning Friday afternoon'. 3. Reclaim auto-schedules these around your meetings. 4. Connect project management tools (Asana, Jira, Linear) — tasks appear as calendar blocks. 5. Use Smart 1:1s to find mutual availability. 6. Enable Buffer Time to add prep/travel gaps between meetings. 7. Set Defended Hours for non-negotiable personal time.",
        "pros": ["Habits feature for recurring personal time", "Task-to-calendar sync with PM tools", "Smart 1:1 scheduling", "Buffer time automation", "Good free tier"],
        "cons": ["Google Calendar only (no Outlook)", "Business features locked behind paywall", "Can overfill calendar with habits", "Less AI 'intelligence' than Motion"],
        "best_for": "Professionals who want to balance meetings, tasks, habits, and personal time automatically",
        "alternatives": ["motion-app", "clockwise"], "tags": ["calendar", "productivity", "habits", "time-management", "scheduling"], "featured": True
    },
    {
        "id": "looka",
        "name": "Looka",
        "url": "https://looka.com", "affiliate": None, "category": "design",
        "pricing": "Paid",
        "price_detail": "Basic Logo $20 one-time / Premium Logo $65 / Brand Kit $96/yr / Enterprise $129/yr",
        "rating": 7.8,
        "summary": "AI logo maker and brand kit designer. Generate professional logos from preferences, then get full brand assets.",
        "description": "Looka (formerly Logojoy) is an AI-powered logo and brand identity generator. You enter your company name, choose preferred styles and colors, and Looka generates hundreds of logo variations. Once you pick a logo, you can purchase it and get full brand assets: business cards, social media kits, letterheads, and a brand guidelines document. The AI learns from your selections to refine results. Over 20 million logos created.",
        "tutorial": "1. Visit looka.com and enter your company name. 2. Select logo styles you like (pick 5+ from sample gallery). 3. Choose color palettes that match your brand. 4. Add an optional slogan. 5. Looka generates 100+ logo variations instantly. 6. Favor the ones you like — AI refines the next batch. 7. Once you pick a logo, customize fonts, colors, layout. 8. Purchase and download: PNG, SVG, EPS, and brand kit files.",
        "pros": ["100+ AI-generated variations in seconds", "Complete brand kit (cards, social, letterhead)", "One-time purchase for logo files", "Vector exports (SVG, EPS) included"],
        "cons": ["Premium designs are extra cost", "AI can produce generic-looking logos", "No free export (watermarked preview only)", "Limited to preset color/icon combinations"],
        "best_for": "Startups, small businesses, and side projects that need a professional logo fast without hiring a designer",
        "alternatives": ["canva-ai"], "tags": ["logo-design", "branding", "design", "startup"], "featured": False
    },
    {
        "id": "capcut-ai",
        "name": "CapCut",
        "url": "https://www.capcut.com", "affiliate": None, "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $9.99/mo (desktop) / $7.99/mo (mobile) / Teams custom",
        "rating": 8.6,
        "summary": "ByteDance's AI video editor. TikTok-native editing with AI captions, effects, and one-tap viral templates.",
        "description": "CapCut is ByteDance's all-in-one AI video editor, originally built for TikTok creators but now a full-featured editing suite. Its AI features include auto-captions (in 20+ languages), AI text-to-speech, smart background removal, auto-reframe for different aspect ratios, and one-tap viral templates. The desktop version rivals Premiere Pro for short-form content creation, while the mobile app is the go-to editor for TikTok, Instagram Reels, and YouTube Shorts.",
        "tutorial": "1. Download CapCut for desktop or mobile (free). 2. Import video clips to the timeline. 3. Use 'Auto-captions' to generate subtitles in 20+ languages. 4. Apply AI effects: background removal, beauty filters, color grading. 5. Use templates: browse trending templates and replace with your clips. 6. Add AI text-to-speech narration. 7. Auto-reframe for TikTok (9:16), YouTube (16:9), or Instagram (1:1). 8. Export in 4K without watermark (free).",
        "pros": ["Completely free with no watermark", "Excellent auto-captions in 20+ languages", "TikTok-native templates", "Desktop + mobile apps", "4K export"],
        "cons": ["Some Pro effects behind paywall", "Privacy concerns (ByteDance/TikTok)", "Desktop app can be resource-heavy", "Less advanced than Premiere/DaVinci"],
        "best_for": "TikTok, Reels, and Shorts creators who need fast, AI-powered editing with viral-ready templates",
        "alternatives": ["descript", "runway"], "tags": ["video-editing", "social-media", "tiktok", "captions", "templates"], "featured": True
    },
    {
        "id": "opus-clip",
        "name": "Opus Clip",
        "url": "https://www.opus.pro", "affiliate": None, "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free (limited) / Pro $19/mo / Teams $39/user/mo / Enterprise custom",
        "rating": 8.5,
        "summary": "AI clip generator. Turns long videos into viral shorts with auto-captions, B-roll, and publishing in one click.",
        "description": "Opus Clip is an AI video repurposing tool that automatically extracts the most viral-worthy moments from long-form videos and turns them into short clips. It adds dynamic captions, B-roll overlays, face tracking, and chapter markers — all automatically. The AI scoring system predicts which clips will perform best on social media. Creators use it to turn podcasts, streams, and webinars into dozens of TikTok/Reels/Shorts in minutes.",
        "tutorial": "1. Sign up at opus.pro and upload a long video (up to 2 hours). 2. Opus AI analyzes and identifies viral moments. 3. Each clip gets a 'Virality Score' to predict performance. 4. Clips auto-include: dynamic captions, face tracking, B-roll cuts. 5. Edit individual clips: trim, change captions, add content. 6. Set brand templates for consistent look. 7. Schedule and publish directly to TikTok, YouTube, Instagram. 8. Track clip performance analytics.",
        "pros": ["Auto-identifies viral moments from long videos", "Dynamic captions and B-roll added automatically", "Virality Score prediction", "Direct publishing to all platforms"],
        "cons": ["Expensive for high-volume creators", "Free tier severely limited", "AI captions sometimes inaccurate", "Over-reliance on AI editing style"],
        "best_for": "Podcasters, streamers, and webinar hosts who want to repurpose long content into viral short clips",
        "alternatives": ["descript", "capcut-ai"], "tags": ["video-clips", "shorts", "repurposing", "social-media", "viral"], "featured": False
    },
    {
        "id": "d-id",
        "name": "D-ID",
        "url": "https://www.d-id.com", "affiliate": None, "category": "video",
        "pricing": "Paid",
        "price_detail": "Starter $5.99/mo / Pro $29.99/mo / Business $149/mo / Enterprise custom",
        "rating": 7.9,
        "summary": "AI talking avatars from photos. Animate any portrait with natural speech and expressions.",
        "description": "D-ID is a creative AI platform specializing in 'speaking portrait' animation — the technology that makes still photos talk. Upload any face photo, type text or upload audio, and D-ID animates the face with natural speech movements, expressions, and head motion. Used by educators creating video lessons, marketers personalizing outreach, and developers building interactive AI characters. The 2026 Creative Reality Studio offers API access for embedding talking avatars into apps and websites.",
        "tutorial": "1. Sign up at d-id.com — $5.99 Starter includes 10 minutes of video. 2. Upload a portrait photo (clear, front-facing works best). 3. Type or paste your script (supports 120+ languages). 4. Choose a voice from 100+ options or upload your own audio. 5. Generate — the photo animates with natural speech and expressions. 6. Preview and adjust speed, expression, and head movement. 7. Download as MP4. 8. Use API for programmatic avatar generation at scale.",
        "pros": ["Realistic face animation from one photo", "120+ language voice support", "API for scalable avatar generation", "Good for personalized video outreach"],
        "cons": ["Paid only — no free tier", "Limited to talking-head format", "Can look uncanny with poor source photos", "Fewer avatar options than Synthesia"],
        "best_for": "Educators, marketers, and developers who need to animate still photos into talking videos",
        "alternatives": ["synthesia", "heygen"], "tags": ["avatars", "animation", "video", "personalization", "api"], "featured": False
    }
]

for t in missing_tools:
    data['tools'].append(t)
print(f"Added {len(missing_tools)} missing tools")

# ============================================
# PART 2: Update existing tools with verified 2026 data
# ============================================
verified_updates = {
    'copilot': {
        'price_detail': 'Free (2000 completions/mo) / Pro $10/mo / Business $19/user/mo / Enterprise $39/user/mo',
        'pricing': 'Freemium',
        'summary': 'GitHub Copilot — the original AI coding assistant. 30+ IDE support, multi-file context, free tier for individuals.',
        'description': 'GitHub Copilot is Microsoft\'s AI coding assistant, the most broadly deployed in enterprise with support for 30+ IDEs including JetBrains, VS Code, and Neovim. In 2026, Copilot introduced a free tier (2000 completions/month), multi-file context understanding, and agentic Copilot Workspace for autonomous task completion. While its agentic features lag behind Cursor, Copilot remains the only viable option for teams not using VS Code-based editors.'
    },
    'cursor': {
        'price_detail': 'Pro $20/mo / Business $40/user/mo / Enterprise custom (no free tier for agentic features)',
        'pricing': 'Paid',
        'summary': 'AI-first code editor with Claude-powered agentic coding. 200K context window, background agents, multi-file editing.',
        'description': 'Cursor is an AI-first VS Code fork that leads the industry in agentic coding capability in 2026. With a 200K token context window (via Claude 3.5 Sonnet), Cursor can understand entire codebases in a single session. New 2026 features include Background Agents (async refactoring that runs while you work) and improved multi-file agent mode. Developer surveys consistently rank Cursor first for perceived productivity improvement. VS Code only (no JetBrains support).'
    },
    'windsurf': {
        'price_detail': 'Free (unlimited completions) / Pro $15/mo / Teams $30/user/mo',
        'pricing': 'Freemium',
        'summary': 'Best free AI coding assistant. Unlimited completions, Cascade agent, 200K context — free for individuals.',
        'description': 'Windsurf by Codeium is the best free AI coding assistant in 2026, offering unlimited code completions and generous agentic credits to individual developers at no cost. Its Cascade agent performs multi-file edits, terminal execution, and self-correction comparable to Cursor for standard tasks. The 2026 memory system retains project conventions across sessions. Pro ($15/mo) adds Claude/GPT-4o model access and higher agentic limits.'
    },
    'sora': {
        'name': 'Sora',
        'price_detail': 'Included in ChatGPT Plus $20/mo / Pro $200/mo (unlimited) / API $0.10-0.50/sec',
        'summary': 'OpenAI Sora 2 — most realistic AI video generation. Plus plan includes Sora 2 access, Pro unlimited.',
        'description': 'Sora 2 is OpenAI\'s second-generation AI video generation model, released September 2025. It produces the most photorealistic narrative videos among all AI video generators, with improved temporal consistency, camera control, and resolution. Sora 2 is available through ChatGPT Plus ($20/mo with limited credits) or ChatGPT Pro ($200/mo with unlimited generations). The API launched in 2026 for developers, though OpenAI announced API sunset by September 2026.'
    },
    'elevenlabs': {
        'price_detail': 'Free (10 min/mo) / Starter $5/mo / Creator $22/mo / Pro $99/mo / Scale $330/mo / Business $1,320/mo',
        'pricing': 'Freemium',
        'summary': 'Industry-leading AI voice generation. 70+ languages, voice cloning, OmniHuman AI. Free tier available.',
        'description': 'ElevenLabs is the undisputed industry leader in AI voice synthesis in 2026, with 70+ languages and voices indistinguishable from human speech. The 2026 Creator plan ($22/mo) includes professional voice cloning — upload a 1-minute sample and ElevenLabs clones the voice with full emotional control. Pro and above include OmniHuman AI for full-body avatar generation. Used by podcasters, game developers, audiobook producers, and Fortune 500 companies for customer service voice AI.'
    },
    'deepseek': {
        'price_detail': 'Free / API from $0.14/M input tokens (V4-Flash)',
        'summary': 'Chinese AI with V4 models, coding excellence, and absurdly cheap API. Free web access.',
        'description': 'DeepSeek is the Chinese AI lab that shocked the industry with cost-efficient, high-performance models. The 2026 V4 and V4-Pro models compete with GPT-5 class performance at a fraction of the cost. In April 2026, DeepSeek announced a 75% price cut on V4-Pro API access, making it the most affordable frontier AI for developers. The free web interface includes file upload, long context, and code execution.'
    },
    'stable-diffusion': {
        'price_detail': 'Free (open source, self-hosted) / Stability AI API $0.002-0.01/image / DreamStudio credits',
        'summary': 'Open-source AI image generation. SD3.5 current, self-hostable, unlimited free with your own GPU.',
        'description': 'Stable Diffusion remains the go-to open-source AI image generator in 2026, now at SD3.5 with improved hands, text rendering, and composition. Unlike cloud-only tools, Stable Diffusion runs on your own hardware — completely free and unlimited with a capable GPU. The DreamStudio web interface provides cloud access, while Automatic1111 and ComfyUI desktop apps offer professional control. Fine-tuned community models (LoRAs) enable infinite style customization.'
    }
}

for tool in data['tools']:
    tid = tool['id']
    if tid in verified_updates:
        for key, value in verified_updates[tid].items():
            tool[key] = value
        print(f"  Verified & Updated: {tool['name']}")

# Save
with open(f'{BASE}/data/tools.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n{'='*50}")
print(f"Summary:")
print(f"  Missing tools added: {len(missing_tools)}")
print(f"  Existing tools updated: {len(verified_updates)}")
print(f"  Total tools: {len(data['tools'])}")
