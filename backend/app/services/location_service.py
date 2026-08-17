from geoalchemy2.shape import to_shape
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.location import Location
from app.schemas.location import LocationCreate, LocationRead


def _to_read_schema(location: Location) -> LocationRead:
    point = to_shape(location.geom)
    return LocationRead(
        id=location.id,
        user_id=location.user_id,
        title=location.title,
        latitude=point.y,
        longitude=point.x,
        city=location.city,
        category=location.category,
    )


def create_location(db: Session, data: LocationCreate) -> LocationRead:
    location = Location(
        user_id=data.user_id,
        geom=func.ST_SetSRID(func.ST_MakePoint(data.longitude, data.latitude), 4326),
        title=data.title,
        city=data.city,
        category=data.category,
    )
    db.add(location)
    db.commit()
    db.refresh(location)
    return _to_read_schema(location)


def list_locations(db: Session, user_id=None) -> list[LocationRead]:
    query = db.query(Location)
    if user_id is not None:
        query = query.filter(Location.user_id == user_id)
    return [_to_read_schema(loc) for loc in query.all()]


def get_location(db: Session, location_id) -> LocationRead | None:
    location = db.get(Location, location_id)
    return _to_read_schema(location) if location else None
