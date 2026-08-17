from sqlalchemy.orm import Session

from app.models.journal_entry import JournalEntry
from app.schemas.journal_entry import JournalEntryCreate


def create_journal_entry(db: Session, data: JournalEntryCreate) -> JournalEntry:
    entry = JournalEntry(
        user_id=data.user_id,
        location_id=data.location_id,
        content=data.content,
        date=data.date,
        mood=data.mood,
        rating=data.rating,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def list_journal_entries(db: Session, user_id=None) -> list[JournalEntry]:
    query = db.query(JournalEntry)
    if user_id is not None:
        query = query.filter(JournalEntry.user_id == user_id)
    return query.order_by(JournalEntry.date.desc()).all()


def get_journal_entry(db: Session, entry_id) -> JournalEntry | None:
    return db.get(JournalEntry, entry_id)
