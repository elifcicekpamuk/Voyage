# Voyage

Your places. Your stories. Your life.

Voya (short for Voyage) is a location-based personal journaling app. Drop a
pin where something happened, write about it, and build a map-based memory
timeline of your life — eventually searchable with AI ("find the places I
visited with friends last summer").

See [claude.md](claude.md) for the technical context/conventions and
[VOYA_ROADMAP.md](VOYA_ROADMAP.md) for the full phased roadmap and DB schema.

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL + PostGIS
- **Frontend:** React, TypeScript, Tailwind CSS, Leaflet/Mapbox (not started yet)
- **AI / Search (later phases):** Vector DB (ChromaDB/FAISS), LangChain/LlamaIndex, OpenAI/Anthropic API

## Status

**Phase 1 (MVP skeleton) — backend in progress.**

- [x] FastAPI + SQLAlchemy + PostGIS backend skeleton
- [x] `User`, `Location`, `JournalEntry` models and CRUD endpoints
- [x] Alembic migrations
- [ ] Frontend (React + map)
- [ ] Manual "click map, add pin + note" end-to-end flow

## Project Structure

```
Voyage/
├── docker-compose.yml     # PostgreSQL + PostGIS container
└── backend/
    ├── requirements.txt
    ├── alembic/            # DB migrations
    └── app/
        ├── main.py         # FastAPI entrypoint
        ├── core/           # config, DB session
        ├── models/         # SQLAlchemy models
        ├── schemas/        # Pydantic request/response models
        ├── services/       # business logic
        └── api/routes/     # endpoint definitions
```

## Backend Setup

1. Start the database:
   ```powershell
   docker compose up -d
   ```
2. Create a virtual environment and install dependencies:
   ```powershell
   cd backend
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
3. Configure environment variables:
   ```powershell
   copy .env.example .env
   ```
4. Apply database migrations:
   ```powershell
   alembic upgrade head
   ```
5. Run the API:
   ```powershell
   uvicorn app.main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`, with interactive docs
at `http://127.0.0.1:8000/docs`.
