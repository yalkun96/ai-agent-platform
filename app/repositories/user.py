from sqlalchemy.orm import Session 
from app.models.users import User
from sqlalchemy import select


def save_user(user: User, db: Session):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(username: str, db: Session):
    get_user_by_username = select(User).where(User.username == username)
    result = db.execute(get_user_by_username)
    return result.scalar_one_or_none()

def get_user_by_id(user_id: int, db: Session):
    user = db.get(User, user_id)
    return user