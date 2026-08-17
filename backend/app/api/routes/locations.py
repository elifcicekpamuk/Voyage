import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.location import LocationCreate, LocationRead
from app.services import location_service

router = APIRouter(prefix="/locations", tags=["locations"])


@router.post("", response_model=LocationRead, status_code=201)
def create_location(payload: LocationCreate, db: Session = Depends(get_db)):
    return location_service.create_location(db, payload)


@router.get("", response_model=list[LocationRead])
def list_locations(user_id: uuid.UUID | None = Query(default=None), db: Session = Depends(get_db)):
    return location_service.list_locations(db, user_id=user_id)


@router.get("/{location_id}", response_model=LocationRead)
def get_location(location_id: uuid.UUID, db: Session = Depends(get_db)):
    location = location_service.get_location(db, location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return location
