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

# 41. Runway ML
if 'runway-ml' not in existing:
    new_tools.append({
        "id": "runway-ml",
        "name": "Runway ML",
        "url": "https://runwayml.com",
        "affiliate": None,
        "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free / Standard $12/mo / Unlimited $76/mo",
        "rating": 9.1,
        "summary": "Professional AI video generation + editing. Gen-2 makes videos from text/images.",
        "description": "Runway is the leading AI video generation platform. Gen-2 creates videos from text or images. In-painting, motion tracking, super-slow-mo — all AI-powered. Used by content creators, filmmakers, and marketers. The free tier gives 125 credits/month.",
        "tutorial": "1. Sign up at runwayml.com (free). 2. Go to Gen-2 tab. 3. Type a prompt (e.g., 'A drone flying over a cyberpunk city at sunset'). 4. Or upload an image as starting frame. 5. Click 'Generate' — 4K video in 45-90 seconds. 6. Use In-painting: upload a video, mask an object, type what to replace.",
        "pros": ["Best AI video quality (Gen-2)", "In-painting and motion tracking", "4K export", "Used by professionals"],
        "cons": ["Expensive for heavy use ($76/mo for unlimited)", "Free tier limited (125 credits/mo)", "Can take 1-2 mins per video"],
        "best_for": "Content creators and filmmakers who want AI video generation",
        "alternatives": ["pika-labs", "genmo", "stable-video"],
        "tags": ["ai-video", "gen-2", "video-generation", "filmmaking"],
        "featured": True
    })

# 42. Pika Labs
if 'pika-labs' not in existing:
    new_tools.append({
        "id": "pika-labs",
        "name": "Pika Labs",
        "url": "https://pika.art",
        "affiliate": None,
        "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free / Standard $8/mo / Pro $24/mo",
        "rating": 8.8,
        "summary": "AI video generation via Discord. Text/image → video in seconds.",
        "description": "Pika generates AI videos from text or images. Works via Discord — type /create, enter prompt, get video. Also: image-to-video, video-to-video (restyle), and camera motion control (zoom, pan, rotate). Great alternative to Runway with a free tier.",
        "tutorial": "1. Join Pika Discord (pika.art). 2. Go to a #generate channel. 3. Type /create prompt: your description. 4. Wait 30-60 seconds. 5. For image-to-video: /animate, upload image. 6. For camera control: add --camera zoom_in or --camera pan_right.",
        "pros": ["Great quality (competitve with Runway)", "Free tier (30 credits/day)", "Camera motion control", "Discord-based (easy)"],
        "cons": ["Discord-only (no web UI yet)", "Free tier has watermarks", "Limited video length (3-7 seconds)"],
        "best_for": "Creators who want AI video without complex software",
        "alternatives": ["runway-ml", "genmo", "stable-video"],
        "tags": ["ai-video", "discord-bot", "video-generation", "free-tier"],
        "featured": False
    })

# 43. Midjourney (already in data.js? check)
if 'midjourney' not in existing:
    new_tools.append({
        "id": "midjourney",
        "url": "https://midjourney.com",
        "affiliate": None,
        "category": "image",
        "pricing": "Paid",
        "price_detail": "Basic $10/mo / Standard $30/mo / Pro $60/mo",
        "rating": 9.4,
        "summary": "The most popular AI image generator. Discord-based, stunning quality.",
        "description": "Midjourney is the leading AI image generator, known for the most artistic and high-quality outputs. Works via Discord — type /imagine, get 4 images, upscale your favorite. Used by 15M+ artists, designers, and creators. V6 model is the latest (2024).",
        "tutorial": "1. Join Midjourney Discord (midjourney.com). 2. Go to a #newbies channel. 3. Type /imagine prompt: your description. 4. Wait 1 minute, get 4 images. 5. Click U1-U4 to upscale (higher res). 6. For variations: click V1-V4. 7. Paid tiers remove daily limits.",
        "pros": ["Best image quality (artistic)", "V6 model (latest, most accurate)", "15M+ community", "Discord community (get feedback)"],
        "cons": ["Discord-only (no web UI)", "No free tier (trial removed)", "Can be expensive ($10-$60/mo)"],
        "best_for": "Artists and designers who want the best AI image quality",
        "alternatives": ["dall-e-3", "stable-diffusion", "leonardo-ai"],
        "tags": ["ai-image", "discord-bot", "artistic", "midjourney-v6"],
        "featured": True
    })

# 44. Leonardo AI
if 'leonardo-ai' not in existing:
    new_tools.append({
        "id": "leonardo-ai",
        "name": "Leonardo AI",
        "url": "https://leonardo.ai",
        "affiliate": None,
        "category": "image",
        "pricing": "Freemium",
        "price_detail": "Free / Apprentice $10/mo / Artisan $24/mo",
        "rating": 8.9,
        "summary": "High-quality AI images with a web UI. Better than Midjourney for some use cases.",
        "description": "Leonardo AI is a web-based AI image generator that rivals Midjourney in quality. Supports SDXL, custom models, image-to-image, and in-painting. The free tier gives 150 tokens/day. Great for product design, concept art, and game assets.",
        "tutorial": "1. Sign up at leonardo.ai (free). 2. Click 'Image Generation'. 3. Enter prompt, pick model (SDXL, Leonardo Vision XL, etc.). 4. Click 'Generate' — get 4 images. 5. Use 'Image Guidance' (image-to-image): upload reference, adjust strength. 6. 'In-painting': upload image, mask area, type what to replace.",
        "pros": ["Web UI (no Discord needed)", "Free tier (150 tokens/day)", "Custom models (train your own)", "Image-to-image and in-painting"],
        "cons": ["Less artistic than Midjourney for some prompts", "Free tier has daily limits", "Can be slow during peak hours"],
        "best_for": "Designers who want a web UI instead of Discord",
        "alternatives": ["midjourney", "dall-e-3", "stable-diffusion"],
        "tags": ["ai-image", "web-ui", "free-tier", "sdxl"],
        "featured": True
    })

# 45. Stable Diffusion (Web UI / Automatic1111)
if 'stable-diffusion' not in existing:
    new_tools.append({
        "id": "stable-diffusion",
        "name": "Stable Diffusion (WebUI)",
        "url": "https://github.com/AUTOMATIC1111/stable-diffusion-webui",
        "affiliate": None,
        "category": "image",
        "pricing": "Free",
        "price_detail": "Free (open-source)",
        "rating": 8.7,
        "summary": "Open-source AI image generation. Run locally, full control, no limits.",
        "description": "Stable Diffusion is the leading open-source AI image generator. Run it locally (WebUI by Automatic1111) for full control — no limits, no subscriptions. Supports custom models, LoRAs, ControlNet, and extensions. The free alternative to Midjourney.",
        "tutorial": "1. Install Python 3.10, Git. 2. Clone: git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui. 3. Run webui-user.bat (Windows) or webui.sh (Mac/Linux). 4. Download a model (e.g., SDXL, Realistic Vision) from Civitai. 5. Place in models/Stable-diffusion/. 6. Refresh UI, select model, type prompt, click 'Generate'.",
        "pros": ["100% free (open-source)", "Run locally (privacy)", "Full control (ControlNet, LoRAs)", "Thousands of custom models"],
        "cons": ["Requires powerful GPU (RTX 3060+ recommended)", "Complex setup (technical)", "Can be slow on CPU"],
        "best_for": "Technical users who want full control and privacy",
        "alternatives": ["midjourney", "dall-e-3", "leonardo-ai"],
        "tags": ["open-source", "local-ai", "stable-diffusion", "free"],
        "featured": False
    })

# 46. Notion AI
if 'notion-ai' not in existing:
    new_tools.append({
        "id": "notion-ai",
        "name": "Notion AI",
        "url": "https://notion.so",
        "affiliate": None,
        "category": "writing",
        "pricing": "Freemium",
        "price_detail": "Free / AI Add-on $10/mo",
        "rating": 8.5,
        "summary": "AI writing assistant inside Notion. Draft, summarize, translate, fix grammar.",
        "description": "Notion AI brings AI directly into your Notion workspace. Highlight text → 'Ask AI': draft from scratch, summarize, translate, fix grammar, make shorter/longer. Also: AI autocomplete (type '/' for AI suggestions). Great for note-taking, writing, and project management.",
        "tutorial": "1. Open Notion, type something. 2. Highlight text → 'Ask AI' (or Cmd/Ctrl+J). 3. Choose: 'Continue writing', 'Summarize', 'Improve writing', 'Fix spelling & grammar', 'Translate to...'. 4. For AI autocomplete: type space, wait — Notion AI suggests continuation. 5. For blank page: type '/ai' → 'Draft with AI'.",
        "pros": ["Integrated into Notion (no context switching)", "Draft, summarize, translate", "AI autocomplete", "Great for note-taking"],
        "cons": ["Requires Notion (learning curve)", "AI add-on is $10/mo", "Less powerful than ChatGPT for long-form"],
        "best_for": "Notion users who want AI assistance in their workflow",
        "alternatives": ["chatgpt", "claude", "notion"],
        "tags": ["ai-writing", "notion", "productivity", "ai-assistant"],
        "featured": False
    })

# 47. Grammarly
if 'grammarly' not in existing:
    new_tools.append({
        "id": "grammarly",
        "name": "Grammarly",
        "url": "https://grammarly.com",
        "affiliate": None,
        "category": "writing",
        "pricing": "Freemium",
        "price_detail": "Free / Premium $12/mo / Business $15/mo",
        "rating": 8.3,
        "summary": "AI grammar and writing assistant. Real-time suggestions as you type.",
        "description": "Grammarly is the world's most popular AI writing assistant. Checks grammar, spelling, punctuation, clarity, engagement, and delivery. The AI suggests rewrites for better wording. Works everywhere: browser extension, MS Office, Google Docs, and mobile keyboard.",
        "tutorial": "1. Install Grammarly extension (Chrome/Edge/Safari). 2. Or use Grammarly Editor (web). 3. Type — Grammarly underlines issues in red/blue/green. 4. Click suggestion to accept. 5. For advanced: Grammarly Premium suggests tone changes, clarity improvements, and plagiarism detection.",
        "pros": ["Works everywhere (browser, Office, mobile)", "Real-time suggestions", "Free tier is powerful", "Plagiarism detection (Premium)"],
        "cons": ["Premium is expensive ($12/mo)", "Can be distracting (too many suggestions)", "Sometimes wrong (context-sensitive)"],
        "best_for": "Writers, students, and professionals who want error-free writing",
        "alternatives": ["chatgpt", "prowritingaid", "hemingway-editor"],
        "tags": ["grammar", "writing-assistant", "ai-editing", "freemium"],
        "featured": False
    })

# 48. Jasper AI
if 'jasper-ai' not in existing:
    new_tools.append({
        "id": "jasper-ai",
        "name": "Jasper AI",
        "url": "https://jasper.ai",
        "affiliate": None,
        "category": "writing",
        "pricing": "Paid",
        "price_detail": "Creator $39/mo / Pro $59/mo / Business custom",
        "rating": 8.0,
        "summary": "AI writing for marketing teams. Blogs, ads, emails, SEO-optimized.",
        "description": "Jasper is the leading AI writing tool for marketing teams. Generates blog posts, ads, emails, and social media posts — SEO-optimized. Integrates with Surfer SEO for ranking. Brand Voice: Jasper learns your brand's tone. Used by 100K+ marketing teams.",
        "tutorial": "1. Sign up at jasper.ai (free trial). 2. Pick a template: Blog Post, Facebook Ad, Email, etc. 3. Enter topic, keywords, tone. 4. Click 'Generate' — Jasper writes. 5. For Blog Post: enter title + outline, Jasper writes 1000+ words. 6. Use 'Brand Voice': upload examples of your writing, Jasper matches your tone.",
        "pros": ["SEO-optimized (integrates with Surfer SEO)", "Brand Voice (learns your tone)", "100K+ marketing teams use it", "Long-form content (1000+ words)"],
        "cons": ["Expensive ($39/mo minimum)", "No free tier (trial only)", "Can sound generic without Brand Voice"],
        "best_for": "Marketing teams who need SEO-optimized content at scale",
        "alternatives": ["chatgpt", "copy-ai", "writesonic"],
        "tags": ["ai-writing", "marketing", "seo", "brand-voice"],
        "featured": True
    })

# 49. Copy.ai
if 'copy-ai' not in existing:
    new_tools.append({
        "id": "copy-ai",
        "name": "Copy.ai",
        "url": "https://copy.ai",
        "affiliate": None,
        "category": "writing",
        "pricing": "Freemium",
        "price_detail": "Free (2000 words/mo) / Pro $36/mo",
        "rating": 7.8,
        "summary": "AI copywriting for marketing. Blogs, ads, social media, emails.",
        "description": "Copy.ai is an AI copywriting tool for marketers. Generate blog intros, Facebook ads, Instagram captions, email subject lines, and more. The free tier gives 2000 words/month. Simple interface — pick a template, enter details, get copy.",
        "tutorial": "1. Sign up at copy.ai (free). 2. Pick a template: Blog Post, Facebook Ad, Email, etc. 3. Enter: product name, description, tone. 4. Click 'Create Copy' — get 10 variations. 5. Edit, copy, paste. 6. For Blog: use 'Blog Post Wizard' — enter keyword, get outline, then full post.",
        "pros": ["Free tier (2000 words/mo)", "Simple interface", "10 variations per prompt", "Good for short-form copy"],
        "cons": ["Free tier is limited", "Less powerful than Jasper for long-form", "Output can be generic"],
        "best_for": "Marketers who need quick copy variations",
        "alternatives": ["jasper-ai", "chatgpt", "writesonic"],
        "tags": ["ai-copywriting", "marketing", "free-tier", "short-form"],
        "featured": False
    })

# 50. Writesonic
if 'writesonic' not in existing:
    new_tools.append({
        "id": "writesonic",
        "name": "Writesonic",
        "url": "https://writesonic.com",
        "affiliate": None,
        "category": "writing",
        "pricing": "Freemium",
        "price_detail": "Free (10k words/mo) / Pro $12.67/mo",
        "rating": 7.9,
        "summary": "AI writer with SEO optimization. Blogs, ads, emails. Free tier generous.",
        "description": "Writesonic is an AI writing tool with a generous free tier (10K words/month). Generates SEO-optimized blog posts, Google ads, Facebook ads, and emails. Also includes Chatsonic (ChatGPT alternative with real-time data from Google).",
        "tutorial": "1. Sign up at writesonic.com (free). 2. Pick: Article/Blog Writer, Paraphrasing Tool, Text Expander, etc. 3. For blog: enter topic + keywords, click 'Generate' — get 1000+ words. 4. Use Chatsonic: chat with AI that has real-time Google data (unlike ChatGPT). 5. Export to WordPress directly.",
        "pros": ["Generous free tier (10K words/mo)", "Chatsonic (real-time data)", "Export to WordPress", "SEO-optimized"],
        "cons": ["Output quality varies", "Pro tier needed for best features", "Can be slow during peak"],
        "best_for": "Bloggers who want SEO content with a free tier",
        "alternatives": ["jasper-ai", "copy-ai", "chatgpt"],
        "tags": ["ai-writing", "seo", "free-tier", "blogging"],
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
