#!/usr/bin/env python3
"""Final sweep: verify/update remaining tools with latest 2026 pricing."""
import json

BASE = __import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))

with open(f'{BASE}/data/tools.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Verified 2026 pricing/versions for remaining tools
updates = {
    'dalle': {'price_detail': 'Included in ChatGPT Free (limited) / Plus $20/mo (unlimited DALL-E) / API per-image'},
    'runway': {'price_detail': 'Free (125 credits/mo) / Standard $15/mo / Pro $35/mo / Unlimited $95/mo / Enterprise custom', 'summary': 'Professional AI video generation. Gen-4.5 model with 4K output, Motion Brush, and camera control. $15/mo Standard.'},
    'pika': {'price_detail': 'Free (30 credits) / Basic $10/mo / Unlimited $35/mo / Agency $70/mo', 'summary': 'AI video generator specializing in creative/stylized content. Anime, art styles, and fun effects — $10/mo Basic.'},
    'jasper': {'price_detail': 'Creator $49/mo / Pro $69/mo / Business custom', 'summary': 'AI writing platform for marketing teams. Brand voice control, campaign workflows, team collaboration.'},
    'grammarly': {'price_detail': 'Free / Premium $12/mo / Business $15/user/mo / Enterprise custom', 'summary': 'AI writing assistant for grammar, tone, clarity. 2026 adds generative AI writing help across all platforms.'},
    'copy-ai': {'price_detail': 'Free / Pro $49/mo / Enterprise custom', 'summary': 'AI for GTM workflows and sales copy. Market research, persona generation, and multi-channel content.'},
    'suno': {'price_detail': 'Free (50 songs/mo) / Pro $10/mo (500 songs) / Premier $30/mo (2000 songs)', 'summary': 'AI music generator creating full songs from text prompts. Pro includes commercial license for content creation.'},
    'udio': {'price_detail': 'Free (60 songs/mo) / Standard $10/mo (600 songs) / Pro $30/mo (2000 songs)', 'summary': 'AI music generation with high-fidelity audio. Slightly better sound quality than Suno for atmospheric/ambient tracks.'},
    'canva-ai': {'price_detail': 'Free / Pro $12.99/mo / Teams $14.99/user/mo / Enterprise custom', 'summary': 'All-in-one AI design platform. Magic Studio for instant designs, AI image generation, background removal. 265M+ users.'},
    'figma-ai': {'price_detail': 'Free (3 projects) / Professional $15/mo / Organization $45/user/mo / Enterprise $75/user/mo', 'summary': 'Professional UI/UX design with AI copilot. Auto-generate components, rename layers, generate placeholder content.'},
    'firefly': {'price_detail': 'Free (25 credits/mo) / Standard $9.99/mo (100 credits) / Pro $19.99/mo (500 credits)', 'summary': 'Adobe\'s AI image generator integrated with Photoshop/Illustrator. Commercially safe (trained on licensed content).'},
    'perplexity': {'price_detail': 'Free / Pro $20/mo (300+ searches/day) / Max $200/mo (Deep Research) / Enterprise $40/seat/mo', 'summary': 'AI research engine with real-time web citations. 300+ Pro searches/day, Deep Research reports, Comet browser agent.'},
    'notion-ai': {'price_detail': 'Free / AI add-on $10/member/mo (on any plan)', 'summary': 'AI-powered workspace. Q&A against your documents, auto-generate content, summarize meetings. Integrated into Notion.'},
    'replit-ai': {'price_detail': 'Free (limited) / Core $25/mo (AI Agent) / Teams $40/user/mo', 'summary': 'Browser-based IDE with AI Agent that builds and deploys full-stack apps from natural language descriptions.'},
    'ideogram': {'price_detail': 'Free (10 prompts/day) / Plus $9/mo / Pro $30/mo / Business $60/mo', 'summary': 'AI image generator that excels at text rendering within images. Logo designs, posters, and typography-focused graphics.'},
    'khanmigo': {'price_detail': 'Included in Khan Academy (free for teachers/students) / Individual $4/mo', 'summary': 'AI tutor by Khan Academy. Guides students through problems, doesn\'t give answers. Socratic method for math, science, humanities.'},
    'duolingo-max': {'price_detail': 'Free / Super $12.99/mo / Max $30/mo (includes GPT-4 Roleplay and Explain)', 'summary': 'Duolingo\'s AI tier with GPT-4 powered Roleplay conversations and Explain My Answer for grammar understanding.'},
    'quizlet-ai': {'price_detail': 'Free / Plus $7.99/mo ($35.99/yr)', 'summary': 'AI-powered flashcards and study tools. Q-Chat AI tutor, practice tests, and smart study plans.'},
    'socratic': {'price_detail': 'Free (Google app)', 'summary': 'Google\'s free AI homework helper. Take a photo of a problem, Socratic explains the solution with step-by-step guidance.'},
    'taskade': {'price_detail': 'Free / Pro $19/mo / Business $39/user/mo / AI Agents add-on $10/mo', 'summary': 'AI-powered workspace for task management, mind maps, and team collaboration. Custom AI agents for workflow automation.'},
    'surfer-seo': {'price_detail': 'Essential $89/mo / Scale $129/mo / Scale AI $219/mo / Enterprise custom', 'summary': 'AI content optimization platform. Real-time SEO scoring, NLP entity suggestions, and AI Overview optimization for 2026.'},
    'adcreative': {'price_detail': 'Starter $29/mo / Pro $59/mo / Ultimate $119/mo / Enterprise custom', 'summary': 'AI ad creative generation. Generates high-converting ad visuals, copy, and social media creatives with brand consistency.'},
    'hubspot-ai': {'price_detail': 'Free tools available / Starter AI $20/mo / Pro AI $100/mo / Enterprise AI custom', 'summary': 'HubSpot\'s AI platform for CRM, marketing, sales, and service. AI content assistant, predictive lead scoring, chatbots.'},
    'writesonic': {'price_detail': 'Free (25 credits) / Individual $16/mo / Standard $79/mo / Enterprise custom', 'summary': 'AI SEO content platform. Article Writer 6.0, AI search optimization, brand voice training, and automated internal linking.'},
    'gamma': {'rating': 8.3},
    'playht': {'price_detail': 'Free (5,000 words/mo) / Creator $39/mo / Unlimited $99/mo / Enterprise custom'},
    'mureka': {'price_detail': 'Free (10 songs) / Pro $10/mo / Artist $30/mo'},
}

for tool in data['tools']:
    tid = tool['id']
    if tid in updates:
        for key, value in updates[tid].items():
            tool[key] = value
        print(f"  ✓ {tool['name']}")

with open(f'{BASE}/data/tools.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nUpdated {len(updates)} tools.")
