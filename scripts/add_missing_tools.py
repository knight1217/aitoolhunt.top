#!/usr/bin/env python3
"""Add 5 missing tools referenced by compare pages to tools.json."""
import json

BASE = __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))

with open(f'{BASE}/data/tools.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_tools = [
    {
        "id": "playht", "name": "Play.ht",
        "url": "https://play.ht", "affiliate": None, "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free (5,000 words/mo) / Creator $39/mo / Unlimited $99/mo",
        "rating": 8.2,
        "summary": "Professional AI text-to-speech with 900+ voices across 140 languages. Ultra-realistic voice cloning and API access.",
        "description": "Play.ht is a powerful text-to-speech platform that generates incredibly natural-sounding AI voices. With over 900 AI voices across 140+ languages and accents, it's one of the most versatile TTS tools available. The standout feature is ultra-realistic voice cloning: upload a 30-second sample of any voice and Play.ht creates a clone that captures tone, pacing, and emotion. Developers can integrate via API for automated voice generation at scale.",
        "tutorial": "1. Sign up at play.ht with email or Google. 2. Choose a voice from the library (filter by language, gender, accent, or use case like 'narration' or 'conversational'). 3. Paste your text (up to 5,000 characters per generation). 4. Adjust speed, pitch, and pauses using the inline editor. 5. Click 'Generate' and your audio appears in seconds. 6. Download as MP3 or WAV, or use the embed player to add to your website. 7. For voice cloning: go to Voice Cloning tab, upload a clean 30-second audio sample, name your clone, wait 1-2 hours for processing.",
        "pros": ["900+ voices across 140 languages", "Ultra-realistic voice cloning", "Developer-friendly API", "Good free tier (5,000 words/mo)"],
        "cons": ["Cloning can take hours", "Premium voices cost extra credits", "UI feels dated compared to ElevenLabs"],
        "best_for": "Content creators, podcasters, and developers who need multi-language TTS at scale",
        "alternatives": ["elevenlabs"],
        "tags": ["text-to-speech", "voice-cloning", "audio", "api"]
    },
    {
        "id": "craft", "name": "Craft",
        "url": "https://www.craft.do", "affiliate": None, "category": "productivity",
        "pricing": "Freemium",
        "price_detail": "Free / Plus $8/mo / Family $15/mo / Team $25/user/mo",
        "rating": 8.4,
        "summary": "Beautiful AI-powered document editor and note-taking app. Native apps for Mac, iOS, Windows, and web.",
        "description": "Craft is a beautifully designed document editor and note-taking app with built-in AI capabilities. Unlike Notion's database-heavy approach, Craft focuses on creating stunning, visually rich documents with drag-and-drop ease. The AI assistant can summarize, translate, rewrite, and generate content directly inside your documents. Native apps on all platforms with seamless iCloud sync make it one of the best note-taking experiences available.",
        "tutorial": "1. Download Craft from craft.do for your platform (Mac, iOS, Windows, or use the web app). 2. Create a new document using templates for meeting notes, project plans, or wikis. 3. Highlight any text and click the AI sparkle icon to summarize, translate, rewrite, or continue writing. 4. Use '/' slash commands to insert images, tables, code blocks, and embeds. 5. Organize documents into folders and spaces via sidebar navigation. 6. Share documents via link with view/edit permissions for collaboration. 7. Use the daily notes feature as a journal that auto-dates each entry.",
        "pros": ["Beautiful native apps on all platforms", "Excellent AI writing assistant", "Superior design and typography", "Fast and responsive even with large docs"],
        "cons": ["No database or table views like Notion", "Free tier limited to 1 space", "Collaboration features behind paywall"],
        "best_for": "Writers, designers, and anyone who values beautiful document creation over complex databases",
        "alternatives": ["notion-ai"],
        "tags": ["note-taking", "writing", "documents", "productivity"]
    },
    {
        "id": "otter", "name": "Otter.ai",
        "url": "https://otter.ai", "affiliate": None, "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free (300 min/mo) / Pro $16.99/mo / Business $30/user/mo / Enterprise custom",
        "rating": 8.5,
        "summary": "Real-time AI meeting transcription and note-taking. Join meetings automatically, transcribe, summarize, and share.",
        "description": "Otter.ai is the leading AI-powered meeting assistant that automatically joins your Zoom, Google Meet, and Microsoft Teams calls to transcribe conversations in real time. It captures every word, identifies speakers, and generates smart summaries with action items. Beyond meetings, Otter can transcribe uploaded audio files, live conversations, and even phone calls through its mobile app. The searchable transcript archive makes finding past conversations effortless.",
        "tutorial": "1. Sign up at otter.ai and connect your Google or Microsoft calendar for auto-join. 2. Otter Assistant will automatically join scheduled meetings (Zoom, Meet, Teams). 3. During the meeting, see live transcription in the Otter web or mobile app. 4. After the meeting, Otter generates an AI summary with key topics, action items, and an outline. 5. Click any word in the transcript to jump to that moment in the audio recording. 6. Highlight and comment on specific transcript sections for team collaboration. 7. Search your entire Otter history to find any past conversation by keyword.",
        "pros": ["Real-time transcription with high accuracy", "Auto-joins meetings across all platforms", "Smart summaries with action items", "Searchable transcript archive"],
        "cons": ["Free tier limited to 30 min per conversation", "Occasional speaker identification errors", "Business plan required for team features"],
        "best_for": "Professionals, teams, and students who attend frequent meetings or lectures",
        "alternatives": ["fireflies"],
        "tags": ["transcription", "meetings", "audio", "productivity"]
    },
    {
        "id": "fireflies", "name": "Fireflies.ai",
        "url": "https://fireflies.ai", "affiliate": None, "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free (800 min storage) / Pro $18/seat/mo / Business $29/seat/mo / Enterprise $49/seat/mo",
        "rating": 8.3,
        "summary": "AI meeting assistant that transcribes, summarizes, and analyzes conversations across all major video platforms.",
        "description": "Fireflies.ai is an AI meeting assistant that automatically joins your video calls to record, transcribe, and analyze conversations. It works across Zoom, Google Meet, Microsoft Teams, Webex, and more. Fireflies goes beyond basic transcription with AI-powered search, smart summaries, conversation analytics (talk time, sentiment, and key topics), and integrations with 50+ apps including Salesforce, Slack, and Notion. The AI can even answer questions about your meetings using natural language.",
        "tutorial": "1. Sign up at fireflies.ai and connect your calendar (Google or Outlook). 2. Invite fred@fireflies.ai to your meetings or let Fireflies auto-join from your calendar. 3. Fireflies joins as a participant, records, and transcribes the entire meeting. 4. After the meeting, receive an email with the recording, transcript, and AI-generated summary. 5. Use the dashboard to search across all meetings by keyword, topic, or speaker. 6. Ask the AI chatbot questions like 'What did Sarah say about the Q3 budget?' and get instant answers. 7. Set up Soundbites to clip and share key moments from any meeting.",
        "pros": ["Works across all major video platforms", "AI chatbot for meeting Q&A", "50+ integrations (CRM, Slack, Notion)", "Conversation analytics and insights"],
        "cons": ["Free tier storage is limited", "Bot joining meetings can feel intrusive", "Transcription not as accurate as Otter in noisy environments"],
        "best_for": "Sales teams, recruiters, and customer success teams who need searchable meeting records",
        "alternatives": ["otter"],
        "tags": ["transcription", "meetings", "sales", "productivity"]
    },
    {
        "id": "mureka", "name": "Mureka",
        "url": "https://www.mureka.ai", "affiliate": None, "category": "audio",
        "pricing": "Freemium",
        "price_detail": "Free (limited generations) / Pro $10/mo / Premium $30/mo",
        "rating": 7.8,
        "summary": "AI music generator with full song composition, lyrics writing, and commercial-use licensing.",
        "description": "Mureka is an AI music generation platform that creates complete songs including melodies, arrangements, and lyrics from simple text prompts. Like Suno and Udio, it produces surprisingly musical results across genres from pop and rock to EDM and classical. Mureka distinguishes itself with commercial-use licensing included in paid plans and a growing library of community-shared tracks. The quality is impressive for AI-generated music, though it can't yet match professional human production.",
        "tutorial": "1. Visit mureka.ai and sign up for a free account. 2. Enter a prompt describing your song (e.g., 'Upbeat indie pop with acoustic guitar, female vocals, about summer road trips'). 3. Choose a genre preset or let AI determine the style. 4. You can write your own lyrics or let Mureka generate them from your prompt. 5. Click 'Generate' and wait 30-60 seconds for two song variations. 6. Listen to both versions, pick your favorite, and extend or remix it. 7. Download the audio file. Pro plan includes commercial-use rights for content creation.",
        "pros": ["Full songs with vocals and instruments", "Commercial license included in paid plans", "Growing community of creators", "Supports lyric customization"],
        "cons": ["Audio quality not professional-grade yet", "Limited free generations", "Smaller community than Suno or Udio"],
        "best_for": "Content creators, indie game developers, and musicians looking for quick song ideas",
        "alternatives": ["suno", "udio"],
        "tags": ["music-generation", "audio", "creative"]
    }
]

data['tools'].extend(new_tools)
with open(f'{BASE}/data/tools.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f'Added {len(new_tools)} tools. Total: {len(data["tools"])}')
