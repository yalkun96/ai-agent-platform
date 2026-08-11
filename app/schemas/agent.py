from pydantic import BaseModel, Field
from app.enums.agent import AIModel
    
class AgentCreate(BaseModel):
    name: str = Field(min_length = 3, max_length = 20)
    model: AIModel
    description: str | None=None


class AgentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=20)
    model: AIModel | None = None
    description: str | None = None

class AgentResponse(BaseModel):
    id: int
    name: str = Field(min_length = 3, max_length = 20)
    model: AIModel
    description: str | None=None


    

    