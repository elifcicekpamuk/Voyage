from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.routes import journal_entries, locations, users

app = FastAPI(title="Voya API")

app.include_router(users.router)
app.include_router(locations.router)
app.include_router(journal_entries.router)


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


@app.get("/health")
def health():
    return {"status": "ok"}
