from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=8, max_length=100)

class UserResponse(BaseModel):
    id: int 
    username: str = Field(min_length=3, max_length=20)
    email: str = Field(min_length=5, max_length=50)