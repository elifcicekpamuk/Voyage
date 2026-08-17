import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.journal_entry import JournalEntryCreate, JournalEntryRead
from app.services import journal_entry_service

router = APIRouter(prefix="/journal-entries", tags=["journal-entries"])


@router.post("", response_model=JournalEntryRead, status_code=201)
def create_journal_entry(payload: JournalEntryCreate, db: Session = Depends(get_db)):
    return journal_entry_service.create_journal_entry(db, payload)


@router.get("", response_model=list[JournalEntryRead])
def list_journal_entries(user_id: uuid.UUID | None = Query(default=None), db: Session = Depends(get_db)):
    return journal_entry_service.list_journal_entries(db, user_id=user_id)


@router.get("/{entry_id}", response_model=JournalEntryRead)
def get_journal_entry(entry_id: uuid.UUID, db: Session = Depends(get_db)):
    entry = journal_entry_service.get_journal_entry(db, entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    return entry
