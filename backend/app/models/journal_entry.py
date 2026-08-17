import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    location_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("locations.id"), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[datetime] = mapped_column(nullable=False)
    mood: Mapped[str | None] = mapped_column(String, nullable=True)
    rating: Mapped[int | None] = mapped_column(Integer, nullable=True)
