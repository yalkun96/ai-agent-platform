from pwdlib import PasswordHash
import jwt
from app.core.config import settings
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.user import get_user_by_id

password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
 
def hash_password(password: str) -> str:
    hashed_password = password_hash.hash(password)
    return hashed_password

def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(data: dict):
    return jwt.encode(
        data,
        settings.secret_key,
        algorithm=settings.algorithm
    )
    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    decoded_jwt = jwt.decode(token, settings.secret_key, 
                             algorithms=[settings.algorithm])
    user_id = decoded_jwt.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user_id = int(user_id)
    user = get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    return user