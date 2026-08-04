from pydantic import BaseModel, Field
from enum import Enum


class AIModel(Enum):
    GPT_5 = "gpt-5"
    CLAUDE =  "claude"
    GEMINI = "gemini"
    
class AgentCreate(BaseModel):
    name: str = Field(min_length = 3, max_length = 20)
    model: AIModel
    description: str | None=None


class AgentUpdate(BaseModel):
    pass

class AgentResponse(BaseModel):
    pass


    

    