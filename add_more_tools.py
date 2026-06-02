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

# 13. LM Studio (already added as lm-studio, skip)

# 14. Gradio
if 'gradio' not in existing:
    new_tools.append({
        "id": "gradio",
        "name": "Gradio",
        "url": "https://gradio.app",
        "affiliate": None,
        "category": "coding",
        "pricing": "Free",
        "price_detail": "Free (open-source)",
        "rating": 8.3,
        "summary": "Build & share ML web demos in minutes. The fastest way to demo AI models.",
        "description": "Gradio is an open-source Python library that lets you build interactive ML demos in minutes. Wrap any Python function with a web UI — no frontend skills needed. Hugging Face uses Gradio for all their model demos. Great for prototyping and sharing models with clients.",
        "tutorial": "1. Install: pip install gradio. 2. Write a Python function (e.g., def classify_text(text): ...). 3. Create interface: gr.Interface(fn=classify_text, inputs='text', outputs='label').launch(). 4. Share publicly: .launch(share=True) gives you a public URL. 5. For Hugging Face: create a Space, pick Gradio template, push your code. 6. Advanced: use gr.ChatInterface for chatbots, gr.Gallery for image galleries.",
        "pros": ["Fastest way to demo ML models", "No frontend code needed", "Auto-generates public share link", "Deep integration with Hugging Face"],
        "cons": ["Python-only", "Limited UI customization", "Not for production (use FastAPI + React)"],
        "best_for": "ML engineers who want to demo models quickly",
        "alternatives": ["streamlit", "dash", "shiny"],
        "tags": ["ml-demo", "python", "open-source", "huggingface"],
        "featured": False
    })

# 15. Streamlit
if 'streamlit' not in existing:
    new_tools.append({
        "id": "streamlit",
        "name": "Streamlit",
        "url": "https://streamlit.io",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free (self-hosted) / Cloud free tier",
        "rating": 8.5,
        "summary": "Turn Python scripts into web apps in minutes. No frontend needed.",
        "description": "Streamlit is the fastest way to build data apps in Python. Write a normal Python script, add Streamlit commands, and get an interactive web app. Popular for AI/ML dashboards, data visualization, and internal tools. Streamlit Cloud lets you deploy from GitHub in one click.",
        "tutorial": "1. Install: pip install streamlit. 2. Create app.py with import streamlit as st. 3. Add widgets: st.slider('X'), st.button('Run'). 4. Run: streamlit run app.py — browser opens automatically. 5. Deploy: push to GitHub, connect to share.streamlit.io. 6. Advanced: st.session_state for state, st.cache for performance.",
        "pros": ["Turns Python script into web app", "Huge community + templates", "Free cloud hosting", "Great for AI/ML dashboards"],
        "cons": ["Python-only", "Limited layout control vs React", "Not for complex multi-page apps"],
        "best_for": "Data scientists who want to build AI/ML web apps without frontend code",
        "alternatives": ["gradio", "dash", "shiny"],
        "tags": ["data-app", "python", "mlops", "freemium"],
        "featured": True
    })

# 16. Weights & Biases
if 'wandb' not in existing:
    new_tools.append({
        "id": "wandb",
        "name": "Weights & Biases (W&B)",
        "url": "https://wandb.ai",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free (individual) / Team $50/user/mo",
        "rating": 8.6,
        "summary": "ML experiment tracking, dataset versioning, and model management. Industry standard.",
        "description": "W&B is the industry-standard MLOps platform. Track experiments (metrics, hyperparameters, git commits), version datasets, monitor model performance in production, and collaborate with your team. Every serious AI lab uses W&B.",
        "tutorial": "1. Install: pip install wandb. 2. Initialize: import wandb; wandb.init(project='my-project'). 3. Log metrics: wandb.log({'loss': 0.5, 'acc': 0.95}). 4. View dashboard: wandb.ai — see all your runs. 5. Dataset versioning: wandb.Artifact logs datasets. 6. Sweeps: hyperparameter search with Bayesian optimization.",
        "pros": ["Industry standard for ML experiment tracking", "Beautiful dashboards", "Great for team collaboration", "Free tier is generous"],
        "cons": ["Learning curve for advanced features", "Can slow down training (disable with mode='disabled')", "UI can feel cluttered"],
        "best_for": "ML engineers and researchers who need experiment tracking and MLOps",
        "alternatives": ["mlflow", "tensorboard", "comet"],
        "tags": ["mlops", "experiment-tracking", "ml", "enterprise"],
        "featured": False
    })

# 17. Hugging Face Hub
if 'huggingface' not in existing:
    new_tools.append({
        "id": "huggingface",
        "name": "Hugging Face Hub",
        "url": "https://huggingface.co",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free / Pro $9/mo / Enterprise custom",
        "rating": 9.2,
        "summary": "The GitHub of AI. 500K+ models, 100K+ datasets. Free inference API.",
        "description": "Hugging Face Hub is the central platform for open AI. Hosts 500K+ models (Llama, Mistral, Stable Diffusion, etc.), 100K+ datasets, and 50K+ demos. Free inference API (serverless) lets you call models without GPUs. Transformers library is the standard for loading models.",
        "tutorial": "1. Sign up at huggingface.co (free). 2. Try models in browser: click any model → 'Deploy' → 'Inference API'. 3. Use via Python: pip install transformers; from transformers import pipeline; pipe = pipeline('text-generation', model='mistralai/Mistral-7B'). 4. Free inference API: get token from settings, call https://api-inference.huggingface.co. 5. Host your own model: create a Space (Gradio/Streamlit/Docker). 6. Fine-tune: use TRL library or AutoTrain.",
        "pros": ["Largest collection of open AI models", "Free inference API (serverless)", "Transformers library = industry standard", "Great community + Spaces for demos"],
        "cons": ["Free inference API has rate limits", "Some models are unmaintained", "Can be overwhelming for beginners"],
        "best_for": "AI/ML engineers who want to use, fine-tune, or share open models",
        "alternatives": ["replicate", "together-ai", "modal"],
        "tags": ["model-hub", "open-source", "inference-api", "transformers"],
        "featured": True
    })

# 18. Replicate
if 'replicate' not in existing:
    new_tools.append({
        "id": "replicate",
        "name": "Replicate",
        "url": "https://replicate.com",
        "affiliate": None,
        "category": "coding",
        "pricing": "Paid",
        "price_detail": "Pay-per-second (e.g., $0.002/sec for Llama 3)",
        "rating": 8.8,
        "summary": "Run open-source AI models in the cloud. No GPU needed. API for image, video, music generation.",
        "description": "Replicate lets you run open-source AI models (Llama, Stable Diffusion, MusicGen, etc.) via API — no GPU needed. Perfect for adding AI features to your app without managing infrastructure. Host your own models too. Used by Unsplash, Vercel, and thousands of startups.",
        "tutorial": "1. Sign up at replicate.com, get API token. 2. Install: pip install replicate. 3. Run a model: replicate.run('stability-ai/sdxl:...', input={'prompt': '...'}). 4. For image generation: use SDXL, DALL-E 3 (via API), or Flux. 5. For text: Llama 3, Mistral, Claude (via API). 6. Deploy your own model: push a Cog Docker image to Replicate.",
        "pros": ["Run 1000+ open models via API", "No GPU/infrastructure to manage", "Host your own models", "Great documentation"],
        "cons": ["Pay-per-second (costs add up)", "Not for fine-tuning (use HF instead)", "Cold starts can be slow"],
        "best_for": "Developers who want to add AI features via API without managing GPUs",
        "alternatives": ["huggingface", "together-ai", "modal"],
        "tags": ["api", "open-models", "serverless", "paid"],
        "featured": True
    })

# 19. Together AI
if 'together-ai' not in existing:
    new_tools.append({
        "id": "together-ai",
        "name": "Together AI",
        "url": "https://together.ai",
        "affiliate": None,
        "category": "coding",
        "pricing": "Paid",
        "price_detail": "Pay-per-token (cheaper than OpenAI)",
        "rating": 8.4,
        "summary": "Run open-source LLMs at scale. Cheaper than OpenAI. Great for production AI.",
        "description": "Together AI provides fast inference for open-source LLMs (Llama 3, Mistral, Gemma, etc.) at a fraction of OpenAI's cost. Also offers GPU clusters for fine-tuning and training. Great for startups that want to avoid vendor lock-in with OpenAI.",
        "tutorial": "1. Sign up at together.ai, get API key. 2. Install: pip install together. 3. Call Llama 3: together.Complete.create(model='meta-llama/Llama-3-8b', prompt='...'). 4. Fine-tune: upload dataset, start a fine-tuning job on Together's GPUs. 5. Deploy: host your fine-tuned model on Together's inference endpoint. 6. Compare: Together Playground lets you compare 20+ models side-by-side.",
        "pros": ["Much cheaper than OpenAI API", "Runs latest open models", "Great for fine-tuning", "OpenAI-compatible API"],
        "cons": ["Smaller model selection than OpenAI", "Fine-tuning requires technical skills", "No consumer chatbot"],
        "best_for": "Startups and enterprises that want cheap LLM inference with open models",
        "alternatives": ["openai", "replicate", "modal"],
        "tags": ["llm-api", "open-models", "cheap", "production"],
        "featured": False
    })

# 20. Modal
if 'modal' not in existing:
    new_tools.append({
        "id": "modal",
        "name": "Modal",
        "url": "https://modal.com",
        "affiliate": None,
        "category": "coding",
        "pricing": "Freemium",
        "price_detail": "Free tier / Pay-as-you-go",
        "rating": 8.7,
        "summary": "Serverless GPU compute for AI. Run any code on expensive hardware — pay only for what you use.",
        "description": "Modal is serverless compute for AI workloads. Run training jobs, inference endpoints, and data pipelines on GPU/TPU hardware — without managing infrastructure. Write Python functions, decorate with @stub.function(gpu='A100'), and deploy. Used by Character.AI, Perplexity, and other AI startups.",
        "tutorial": "1. Install: pip install modal. 2. Authenticate: modal setup. 3. Write a function: @stub.function(gpu='T4') def generate(prompt): ... 4. Deploy: modal deploy app.py. 5. Call remotely: stub.run(generate, 'a cat'). 6. For web endpoints: @stub.function() @modal.web_server(8000) def serve(): .... 7. Monitor: modal dashboard shows logs and metrics.",
        "pros": ["Access to A100/H100 GPUs without buying", "Pay only for actual usage", "Great for inference endpoints", "Used by top AI startups"],
        "cons": ["Python-only", "Learning curve for configuration", "Can get expensive if not monitored"],
        "best_for": "AI engineers who need GPU compute without infrastructure management",
        "alternatives": ["replicate", "together-ai", "aws-sagemaker"],
        "tags": ["serverless", "gpu", "inference", "training"],
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
