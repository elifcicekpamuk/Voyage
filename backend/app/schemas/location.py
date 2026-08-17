import uuid

from pydantic import BaseModel, ConfigDict


class LocationCreate(BaseModel):
    user_id: uuid.UUID
    title: str
    latitude: float
    longitude: float
    city: str | None = None
    category: str | None = None


class LocationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    user_id: uuid.UUID
    title: str
    latitude: float
    longitude: float
    city: str | None = None
    category: str | None = None
