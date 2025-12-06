# Fraser Valley Agent Intel

Browser-based property intelligence experience for Fraser Valley real estate agents. Backend FastAPI with stubbed integrations, frontend React + Vite with browser-side webLLM mocks.

## Backend (FastAPI)

Prereqs: Python 3.11+. Install deps:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run API (SQLite dev):

```bash
uvicorn backend.main:app --reload
```

Endpoints of note:
- `GET /health`
- `GET /agents`
- `GET /agent/resolve?name=&phone=`
- `GET /agent/{agent_id}/listings`
- `GET /listing/{listing_id}`
- `GET /listing/{listing_id}/intel`
- `POST /listing/{listing_id}/refresh_intel`

Startup seeds 3 agents, 8 listings, and generates intel JSON via stubbed data sources.

## Frontend (React + Vite + TS)

Install and run:

```bash
cd frontend
npm install
npm run dev
```

Routes:
- `/` landing
- `/agent` agent portal
- `/agent/:id/listings` listings table
- `/listing/:id` property intelligence view with charts + AI outputs

The browser-side `webllmClient.ts` returns deterministic AI-style content and chart specs so the experience works without remote LLMs.

## Data integrations

`backend/services/sources.py` contains stubbed functions for ParcelMapBC, ALR, BC hazard layers, municipal GIS, OSM/TransLink, StatCan, BC Stats, FVRD, weather, crime/health, imagery, and more. Replace these with real HTTP clients later.
