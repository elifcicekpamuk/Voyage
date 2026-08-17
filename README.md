# Voyage

**Every place has a story. Voya remembers them with you.**

Voya turns your life into a living map. Drop a pin where something
happened, write it down, and watch your memories build into a personal
timeline you can revisit, search, and relive — one place at a time.

No more scrolling through camera rolls trying to remember *where* that
trip was, or losing the little moments between the big ones. If you were
there, Voya remembers it with you.

## What you can do with Voya

- 📍 **Pin it** — Drop a marker anywhere in the world the moment something worth remembering happens.
- 📓 **Journal it** — Attach a note, a date, a mood to every place.
- 🗺️ **Relive it** — Scroll your life as a map and a timeline, not a folder of files.
- ✨ **Ask it** *(coming soon)* — "Where did I go with my friends last summer?" Voya's AI reads your journal and finds the answer.
- 📊 **See it** *(coming soon)* — Cities visited, favorite spots, your mood over the year, visualized.

## How it works today

Voya is early — we're building it in public, one phase at a time. Right
now the backend foundation is live: a FastAPI service backed by
PostgreSQL + PostGIS that stores users, places, and journal entries with
real geospatial data underneath. The map and journal UI, the AI-powered
search, and the yearly recap are next.

Curious about where this is headed? The full phase-by-phase plan lives in
[VOYA_ROADMAP.md](VOYA_ROADMAP.md).

## Built with

| Layer | Stack |
|---|---|
| Frontend | React, TypeScript, Tailwind CSS, Leaflet/Mapbox *(not started yet)* |
| Backend | Python, FastAPI, SQLAlchemy |
| Database | PostgreSQL + PostGIS |
| AI *(later phases)* | Vector search (ChromaDB/FAISS), RAG, LLM APIs |

## Project layout

```
Voyage/
├── docker-compose.yml     # PostgreSQL + PostGIS
└── backend/
    ├── requirements.txt
    ├── alembic/            # database migrations
    └── app/
        ├── main.py         # FastAPI entrypoint
        ├── core/           # config, DB session
        ├── models/         # SQLAlchemy models
        ├── schemas/        # request/response contracts
        ├── services/       # business logic
        └── api/routes/     # API endpoints
```

## Running it locally

```powershell
# 1. Start the database
docker compose up -d

# 2. Set up the backend
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
alembic upgrade head

# 3. Run the API
uvicorn app.main:app --reload
```

The API comes up at `http://127.0.0.1:8000`, with interactive docs at
`http://127.0.0.1:8000/docs`.
