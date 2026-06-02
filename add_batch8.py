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

# 61. GitHub Copilot
if 'github-copilot' not in existing:
    new_tools.append({
        "id": "github-copilot",
        "name": "GitHub Copilot",
        "url": "https://github.com/features/copilot",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free for students/OSS / $10/mo / Business $19/mo",
        "rating": 9.2,
        "summary": "AI pair programmer by GitHub. Code completions in real-time.",
        "description": "GitHub Copilot is the most widely-used AI coding assistant. Trained on public code (billions of lines). Supports VS Code, Visual Studio, Neovim, JetBrains. Chat: Copilot Chat answers coding questions. Free for students, teachers, and open-source maintainers.",
        "tutorial": "1. Install Copilot extension (VS Code/JetBrains). 2. Sign in with GitHub. 3. Start typing — Copilot suggests completions (gray text). 4. Tab to accept. 5. Copilot Chat: Cmd/Ctrl+I → ask coding questions. 6. '/' commands: /fix, /tests, /docs, /explain.",
        "pros": ["Most widely-used AI coder (10M+ devs)", "Free for students/OSS", "Chat mode (fix, tests, docs)", "Supports 20+ languages"],
        "cons": ["$10/mo for individuals (after free tier)", "Can suggest insecure code (review needed)", "Telemetry concerns (code sent to cloud)"],
        "best_for": "Developers who want the most mature AI coding assistant",
        "alternatives": ["cursor", "cody", "codeium"],
        "tags": ["ai-coding", "copilot", "github", "code-completion"],
        "featured": True
    })

# 62. Replit AI
if 'replit-ai' not in existing:
    new_tools.append({
        "id": "replit-ai",
        "name": "Replit AI",
        "url": "https://replit.com/ai",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free / Core $7/mo / Teams $20/mo",
        "rating": 8.7,
        "summary": "AI coding inside the browser IDE. Build full apps without setup.",
        "description": "Replit AI is built into the Replit browser IDE. Type comments, get code. 'Import from GitHub' → Replit AI adds features. 'Ask Replit' (AI chat): debug, explain, refactor. Great for learning and rapid prototyping. Free tier: unlimited public Repls, AI limited.",
        "tutorial": "1. Go to replit.com, sign up (free). 2. Create new Repl (e.g., 'Python'). 3. Type comment: '# create a flask app with login'. 4. Replit AI suggests code. 5. 'Ask Replit' (side panel): debug, explain. 6. 'Import from GitHub': paste repo URL, Replit AI adds features.",
        "pros": ["Browser-based (no setup)", "Great for learning", "Import from GitHub + AI adds features", "Free tier (unlimited public Repls)"],
        "cons": ["Free tier AI limited", "Less powerful than Cursor for large codebases", "Browser IDE (not for everyone)"],
        "best_for": "Students and developers who want zero-setup coding with AI",
        "alternatives": ["bolt-new", "cursor", "v0-dev"],
        "tags": ["ai-coding", "browser-ide", "replit", "zero-setup"],
        "featured": False
    })

# 63. V0 (Vercel)
if 'v0-dev' not in existing:
    new_tools.append({
        "id": "v0-dev",
        "name": "v0 (by Vercel)",
        "url": "https://v0.dev",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free / Promium $20/mo",
        "rating": 8.8,
        "summary": "AI UI generator. Prompt → React/Tailwind code. Copy-paste into project.",
        "description": "v0 (by Vercel) generates UI code from prompts. Type 'A dashboard with sidebar and dark mode' — get React + Tailwind CSS code. Copy-paste into your project. Free tier: 10 prompts/day. Great for UI scaffolding.",
        "tutorial": "1. Go to v0.dev (free signup with GitHub/Google). 2. Type prompt: 'A pricing page with 3 tiers, Tailwind, dark mode'. 3. v0 generates 3 variations. 4. Click to customize: modify prompt, or edit code directly. 5. Copy code (React/Tailwind) → paste into your project. 6. 'Download as ZIP' (Pro).",
        "pros": ["Generates real UI code (React/Tailwind)", "Copy-paste into your project", "3 variations per prompt", "Great for UI scaffolding"],
        "cons": ["Free tier: 10 prompts/day", "$20/mo for unlimited", "Code quality varies (review needed)"],
        "best_for": "Frontend devs who want to scaffold UI fast",
        "alternatives": ["bolt-new", "lovable", "cursor"],
        "tags": ["ai-ui", "react", "tailwind", "vercel"],
        "featured": True
    })

# 64. ElevenLabs (already exists? check)
if 'elevenlabs' not in existing and 'elevenlabs' not in existing:
    # Check if 'elevenlabs' or similar exists
    pass

# Actually, let me check what's already in existing
print("Checking for ElevenLabs, PlayHT, Rime, etc.")
missing_voice = [x for x in ['elevenlabs', 'playht', 'rime-ai', 'resemble-ai', 'murf', 'speechify', 'listne', 'otter-ai', 'tldv', 'read-ai'] if x not in existing]
print(f"Missing voice/meeting tools: {missing_voice[:10]}")

print(f"\nAdding {len(new_tools)} tools in this batch...")
data['tools'].extend(new_tools)

# Write back
new_json = json.dumps(data, indent=2, ensure_ascii=False)
new_json = new_json.replace('  ', '    ')

new_content = f"// Auto-generated from tools.json -- embedded for file:// compatibility\nwindow.__TOOLS_DATA__ = {new_json};\n"

with open('js/data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Done! Total tools: {len(data['tools'])}")
