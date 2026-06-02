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

# 76. Otter.ai (add if not exists - check was wrong earlier)
if 'otter-ai' not in existing:
    new_tools.append({
        "id": "otter-ai",
        "name": "Otter.ai",
        "url": "https://otter.ai",
        "affiliate": None,
        "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $16.99/mo / Business $30/mo",
        "rating": 8.8,
        "summary": "Real-time transcription + AI summary. Best for meetings.",
        "description": "Otter.ai is the leading real-time transcription tool. Joins Zoom/Meet/Teams automatically, transcribes everything, then AI summarizes: key topics, action items, sentiment. Free: 300 mins/mo. Used by 20M+ people.",
        "tutorial": "1. Sign up at otter.ai (free). 2. Install Chrome extension (for Google Meet) OR connect calendar. 3. Otter auto-joins meetings. 4. After meeting: get email with transcript + AI summary. 5. 'OtterPilot' (Pro): asks follow-up questions about the meeting. 6. Search across all meetings: 'What did John say about budget?'",
        "pros": ["Real-time transcription (not just post-meeting)", "AI summary + action items", "Free: 300 mins/mo", "20M+ users"],
        "cons": ["Free tier: 30 mins/meeting limit", "Pro needed for OtterPilot (AI Q&A)", "Can struggle with heavy accents"],
        "best_for": "Professionals who want searchable meeting transcripts + AI summary",
        "alternatives": ["fireflies-ai", "tldv", "read-ai"],
        "tags": ["transcription", "meeting-notes", "ai-summary", "real-time"],
        "featured": True
    })

# 77. Ada (AI Customer Service)
if 'ada' not in existing:
    new_tools.append({
        "id": "ada",
        "name": "Ada",
        "url": "https://www.ada.cx",
        "affiliate": None,
        "category": "business",
        "pricing": "Paid",
        "price_detail": "Custom pricing (Enterprise)",
        "rating": 8.1,
        "summary": "Enterprise AI chatbot for customer service. Automates 70%+ of inquiries.",
        "description": "Ada is the leading AI customer service automation platform. Deploys on web, mobile, SMS, WhatsApp, and social. Automates 70%+ of inquiries. No-code builder. Used by 300+ enterprises (Verizon, Zoom, etc.).",
        "tutorial": "1. Sign up at ada.cx (enterprise demo). 2. 'Automation Builder': no-code, drag-and-drop. 3. Train: upload knowledge base (PDFs, help docs). 4. Deploy: web widget, SMS, WhatsApp. 5. 'Ada Glass': human handoff (escalates to agent). 6. Analytics: see automation rate, top questions.",
        "pros": ["Automates 70%+ of inquiries", "No-code builder", "Multi-channel (web, SMS, WhatsApp)", "300+ enterprise customers"],
        "cons": ["Enterprise-only (no self-serve pricing)", "Setup takes 2-4 weeks", "Requires training data (knowledge base)"],
        "best_for": "Enterprises wanting to automate customer service inquiries",
        "alternatives": ["intercom-finomial", "drift", "zendesk-ai"],
        "tags": ["customer-service", "ai-chatbot", "enterprise", "no-code"],
        "featured": False
    })

# 78. Intercom Fin (AI Customer Support)
if 'intercom-fin' not in existing:
    new_tools.append({
        "id": "intercom-fin",
        "name": "Intercom Fin (AI Bot)",
        "url": "https://www.intercom.com/ai-chatbot",
        "affiliate": None,
        "category": "business",
        "pricing": "Paid",
        "price_detail": "Fin AI Bot: $0.99/resolution (add-on to Intercom)",
        "rating": 8.5,
        "summary": "AI chatbot that resolves 50%+ of support questions. Pay-per-resolution.",
        "description": "Fin is Intercom's AI bot. Reads your help docs, resolves questions accurately. 'Pay-per-resolution' ($0.99 per resolved conversation) — you only pay when Fin succeeds. Integrates with Intercom (already used by 25K+ businesses).",
        "tutorial": "1. Have an Intercom account (required). 2. Enable 'Fin AI Bot' in settings. 3. 'Train': Fin reads your help docs automatically. 4. Set 'Autopilot': Fin handles all new conversations. 5. 'Copilot': Fin suggests answers to human agents. 6. Analytics: see resolution rate, cost per resolution.",
        "pros": ["Pay-per-resolution ($0.99, only when successful)", " Reads help docs (accurate answers)", "Copilot mode (assists human agents)", "25K+ businesses on Intercom"],
        "cons": ["Requires Intercom subscription ($$)", "Can hallucinate if help docs are incomplete", "Not for complex technical support"],
        "best_for": "Businesses already using Intercom who want AI to resolve support tickets",
        "alternatives": ["ada", "zendesk-ai", "drift"],
        "tags": ["customer-support", "ai-bot", "pay-per-resolution", "intercom"],
        "featured": False
    })

# 79. Gong (AI Sales Intelligence)
if 'gong' not in existing:
    new_tools.append({
        "id": "gong",
        "name": "Gong",
        "url": "https://www.gong.io",
        "affiliate": None,
        "category": "business",
        "pricing": "Paid",
        "price_detail": "Custom pricing (Enterprise)",
        "rating": 8.7,
        "summary": "AI sales call analysis. Records, transcribes, and gives coaching insights.",
        "description": "Gong is AI for sales teams. Records + transcribes all sales calls (Zoom/Meet/Teams), then AI analyzes: talk-to-listen ratio, objections handled, next steps. 'Gong Insights': tells you which reps are struggling and why. Used by 100K+ sales reps.",
        "tutorial": "1. Sign up at gong.io (enterprise demo). 2. Connect calendar + video conferencing. 3. Gong auto-records + transcribes calls. 4. 'Gong Insights': see talk-to-listen ratio, filler words, next steps mentioned. 5. 'Deal Board': AI flags at-risk deals. 6. Coaching: share specific call clips with reps.",
        "pros": ["Records + transcribes all sales calls automatically", "AI coaching insights (talk-to-listen, objections)", "Deal risk detection", "100K+ sales reps use it"],
        "cons": ["Expensive (enterprise pricing, no self-serve)", "Can feel surveillance-heavy for reps", "Learning curve for managers"],
        "best_for": "Sales leaders who want AI insights into rep performance and deal health",
        "alternatives": ["chorous", "outreach", "salesloft"],
        "tags": ["sales-intelligence", "call-analysis", "ai-coaching", "enterprise"],
        "featured": False
    })

# 80. Jasper Chat (already exists as jasper-ai? Check)
if 'jasper-chat' not in existing:
    new_tools.append({
        "id": "jasper-chat",
        "name": "Jasper Chat",
        "url": "https://www.jasper.ai/chat",
        "affiliate": None,
        "category": "writing",
        "pricing": "Freemium",
        "price_detail": "Free trial / Creator $39/mo / Pro $59/mo",
        "rating": 7.9,
        "summary": "Jasper's ChatGPT alternative with brand voice and SEO integration.",
        "description": "Jasper Chat is like ChatGPT but trained on marketing content. 'Brand Voice': Jasper learns your brand's tone. Integrates with Surfer SEO (writes ranking content). Used by 100K+ marketing teams. Free trial, then $39/mo.",
        "tutorial": "1. Sign up at jasper.ai. 2. 'Brand Voice': upload examples of your writing. 3. Chat: 'Write a blog post about...' — Jasper matches your tone. 4. 'Jasper Commands': highlight text → 'Rewrite to be more concise'. 5. Integrate Surfer SEO: Jasper writes content that ranks. 6. 'Plagiarism Checker': built-in.",
        "pros": ["Brand Voice (learns your tone)", "Integrates with Surfer SEO", "Plagiarism checker built-in", "100K+ marketing teams"],
        "cons": ["$39/mo minimum (no free tier)", "Less capable than ChatGPT for non-marketing tasks", "Surfer SEO integration costs extra"],
        "best_for": "Marketing teams who want AI writing that matches their brand voice",
        "alternatives": ["chatgpt", "copy-ai", "writesonic"],
        "tags": ["ai-writing", "brand-voice", "seo", "marketing"],
        "featured": False
    })

# 81. Copy.ai (already added? Check batch5)
if 'copy-ai' not in existing and 'copyai' not in existing:
    new_tools.append({
        "id": "copy-ai",
        "name": "Copy.ai",
        "url": "https://www.copy.ai",
        "affiliate": None,
        "category": "writing",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $36/mo / Team $186/mo",
        "rating": 7.8,
        "summary": "AI copywriting for marketing. Blogs, ads, emails, social media.",
        "description": "Copy.ai generates marketing copy: blog intros, Facebook ads, email subject lines, Instagram captions. Free tier: 2000 words/mo. 'Chat by Copy.ai': ChatGPT alternative with marketing templates. Used by 10M+ marketers.",
        "tutorial": "1. Sign up at copy.ai (free). 2. Pick template: 'Blog Post', 'Facebook Ad', 'Email', etc. 3. Enter: product name, description, tone. 4. Click 'Create Copy' — get 10 variations. 5. 'Chat by Copy.ai': chat for long-form content. 6. 'Workflows': automate content pipelines (Pro).",
        "pros": ["Free tier (2000 words/mo)", "10 variations per prompt", "Chat by Copy.ai (ChatGPT alternative)", "10M+ marketers"],
        "cons": ["Free tier limited", "Output quality varies", "Pro tier needed for workflows"],
        "best_for": "Marketers who need quick copy variations for ads/emails",
        "alternatives": ["jasper-ai", "chatgpt", "writesonic"],
        "tags": ["ai-copywriting", "marketing", "free-tier", "chatgpt-alternative"],
        "featured": False
    })

# 82. Writer (Enterprise AI Writing)
if 'writer' not in existing:
    new_tools.append({
        "id": "writer",
        "name": "Writer",
        "url": "https://writer.com",
        "affiliate": None,
        "category": "writing",
        "pricing": "Paid",
        "price_detail": "Custom pricing (Enterprise)",
        "rating": 8.0,
        "summary": "Enterprise AI writing. Enforces brand guidelines across all content.",
        "description": "Writer is AI writing for enterprises. 'Brand Compliance': ensures all content follows brand guidelines (tone, terminology, legal). 'AI Content Detector': checks if content is AI-generated. Used by big tech (Uber, Twitter, etc.).",
        "tutorial": "1. Sign up at writer.com (enterprise demo). 2. 'Brand Settings': define your brand's tone, terminology, legal phrases. 3. 'Writer Assistant': Chrome extension — checks content as you write (Google Docs, Figma, etc.). 4. 'AI Content Detector': paste content → Writer tells you if it's AI-generated. 5. API: integrate into CMS.",
        "pros": ["Brand Compliance (enforces guidelines)", "AI Content Detector (unique)", "Chrome extension (works everywhere)", "Used by Uber, Twitter"],
        "cons": ["Enterprise-only (no self-serve pricing)", "Setup requires training on brand guidelines", "Less creative than ChatGPT"],
        "best_for": "Enterprises who need brand-compliant AI writing across teams",
        "alternatives": ["jasper-ai", "grammarly", "chatgpt-enterprise"],
        "tags": ["enterprise-writing", "brand-compliance", "ai-detector", "chrome-extension"],
        "featured": False
    })

# 83. Electric AI (IT Support Automation)
if 'electric-ai' not in existing:
    new_tools.append({
        "id": "electric-ai",
        "name": "Electric AI (IT Copilot)",
        "url": "https://www.electric.ai",
        "affiliate": None,
        "category": "business",
        "pricing": "Paid",
        "price_detail": "Custom pricing (SMB-focused)",
        "rating": 7.6,
        "summary": "AI IT support. Automates password resets, software requests, troubleshooting.",
        "description": "Electric is AI for IT support. Automates 50%+ of IT tickets: password resets, software install requests, troubleshooting. 'Electric AI': chat to resolve issues. For SMBs (10-500 employees) who can't afford full IT team.",
        "tutorial": "1. Sign up at electric.ai (SMB demo). 2. Install Electric agent on employee devices. 3. Employees chat with 'Electric AI' for IT help. 4. Automations: password reset (self-service), software requests (auto-approve). 5. 'IT Insights': see top IT issues across company. 6. Integrate: Slack, Okta, Azure AD.",
        "pros": ["Automates 50%+ of IT tickets", "Self-service for employees (password reset, etc.)", "SMB-focused (10-500 employees)", "Slack integration"],
        "cons": ["SMB-only (not for enterprises with existing IT)", "Setup takes 2-4 weeks", "Limited to IT tasks (not general AI)"],
        "best_for": "SMBs who want to automate IT support without hiring IT team",
        "alternatives": ["servicenow", "zendesk-ai", "freshservice"],
        "tags": ["it-support", "automation", "smb", "ai-copilot"],
        "featured": False
    })

# 84. Recast (AI Nutrition Coach)
if 'recast' not in existing:
    new_tools.append({
        "id": "recast",
        "name": "Recast (AI Nutrition)",
        "url": "https://www.recast.com",
        "affiliate": None,
        "category": "health",
        "pricing": "Freemium",
        "price_detail": "Free / Premium $9.99/mo",
        "rating": 7.4,
        "summary": "AI nutrition coach. Tracks food, gives personalized advice.",
        "description": "Recast is an AI nutrition coach. Snap photo of food → AI recognizes ingredients + calories. 'Coach': AI gives personalized nutrition advice (based on goals: weight loss, muscle gain, etc.). Free: basic tracking. Premium: personalized coaching.",
        "tutorial": "1. Download Recast app (iOS/Android). 2. 'Snap Food': take photo → AI recognizes ingredients + calories. 3. 'Coach': set goal (weight loss, muscle gain), AI gives daily advice. 4. 'Meal Planner': AI suggests meals based on preferences. 5. 'Grocery List': AI generates shopping list. 6. Premium: 1-on-1 coaching (human nutritionist review).",
        "pros": ["Snap photo → AI recognizes food + calories", "Personalized coaching (based on goals)", "Meal planner + grocery list", "Free tier (basic tracking)"],
        "cons": ["Photo recognition can be inaccurate", "Premium needed for personalized coaching", "Not a substitute for doctor/nutritionist"],
        "best_for": "People who want AI-assisted nutrition tracking and coaching",
        "alternatives": ["myfitnesspal", "noom", "cronometer"],
        "tags": ["nutrition", "ai-coach", "food-tracking", "health"],
        "featured": False
    })

# 85. Woebot (AI Mental Health)
if 'woebot' not in existing:
    new_tools.append({
        "id": "woebot",
        "name": "Woebot",
        "url": "https://woebot.io",
        "affiliate": None,
        "category": "health",
        "pricing": "Free",
        "price_detail": "Free (research-backed)",
        "rating": 7.9,
        "summary": "AI mental health chatbot. CBT-based, clinically validated.",
        "description": "Woebot is an AI mental health chatbot based on Cognitive Behavioral Therapy (CBT). 100% free, no ads. 'Check-ins': daily mood tracking + AI conversation. Clinically validated (studies show it reduces depression/anxiety). NOT a crisis hotline (for that, call 988).",
        "tutorial": "1. Download Woebot app (iOS/Android) or Facebook Messenger. 2. 'Check-in': daily 10-min conversation with Woebot. 3. 'Lessons': learn CBT techniques (reframing negative thoughts, etc.). 4. 'Mood Tracker': see patterns over time. 5. 'Crisis Resources': if in crisis, Woebot provides hotlines (but NOT a replacement for human help).",
        "pros": ["100% free, no ads", "CBT-based (clinically validated)", "Mood tracking + patterns", "NOT a data-harvesting app (privacy-focused)"],
        "cons": ["NOT for crisis situations (call 988 instead)", "Can feel repetitive after weeks", "No human therapist (CBT self-help only)"],
        "best_for": "People who want free, CBT-based mental health support (not crisis)",
        "alternatives": ["headspace", "calm", "betterhelp"],
        "tags": ["mental-health", "cbt", "free", "chatbot"],
        "featured": False
    })

# 86. MasterClass (AI-Personalized Learning)
if 'masterclass' not in existing:
    new_tools.append({
        "id": "masterclass",
        "name": "MasterClass",
        "url": "https://www.masterclass.com",
        "affiliate": None,
        "category": "education",
        "pricing": "Paid",
        "price_detail": "$10/mo (billed annually, $120/yr)",
        "rating": 8.6,
        "summary": "Celebrity-taught classes. AI recommends personalized learning path.",
        "description": "MasterClass has 100+ celebrity instructors: Gordon Ramsay (cooking), Serena Williams (tennis), Neil Gaiman (writing), etc. 'AI Learning Path': MasterClass recommends what to watch next based on your goals. $10/mo billed annually ($120/yr).",
        "tutorial": "1. Sign up at masterclass.com ($120/yr). 2. Pick class: e.g., 'Neil Gaiman Teaches Storytelling'. 3. Watch 10-20 min video lessons (high production value). 4. 'Workbooks': download PDF exercises. 5. 'AI Learning Path': tell MasterClass your goal ('I want to write a novel'), get personalized class sequence. 6. Mobile app: download for offline.",
        "pros": ["Celebrity instructors (unmatched quality)", "AI Learning Path (personalized)", "High production value (Netflix-quality)", "$10/mo (billed annually, good value)"],
        "cons": ["No certificate (not for professional skilling)", "Annual billing only ($120 upfront)", "Can be passive (watching ≠ doing)"],
        "best_for": "People who want to learn from celebrities (cooking, writing, sports, etc.)",
        "alternatives": ["coursera", "skillshare", "udemy"],
        "tags": ["celebrity-instructors", "learning", "ai-personalized", "video-classes"],
        "featured": True
    })

# 87. Brilliant (AI Learning for STEM)
if 'brilliant' not in existing:
    new_tools.append({
        "id": "brilliant",
        "name": "Brilliant",
        "url": "https://brilliant.org",
        "affiliate": None,
        "category": "education",
        "pricing": "Freemium",
        "price_detail": "Free (limited) / Premium $24.99/mo",
        "rating": 8.8,
        "summary": "Interactive STEM learning. Math, CS, data science. AI gives hints.",
        "description": "Brilliant is interactive learning for STEM: math, computer science, data science, physics. NOT videos — you solve problems interactively. 'AI Hints': stuck? AI gives progressively more specific hints. Free: 7-day trial. Premium: full access.",
        "tutorial": "1. Sign up at brilliant.org (free trial). 2. Pick topic: 'Data Science', 'Computer Science', 'Math', etc. 3. Solve interactive problems (NOT videos). 4. Stuck? 'AI Hint': progressively more specific. 5. 'Today's Challenge': daily problem (free). 6. Premium: $24.99/mo for full access.",
        "pros": ["Interactive (not passive videos)", "AI Hints (progressive help)", "Covers math, CS, data science", "Free trial (7 days)"],
        "cons": ["Premium is expensive ($24.99/mo)", "Less broad than Coursera (STEM-only)", "Can be challenging for beginners"],
        "best_for": "People who want to learn STEM interactively (not watch videos)",
        "alternatives": ["coursera", "khan-academy", "edx"],
        "tags": ["stem", "interactive-learning", "ai-hints", "math-cs"],
        "featured": True
    })

# 88. Khan Academy (Khanmigo AI Tutor)
if 'khan-academy' not in existing:
    new_tools.append({
        "id": "khan-academy",
        "name": "Khan Academy (Khanmigo AI)",
        "url": "https://www.khanacademy.org",
        "affiliate": None,
        "category": "education",
        "pricing": "Free",
        "price_detail": "100% Free (Khanmigo AI: donation-based)",
        "rating": 9.0,
        "summary": "Free education for all. Khanmigo AI tutor: personalized learning.",
        "description": "Khan Academy is 100% free education (funded by donations). 'Khanmigo': AI tutor powered by GPT-4 (donation-based, ~$10/mo suggested). Personalized learning: math, science, humanities, SAT prep. Used by 100M+ students.",
        "tutorial": "1. Sign up at khanacademy.org (free). 2. Pick subject: 'Math', 'Science', 'Humanities', etc. 3. Watch videos + do exercises. 4. 'Khanmigo AI Tutor': chat for help (donation-based, ~$10/mo). 5. 'SAT Prep': full practice tests. 6. 'Teacher Dashboard': teachers assign work, see student progress.",
        "pros": ["100% FREE (no ads, no paywall)", "Khanmigo AI tutor (GPT-4 powered)", "100M+ students", "SAT prep, AP courses"],
        "cons": ["Khanmigo is donation-based (not fully free)", "Less interactive than Brilliant", "Videos can be dry (traditional lecture style)"],
        "best_for": "Students who want free, high-quality education (supported by donations)",
        "alternatives": ["brilliant", "coursera", "edx"],
        "tags": ["free-education", "ai-tutor", "khanmigo", "non-profit"],
        "featured": True
    })

# 89. EdX (Harvard/MIT AI Courses)
if 'edx' not in existing:
    new_tools.append({
        "id": "edx",
        "name": "edX (Harvard/MIT)",
        "url": "https://www.edx.org",
        "affiliate": None,
        "category": "education",
        "pricing": "Freemium",
        "price_detail": "Free (audit) / Verified $50-$300/course",
        "rating": 8.4,
        "summary": "Harvard/MIT online courses. AI courses from top universities.",
        "description": "edX is Harvard + MIT's online learning platform. 4000+ courses from top universities (Harvard, MIT, Stanford, etc.). 'Audit' (free): watch videos, do exercises (no certificate). 'Verified' ($50-$300): certificate + graded assignments. AI courses: 'AI for Everyone' (Andrew Ng), etc.",
        "tutorial": "1. Sign up at edx.org (free). 2. Search: 'AI', 'Machine Learning', etc. 3. 'Audit' (free): watch videos, do exercises (no certificate). 4. 'Verified' ($50-$300): get certificate + graded assignments. 5. 'MicroBachelors/Masters': full degree online. 6. 'ChatGPT for Everyone' (Andrew Ng): popular AI course.",
        "pros": ["Harvard/MIT quality (top universities)", "Free audit (no certificate)", "Certificates available ($50-$300)", "MicroDegrees (Bachelors/Masters)"],
        "cons": ["Free = no certificate (limits resumé value)", "Can be academic/theoretical (less hands-on than Udemy)", "Some courses are outdated (AI moves fast)"],
        "best_for": "Students who want university-quality courses (free or certified)",
        "alternatives": ["coursera", "khan-academy", "udemy"],
        "tags": ["university-courses", "free-audit", "certificates", "harvard-mit"],
        "featured": False
    })

# 90. Duolingo Max (AI Language Learning)
if 'duolingo-max' not in existing:
    new_tools.append({
        "id": "duolingo-max",
        "name": "Duolingo Max (AI Features)",
        "url": "https://www.duolingo.com/max",
        "affiliate": None,
        "category": "education",
        "pricing": "Paid",
        "price_detail": "Max: $30/mo (includes Super: ad-free + unlimited hearts)",
        "rating": 8.2,
        "summary": "Duolingo with GPT-4: 'Explain My Answer', 'Roleplay' conversations.",
        "description": "Duolingo Max adds GPT-4 features to Duolingo: 'Explain My Answer' (AI explains why your answer was wrong), 'Roleplay' (AI conversation partner — practice real dialogues). $30/mo. 'Super Duolingo' ($12.99/mo): ad-free + unlimited hearts (no AI features).",
        "tutorial": "1. Download Duolingo (iOS/Android). 2. Subscribe to 'Max' ($30/mo). 3. 'Explain My Answer': after wrong answer, AI explains in detail. 4. 'Roleplay': practice real dialogues with AI (e.g., ordering coffee in Paris). 5. 'Super Duolingo' ($12.99/mo): ad-free + unlimited hearts (no AI). 6. 40+ languages.",
        "pros": ["GPT-4 features (Explain My Answer, Roleplay)", "40+ languages", "Gamified (addictive learning)", "Super Duolingo: ad-free ($12.99/mo)"],
        "cons": ["Max is expensive ($30/mo)", "Roleplay is limited (canned scenarios)", "Gamification can feel shallow (not for fluency)"],
        "best_for": "Language learners who want AI-assisted practice (explanations + roleplay)",
        "alternatives": ["babbel", "rosetta-stone", "hello-talk"],
        "tags": ["language-learning", "gpt-4", "roleplay", "gamified"],
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
