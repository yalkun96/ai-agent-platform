from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import *
from app.services.user import *
from app.models.users import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_data = create_user_service(user, db)
    return user_data

@router.post("/login", response_model=Token, status_code=200)
def login_user(user: OAuth2PasswordRequestForm = Depends()
               , db: Session = Depends(get_db)):
    user_login_data = login_user_service(user.username, user.password, db)
    return user_login_data