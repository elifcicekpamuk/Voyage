from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, data: UserCreate) -> User:
    user = User(email=data.email, name=data.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def list_users(db: Session) -> list[User]:
    return db.query(User).order_by(User.created_at.desc()).all()


def get_user(db: Session, user_id) -> User | None:
    return db.get(User, user_id)
