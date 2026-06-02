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

# HeyGen
if 'heygen' not in existing:
    new_tools.append({
        "id": "heygen",
        "name": "HeyGen",
        "url": "https://heygen.com",
        "affiliate": None,
        "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free / Creator $24/mo / Team $69/mo",
        "rating": 9.0,
        "summary": "AI avatar videos. Type text, get a talking head video in minutes.",
        "description": "HeyGen creates AI avatar videos from text. Pick an avatar (100+), type script, and HeyGen generates a talking head video — lip-synced, natural expressions, 40+ languages. Used by 10K+ companies for marketing, training, and sales videos.",
        "tutorial": "1. Sign up at heygen.com (free). 2. Click 'Create Video'. 3. Pick avatar (or upload your own photo for custom avatar). 4. Type script (or paste doc). 5. Choose voice (40+ languages, 200+ accents). 6. Click 'Generate' — 2-5 mins. 7. Edit: adjust speed, add captions, background.",
        "pros": ["Best AI avatar quality (lip-sync is amazing)", "40+ languages, 200+ accents", "Custom avatar (upload your photo)", "Used by 10K+ companies"],
        "cons": ["Free tier very limited (1 video/mo, watermarked)", "Custom avatar requires Pro ($69/mo)", "Can be expensive for high volume"],
        "best_for": "Marketers and trainers who need avatar videos",
        "alternatives": ["synthesia", "d-id", "runway-ml"],
        "tags": ["ai-avatar", "video-generation", "marketing", "multilingual"],
        "featured": True
    })

# Bolt.new
if 'bolt-new' not in existing:
    new_tools.append({
        "id": "bolt-new",
        "name": "Bolt.new",
        "url": "https://bolt.new",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $20/mo",
        "rating": 8.6,
        "summary": "AI web dev playground. Prompt → full-stack web app (React/Node). Runs in browser.",
        "description": "Bolt.new (by StackBlitz) is an AI-powered web dev playground. Type a prompt, get a full-stack web app (React, Vue, Node, etc.) — running instantly in your browser. No setup, no install. Export to GitHub or download ZIP. Free tier includes 10M tokens/day.",
        "tutorial": "1. Go to bolt.new (free, no signup needed). 2. Type prompt: 'Build a todo app with React and localStorage'. 3. Bolt generates the full project — code + preview. 4. Edit: type '/edit [instruction]' to modify. 5. Run: code runs instantly in browser (StackBlitz WebContainers). 6. Export: push to GitHub or download ZIP.",
        "pros": ["Full-stack apps in browser (no setup)", "Free tier (10M tokens/day)", "Export to GitHub", "StackBlitz WebContainers (real Node.js in browser)"],
        "cons": ["Less powerful than Cursor for large codebases", "Free tier has limits", "Browser-only (no local dev)"],
        "best_for": "Quick prototypes and full-stack web app demos",
        "alternatives": ["cursor", "v0-dev", "lovable"],
        "tags": ["ai-coding", "web-dev", "full-stack", "browser-based"],
        "featured": True
    })

# Lovable
if 'lovable' not in existing:
    new_tools.append({
        "id": "lovable",
        "name": "Lovable",
        "url": "https://lovable.dev",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $24/mo / Business custom",
        "rating": 8.4,
        "summary": "AI web app builder. Prompt → deployed web app. No coding needed.",
        "description": "Lovable builds full web apps from prompts — and deploys them instantly. Describe your app (e.g., 'A project management tool with drag-and-drop'), and Lovable generates the UI, backend, and database — then deploys to a live URL. Great for non-coders who want to ship products.",
        "tutorial": "1. Go to lovable.dev, sign up (free). 2. Type prompt: describe your app. 3. Lovable generates UI + backend + database. 4. Preview: click around, test. 5. Edit: type '/edit [changes]'. 6. Deploy: Lovable deploys to a live URL (free .lovable.app subdomain). 7. Connect custom domain (Pro).",
        "pros": ["Full app (UI + backend + DB) from prompt", "Instant deploy to live URL", "No coding needed", "Great for non-coders"],
        "cons": ["Free tier limited (5 edits/day)", "Less control than coding manually", "Pro tier needed for custom domain"],
        "best_for": "Non-coders who want to build and ship web apps",
        "alternatives": ["bolt-new", "v0-dev", "cursor"],
        "tags": ["ai-coding", "no-code", "web-app", "deployment"],
        "featured": True
    })

# Sourcegraph Cody
if 'cody' not in existing:
    new_tools.append({
        "id": "cody",
        "name": "Cody (Sourcegraph)",
        "url": "https://sourcegraph.com/cody",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free (unlimited) / Pro $9/mo / Enterprise custom",
        "rating": 8.5,
        "summary": "AI coding assistant by Sourcegraph. Unlimited code completions (free).",
        "description": "Cody is Sourcegraph's AI coding assistant. Unlike Copilot (limited completions), Cody Free gives UNLIMITED code completions and 500 chat messages/mo. Understands your entire codebase (not just open file). Supports 20+ LLMs (Claude, GPT-4, etc.).",
        "tutorial": "1. Install Cody extension (VS Code / JetBrains / Neovim). 2. Sign in with Sourcegraph (free). 3. Start typing — Cody autocompletes (unlimited, free). 4. Chat: Cmd/Ctrl+K → ask coding questions. 5. 'Explain this code': select code, right-click → Cody → Explain. 6. Switch LLM: Cody supports Claude, GPT-4, Mixtral (choose in settings).",
        "pros": ["UNLIMITED code completions (free!)", "Understands entire codebase", "Supports 20+ LLMs (your choice)", "500 chat messages/mo (free)"],
        "cons": ["Less integrated than Copilot (Microsoft ecosystem)", "Can be slow on very large codebases", "Chat limit (500/mo free, unlimited Pro)"],
        "best_for": "Developers who want unlimited AI completions for free",
        "alternatives": ["github-copilot", "cursor", "codeium"],
        "tags": ["ai-coding", "free", "unlimited-completions", "vscode-extension"],
        "featured": False
    })

# Synthesia
if 'synthesia' not in existing:
    new_tools.append({
        "id": "synthesia",
        "name": "Synthesia",
        "url": "https://synthesia.io",
        "affiliate": None,
        "category": "video",
        "pricing": "Paid",
        "price_detail": "Personal $22.5/mo / Enterprise custom",
        "rating": 8.8,
        "summary": "AI avatar video platform for enterprise. 140+ avatars, 120+ languages.",
        "description": "Synthesia is the enterprise-grade AI avatar video platform. 140+ diverse avatars, 120+ languages, and custom avatar creation. Used by 50K+ companies (including Nike, Barclays, Microsoft). API available for programmatic video generation.",
        "tutorial": "1. Sign up at synthesia.io. 2. Click 'Create Video'. 3. Pick avatar (140+ options, or custom). 4. Type script (120+ languages). 5. Customize: background, music, logos. 6. Generate — 5-10 mins. 7. For API: use Synthesia API to generate videos programmatically (Enterprise).",
        "pros": ["Enterprise-grade (50K+ companies)", "140+ avatars, 120+ languages", "Custom avatar creation", "API for programmatic generation"],
        "cons": ["Expensive (Personal $22.5/mo)", "No free tier (trial only)", "Custom avatar requires Enterprise"],
        "best_for": "Enterprises needing avatar videos at scale",
        "alternatives": ["heygen", "d-id", "pictory"],
        "tags": ["ai-avatar", "enterprise", "video-generation", "multilingual"],
        "featured": False
    })

# D-ID
if 'd-id' not in existing:
    new_tools.append({
        "id": "d-id",
        "name": "D-ID",
        "url": "https://d-id.com",
        "affiliate": None,
        "category": "video",
        "pricing": "Freemium",
        "price_detail": "Free trial / Pro $49/mo / Advanced $220/mo",
        "rating": 8.2,
        "summary": "AI talking photo/video. Upload a photo, make it talk. Also: AI video assistant (chat with video).",
        "description": "D-ID creates AI talking videos from a single photo. Upload a face photo, type/script, and D-ID animates the photo to speak — lip-synced. Also: 'AI Video Assistant' — chat with a video (upload a video, ask questions about it). API available.",
        "tutorial": "1. Go to d-id.com, sign up. 2. Click 'Create Video'. 3. Upload a photo (face). 4. Type script or paste text. 5. Choose voice (100+). 6. Click 'Generate' — 1-3 mins. 7. For API: use D-ID API to generate talking photos programmatically.",
        "pros": ["Photo → talking video (unique)", "API available", "100+ voices", "AI Video Assistant (chat with video)"],
        "cons": ["Free trial very limited", "Pro tier expensive ($49/mo)", "Photo quality affects output"],
        "best_for": "Creators who want talking photos/videos",
        "alternatives": ["heygen", "synthesia", "runway-ml"],
        "tags": ["ai-avatar", "talking-photo", "video-generation", "api"],
        "featured": False
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
