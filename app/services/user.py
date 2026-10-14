from pydantic import BaseModel, Field
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password
from app.models.users import User
from sqlalchemy.orm import Session
from app.repositories.user import save_user
from app.repositories.user import get_user_by_username
from app.core.security import verify_password, create_access_token
from fastapi import HTTPException




def create_user_service(user_create: UserCreate, db: Session):
   
   hashed_password = hash_password(user_create.password)
   
   create_user = User(
       username=user_create.username,
       email=user_create.email,
       hashed_password=hashed_password
   )
   save_user(create_user, db)
   return create_user

def get_user_by_username_service(username: str, db: Session):
    return get_user_by_username(username, db)

def login_user_service(username: str, password: str, db: Session):

    user = get_user_by_username_service(username, db)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    password_is_valid = verify_password(
        password,
        user.hashed_password
    )
    if password_is_valid:
        access_token = create_access_token({"sub": str(user.id)})
        return {"access_token": access_token, "token_type": "bearer"}

    
    raise HTTPException(
        status_code=401,
        detail="Invalid username or password"
    )

        