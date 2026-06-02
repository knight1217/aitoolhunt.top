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

# 21. Zeus AI Assistant
if 'zeus' not in existing:
    new_tools.append({
        "id": "zeus",
        "name": "Zeus AI Assistant",
        "url": "https://zeus.ai",
        "affiliate": None,
        "category": "chat",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $15/mo",
        "rating": 8.0,
        "summary": "AI assistant with real-time web access and advanced reasoning capabilities.",
        "description": "Zeus AI Assistant combines real-time web browsing with advanced reasoning to provide up-to-date answers. Unlike static models, Zeus can search the web for current information, verify facts, and provide citations. Great for research and staying current.",
        "tutorial": "1. Go to zeus.ai and sign up. 2. Start chatting - Zeus automatically searches the web when needed. 3. Ask for current events: 'What happened in tech today?'. 4. Use for research: 'Find recent papers on quantum computing'. 5. Enable 'Deep Research' mode for comprehensive reports.",
        "pros": ["Real-time web access", "Fact checking with citations", "Research-focused", "Free tier available"],
        "cons": ["Less known than ChatGPT", "Sometimes slower due to web searches", "Limited creative writing"],
        "best_for": "Researchers and users who need current information",
        "alternatives": ["chatgpt", "perplexity", "claude"],
        "tags": ["chatbot", "web-access", "research", "freemium"],
        "featured": False
    })

# 22. YouChat
if 'youchat' not in existing:
    new_tools.append({
        "id": "youchat",
        "name": "YouChat",
        "url": "https://you.com",
        "affiliate": None,
        "category": "chat",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $20/mo",
        "rating": 8.3,
        "summary": "Search-engine-integrated AI chat. Real-time web results with AI synthesis.",
        "description": "YouChat is an AI chatbot built into the You.com search engine. It provides real-time web search results with AI-synthesized answers. Great for research, fact-checking, and getting current information without leaving the chat interface.",
        "tutorial": "1. Go to you.com and click 'Chat'. 2. Sign up for free (optional but recommended). 3. Ask anything - YouChat searches the web in real-time. 4. Click citations to verify sources. 5. Use 'AI Mode' for more creative tasks. 6. Upgrade to Pro for GPT-4 quality and unlimited searches.",
        "pros": ["Real-time web search", "Shows citations", "No hallucinations (verifiable)", "Free tier is generous"],
        "cons": ["Less creative than Claude", "Occasional slow searches", "Search-oriented (less good for coding)"],
        "best_for": "Users who want verified, citation-backed AI answers",
        "alternatives": ["chatgpt", "perplexity", "bing-chat"],
        "tags": ["chatbot", "search", "citations", "freemium"],
        "featured": False
    })

# 23. Bing Chat (Microsoft Copilot)
if 'bing-chat' not in existing:
    new_tools.append({
        "id": "bing-chat",
        "name": "Microsoft Copilot (Bing Chat)",
        "url": "https://copilot.microsoft.com",
        "affiliate": None,
        "category": "chat",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $20/mo (Microsoft 365)",
        "rating": 8.4,
        "summary": "Microsoft's AI powered by GPT-4. Free, with web access and DALL-E 3 image generation.",
        "description": "Microsoft Copilot (formerly Bing Chat) is free and powered by GPT-4. It has real-time web access, can generate images via DALL-E 3, and is integrated into Windows/Microsoft 365. The free tier has higher limits than ChatGPT Free.",
        "tutorial": "1. Go to copilot.microsoft.com (Edge recommended). 2. Sign in with Microsoft account (free). 3. Choose conversation style: Creative, Balanced, or Precise. 4. Ask anything - it searches the web automatically. 5. Generate images: 'Create an image of...'. 6. Use in Windows: Win+C opens Copilot.",
        "pros": ["Free GPT-4 (no paywall)", "DALL-E 3 image generation included", "Real-time web access", "Integrated into Windows/Office"],
        "cons": ["Requires Microsoft account", "Sometimes pushes Bing search", "Less customizable than ChatGPT"],
        "best_for": "Windows users who want free GPT-4 with web access",
        "alternatives": ["chatgpt", "claude", "gemini"],
        "tags": ["chatbot", "free-gpt4", "microsoft", "image-gen"],
        "featured": True
    })

# 24. Ernie Bot (Wenxin Yiyan)
if 'ernie' not in existing:
    new_tools.append({
        "id": "ernie",
        "name": "Ernie Bot (Wenxin Yiyan)",
        "url": "https://yiyan.baidu.com",
        "affiliate": None,
        "category": "chat",
        "pricing": "Freemium",
        "price_detail": "Free / Premium membership",
        "rating": 8.1,
        "summary": "Baidu's Chinese AI chatbot. Strong in Chinese language understanding and local knowledge.",
        "description": "Ernie Bot (Wenxin Yiyan) is Baidu's answer to ChatGPT, optimized for Chinese language and culture. It excels at Chinese writing, poetry, local business knowledge, and understanding Chinese idioms. Also available in English with decent performance.",
        "tutorial": "1. Go to yiyan.baidu.com and sign up with Chinese phone number. 2. Chat in Chinese - it understands context, idioms, and cultural references. 3. Try creative writing: 'Write a poem in Tang dynasty style'. 4. Use for business: 'Draft a WeChat official account post'. 5. English available but less fluent than Chinese.",
        "pros": ["Best-in-class Chinese understanding", "Deep cultural knowledge of China", "Integrated with Baidu search", "Free tier available"],
        "cons": ["Chinese-centric (less good at other languages)", "Requires Chinese phone number", "Limited API access outside China"],
        "best_for": "Chinese-speaking users who need culturally-aware AI",
        "alternatives": ["chatgpt", "qianwen", "doubao"],
        "tags": ["chatbot", "chinese", "baidu", "local-knowledge"],
        "featured": False
    })

# 25. Qianwen (Tongyi Qianwen)
if 'qianwen' not in existing:
    new_tools.append({
        "id": "qianwen",
        "name": "Qianwen (Tongyi Qianwen)",
        "url": "https://tongyi.aliyun.com",
        "affiliate": None,
        "category": "chat",
        "pricing": "Freemium",
        "price_detail": "Free / Premium membership",
        "rating": 8.2,
        "summary": "Alibaba's AI assistant. Strong in e-commerce, business, and Chinese language tasks.",
        "description": "Qianwen (Tongyi Qianwen) is Alibaba's large language model, integrated into Alibaba's ecosystem (Taobao, Tmall, Alipay, DingTalk). It excels at e-commerce tasks, business writing, and Chinese language understanding. Free tier available via Alibaba Cloud.",
        "tutorial": "1. Go to tongyi.aliyun.com and sign up. 2. Use in DingTalk (Alibaba's Slack) for business workflows. 3. Try e-commerce features: 'Write a product description for...'. 4. Generate images: Qianwen can create product images. 5. API access via Alibaba Cloud for developers.",
        "pros": ["Integrated into Alibaba ecosystem", "Strong e-commerce features", "Chinese business writing", "Free tier available"],
        "cons": ["Less capable in English", "Requires Alibaba account", "API pricing complex"],
        "best_for": "Chinese businesses using Alibaba ecosystem",
        "alternatives": ["chatgpt", "ernie", "doubao"],
        "tags": ["chatbot", "chinese", "ecommerce", "alibaba"],
        "featured": False
    })

# 26. Doubao (Doubao)
if 'doubao' not in existing:
    new_tools.append({
        "id": "doubao",
        "name": "Doubao",
        "url": "https://www.doubao.com",
        "affiliate": None,
        "category": "chat",
        "pricing": "Free",
        "price_detail": "Free (ByteDance)",
        "rating": 8.0,
        "summary": "ByteDance's AI chatbot. Free, fast, and integrated with TikTok/Douyin ecosystem.",
        "description": "Doubao is ByteDance's AI assistant, completely free and optimized for Chinese users. It's integrated with TikTok/Douyin (for content creation) and offers image generation, voice cloning, and real-time search. The mobile app is well-designed.",
        "tutorial": "1. Download Doubao app (iOS/Android) or use web version. 2. Sign up with phone number. 3. Chat - it's fast and free. 4. Generate images: 'Create an image of...'. 5. Use for content creation: 'Write a TikTok script about...'. 6. Voice mode: hold mic and speak.",
        "pros": ["100% free (no paywall)", "Fast response times", "Integrated with TikTok/Douyin", "Good mobile app"],
        "cons": ["Chinese-focused", "Less capable than GPT-4 at complex reasoning", "Limited API access"],
        "best_for": "Chinese users who want free, fast AI for daily tasks",
        "alternatives": ["chatgpt", "ernie", "qianwen"],
        "tags": ["chatbot", "free", "chinese", "bytedance"],
        "featured": False
    })

# 27. Perplexity Pro
if 'perplexity-pro' not in existing:
    new_tools.append({
        "id": "perplexity-pro",
        "name": "Perplexity Pro",
        "url": "https://perplexity.ai",
        "affiliate": None,
        "category": "chat",
        "pricing": "Paid",
        "price_detail": "$20/mo (Pro)",
        "rating": 9.0,
        "summary": "The best AI search engine. Pro version uses GPT-4, Claude 3.5, and other top models.",
        "description": "Perplexity Pro is the paid tier of Perplexity AI, using top models (GPT-4, Claude 3.5 Sonnet, Mistral Large) for highest-quality answers. Pro users get unlimited Pro searches, file analysis, and image generation. The best AI search experience available.",
        "tutorial": "1. Go to perplexity.ai and sign up. 2. Subscribe to Pro ($20/mo). 3. Choose your model: GPT-4o, Claude 3.5 Sonnet, Mistral Large, etc. 4. Search: 'Best noise-canceling headphones 2024' - get a synthesized answer with citations. 5. Upload files (PDF, etc.) for analysis. 6. Image generation: 'Create an image of...' (Pro only).",
        "pros": ["Uses top models (GPT-4, Claude)", "Unlimited Pro searches", "File analysis (PDF, etc.)", "Image generation (Pro)"],
        "cons": ["$20/mo paywall", "Less customizable than ChatGPT", "No memory across searches"],
        "best_for": "Researchers and professionals who want the best AI search",
        "alternatives": ["chatgpt-plus", "youchat", "bing-chat"],
        "tags": ["search", "pro", "gpt4", "claude"],
        "featured": True
    })

# 28. Claude 3.5 Sonnet (mention as standalone)
if 'claude-35' not in existing:
    new_tools.append({
        "id": "claude-35",
        "name": "Claude 3.5 Sonnet",
        "url": "https://claude.ai",
        "affiliate": None,
        "category": "chat",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $20/mo",
        "rating": 9.4,
        "summary": "Anthropic's most capable model. Beats GPT-4o on many benchmarks. 200K context.",
        "description": "Claude 3.5 Sonnet is Anthropic's flagship model, beating GPT-4o on many benchmarks (especially coding and analysis). It has a 200K token context window (entire book), excellent writing quality, and 'Artifacts' - an interactive preview panel for code/documents. The best all-around AI model available today.",
        "tutorial": "1. Go to claude.ai and sign up. 2. Start chatting - try complex tasks: 'Refactor this 500-line function', 'Summarize this 50-page PDF'. 3. Use Artifacts: ask for code/document/diagram, and it appears in a side panel. 4. Upload files: PDF, Word, Excel - Claude reads them all. 5. Pro tier ($20/mo) gives 5x more usage.",
        "pros": ["Beats GPT-4o on many tasks", "200K context (entire book)", "Artifacts feature is amazing", "Best coding model"],
        "cons": ["No image generation", "Pro tier needed for heavy use", "Sometimes overly cautious"],
        "best_for": "Developers, writers, and analysts who need top-tier AI",
        "alternatives": ["chatgpt", "gemini", "perplexity"],
        "tags": ["chatbot", "top-tier", "coding", "analysis"],
        "featured": True
    })

# 29. GPT-4o (OpenAI)
if 'gpt4o' not in existing:
    new_tools.append({
        "id": "gpt4o",
        "name": "GPT-4o (OpenAI)",
        "url": "https://chat.openai.com",
        "affiliate": None,
        "category": "chat",
        "pricing": "Freemium",
        "price_detail": "Free / Plus $20/mo / Pro $200/mo",
        "rating": 9.2,
        "summary": "OpenAI's fastest, cheapest flagship model. Multimodal: text, vision, audio.",
        "description": "GPT-4o ('o' for 'omni') is OpenAI's flagship multimodal model. It's faster and 50% cheaper than GPT-4 Turbo, with the same capabilities: text, vision (image understanding), and audio (voice mode). The free tier uses GPT-4o mini; Plus gets full GPT-4o with higher limits.",
        "tutorial": "1. Go to chat.openai.com and sign up. 2. Free tier uses GPT-4o mini (good enough for most tasks). 3. Plus ($20/mo): full GPT-4o, higher message limits, faster responses. 4. Voice mode: click the headphones icon, speak naturally. 5. Upload images: click paperclip, analyze screenshots/photos. 6. Pro ($200/mo): highest limits + o1 reasoning model.",
        "pros": ["Fastest flagship model", "Multimodal (text+vision+audio)", "Huge plugin ecosystem", "Regular updates"],
        "cons": ["Free tier has message limits", "Can hallucinate confidently", "Privacy concerns"],
        "best_for": "Everyone - the most versatile AI available",
        "alternatives": ["claude", "gemini", "perplexity"],
        "tags": ["chatbot", "multimodal", "fast", "versatile"],
        "featured": True
    })

# 30. o1 (OpenAI Reasoning Model)
if 'o1' not in existing:
    new_tools.append({
        "id": "o1",
        "name": "o1 (OpenAI Reasoning Model)",
        "url": "https://chat.openai.com",
        "affiliate": None,
        "category": "chat",
        "pricing": "Paid",
        "price_detail": "ChatGPT Pro $200/mo (unlimited) / API pay-per-token",
        "rating": 9.0,
        "summary": "OpenAI's reasoning model. Thinks before responding. Best for math, coding, science.",
        "description": "o1 is OpenAI's reasoning model that 'thinks' before responding - it spends more time reasoning, leading to fewer errors on complex tasks. Beats GPT-4o on math, coding, and scientific reasoning. Available via ChatGPT Pro ($200/mo) or API (pay-per-token).",
        "tutorial": "1. Subscribe to ChatGPT Pro ($200/mo) - includes unlimited o1. 2. Or use API: openai.ChatCompletion.create(model='o1', messages=[...]). 3. Use for: complex math, multi-step coding, scientific reasoning, logic puzzles. 4. Be patient - o1 takes 10-30 seconds to 'think'. 5. Not for: quick chats, creative writing (use GPT-4o instead).",
        "pros": ["Best reasoning model available", "Fewer errors on complex tasks", "Great for math/coding/science", "Chain-of-thought transparency"],
        "cons": ["$200/mo (Pro) or expensive API", "Slower than GPT-4o", "Not for creative tasks"],
        "best_for": "Researchers, scientists, and developers solving hard problems",
        "alternatives": ["gpt4o", "claude-35", "gemini-advanced"],
        "tags": ["reasoning", "math", "coding", "science"],
        "featured": False
    })

print(f"\nAdding {len(new_tools)} more tools...")
data['tools'].extend(new_tools)

# Write back
new_json = json.dumps(data, indent=2, ensure_ascii=False)
# Fix: replace 2-space with 4-space to match original
new_json = new_json.replace('  ', '    ')

new_content = f"// Auto-generated from tools.json -- embedded for file:// compatibility\nwindow.__TOOLS_DATA__ = {new_json};\n"

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Done! Total tools: {len(data['tools'])}")
