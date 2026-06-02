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

# 1. OpenAI Codex
if 'openai-codex' not in existing:
    new_tools.append({
        "id": "openai-codex",
        "name": "OpenAI Codex",
        "url": "https://openai.com/blog/openai-codex",
        "affiliate": None,
        "category": "coding",
        "pricing": "Paid",
        "price_detail": "API usage-based pricing",
        "rating": 8.7,
        "summary": "OpenAI's code-generation model powering GitHub Copilot. Now available via API.",
        "description": "Codex is OpenAI's specialized model for code generation, trained on 54M+ GitHub repositories. It powers GitHub Copilot and is available via OpenAI API. Codex understands dozens of programming languages and can translate natural language to code, explain code, and debug.",
        "tutorial": "1. Sign up at platform.openai.com and get an API key. 2. Install OpenAI Python library: pip install openai. 3. Call the Codex endpoint via openai.ChatCompletion.create with model='gpt-4'. 4. For code completion, use the dedicated code endpoint or fine-tune on your codebase. 5. Integrate into your IDE via Copilot or build custom workflows. 6. Monitor usage in the OpenAI dashboard.",
        "pros": ["Powers GitHub Copilot", "Supports 50+ languages", "Strong code explanation ability", "Available via stable API"],
        "cons": ["No standalone product (API only)", "Can generate insecure code", "API costs add up for heavy use"],
        "best_for": "Developers building AI coding features into their products",
        "alternatives": ["cursor", "copilot", "claude-code-tool"],
        "tags": ["coding", "api", "code-generation", "paid"],
        "featured": False
    })

# 2. Mistral AI
if 'mistral' not in existing:
    new_tools.append({
        "id": "mistral",
        "name": "Mistral AI",
        "url": "https://mistral.ai",
        "affiliate": None,
        "category": "chat",
        "pricing": "Freemium",
        "price_detail": "Free / Pro EUR5.99/mo / Premier EUR24.99/mo",
        "rating": 8.9,
        "summary": "European AI lab's chat assistant. Open-weight models, strong multilingual, privacy-focused.",
        "description": "Mistral AI is a European AI lab offering both a chat assistant (Le Chat) and open-weight models (Mistral 7B, Mixtral 8x7B, Mistral Large). Le Chat competes with ChatGPT and Claude, with a focus on multilingual support and European data privacy.",
        "tutorial": "1. Go to mistral.ai and sign up. 2. Use Le Chat in browser. 3. For API access: get an API key from console.mistral.ai. 4. Use the API: pip install mistralai, then client.chat(...) with model='mistral-large'. 5. Try their open models via Ollama or Hugging Face. 6. Self-host for privacy.",
        "pros": ["Strong multilingual (EU languages)", "Open-weight models available", "Competitive pricing", "European data privacy compliance"],
        "cons": ["Smaller ecosystem than OpenAI", "Fewer plugins", "Less known in US market"],
        "best_for": "European users; developers wanting open-weight models",
        "alternatives": ["chatgpt", "claude", "gemini"],
        "tags": ["chatbot", "multilingual", "open-weight", "eu"],
        "featured": True
    })

# 3. Cohere
if 'cohere' not in existing:
    new_tools.append({
        "id": "cohere",
        "name": "Cohere",
        "url": "https://cohere.com",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free tier / Enterprise pricing",
        "rating": 8.4,
        "summary": "Enterprise-focused LLM API. Specializes in RAG, retrieval, and production AI systems.",
        "description": "Cohere builds large language models designed for enterprise use cases - especially retrieval-augmented generation (RAG), semantic search, and chat. Their models (Command R, Command R+) are optimized for production systems.",
        "tutorial": "1. Sign up at dashboard.cohere.com. 2. Get an API key. 3. Install: pip install cohere. 4. For chat: cohere.Client(api_key).chat(message=...). 5. For RAG: use Cohere Embed endpoints to vectorize documents. 6. Deploy via Cohere managed infrastructure or fine-tune for custom models.",
        "pros": ["Best-in-class RAG/retrieval", "Strong enterprise focus", "Competitive pricing for production", "Excellent documentation"],
        "cons": ["Not a consumer chatbot", "Smaller model sizes than GPT-4", "Less suitable for creative writing"],
        "best_for": "Enterprises building RAG systems and production AI",
        "alternatives": ["chatgpt", "claude", "gemini"],
        "tags": ["enterprise", "rag", "api", "production"],
        "featured": False
    })

# 4. Poe
if 'poe' not in existing:
    new_tools.append({
        "id": "poe",
        "name": "Poe",
        "url": "https://poe.com",
        "affiliate": None,
        "category": "chat",
        "pricing": "Freemium",
        "price_detail": "Free / Quarterly sub for premium bots",
        "rating": 8.1,
        "summary": "Quora's AI chatbot platform. Access GPT-4, Claude, Llama, and 20+ bots in one place.",
        "description": "Poe (Platform for Open Exploration) by Quora lets you access multiple AI chatbots in one interface - GPT-4o, Claude 3.5 Sonnet, Llama 3.2, Gemini, and many community-created bots. One subscription for all models.",
        "tutorial": "1. Go to poe.com and sign up with email or Google. 2. Pick a bot from the left sidebar. 3. Start chatting. 4. Create your own bot: click Create a bot, pick a base model, add system instructions. 5. Use Points system: each message costs points; subscribe for more. 6. Try multi-bot chats.",
        "pros": ["Access 20+ AI models in one place", "Compare models side-by-side", "Create custom bots", "Single subscription"],
        "cons": ["Quora account required", "Points system can be confusing", "Not all models on free tier"],
        "best_for": "Users who want to try multiple AI models without multiple subscriptions",
        "alternatives": ["chatgpt", "claude", "perplexity"],
        "tags": ["chatbot", "multi-model", "comparison", "quora"],
        "featured": False
    })

# 5. v0.dev
if 'v0-dev' not in existing:
    new_tools.append({
        "id": "v0-dev",
        "name": "v0.dev",
        "url": "https://v0.dev",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $20/mo",
        "rating": 8.6,
        "summary": "Vercel's AI UI generator. Describe a UI, get React/Tailwind code instantly.",
        "description": "v0.dev by Vercel generates production-ready UI components from text descriptions. Describe what you want and v0 generates React + Tailwind CSS code. You can iterate visually - click elements to modify, then copy the code into your project.",
        "tutorial": "1. Go to v0.dev and sign in with GitHub or Google. 2. Describe your UI. 3. v0 generates multiple variants - pick one. 4. Click any element to modify. 5. When satisfied, click Code tab and copy the React/Tailwind code. 6. Paste into your project. Free tier: 10 messages/month.",
        "pros": ["Generates production-ready code", "React + Tailwind out of the box", "Visual iteration", "Copy-paste into any project"],
        "cons": ["Free tier very limited (10 messages/mo)", "Only React/Tailwind output", "Generated code may need tweaking"],
        "best_for": "Frontend developers who want to skip writing boilerplate UI code",
        "alternatives": ["cursor", "windsurf", "claude-code-tool"],
        "tags": ["ui-generation", "react", "tailwind", "coding"],
        "featured": True
    })

# 6. Ollama
if 'ollama' not in existing:
    new_tools.append({
        "id": "ollama",
        "name": "Ollama",
        "url": "https://ollama.com",
        "affiliate": None,
        "category": "coding",
        "pricing": "Free",
        "price_detail": "Free (open-source)",
        "rating": 8.8,
        "summary": "Run Llama 3, Mistral, Gemma, and 50+ open models locally. No cloud needed.",
        "description": "Ollama lets you download and run large language models locally on your Mac, Windows, or Linux machine. It bundles model weights, configuration, and dependencies into one package. Supports Llama 3, Mistral, Gemma, Phi-3, and dozens more.",
        "tutorial": "1. Download Ollama from ollama.com. 2. Open terminal and run ollama serve to start the server. 3. Pull a model: ollama pull llama3. 4. Run it: ollama run llama3. 5. For coding: ollama pull codellama. 6. Use via API at localhost:11434. 7. Try the Ollama Python library: pip install ollama.",
        "pros": ["Runs 100% locally (privacy)", "Supports 50+ open models", "OpenAI-compatible API", "No subscription fees"],
        "cons": ["Requires decent hardware (RAM/GPU)", "Slower than cloud AIs on weak machines", "No official mobile app"],
        "best_for": "Privacy-conscious users; developers wanting local AI",
        "alternatives": ["lm-studio", "huggingchat", "groq"],
        "tags": ["local", "open-source", "privacy", "free"],
        "featured": True
    })

# 7. Grok (xAI)
if 'grok' not in existing:
    new_tools.append({
        "id": "grok",
        "name": "Grok",
        "url": "https://grok.com",
        "affiliate": None,
        "category": "chat",
        "pricing": "Paid",
        "price_detail": "X Premium+ ($16/mo) required",
        "rating": 7.8,
        "summary": "Elon Musk's AI with real-time X (Twitter) access. Unfiltered, edgy responses.",
        "description": "Grok is xAI's chatbot, exclusively available to X (Twitter) Premium+ subscribers. Its killer feature is real-time access to X platform data. Grok is known for a more irreverent, less censored tone than competitors.",
        "tutorial": "1. Subscribe to X Premium+ ($16/mo). 2. On X.com, click Grok in the sidebar. 3. Ask anything - Grok can search X in real-time. 4. Try Fun Mode for more creative responses. 5. Grok can generate images via FLUX model. 6. No standalone access - must use via X platform.",
        "pros": ["Real-time X (Twitter) data access", "Less censored than competitors", "Image generation included", "Good for breaking news"],
        "cons": ["Requires X Premium+ subscription", "No standalone web/app access", "Can be unreliable on sensitive topics"],
        "best_for": "X (Twitter) power users who want real-time AI insights",
        "alternatives": ["chatgpt", "claude", "perplexity"],
        "tags": ["realtime", "twitter", "xai", "paid"],
        "featured": False
    })

# 8. Phind
if 'phind' not in existing:
    new_tools.append({
        "id": "phind",
        "name": "Phind",
        "url": "https://phind.com",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $20/mo",
        "rating": 8.5,
        "summary": "AI search engine for developers. Finds answers from documentation, GitHub issues, and Stack Overflow.",
        "description": "Phind is an AI-powered search engine designed specifically for developers. Unlike general AIs, Phind searches across documentation, GitHub issues, Stack Overflow, and technical blogs to find precise answers. It can write code, explain concepts, and debug errors - all with cited sources.",
        "tutorial": "1. Go to phind.com (no signup required for basic use). 2. Type a technical question. 3. Phind searches documentation and Stack Overflow, then synthesizes an answer with citations. 4. Click citations to verify sources. 5. For code generation: describe what you need. 6. Sign up for Pro ($20/mo) for GPT-4 quality responses.",
        "pros": ["Designed specifically for developers", "Cites sources", "No signup required for basic use", "Excellent for debugging"],
        "cons": ["Less versatile than ChatGPT for non-technical tasks", "Pro tier required for best quality", "Smaller context than Claude"],
        "best_for": "Developers who want accurate, cited technical answers",
        "alternatives": ["chatgpt", "perplexity", "stack-overflow"],
        "tags": ["developer", "search", "coding", "technical"],
        "featured": True
    })

# 9. Tabnine
if 'tabnine' not in existing:
    new_tools.append({
        "id": "tabnine",
        "name": "Tabnine",
        "url": "https://tabnine.com",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $12/mo / Enterprise custom",
        "rating": 8.2,
        "summary": "AI code completion with privacy. Run locally or in your VPC. Supports 30+ languages and all IDEs.",
        "description": "Tabnine is an AI code completion tool that prioritizes privacy. Unlike GitHub Copilot, Tabnine can run 100% locally (on-premise) - your code never leaves your machine. It supports 30+ languages and all major IDEs.",
        "tutorial": "1. Install Tabnine extension in VS Code or JetBrains IDE. 2. Sign up at tabnine.com. 3. Free tier gives basic completions. 4. Pro tier ($12/mo): advanced AI model. 5. For privacy: enable Local Model mode. 6. Team tier: upload your codebase to train a custom model.",
        "pros": ["Can run 100% locally (privacy)", "Supports 30+ languages", "All major IDEs supported", "Team-trained custom models"],
        "cons": ["Less accurate than Copilot for some languages", "Local model requires good hardware", "UI is less polished"],
        "best_for": "Enterprise developers with privacy/security requirements",
        "alternatives": ["copilot", "cursor", "codium"],
        "tags": ["coding", "privacy", "local", "ide"],
        "featured": False
    })

# 10. Codium
if 'codium' not in existing:
    new_tools.append({
        "id": "codium",
        "name": "Codum",
        "url": "https://codum.com",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free (individual) / Team $12/user/mo",
        "rating": 8.7,
        "summary": "Free AI code completion. 70+ languages, all IDEs, and it's actually free (no usage limits).",
        "description": "Codum is the only AI code completion tool that is truly free for individual developers - no usage limits, no credit card required. It supports 70+ languages and all major IDEs. Codum also includes a Chat feature for free.",
        "tutorial": "1. Install Codum extension in VS Code, JetBrains, or other supported IDE. 2. Sign up at codum.com (free). 3. Start coding - completions appear automatically. 4. Use Codum Chat: select code, right-click Codum Chat. 5. For refactoring: ask Codum to refactor. 6. Team tier: deploy on your own infrastructure.",
        "pros": ["100% free for individuals (no limits)", "70+ languages supported", "Chat feature included for free", "On-premise option for teams"],
        "cons": ["Slightly less accurate than Copilot", "Smaller user community", "Chat feature less capable than Claude"],
        "best_for": "Developers who want free, unlimited AI code completion",
        "alternatives": ["copilot", "tabnine", "cursor"],
        "tags": ["coding", "free", "completion", "ide"],
        "featured": True
    })

# 11. LM Studio
if 'lm-studio' not in existing:
    new_tools.append({
        "id": "lm-studio",
        "name": "LM Studio",
        "url": "https://lmstudio.ai",
        "affiliate": None,
        "category": "coding",
        "pricing": "Free",
        "price_detail": "Free (open-source)",
        "rating": 8.6,
        "summary": "Run LLMs locally with a GUI. Download, chat, and experiment with open models - no coding needed.",
        "description": "LM Studio is a desktop app for running large language models locally. Unlike Ollama (CLI-based), LM Studio has a full GUI - you can browse models, download them, chat, and adjust parameters (temperature, top-p) visually. Great for non-technical users who want local AI.",
        "tutorial": "1. Download LM Studio from lmstudio.ai (Mac/Windows/Linux). 2. Open the app and go to the Discover tab. 3. Pick a model (Llama 3.2 3B for fast inference, Mistral 7B for quality). 4. Click Download - wait for it to finish. 5. Go to the Chat tab and start chatting. 6. Adjust parameters: temperature (creativity), context length, system prompt.",
        "pros": ["Full GUI - no CLI needed", "Browse and download models visually", "Adjust parameters with sliders", "Good for non-technical users"],
        "cons": ["Requires good hardware for larger models", "Less flexible than Ollama for developers", "No API server by default"],
        "best_for": "Non-technical users who want to run AI locally with a GUI",
        "alternatives": ["ollama", "huggingchat", "groq"],
        "tags": ["local", "gui", "open-source", "free"],
        "featured": False
    })

# 12. HuggingChat
if 'huggingchat' not in existing:
    new_tools.append({
        "id": "huggingchat",
        "name": "HuggingChat",
        "url": "https://huggingface.co/chat",
        "affiliate": None,
        "category": "chat",
        "pricing": "Free",
        "price_detail": "Free (open-source)",
        "rating": 8.0,
        "summary": "Open-source ChatGPT alternative. Runs on Hugging Face inference API. No account needed.",
        "description": "HuggingChat is an open-source chatbot by Hugging Face. It uses various open-weight models (Llama, Mistral, Phi, etc.) served via Hugging Face's inference API. No account needed - just go to the website and start chatting. 100% free and open-source.",
        "tutorial": "1. Go to huggingface.co/chat. 2. No signup needed - start chatting immediately. 3. Pick a model from the dropdown (Llama 3.2, Mistral 7B, Phi-3, etc.). 4. Each model has different strengths - try a few. 5. For coding: pick Codellama or DeepSeek Coder. 6. Share chats via URL. No history saved unless you sign in.",
        "pros": ["100% free, no account needed", "Multiple open-weight models", "Open-source", "No usage limits"],
        "cons": ["Slower than paid AIs", "Sometimes unavailable (high demand)", "No memory across sessions"],
        "best_for": "Users who want a free, open-source ChatGPT alternative",
        "alternatives": ["chatgpt", "claude", "perplexity"],
        "tags": ["chatbot", "open-source", "free", "huggingface"],
        "featured": False
    })

print(f"\nAdding {len(new_tools)} new tools...")
data['tools'].extend(new_tools)

# Write back
new_json = json.dumps(data, indent=2, ensure_ascii=False)
# Fix indentation: replace 2-space with 4-space to match original
new_json = new_json.replace('  ', '    ')

new_content = f"// Auto-generated from tools.json -- embedded for file:// compatibility\nwindow.__TOOLS_DATA__ = {new_json};\n"

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Done! Total tools: {len(data['tools'])}")
