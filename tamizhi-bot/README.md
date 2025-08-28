# Tamizhi BOT

Bilingual Tamil–English chatbot (Tamil, English, Tanglish) built with FastAPI.

## Features

- Language detect: Tamil/English/Mix
- Intents: greeting, farewell, math, Wikipedia, translation (placeholder), culture
- SQLite chat history persistence
- REST endpoints: `/healthz`, `/chat`, `/tts`
- Optional Streamlit UI

## Quickstart

```bash
cd tamizhi-bot
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
# Install runtime deps
python -m pip install fastapi==0.115.0 uvicorn[standard]==0.30.0 \
  pydantic==2.9.2 httpx==0.27.2 loguru==0.7.2 sqlalchemy==2.0.35 \
  wikipedia-api==0.6.0 gTTS==2.5.3

# Run API
uvicorn app.main:app --reload --port 8000
```

Test endpoints:

```bash
curl -s http://localhost:8000/healthz
curl -s -X POST http://localhost:8000/chat -H 'content-type: application/json' \
  -d '{"message":"Vanakkam"}'
```

## Streamlit UI (optional)

```bash
python -m pip install streamlit==1.37.1
streamlit run ui/streamlit_app.py
```

## Notes

- Translation currently uses a placeholder. To use real models, integrate IndicTrans2 via HuggingFace in `app/services/translate.py`.
- TTS uses Google TTS (`gTTS`) for Tamil/English.