import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class JournalEntryCreate(BaseModel):
    user_id: uuid.UUID
    location_id: uuid.UUID
    content: str
    date: datetime
    mood: str | None = None
    rating: int | None = None


class JournalEntryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    user_id: uuid.UUID
    location_id: uuid.UUID
    content: str
    date: datetime
    mood: str | None = None
    rating: int | None = None
