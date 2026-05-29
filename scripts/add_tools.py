#!/usr/bin/env python3
"""Add 21 new tools to tools.json and regenerate data.js"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load current data
with open(os.path.join(BASE, 'data', 'tools.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {t['id'] for t in data['tools']}

new_tools = [
    # ===== AI Chat (1 new) =====
    {
        "id": "deepseek",
        "name": "DeepSeek",
        "url": "https://chat.deepseek.com",
        "affiliate": None,
        "category": "chat",
        "pricing": "Freemium",
        "price_detail": "Free / API pay-as-you-go",
        "rating": 9.2,
        "summary": "The open-source AI powerhouse. R1 reasoning model rivals GPT-4, free web & app access.",
        "description": "DeepSeek shook the AI world with its R1 reasoning model, matching GPT-4 performance at a fraction of the cost. The free chat interface offers web search, file upload, and a massive 1M token context window. Open-source models available via API at extremely competitive prices.",
        "tutorial": "1. Go to chat.deepseek.com and sign up (free). 2. Type your question — DeepSeek shows its reasoning process (Chain of Thought) before answering. 3. Toggle 'Deep Think' mode for complex problems — the model spends more time reasoning through math, coding, and logic. 4. Upload files (PDFs, images, code) for analysis using the attachment button. 5. Enable web search for real-time information (toggle next to input box). 6. Use the mobile app (iOS/Android) for on-the-go access. The API is priced at $0.14/M input tokens for R1 — significantly cheaper than GPT-4.",
        "pros": ["R1 reasoning is outstanding", "Completely free chat", "1M token context", "Cheapest API pricing"],
        "cons": ["Occasional server overload", "Chinese censorship on sensitive topics", "Smaller ecosystem than OpenAI"],
        "best_for": "Developers, researchers, and anyone wanting GPT-4 level AI for free",
        "alternatives": ["chatgpt", "claude", "perplexity"],
        "tags": ["chatbot", "reasoning", "open-source", "coding"],
        "featured": True
    },
    
    # ===== AI Image (3 new) =====
    {
        "id": "leonardo",
        "name": "Leonardo AI",
        "url": "https://leonardo.ai",
        "affiliate": None,
        "category": "image",
        "pricing": "Freemium",
        "price_detail": "Free (150 tokens/day) / Apprentice $12/mo / Artisan $30/mo / Maestro $60/mo",
        "rating": 8.7,
        "summary": "Gaming & design-focused AI image generator. Train custom models on your own artwork.",
        "description": "Leonardo AI is purpose-built for game assets, concept art, and design work. Its standout feature is custom model training — upload 10-20 images of your art style, and Leonardo learns to generate images matching your aesthetic. The platform includes Realtime Canvas (draw + AI completes) and Realtime Gen (see images appear as you type).",
        "tutorial": "1. Sign up at leonardo.ai (free: 150 tokens/day). 2. Choose a preset model (Leonardo Lightning, Anime, Photography, etc.) or train your own. 3. Type a prompt and hit Generate — outputs are consistently high quality. 4. Use Image Guidance: upload a reference image to control composition (similar to ControlNet). 5. Try Realtime Canvas: sketch a rough drawing on the left, AI renders it photorealistic on the right. 6. For game assets: use the 'Tiling' toggle to generate seamless textures. Tutorial on training custom models: Upload 15-20 images → name the model → wait 30 min → generate in your style forever.",
        "pros": ["Custom model training", "Game asset optimized", "Realtime Canvas is magic", "Good free tier"],
        "cons": ["Less artistic than Midjourney", "Complex UI with many options", "Credit system confusing"],
        "best_for": "Game developers, concept artists, and designers who need consistent visual styles",
        "alternatives": ["midjourney", "stable-diffusion", "dalle"],
        "tags": ["image-generation", "game-dev", "design", "custom-models"],
        "featured": True
    },
    {
        "id": "firefly",
        "name": "Adobe Firefly",
        "url": "https://firefly.adobe.com",
        "affiliate": None,
        "category": "image",
        "pricing": "Freemium",
        "price_detail": "Free (25 credits/mo) / Premium $4.99/mo (100 credits)",
        "rating": 8.3,
        "summary": "Adobe's commercially-safe AI image generator. Trained on licensed content — no copyright risk.",
        "description": "Adobe Firefly is the only major AI image generator trained exclusively on licensed and public domain content, making it the safest choice for commercial use. It integrates deeply with Photoshop, Illustrator, and Express. Features include Generative Fill, Text to Image, Text Effects, and Generative Recolor.",
        "tutorial": "1. Go to firefly.adobe.com and sign in with Adobe ID (free tier available). 2. For text-to-image: describe what you want, choose aspect ratio and style (Photo, Art, Graphic). 3. Generative Fill in Photoshop: select an area → click 'Generative Fill' → describe what should be there → Firefly fills it seamlessly. 4. Text Effects: type a word ('FIRE'), describe the effect ('made of flames and smoke'), get editable vector text. 5. Generative Recolor: upload a vector, describe a color palette ('pastel sunset colors'), Firefly recolors instantly. 6. All Firefly-generated content includes Content Credentials (digital nutrition label) proving AI origin.",
        "pros": ["Commercially safe (licensed training)", "Deep Adobe integration", "Generative Fill in Photoshop", "Content Credentials"],
        "cons": ["Less creative than Midjourney", "More expensive for heavy use", "Adobe ecosystem lock-in"],
        "best_for": "Professional designers, agencies, and anyone who needs legally safe AI images",
        "alternatives": ["midjourney", "dalle", "leonardo"],
        "tags": ["image-generation", "adobe", "commercial-safe", "design"],
        "featured": False
    },
    {
        "id": "ideogram",
        "name": "Ideogram",
        "url": "https://ideogram.ai",
        "affiliate": None,
        "category": "image",
        "pricing": "Freemium",
        "price_detail": "Free (20 slow gen/day) / Plus $8/mo / Pro $20/mo",
        "rating": 8.4,
        "summary": "Best AI for text in images. Logos, posters, memes — text that's actually readable.",
        "description": "Ideogram cracked the hardest problem in AI image generation: rendering readable text within images. It excels at logos, posters, t-shirt designs, and memes where text accuracy matters. The V2 model produces stunning images with precise typography. Web app is clean and beginner-friendly.",
        "tutorial": "1. Go to ideogram.ai and sign up with Google (free: 20 slow generations/day). 2. Type your prompt — include text in quotes: 'A vintage travel poster saying EXPLORE in bold gold letters, art deco style'. 3. Choose aspect ratio: square (1:1), landscape (16:9), portrait (10:16). 4. Pick a style: Realistic, Design, 3D, Anime, etc. 5. For logos: 'Minimalist tech logo, the word NEXUS in sleek sans-serif, blue and purple gradient, clean background'. 6. Remix feature: click any public image → Remix → modify the prompt to create variations. Plus plan ($8/mo) gives 400 fast generations + private mode.",
        "pros": ["Best text rendering in AI images", "Logo/poster specialist", "Clean simple UI", "Remix community"],
        "cons": ["Less artistic range than Midjourney", "Smaller community", "Free tier is slow"],
        "best_for": "Graphic designers, marketers, and anyone creating images with text (logos, posters, memes)",
        "alternatives": ["midjourney", "dalle", "canva-ai"],
        "tags": ["image-generation", "text-in-image", "logo-design", "typography"],
        "featured": False
    },
    
    # ===== AI Video (2 new) =====
    {
        "id": "pika",
        "name": "Pika Labs",
        "url": "https://pika.art",
        "affiliate": None,
        "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free (limited) / Standard $10/mo / Unlimited $35/mo / Pro $70/mo",
        "rating": 8.5,
        "summary": "Fast, creative AI video generator. Pikaffects make anything explode, melt, or inflate.",
        "description": "Pika is the most fun AI video tool. Its Pikaffects feature lets you apply wild transformations to images and videos — make objects explode, melt, inflate, or turn to cake. The Pika 2.0 model generates high-quality videos from text, images, or existing clips. Web app is dead simple: describe, click, watch.",
        "tutorial": "1. Sign up at pika.art (free credits for new users). 2. Click 'Text to Video': describe your scene — 'A cute corgi puppy running through a field of sunflowers, slow motion, cinematic'. 3. Try Pikaffects: upload any image → pick an effect (Explode, Melt, Inflate, Cake-ify, etc.) → watch the magic. 4. Image to Video: upload a photo + describe how it should move ('The person turns and smiles at the camera'). 5. Use 'Lip Sync': upload a video of someone speaking + audio clip → Pika syncs the lips automatically. 6. Adjust 'Motion Strength' (1-10) to control how much the scene changes. Standard plan ($10/mo) removes watermark and adds HD export.",
        "pros": ["Pikaffects are uniquely fun", "Very fast generation", "Simple UX", "Lip sync feature"],
        "cons": ["Shorter clips than Runway", "Less photorealistic", "Watermark on free tier"],
        "best_for": "Social media creators, meme makers, and anyone who wants fast, fun AI videos",
        "alternatives": ["runway", "sora", "kling"],
        "tags": ["video-generation", "creative", "social-media", "fun"],
        "featured": True
    },
    {
        "id": "sora",
        "name": "Sora",
        "url": "https://sora.com",
        "affiliate": None,
        "category": "video",
        "pricing": "Bundled",
        "price_detail": "Included with ChatGPT Plus ($20/mo) / Pro ($200/mo)",
        "rating": 8.8,
        "summary": "OpenAI's groundbreaking video generator. Photorealistic clips up to 60 seconds.",
        "description": "Sora by OpenAI set a new standard for AI video generation. It creates stunningly realistic video clips from text prompts, with a deep understanding of physics, lighting, and camera movement. Included with ChatGPT Plus/Pro subscriptions. Storyboard feature lets you chain multiple prompts into a narrative timeline.",
        "tutorial": "1. Subscribe to ChatGPT Plus ($20/mo) or Pro ($200/mo) at chat.openai.com. 2. Access Sora at sora.com (linked from your OpenAI account). 3. Type a detailed prompt: 'A Tokyo street at night, rain falling, neon signs reflecting on wet pavement, a woman with a transparent umbrella walks past a ramen shop, slow motion, cinematic lighting'. 4. Use Storyboard: chain multiple scenes together on a timeline — 'Scene 1: wide shot of city → Scene 2: close-up of umbrella → Scene 3: reveal face'. 5. For best results, include camera directions: 'dolly zoom', 'aerial shot', 'tracking shot'. 6. Plus users get 50 priority videos/month at 480p; Pro users get 500 videos at 1080p, up to 60 seconds.",
        "pros": ["Industry-leading photorealism", "Storyboard for narratives", "Physics understanding", "Up to 60 seconds"],
        "cons": ["Requires ChatGPT subscription", "Limited to Plus/Pro users", "Strict content filtering", "High demand = wait times"],
        "best_for": "Filmmakers, content creators, and anyone who wants the most realistic AI video available",
        "alternatives": ["runway", "pika", "kling"],
        "tags": ["video-generation", "openai", "photorealistic", "storyboard"],
        "featured": True
    },
    
    # ===== AI Coding (2 new) =====
    {
        "id": "windsurf",
        "name": "Windsurf",
        "url": "https://codeium.com/windsurf",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $15/mo",
        "rating": 9.0,
        "summary": "AI-native IDE with 'Cascade' — the first agentic AI that reads, writes, and runs code across your entire project.",
        "description": "Windsurf (by Codeium) introduced Cascade, an AI agent that doesn't just autocomplete — it understands your full codebase and can create, edit, and run files across multiple directories. It's like having a senior developer who reads your entire project before making changes. The free tier is remarkably generous.",
        "tutorial": "1. Download Windsurf from codeium.com/windsurf (Windows/Mac/Linux). 2. Sign in with Google or GitHub. 3. Open your project folder — Windsurf indexes your entire codebase. 4. Press Cmd+L (Ctrl+L) to open Cascade: describe what you want ('Build a REST API endpoint for user registration with input validation'). 5. Cascade shows a plan first, then executes file by file — you approve/reject each change. 6. Press Cmd+I for inline editing: select code, describe the change ('Add try/catch error handling'), Cascade rewrites it. Free tier: unlimited autocomplete + 200 Cascade premium requests/month.",
        "pros": ["Cascade AI agent is revolutionary", "Reads entire codebase before acting", "Generous free tier", "Beautiful UI"],
        "cons": ["Newer product, growing pains", "Less plugin ecosystem than VS Code", "Pro needed for heavy Cascade use"],
        "best_for": "Developers who want an AI that can handle multi-file, multi-step coding tasks autonomously",
        "alternatives": ["cursor", "copilot", "cody"],
        "tags": ["code-editor", "ai-agent", "ide", "developer-tools"],
        "featured": True
    },
    {
        "id": "replit-ai",
        "name": "Replit AI",
        "url": "https://replit.com",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free / Core $15/mo / Teams $33/user/mo",
        "rating": 8.2,
        "summary": "Code in your browser. AI builds entire apps from a single prompt. No setup needed.",
        "description": "Replit is a browser-based development environment with AI deeply embedded. Its Agent can build complete web apps, APIs, and games from natural language prompts. Everything runs in the cloud — no local setup, no dependency hell. Great for prototyping, learning, and shipping MVPs fast.",
        "tutorial": "1. Go to replit.com and sign up (free). 2. Click 'Create Repl' → pick a template (Python, Node.js, HTML/CSS/JS, etc.). 3. Press Cmd+I (Ctrl+I) to open the AI panel: describe your app — 'Create a to-do list app with dark mode and local storage'. 4. The AI generates the code, installs dependencies, and runs it — all in your browser. 5. Ask follow-ups: 'Add a due date feature with a date picker' — AI edits the code and restarts. 6. Deploy with one click: your app gets a public URL (username.replit.app). Core plan ($15/mo) for always-on deployment and more compute.",
        "pros": ["Zero setup — works in browser", "AI builds full apps from prompts", "Instant deployment", "Great for learning"],
        "cons": ["Not for large production apps", "Limited compute on free tier", "Vendor lock-in concerns"],
        "best_for": "Beginners, students, and indie makers who want to go from idea to deployed app in minutes",
        "alternatives": ["cursor", "copilot", "codeium"],
        "tags": ["online-ide", "browser-based", "code-assistant", "deployment"],
        "featured": False
    },
    
    # ===== AI Audio (1 new) =====
    {
        "id": "udio",
        "name": "Udio",
        "url": "https://www.udio.com",
        "affiliate": None,
        "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free (10 credits/day) / Standard $10/mo / Pro $30/mo",
        "rating": 9.0,
        "summary": "Suno's top rival. Some say Udio makes even better music. Incredible vocal quality.",
        "description": "Udio is the strongest competitor to Suno, founded by ex-Google DeepMind researchers. Many users prefer Udio's vocal quality and musical coherence — voices sound more natural and the production feels more polished. Supports custom lyrics, genre mixing, and extending/remixing tracks. V2 model is remarkably good.",
        "tutorial": "1. Go to udio.com and sign up (10 free credits/day). 2. Describe your song in the text box: 'A melancholic indie folk song about autumn, fingerpicked acoustic guitar, soft male vocals, minimal production'. 3. Or write custom lyrics: paste them in the 'Custom' tab, add genre tags in brackets: '[Verse][Chorus][Bridge]'. 4. Click 'Create' — Udio generates two 30-second clips. Click 'Extend' on the one you like to add more sections. 5. Use 'Remix' to create variations: adjust the 'variance' slider (low = subtle changes, high = wild variations). 6. Download your finished song as MP3 or WAV. Standard plan ($10/mo) for commercial use rights and more generations.",
        "pros": ["Incredible vocal quality", "Natural sounding production", "Extend/remix features", "Strong community"],
        "cons": ["Shorter generations than Suno", "Smaller user base", "Custom mode has learning curve"],
        "best_for": "Music creators who want the most natural-sounding AI vocals",
        "alternatives": ["suno", "aiva", "soundraw"],
        "tags": ["music", "audio-generation", "creative", "songwriting"],
        "featured": True
    },
    
    # ===== AI Writing (1 new) =====
    {
        "id": "copy-ai",
        "name": "Copy.ai",
        "url": "https://www.copy.ai",
        "affiliate": None,
        "category": "writing",
        "pricing": "Freemium",
        "price_detail": "Free (2,000 words/mo) / Pro $49/mo / Team $249/mo",
        "rating": 8.1,
        "summary": "AI for GTM teams. Automate sales outreach, content marketing, and lead research.",
        "description": "Copy.ai has evolved from a copywriting tool to a full GTM (Go-To-Market) AI platform. It builds automated workflows for sales prospecting, content creation, and lead enrichment. The no-code workflow builder connects AI models to your sales and marketing stack. Free tier gives 2,000 words/month.",
        "tutorial": "1. Sign up at copy.ai (free, no credit card). 2. From the dashboard, choose a workflow: 'Blog Post Wizard', 'Cold Email Sequence', 'Social Media Calendar', etc. 3. For blog posts: enter topic + target audience + keywords → AI generates outline → approve → AI writes full article. 4. For sales outreach: connect LinkedIn Sales Navigator → Copy.ai researches prospects → drafts personalized cold emails. 5. Use Brand Voice: upload your style guide or example content → Copy.ai matches your tone across all outputs. 6. Create automated workflows: 'When new blog post is approved → generate 5 social media posts + email newsletter draft'. Pro plan ($49/mo) for unlimited words and workflows.",
        "pros": ["No-code AI workflows", "Sales + marketing automation", "Brand voice feature", "Good free tier"],
        "cons": ["Expensive Pro plan", "GTM focus may not fit solo creators", "Less creative than direct ChatGPT use"],
        "best_for": "Marketing teams, sales teams, and businesses automating their GTM content engine",
        "alternatives": ["jasper", "writesonic", "rytr"],
        "tags": ["writing", "marketing", "automation", "sales"],
        "featured": False
    },
    
    # ===== AI Design (1 new) =====
    {
        "id": "figma-ai",
        "name": "Figma AI",
        "url": "https://www.figma.com/ai",
        "affiliate": None,
        "category": "design",
        "pricing": "Freemium",
        "price_detail": "Free / Professional $15/mo / Organization $45/user/mo",
        "rating": 8.8,
        "summary": "AI inside the world's #1 design tool. Generate designs, rename layers, auto-prototype.",
        "description": "Figma AI brings generative AI into Figma's design platform. Turn text descriptions into UI mockups, automatically generate design variations, rename all your messy layers in one click, and create interactive prototypes from static designs. First drafts feature jumps from blank canvas to design in seconds.",
        "tutorial": "1. Open Figma (free account at figma.com). 2. Click 'Actions' → 'First Draft': describe your design — 'A mobile app home screen for a fitness tracker with workout stats, heart rate, and a start running button'. 3. AI generates a complete UI mockup with proper spacing, fonts, and components. 4. Select any text → 'AI > Rewrite' to generate alternative copy. 5. 'AI > Rename Layers': turn 'Rectangle 1427' into 'Sign Up Button' across your entire file. 6. Generate prototype interactions: select a button → 'AI > Add Interaction' → describe ('Navigate to dashboard with slide animation'). Free tier covers basic AI features; Professional ($15/mo) for unlimited.",
        "pros": ["World's #1 design tool", "AI-generated mockups from text", "Layer renaming is huge time saver", "Team collaboration"],
        "cons": ["AI features still rolling out", "Free tier limits AI usage", "Learning curve for Figma itself"],
        "best_for": "UX/UI designers, product teams, and anyone designing digital interfaces",
        "alternatives": ["canva-ai", "microsoft-designer", "uxpilot"],
        "tags": ["design", "ui-design", "prototyping", "collaboration"],
        "featured": False
    },
    
    # ===== AI Productivity (1 new) =====
    {
        "id": "taskade",
        "name": "Taskade",
        "url": "https://www.taskade.com",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $8/mo / Business $16/user/mo",
        "rating": 8.3,
        "summary": "AI-powered workspace. Mind maps, task lists, and AI agents working together in one tool.",
        "description": "Taskade combines project management, mind mapping, and AI agents into one workspace. Its AI can generate task breakdowns, create mind maps from topics, automate project workflows, and even act as autonomous agents that complete research tasks. Built-in chat with AI across your entire workspace.",
        "tutorial": "1. Sign up at taskade.com (free for up to 5 workspaces). 2. Create a new project: 'Plan product launch' → AI auto-generates task breakdown with subtasks and deadlines. 3. Switch views: the same project can be viewed as a list, board (Kanban), mind map, or table — AI-generated content works in all views. 4. Use AI agents: type '@agent research competitors for [your product]' → the agent browses the web and adds findings as structured notes. 5. Mind map mode: start with a topic → AI generates branches and subtopics → drag to reorganize → one click back to task list. 6. Workspace chat: ask AI 'What tasks are overdue?' or 'Summarize this week's progress'. Pro plan ($8/mo) for unlimited AI and collaboration.",
        "pros": ["Multiple views (list/mind map/board)", "AI agents can research autonomously", "Generous free tier", "Real-time collaboration"],
        "cons": ["UI can feel cluttered", "AI agents sometimes need retries", "Less polished than Notion"],
        "best_for": "Project managers, students, and teams who want AI-powered task organization",
        "alternatives": ["notion-ai", "mem", "clickup-ai"],
        "tags": ["productivity", "project-management", "mind-mapping", "ai-agents"],
        "featured": False
    },
    
    # ===== AI Marketing (4 new — fills empty category) =====
    {
        "id": "hubspot-ai",
        "name": "HubSpot AI",
        "url": "https://www.hubspot.com/products/ai",
        "affiliate": None,
        "category": "marketing",
        "pricing": "Freemium",
        "price_detail": "Free tools / Starter $20/mo / Professional $890/mo",
        "rating": 8.5,
        "summary": "AI baked into the world's #1 CRM platform. Content, emails, chatbots, and analytics.",
        "description": "HubSpot's AI suite (Breeze) is embedded across their marketing, sales, and service hubs. AI content writer generates blog posts, landing pages, and emails. AI chatbot handles customer inquiries. Predictive lead scoring identifies your best prospects. Available in both free and paid HubSpot plans.",
        "tutorial": "1. Sign up at hubspot.com (free CRM + AI tools). 2. In Marketing Hub: go to Content → 'Create with AI' → describe your content (type, topic, tone) → AI drafts it. 3. For emails: open Email tool → 'Generate with AI' → enter goal + audience → AI writes subject line + body. 4. AI Chatbot: go to Conversations → Chatflows → 'Create with AI' → set chatbot purpose (qualify leads, support, book meetings). 5. Social Media AI: connect your accounts → AI suggests post content based on your industry and trending topics. 6. AI Reporting: ask questions like 'What channel brought the most leads this month?' — AI builds a report. Free tools are generous; paid plans scale with business size.",
        "pros": ["Full CRM integration", "Free tier is solid", "Multi-channel AI (email/social/chat)", "Predictive analytics"],
        "cons": ["Pro plans are expensive", "Complex platform to navigate", "AI features vary by plan tier"],
        "best_for": "Marketing teams and businesses already using or considering HubSpot CRM",
        "alternatives": ["jasper", "copy-ai", "writesonic"],
        "tags": ["marketing", "crm", "automation", "analytics"],
        "featured": False
    },
    {
        "id": "writesonic",
        "name": "Writesonic",
        "url": "https://writesonic.com",
        "affiliate": None,
        "category": "marketing",
        "pricing": "Freemium",
        "price_detail": "Free (25 credits) / Individual $16/mo / Standard $79/mo",
        "rating": 8.0,
        "summary": "AI content platform with SEO optimization built in. Rank higher while writing faster.",
        "description": "Writesonic combines AI writing with real-time SEO data. It researches competitors, identifies keywords, and generates content that's optimized to rank. The platform covers blogs, ads, emails, product descriptions, and social media. ChatSonic gives you ChatGPT-like conversations with web search.",
        "tutorial": "1. Sign up at writesonic.com (25 free credits, about 12,500 words). 2. Choose 'AI Article Writer': enter your topic + keywords → AI researches top ranking pages → generates an SEO-optimized outline → writes the full article. 3. SEO Checker: paste your content → get a score + specific suggestions for improving rankings. 4. ChatSonic: like ChatGPT but with real-time web access and image generation. 5. For ads: choose 'AI Ad Copy' → select platform (Google/Facebook/LinkedIn) → enter product details → AI generates multiple ad variations with headlines and descriptions. 6. Brand Voice: upload your style guide → Writesonic matches your tone across all content. Individual plan ($16/mo) for unlimited words.",
        "pros": ["SEO optimization built in", "Competitor research feature", "ChatSonic with web search", "Landing page generator"],
        "cons": ["Credit system limiting", "SEO data quality varies", "Output can feel templated"],
        "best_for": "Content marketers and SEO specialists who want AI that understands rankings",
        "alternatives": ["jasper", "surfer-seo", "copy-ai"],
        "tags": ["marketing", "seo", "content-writing", "ads"],
        "featured": False
    },
    {
        "id": "surfer-seo",
        "name": "Surfer SEO",
        "url": "https://surferseo.com",
        "affiliate": None,
        "category": "marketing",
        "pricing": "Paid",
        "price_detail": "Essential $89/mo / Scale $129/mo / Enterprise $219/mo",
        "rating": 8.6,
        "summary": "AI-powered SEO content optimization. Analyze top 50 ranking pages and optimize your content to beat them.",
        "description": "Surfer SEO doesn't just write content — it reverse-engineers what's ranking on Google and tells you exactly how to optimize. It analyzes the top 50 results for your keyword, identifies common terms, structure patterns, and word counts, then gives you a real-time score as you write or optimize content.",
        "tutorial": "1. Sign up at surferseo.com (7-day money-back guarantee). 2. Click 'Content Editor' → enter your target keyword + location → Surfer analyzes top 50 ranking pages. 3. You'll see: recommended word count, headings structure, key terms to include (with frequency), and questions to answer. 4. Write directly in Surfer or paste your draft — the Content Score updates in real time as you optimize. 5. Aim for a green score (70+) for best ranking potential. 6. Use 'Audit' to analyze existing pages: paste URL → Surfer shows what's missing vs. competitors → implement suggestions to climb rankings. The platform also includes 'Grow Flow' — weekly AI-generated SEO tasks prioritized by impact.",
        "pros": ["Data-driven SEO optimization", "Real-time content scoring", "Competitor analysis", "Grow Flow weekly tasks"],
        "cons": ["Expensive starting price", "No free tier", "Only for SEO content (not other writing)"],
        "best_for": "SEO specialists, content managers, and businesses serious about organic search traffic",
        "alternatives": ["writesonic", "clearscope", "frasr"],
        "tags": ["marketing", "seo", "content-optimization", "analytics"],
        "featured": False
    },
    {
        "id": "adcreative",
        "name": "AdCreative AI",
        "url": "https://www.adcreative.ai",
        "affiliate": None,
        "category": "marketing",
        "pricing": "Paid",
        "price_detail": "Startup $29/mo / Professional $59/mo / Agency $149/mo",
        "rating": 8.2,
        "summary": "AI that creates ad creatives proven to convert. Generates hundreds of ad variations in minutes.",
        "description": "AdCreative AI uses machine learning trained on millions of high-performing ads to generate creatives that are statistically more likely to convert. Upload your brand assets, describe your product, and it generates hundreds of ad variations for Facebook, Instagram, Google, LinkedIn, and TikTok — complete with copy.",
        "tutorial": "1. Sign up at adcreative.ai (7-day free trial). 2. Connect your ad accounts (Facebook, Google, LinkedIn, etc.). 3. Upload brand assets: logo, brand colors, product images (transparent background works best). 4. Create a project: describe your product, target audience, and unique selling point. 5. AI generates 100+ ad variations — each with a Creative Score predicting conversion probability. 6. Pick the best ones and export directly to your ad accounts, or download as images. The platform learns from your ad performance over time and improves recommendations.",
        "pros": ["Creative scoring predicts performance", "Hundreds of variations fast", "Direct integration with ad platforms", "Learns from your results"],
        "cons": ["No free tier (trial only)", "Limited to ad creatives", "Needs good brand assets to work well"],
        "best_for": "Marketing teams and agencies running paid ad campaigns at scale",
        "alternatives": ["canva-ai", "creatopy", "bannerflow"],
        "tags": ["marketing", "ads", "creative-design", "automation"],
        "featured": False
    },
    
    # ===== AI Education (4 new — fills empty category) =====
    {
        "id": "khanmigo",
        "name": "Khanmigo",
        "url": "https://www.khanmigo.ai",
        "affiliate": None,
        "category": "education",
        "pricing": "Paid",
        "price_detail": "$4/mo or $44/year",
        "rating": 8.7,
        "summary": "AI tutor from Khan Academy. Doesn't give answers — guides students to discover them. For learners & teachers.",
        "description": "Khanmigo is Khan Academy's AI tutor, built on GPT-4. Unlike ChatGPT (which just gives answers), Khanmigo uses Socratic questioning to guide students toward understanding. It can tutor math, science, humanities, and even help with essay writing. Teacher mode includes lesson planning, rubric generation, and progress tracking.",
        "tutorial": "1. Go to khanmigo.ai and sign up ($4/month, 50% sibling discount). 2. Start a tutoring session: pick a subject (Math, Science, Humanities, Coding). 3. Type your question or upload a problem — Khanmigo won't give the answer. It asks guiding questions: 'What do you think the first step is? Why?'. 4. For essay writing: paste your draft → Khanmigo asks 'What's your thesis? Does this paragraph support it?' (never writes for you). 5. Teacher mode: generate lesson plans, create rubric-aligned assessments, and get class-level progress insights. 6. Parent mode: see what your child is working on and receive weekly progress summaries. Also includes AI history simulations — chat with historical figures like Albert Einstein.",
        "pros": ["Research-backed pedagogy", "Never gives answers — teaches thinking", "Covers all K-12 subjects", "Teacher tools included"],
        "cons": ["$4/month (Khan Academy content is free)", "Not for professional/adult learning", "Requires patience with Socratic method"],
        "best_for": "Students (K-12), parents, and teachers who want pedagogically sound AI tutoring",
        "alternatives": ["chatgpt", "socratic", "quizlet-ai"],
        "tags": ["education", "tutoring", "k-12", "teachers"],
        "featured": True
    },
    {
        "id": "duolingo-max",
        "name": "Duolingo Max",
        "url": "https://www.duolingo.com/max",
        "affiliate": None,
        "category": "education",
        "pricing": "Paid",
        "price_detail": "$29.99/mo or $167.99/year",
        "rating": 8.4,
        "summary": "Duolingo supercharged with GPT-4. Roleplay conversations and explain-my-answer feedback.",
        "description": "Duolingo Max adds two GPT-4 powered features to Duolingo Super: 'Explain My Answer' breaks down why your response was right or wrong with grammar explanations, and 'Roleplay' lets you have freeform conversations with AI characters in your target language — practicing real-world scenarios like ordering coffee or negotiating a hotel room.",
        "tutorial": "1. Download Duolingo app (iOS/Android) and subscribe to Max ($29.99/mo). 2. Start any lesson — when you get an answer wrong, tap 'Explain My Answer' for a GPT-4 breakdown of the grammar and vocabulary. 3. After certain lessons, tap 'Roleplay': you'll enter a scenario (e.g., 'You're at a Parisian bakery') and have a natural conversation with an AI character. 4. The AI adapts to your level — it'll use simpler language if you struggle, more complex if you're advanced. 5. Unlimited hearts (mistakes) and personalized practice sessions. 6. Available for Spanish and French (English speakers) with more languages rolling out. The Super plan ($12.99/mo) is enough for most learners; Max adds the two GPT-4 features.",
        "pros": ["Gamified learning that works", "Roleplay is genuinely useful", "Grammar explanations on demand", "Massive language course library"],
        "cons": ["Expensive vs regular Duolingo", "GPT-4 features limited to few languages", "Still needs self-discipline to be consistent"],
        "best_for": "Language learners who want AI-powered conversation practice and grammar feedback",
        "alternatives": ["chatgpt", "memrise", "babbel"],
        "tags": ["education", "language-learning", "conversation", "mobile"],
        "featured": False
    },
    {
        "id": "quizlet-ai",
        "name": "Quizlet AI",
        "url": "https://quizlet.com/features/q-chat",
        "affiliate": None,
        "category": "education",
        "pricing": "Freemium",
        "price_detail": "Free (limited) / Plus $7.99/mo or $35.99/year",
        "rating": 8.1,
        "summary": "AI study tools for 60M+ students. Q-Chat tutor, Magic Notes, and AI-generated flashcards.",
        "description": "Quizlet's AI suite helps students study smarter. Q-Chat is an AI tutor that quizzes you on your study material using natural conversation. Magic Notes turns your class notes into flashcards, practice tests, and study guides in seconds. AI-powered 'Learn' mode adapts to what you don't know.",
        "tutorial": "1. Sign up at quizlet.com (free). 2. Create a study set: paste your notes, textbook excerpts, or vocabulary lists → AI generates flashcards with images and audio. 3. Use Q-Chat: pick a study set → start a conversation → the AI asks you questions, gives hints, and adapts to your weak areas. 4. Magic Notes: upload a PDF or photo of your handwritten notes → Quizlet converts them into an organized study set with key terms highlighted. 5. 'Learn' mode: AI tracks your progress and keeps quizzing you on what you get wrong until you master it. 6. 'Test' mode: AI generates a practice test with multiple question types (multiple choice, written, true/false) based on your material. Plus ($7.99/mo) for ad-free and advanced AI features.",
        "pros": ["60M+ user community = huge study set library", "Magic Notes is a time-saver", "AI adapts to your learning gaps", "Multiple study modes"],
        "cons": ["Plus plan needed for best AI features", "Can be distracting with gamification", "Less deep than Khanmigo"],
        "best_for": "Students who want to study more efficiently with AI-generated flashcards and quizzes",
        "alternatives": ["khanmigo", "anki", "studocu"],
        "tags": ["education", "flashcards", "study-tools", "ai-tutor"],
        "featured": False
    },
    {
        "id": "socratic",
        "name": "Socratic by Google",
        "url": "https://socratic.org",
        "affiliate": None,
        "category": "education",
        "pricing": "Free",
        "price_detail": "Completely free",
        "rating": 8.0,
        "summary": "Google's AI homework helper. Take a photo of any problem, get step-by-step explanations.",
        "description": "Socratic is Google's free AI learning app for high school and college students. Point your camera at a math problem, chemistry equation, or history question — Socratic's AI identifies the problem and provides step-by-step explanations, videos, and curated web resources. Built on Google's AI and search technology.",
        "tutorial": "1. Download the Socratic app (iOS/Android) — it's 100% free. 2. Open the app and point your camera at a homework problem (math, science, history, literature). 3. Tap the shutter — Socratic's AI identifies the subject and specific concept. 4. You'll see: a step-by-step solution, top video explanations from YouTube/Khan Academy, and related Q&A from the web. 5. For math: the app shows each step of the solution with explanations of WHY each step works. 6. For essays: type a topic ('Explain the causes of WWI') → Socratic surfaces the most relevant educational resources. Subjects covered: Algebra, Geometry, Trigonometry, Calculus, Biology, Chemistry, Physics, History, Literature.",
        "pros": ["100% free", "Camera-based problem solving is magical", "Google-quality search results", "Covers most high school subjects"],
        "cons": ["App-only (no web version)", "Struggles with very advanced problems", "Limited to established subjects"],
        "best_for": "High school and college students who need quick, free homework help",
        "alternatives": ["khanmigo", "photamath", "chatgpt"],
        "tags": ["education", "homework-help", "free", "mobile"],
        "featured": False
    },
]

# Filter out any that already exist
actually_new = [t for t in new_tools if t['id'] not in existing_ids]
print(f'Adding {len(actually_new)} new tools. Skipping {len(new_tools) - len(actually_new)} duplicates.')

# Add new tools
data['tools'].extend(actually_new)

# Clear upcoming list (all 5 converted to real tools)
data['upcoming'] = [
    {"name": "Grok (xAI)", "category": "chat", "eta": "Coming soon"},
    {"name": "Synthesia", "category": "video", "eta": "Coming soon"},
    {"name": "Claude Code", "category": "coding", "eta": "Coming soon"},
    {"name": "Gamma", "category": "design", "eta": "Coming soon"},
    {"name": "Luma Dream Machine", "category": "video", "eta": "Coming soon"},
]

# Add more comparison pairs
new_comparisons = [
    {"id": "chatgpt-vs-deepseek", "title": "ChatGPT vs DeepSeek", "tools": ["chatgpt", "deepseek"]},
    {"id": "claude-vs-gemini", "title": "Claude vs Gemini", "tools": ["claude", "gemini"]},
    {"id": "suno-vs-udio", "title": "Suno vs Udio", "tools": ["suno", "udio"]},
    {"id": "midjourney-vs-stable-diffusion", "title": "Midjourney vs Stable Diffusion", "tools": ["midjourney", "stable-diffusion"]},
    {"id": "windsurf-vs-cursor", "title": "Windsurf vs Cursor", "tools": ["windsurf", "cursor"]},
    {"id": "runway-vs-sora", "title": "Runway vs Sora", "tools": ["runway", "sora"]},
    {"id": "ideogram-vs-dalle", "title": "Ideogram vs DALL-E 3", "tools": ["ideogram", "dalle"]},
    {"id": "pika-vs-runway", "title": "Pika Labs vs Runway", "tools": ["pika", "runway"]},
    {"id": "chatgpt-vs-perplexity", "title": "ChatGPT vs Perplexity AI", "tools": ["chatgpt", "perplexity"]},
    {"id": "khanmigo-vs-duolingo", "title": "Khanmigo vs Duolingo Max", "tools": ["khanmigo", "duolingo-max"]},
]
existing_comp_ids = {c['id'] for c in data['comparisons']}
new_comps = [c for c in new_comparisons if c['id'] not in existing_comp_ids]
data['comparisons'].extend(new_comps)
print(f'Added {len(new_comps)} new comparison pairs. Total: {len(data["comparisons"])}')

# Count by category
from collections import Counter
cat_count = Counter(t['category'] for t in data['tools'])
total_tools = len(data['tools'])
total_cats = len(data['categories'])
cats_filled = len(cat_count)
print(f'\nTools per category:')
for cat_id, count in sorted(cat_count.items()):
    cat_name = next((c['name'] for c in data['categories'] if c['id'] == cat_id), cat_id)
    print(f'  {cat_name} ({cat_id}): {count}')
print(f'\nTotal tools: {total_tools}')
print(f'Total categories: {total_cats}')
print(f'Categories with tools: {cats_filled}')

# Save tools.json
with open(os.path.join(BASE, 'data', 'tools.json'), 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print('\nSaved tools.json')

# Generate data.js
tools_js = json.dumps(data, indent=2, ensure_ascii=False)
js_content = f'// Auto-generated from tools.json — embedded for file:// compatibility\nwindow.__TOOLS_DATA__ = {tools_js};\n'
with open(os.path.join(BASE, 'js', 'data.js'), 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Saved data.js')
