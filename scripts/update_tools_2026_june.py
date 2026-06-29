#!/usr/bin/env python3
"""
Update tools.json with latest 2026 data:
- Move 4 upcoming tools → active
- Add AI App Builder category + Lovable/Bolt.new/v0
- Add 6 missing hot tools
- Update existing tool pricing/info
"""
import json

BASE = __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))

with open(f'{BASE}/data/tools.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ============================================
# PART 1: Add AI App Builder category
# ============================================
data['categories'].append({
    "id": "app-builder",
    "name": "AI App Builders",
    "icon": "🏗️",
    "description": "Build full-stack apps with AI. No coding required."
})

# ============================================
# PART 2: 4 upcoming tools → active
# ============================================

new_active = [
    {
        "id": "synthesia",
        "name": "Synthesia",
        "url": "https://www.synthesia.io",
        "affiliate": None,
        "category": "video",
        "pricing": "Paid",
        "price_detail": "Free / Starter $29/mo / Creator $89/mo / Enterprise custom",
        "rating": 8.6,
        "summary": "AI-powered video creation with digital avatars. Turn text into professional talking-head videos in 140+ languages.",
        "description": "Synthesia is the leading AI video generation platform for creating professional videos with AI avatars. Instead of filming yourself or hiring actors, you type a script and an AI avatar delivers it in natural speech across 140+ languages. Used by 50,000+ companies including Nike, Amazon, and BBC. The platform includes 230+ AI avatars, custom avatar creation, screen recording, and brand templates for consistent corporate video production.",
        "tutorial": "1. Sign up at synthesia.io — free demo video available. 2. Choose from 230+ AI avatars or create your own custom avatar. 3. Type or paste your script (supports 140+ languages). 4. Select a video template or start from scratch. 5. Add background, text overlays, images, and screen recordings. 6. Preview the AI avatar delivering your script naturally. 7. Generate the video — processing takes 2-5 minutes. 8. Download as MP4 or share via link. 9. For teams: create brand kits with logos, colors, and approved avatars.",
        "pros": [
            "230+ AI avatars, 140+ languages",
            "No filming equipment needed",
            "Custom avatar creation available",
            "Enterprise brand controls",
            "SOC 2 Type II compliant"
        ],
        "cons": [
            "No free plan (only demo)",
            "Expensive for individual creators",
            "Avatars can still feel slightly robotic",
            "Limited video editing features"
        ],
        "best_for": "Corporate training, sales outreach, and marketing teams who need high-volume professional video content",
        "alternatives": ["heygen", "runway"],
        "tags": ["video-generation", "avatars", "corporate", "multilingual"],
        "featured": True
    },
    {
        "id": "claude-code",
        "name": "Claude Code",
        "url": "https://claude.com/product/claude-code",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free CLI + API cost / Included in Claude Pro $20/mo / Max $100-200/mo",
        "rating": 9.2,
        "summary": "Anthropic's agentic coding tool. Reads entire codebases, edits files, runs commands — 125K+ GitHub stars.",
        "description": "Claude Code is Anthropic's agentic coding system that runs natively in the terminal. Unlike IDE-based copilots, Claude Code can read your entire codebase, understand project architecture, edit multiple files, run shell commands, manage git operations, and even debug across repositories. With a 1M token context window and SWE-bench score of 80.8%, it's currently the most capable autonomous coding agent. Anthropic themselves report the majority of their code is now written by Claude Code.",
        "tutorial": "1. Install via npm: 'npm install -g @anthropic-ai/claude-code' or use with Claude Pro/Max subscription. 2. Navigate to your project directory and run 'claude'. 3. Claude Code reads your entire codebase (supports 1M token context). 4. Describe what you want to build or fix in natural language. 5. Claude proposes changes — review the diff before approving. 6. It executes shell commands, creates files, and manages git automatically. 7. For complex tasks, Claude breaks them into subtasks and works through them sequentially. 8. Use '/memory' to save project conventions that persist across sessions. 9. Integrate with VS Code or JetBrains via MCP protocol for IDE usage.",
        "pros": [
            "SWE-bench 80.8% — highest autonomous coding score",
            "1M token context handles entire codebases",
            "Free CLI tool (pay only API usage)",
            "Handles multi-file refactors gracefully",
            "Terminal-native — works with any stack"
        ],
        "cons": [
            "API costs can add up on large projects",
            "Requires terminal comfort (no GUI)",
            "Max plan needed for unlimited usage",
            "Occasionally over-engineers simple fixes"
        ],
        "best_for": "Senior developers who want an AI pair programmer that truly understands their entire codebase",
        "alternatives": ["cursor", "copilot", "windsurf"],
        "tags": ["coding", "agent", "terminal", "cli", "devtools"],
        "featured": True
    },
    {
        "id": "gamma",
        "name": "Gamma",
        "url": "https://gamma.app",
        "affiliate": None,
        "category": "design",
        "pricing": "Freemium",
        "price_detail": "Free (10 cards) / Plus $10/mo / Pro $20/mo / Enterprise custom",
        "rating": 8.3,
        "summary": "AI-powered presentation and document creator. Generate beautiful slides, docs, and webpages in seconds.",
        "description": "Gamma is an AI-native presentation and document creation platform that generates professional slides, documents, and webpages from a single prompt. With over 300 million users, Gamma has become the go-to alternative to PowerPoint and Google Slides. You describe your topic, and Gamma creates a complete presentation with AI-generated content, layouts, images, and charts. Export to PowerPoint, PDF, or share as an interactive webpage.",
        "tutorial": "1. Visit gamma.app and sign up for free (Google/email). 2. Click 'Create New' and choose Presentation, Document, or Webpage. 3. Enter your topic or paste an outline — Gamma generates a complete first draft in seconds. 4. Use AI chat to refine: 'Make this slide more visual' or 'Add a comparison chart'. 5. Customize the theme, colors, and fonts with one click. 6. Add AI-generated images, charts, and diagrams inline. 7. Present directly in browser with smooth transitions — no Powerpoint needed. 8. Export as PDF, PPTX, or share via link with view/edit permissions.",
        "pros": [
            "Creates full presentations in seconds",
            "Beautiful default designs and themes",
            "AI chat for real-time editing",
            "Export to PPTX, PDF, or share link",
            "300M+ users, proven reliability"
        ],
        "cons": [
            "Free tier limited to 10 cards",
            "AI content sometimes needs heavy editing",
            "Less control than traditional design tools",
            "No offline mode"
        ],
        "best_for": "Anyone who regularly creates presentations and wants to save hours on slide design",
        "alternatives": ["canva-ai", "figma-ai"],
        "tags": ["presentations", "slides", "design", "documents", "productivity"],
        "featured": False
    },
    {
        "id": "luma-dream-machine",
        "name": "Luma Dream Machine",
        "url": "https://lumalabs.ai/dream-machine",
        "affiliate": None,
        "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free (30 generations/mo) / Lite $9.99/mo / Plus $29.99/mo / Pro $99.99/mo",
        "rating": 8.1,
        "summary": "AI video generator from Luma Labs. Turn text and images into cinematic video clips with stunning realism.",
        "description": "Luma Dream Machine is an AI video generation platform from Luma Labs that creates high-quality, cinematic video clips from text prompts or reference images. Known for its photorealistic output and smooth motion, Dream Machine excels at creating short-form video content with natural camera movement and lighting. The 2026 version includes Ray 2 model with improved temporal consistency and longer generation times.",
        "tutorial": "1. Visit lumalabs.ai and sign up for free (30 free generations/month). 2. Choose 'Text to Video' or 'Image to Video' mode. 3. For text: describe your scene — 'Cinematic drone shot of Tokyo at night, neon lights reflecting on wet streets'. 4. For image: upload a reference photo and Luma adds realistic motion. 5. Adjust settings: duration (5-10s), style, and camera movement. 6. Click 'Generate' — processing takes 1-3 minutes. 7. Download as MP4 or share via link. 8. Use the 'Extend' feature to lengthen clips up to 30 seconds.",
        "pros": [
            "Photorealistic output quality",
            "Free tier with 30 generations/month",
            "Image-to-video works exceptionally well",
            "Natural camera movement effects",
            "Ray 2 model improves consistency"
        ],
        "cons": [
            "Max 10 seconds per generation",
            "Text-to-video can be hit-or-miss",
            "Slower than Runway for batch work",
            "Limited editing/customization options"
        ],
        "best_for": "Content creators and filmmakers who want quick, cinematic B-roll and visual concept videos",
        "alternatives": ["runway", "sora", "pika", "kling"],
        "tags": ["video-generation", "cinematic", "text-to-video", "image-to-video"],
        "featured": False
    },
    # ============================================
    # PART 3: AI App Builders
    # ============================================
    {
        "id": "lovable",
        "name": "Lovable",
        "url": "https://lovable.dev",
        "affiliate": None,
        "category": "app-builder",
        "pricing": "Freemium",
        "price_detail": "Free / Starter $20/mo / Pro $50/mo / Team $100/mo / Enterprise custom",
        "rating": 9.0,
        "summary": "The fastest-growing AI app builder of 2026. Describe your idea, Lovable builds the full-stack app with frontend, backend, and database.",
        "description": "Lovable is the breakout AI app builder of 2026, reaching $100M ARR by enabling anyone to build full-stack web applications from a simple text description. It generates React frontends, Supabase backends, and PostgreSQL databases automatically. Users describe features like 'make a marketplace for vintage clothes' and Lovable produces a working, deployed application with authentication, database, and API integrations. Used by founders, product managers, and non-technical entrepreneurs to go from idea to MVP in hours instead of months.",
        "tutorial": "1. Visit lovable.dev and sign up with Google. 2. Describe your app idea in plain English: 'Build a habit tracker with daily streaks, reminders, and data visualization'. 3. Lovable generates a complete React + Supabase app with database schema, auth, and UI. 4. Preview the live app immediately — every generation deploys automatically. 5. Chat with Lovable to iterate: 'Add dark mode', 'Connect Stripe for payments', 'Add user profiles'. 6. Use visual editor to tweak UI components directly. 7. Connect your custom domain with one click. 8. Export code to GitHub for full developer control. 9. Deploy to production with built-in Vercel integration.",
        "pros": [
            "Full-stack apps from a single prompt",
            "Automatic database + auth setup",
            "Instant deployment with live preview",
            "GitHub export for developer control",
            "Supabase for production-ready backend"
        ],
        "cons": [
            "Generated code can be messy under the hood",
            "Best for MVPs, not complex production apps",
            "Limited to React/Supabase stack",
            "Can struggle with very specific business logic"
        ],
        "best_for": "Non-technical founders, product managers, and solo entrepreneurs who want to ship an MVP in days",
        "alternatives": ["bolt-new", "v0"],
        "tags": ["app-builder", "no-code", "full-stack", "react", "startup"],
        "featured": True
    },
    {
        "id": "bolt-new",
        "name": "Bolt.new",
        "url": "https://bolt.new",
        "affiliate": None,
        "category": "app-builder",
        "pricing": "Freemium",
        "price_detail": "Free (limited tokens) / Pro $20/mo / Team $50/user/mo / Enterprise custom",
        "rating": 8.7,
        "summary": "StackBlitz's AI app builder. Build and deploy full-stack web apps directly in the browser — no setup needed.",
        "description": "Bolt.new by StackBlitz is a browser-based AI app builder that lets you create full-stack web applications without installing anything. Unlike other AI builders, Bolt.new runs actual Node.js in the browser via WebContainers, giving you a real development environment. You can prompt Bolt to build apps, then dive into the code with a full VS Code-like editor, run terminal commands, and install npm packages — all in the browser. It supports React, Next.js, Vue, Svelte, and more.",
        "tutorial": "1. Visit bolt.new — no signup needed to try. 2. Describe your app: 'Build a real-time collaborative whiteboard with WebSocket'. 3. Bolt generates the complete project with all dependencies configured. 4. The app runs instantly in the browser preview — no build step needed. 5. Switch to code view to edit files directly with full IDE features. 6. Run 'npm install <package>' in the built-in terminal to add dependencies. 7. Deploy to Netlify or StackBlitz with one click. 8. Export to GitHub or download as ZIP for local development.",
        "pros": [
            "Real browser-based dev environment",
            "No installation or setup required",
            "Full terminal + npm access",
            "Supports multiple frameworks",
            "One-click deployment"
        ],
        "cons": [
            "Free tier has low token limits",
            "WebContainer limitations on some Node features",
            "Can be slower than local development",
            "Less polished UI generation than Lovable"
        ],
        "best_for": "Developers who want the speed of AI generation with the control of a real dev environment",
        "alternatives": ["lovable", "v0"],
        "tags": ["app-builder", "web-development", "browser-ide", "full-stack"],
        "featured": True
    },
    {
        "id": "v0",
        "name": "v0 by Vercel",
        "url": "https://v0.dev",
        "affiliate": None,
        "category": "app-builder",
        "pricing": "Freemium",
        "price_detail": "Free (200 credits/mo) / Premium $20/mo / Team $30/user/mo / Enterprise custom",
        "rating": 8.5,
        "summary": "Vercel's AI UI generator. Generate production-ready React/Tailwind components and full pages from text prompts.",
        "description": "v0 by Vercel is an AI-powered UI generation tool that creates production-ready React components using Tailwind CSS and shadcn/ui. Unlike broader app builders, v0 focuses specifically on generating pixel-perfect frontend code. You describe the UI you want, and v0 outputs clean, copy-pasteable React components. Tightly integrated with the Vercel ecosystem, v0 is the go-to tool for frontend developers who want to rapidly prototype and build polished user interfaces.",
        "tutorial": "1. Visit v0.dev and sign in with GitHub or Google. 2. Describe your UI: 'A SaaS pricing page with 3 tiers, feature comparison table, and FAQ accordion'. 3. v0 generates the complete React component with Tailwind styling. 4. Preview the rendered output immediately. 5. Iterate with chat: 'Make the middle tier highlighted as recommended', 'Add hover animations'. 6. Copy the generated code directly into your project. 7. Use v0 Blocks for pre-built components like navbars, footers, and hero sections. 8. Connect to your Vercel project for one-click deployment.",
        "pros": [
            "Cleanest generated React/Tailwind code",
            "shadcn/ui component library integration",
            "Vercel ecosystem native deployment",
            "Excellent for UI prototyping",
            "v0 Blocks library for common patterns"
        ],
        "cons": [
            "Frontend only — no backend generation",
            "Less capable for full apps than Lovable",
            "200 credits/month on free tier",
            "Tailwind-specific (no CSS modules, etc.)"
        ],
        "best_for": "Frontend developers and designers who want to rapidly generate polished React components",
        "alternatives": ["lovable", "bolt-new"],
        "tags": ["app-builder", "react", "tailwind", "ui-design", "frontend"],
        "featured": False
    },
    # ============================================
    # PART 4: 6 missing hot tools
    # ============================================
    {
        "id": "notebooklm",
        "name": "NotebookLM",
        "url": "https://notebooklm.google.com",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Free",
        "price_detail": "Completely free — Google account required",
        "rating": 8.9,
        "summary": "Google's AI research assistant. Upload docs and get summaries, audio overviews, and answers grounded in your sources.",
        "description": "NotebookLM is Google's free AI-powered research and note-taking tool that transforms your documents into an interactive knowledge base. Upload PDFs, Google Docs, websites, YouTube videos, or paste text — NotebookLM reads everything and becomes an expert on YOUR content. Its killer feature is Audio Overviews: two AI hosts generate a podcast-style discussion of your documents. Updated in March 2026 with visualization tools and Google Classroom integration.",
        "tutorial": "1. Visit notebooklm.google.com and sign in with your Google account. 2. Create a new notebook and name it (e.g., 'Q3 Market Research'). 3. Add sources: upload PDFs, paste URLs, add Google Docs, or paste text. 4. NotebookLM instantly processes all sources and can answer questions grounded ONLY in your documents. 5. Ask: 'What are the key trends across all these reports?' — every answer includes inline citations. 6. Click 'Audio Overview' to generate a podcast-style conversation about your documents. 7. Use the 'Notebook Guide' for auto-generated FAQ, study guide, table of contents, and timeline. 8. Create multiple notebooks for different projects — all free and unlimited.",
        "pros": [
            "Completely free, no limits",
            "Audio Overviews are genuinely useful",
            "Answers grounded in YOUR documents only",
            "Supports PDFs, URLs, YouTube, Google Docs",
            "Google Classroom integration (2026)"
        ],
        "cons": [
            "Requires Google account",
            "No offline access",
            "Limited to uploaded sources (no web search)",
            "Audio quality varies by topic complexity"
        ],
        "best_for": "Students, researchers, and professionals who need to extract insights from large document collections",
        "alternatives": ["perplexity", "notion-ai"],
        "tags": ["research", "study", "productivity", "free", "google"],
        "featured": True
    },
    {
        "id": "kling",
        "name": "Kling",
        "url": "https://klingai.com",
        "affiliate": None,
        "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free (limited) / Standard $9.99/mo / Pro $29.99/mo / Premium $79.99/mo",
        "rating": 8.4,
        "summary": "Kuaishou's AI video generator. Sora's strongest competitor — excels at high-consistency UGC-style short videos.",
        "description": "Kling is Kuaishou's powerful AI video generation platform that has emerged as OpenAI Sora's strongest competitor. Built by the team behind one of China's largest short-video platforms, Kling excels at generating high-consistency, natural-looking UGC (user-generated content) style videos. Its strength lies in maintaining character consistency across clips and producing videos that look like real phone footage rather than CGI. Particularly popular for social media content, product demos, and lifestyle videos.",
        "tutorial": "1. Visit klingai.com and sign up (email or phone). 2. Choose 'Text to Video' or 'Image to Video' mode. 3. For text: describe your scene with details about subject, action, setting, and style. 4. For image: upload a reference photo and Kling generates matching video. 5. Select video duration (5-10 seconds) and quality (Standard/High). 6. Add 'Motion Brush' to control specific element movements. 7. Generate — processing takes 1-5 minutes. 8. Use 'Extend' to create longer videos from the generated clip.",
        "pros": [
            "Excellent character and scene consistency",
            "Natural-looking UGC-style output",
            "Motion Brush for precise control",
            "Strong at human motion and expressions",
            "Free tier available"
        ],
        "cons": [
            "Interface primarily in Chinese",
            "Slower generation than Runway",
            "Limited to 10-second clips",
            "Fewer cinematic effects than Sora"
        ],
        "best_for": "Social media creators and marketers who need realistic, consistent short-form video content",
        "alternatives": ["sora", "runway", "luma-dream-machine", "pika"],
        "tags": ["video-generation", "social-media", "ugc", "short-video"],
        "featured": False
    },
    {
        "id": "heygen",
        "name": "HeyGen",
        "url": "https://www.heygen.com",
        "affiliate": None,
        "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free (2 min/mo) / Creator $29/mo / Business $89/mo / Enterprise custom",
        "rating": 8.7,
        "summary": "AI video translation and digital avatars. Translate videos into 40+ languages while preserving voice and lip sync.",
        "description": "HeyGen is an AI video platform specializing in video translation and AI avatar creation. Its standout feature is instant video translation: upload a video of yourself speaking English, and HeyGen outputs the same video with your voice and lips perfectly synced in Spanish, Mandarin, Arabic, or 40+ other languages. Used by content creators, educators, and enterprises to create localized video content at scale without reshooting.",
        "tutorial": "1. Sign up at heygen.com — 2 free minutes/month. 2. Choose a workflow: AI Avatar Video, Video Translate, or Personalized Video. 3. For avatar video: select from 300+ AI avatars or create your own. 4. Type your script and choose language — avatar speaks naturally. 5. For video translation: upload your video (max 500MB). 6. Select target language(s) — HeyGen clones your voice and syncs lips. 7. Preview and download. 8. For personalized videos: connect CRM data to generate thousands of customized sales videos.",
        "pros": [
            "Best-in-class video translation with lip sync",
            "Voice cloning preserves speaker identity",
            "40+ languages supported",
            "300+ AI avatars + custom avatar creation",
            "CRM integration for personalized video at scale"
        ],
        "cons": [
            "Free tier only 2 minutes/month",
            "Custom avatar creation takes 24-48 hours",
            "Expensive for high-volume usage",
            "Some languages have accent limitations"
        ],
        "best_for": "Content creators going multilingual, sales teams scaling personalized outreach, and global training teams",
        "alternatives": ["synthesia", "elevenlabs"],
        "tags": ["video-translation", "avatars", "multilingual", "personalization", "sales"],
        "featured": True
    },
    {
        "id": "descript",
        "name": "Descript",
        "url": "https://www.descript.com",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free (1 hr/mo) / Hobbyist $24/mo / Creator $35/mo / Business $50/user/mo",
        "rating": 8.8,
        "summary": "AI-powered video and podcast editor. Edit media by editing text — delete words from transcript and video updates automatically.",
        "description": "Descript is an all-in-one video and podcast editing platform that reimagines editing as a document-based workflow. You edit your video or audio by editing the transcript text — delete a sentence from the transcript and it's removed from the media. Features include AI voice cloning (Overdub), filler word removal, studio sound enhancement, screen recording, and collaboration tools. Used by top podcasters, YouTubers, and marketing teams who want to edit content as fast as editing a Google Doc.",
        "tutorial": "1. Download Descript for Mac or Windows (web version available). 2. Create a new project — import video/audio files or record directly. 3. Descript automatically transcribes your media (95%+ accuracy). 4. Edit by highlighting and deleting text in the transcript — media updates instantly. 5. Use AI Actions: 'Remove filler words', 'Remove silence', 'Create social clips'. 6. Correct mistakes with Overdub: type corrected text and your AI voice reads it. 7. Add Studio Sound one-click audio enhancement. 8. Export as MP4, MP3, or publish directly to YouTube, Spotify, etc.",
        "pros": [
            "Revolutionary transcript-based editing",
            "AI voice cloning (Overdub) for corrections",
            "Automatic filler word and silence removal",
            "Built-in screen recording",
            "Team collaboration features"
        ],
        "cons": [
            "Desktop app required for full features",
            "Overdub requires voice training (10 min)",
            "Higher plans needed for watermark-free export",
            "Can struggle with heavy accents"
        ],
        "best_for": "Podcasters, YouTubers, and content teams who edit audio/video regularly",
        "alternatives": ["elevenlabs"],
        "tags": ["podcast", "video-editing", "transcription", "content-creation"],
        "featured": False
    },
    {
        "id": "consensus",
        "name": "Consensus",
        "url": "https://consensus.app",
        "affiliate": None,
        "category": "education",
        "pricing": "Freemium",
        "price_detail": "Free / Premium $11.99/mo / Team $15.99/user/mo",
        "rating": 8.5,
        "summary": "AI academic search engine. Ask research questions and get answers backed by real scientific papers with citations.",
        "description": "Consensus is an AI-powered academic search engine that uses natural language processing to find and summarize scientific research. Unlike Google Scholar which returns a list of papers, Consensus directly answers your research questions by analyzing findings across hundreds of papers simultaneously. It extracts key findings, shows the consensus among researchers, and provides inline citations. Used by students, researchers, and professionals who need evidence-based answers quickly.",
        "tutorial": "1. Visit consensus.app and sign up for free. 2. Ask a research question: 'Does intermittent fasting improve cognitive function?' 3. Consensus searches 200M+ papers and returns a synthesized answer. 4. View the 'Consensus Meter' showing how many papers support vs. refute the claim. 5. Browse top papers with key findings extracted automatically. 6. Filter by study type: RCT, meta-analysis, systematic review, etc. 7. Use 'Copilot' for deeper analysis and follow-up questions. 8. Cite papers directly with auto-generated citations. 9. Export findings as a summary report.",
        "pros": [
            "200M+ papers indexed",
            "Direct answers with paper citations",
            "Consensus Meter shows research agreement",
            "Filter by study design type",
            "Auto-generated citations"
        ],
        "cons": [
            "Limited to indexed papers (some paywalled)",
            "Premium needed for unlimited searches",
            "Best for STEM, weaker in humanities",
            "Can oversimplify nuanced research"
        ],
        "best_for": "Students writing literature reviews, researchers validating hypotheses, and professionals needing evidence-based answers",
        "alternatives": ["elicit", "perplexity"],
        "tags": ["research", "academic", "science", "papers", "literature-review"],
        "featured": False
    },
    {
        "id": "elicit",
        "name": "Elicit",
        "url": "https://elicit.com",
        "affiliate": None,
        "category": "education",
        "pricing": "Freemium",
        "price_detail": "Free (5,000 credits/mo) / Plus $12/mo / Pro $49/mo / Enterprise custom",
        "rating": 8.4,
        "summary": "AI research assistant for systematic literature reviews. Extract data from papers, compare findings, and build evidence tables.",
        "description": "Elicit is an AI research assistant designed specifically for conducting systematic literature reviews. Unlike general-purpose AI search, Elicit understands the academic workflow: you define a research question, and it finds relevant papers, extracts key data points (sample size, methodology, effect sizes), and helps you build structured evidence tables. Used by researchers at top universities and organizations who need to synthesize large volumes of academic literature efficiently.",
        "tutorial": "1. Sign up at elicit.com — 5,000 free credits/month. 2. Enter your research question: 'What is the effect of mindfulness meditation on workplace productivity?' 3. Elicit returns a table of relevant papers with extracted data columns. 4. Customize columns to extract: sample size, intervention type, outcome measures, effect size, p-values. 5. Use 'High Accuracy Mode' for critical extractions (costs more credits). 6. Compare findings across papers side-by-side in the table view. 7. Export data to CSV for meta-analysis or systematic review. 8. Use 'Define Concepts' to ensure consistent extraction across all papers.",
        "pros": [
            "Systematic review workflow built-in",
            "Automated data extraction from papers",
            "Customizable extraction columns",
            "High Accuracy Mode for critical work",
            "CSV export for meta-analysis"
        ],
        "cons": [
            "Learning curve for extraction setup",
            "Credit system limits free tier",
            "Requires verification of extracted data",
            "Less effective for qualitative research"
        ],
        "best_for": "Graduate students, academic researchers, and analysts conducting systematic literature reviews",
        "alternatives": ["consensus", "perplexity"],
        "tags": ["research", "academic", "systematic-review", "meta-analysis", "literature-review"],
        "featured": False
    }
]

# Add all new tools to tools array
for tool in new_active:
    data['tools'].append(tool)

# Remove all 4 from upcoming list
upcoming_names_to_remove = ['Synthesia', 'Claude Code', 'Gamma', 'Luma Dream Machine']
data['upcoming'] = [u for u in data['upcoming'] if u['name'] not in upcoming_names_to_remove]

# ============================================
# PART 5: Update existing tool data
# ============================================
updates = {
    'chatgpt': {
        'price_detail': 'Free / Plus $20/mo / Pro $200/mo / Team $25-30/user/mo',
        'description': 'ChatGPT by OpenAI is the world\'s most popular AI assistant, used by over 300 million weekly active users. The 2026 version runs on GPT-5.5 (Plus) and GPT-5.5 Thinking (Pro), with capabilities spanning text generation, image creation (DALL-E integration), data analysis, coding, and web browsing. The free tier now includes GPT-5.3 Instant with solid performance for everyday tasks. ChatGPT has evolved from a chatbot into a full platform with GPTs (custom AI agents), Memory, Canvas for document editing, and Sora 2 video generation (Pro tier).',
        'summary': 'The world\'s most popular AI assistant. 300M+ weekly users. GPT-5.5, image gen, code, browsing, and Sora 2 video (Pro).'
    },
    'gemini': {
        'price_detail': 'Free / AI Plus $7.99/mo / AI Pro $19.99/mo / AI Ultra $99.99/mo',
        'description': 'Google Gemini is the largest AI service by user count in 2026, with over 750 million monthly active users. It integrates deeply with Google Workspace (Gmail, Docs, Sheets, Drive, YouTube) and Android. The May 2026 pricing restructure introduced three paid tiers with increasing context windows and capabilities. Gemini\'s 1M+ token context window enables analysis of entire books, codebases, and video libraries in a single session.',
        'summary': 'Google\'s AI with 750M+ monthly users. Deep Google Workspace integration, 1M+ token context, and Veo 3.1 video gen.'
    },
    'midjourney': {
        'price_detail': 'Basic $10/mo (200 images) / Standard $30/mo / Pro $60/mo / Mega $120/mo',
        'description': 'Midjourney remains the gold standard for AI-generated artistic imagery in 2026. The current V7 model delivers unprecedented photorealism and artistic control, while V8 is in early alpha with rumored video generation capabilities. Accessible via Discord or the dedicated web app, Midjourney continues to be the go-to tool for concept artists, game developers, and creative professionals.',
        'summary': 'The gold standard for AI image generation. V7 model with unparalleled artistic quality and photorealism. V8 in alpha.'
    },
    'claude': {
        'price_detail': 'Free / Pro $20/mo / Max $100-200/mo / Team $25/user/mo / Enterprise custom',
        'description': 'Claude by Anthropic is the premier AI assistant for deep analysis, long-form writing, and complex reasoning. The 2026 flagship model Claude Opus 4.7 (knowledge cutoff January 2026) excels at nuanced tasks requiring careful thought. Claude\'s 500K+ token context window enables analysis of entire books and codebases. The introduction of Claude Code has made Anthropic a leader in AI-assisted software development, with the majority of Anthropic\'s own code now written by Claude.',
        'summary': 'Anthropic\'s AI for deep reasoning and analysis. Opus 4.7 model, 500K+ context, and Claude Code for autonomous development.'
    }
}

for tool in data['tools']:
    tid = tool['id']
    if tid in updates:
        for key, value in updates[tid].items():
            tool[key] = value
        print(f"  Updated: {tool['name']}")

# Save
with open(f'{BASE}/data/tools.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n{'='*50}")
print(f"Summary:")
print(f"  New tools added: {len(new_active)}")
print(f"  Existing tools updated: {len(updates)}")
print(f"  Upcoming remaining: {len(data['upcoming'])}")
print(f"  Total tools: {len(data['tools'])}")
print(f"  Total categories: {len(data['categories'])}")
