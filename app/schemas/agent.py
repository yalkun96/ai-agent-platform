from pydantic import BaseModel, Field

from app.enums.agent import AIProvider


class AgentCreate(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    description: str | None = None
    system_prompt: str | None = None
    provider: AIProvider
    model_name: str
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=256, ge=1, le=1024)
    is_active: bool = Field(default=True)


class AgentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=20)
    description: str | None = None
    system_prompt: str | None = None
    provider: AIProvider | None = None
    model_name: str | None = None
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=256, ge=1, le=1024)
    is_active: bool = Field(default=True)


class AgentResponse(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=20)
    description: str | None = None
    system_prompt: str | None = None
    provider: AIProvider
    model_name: str
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=256, ge=1, le=1024)
    is_active: bool = Field(default=True)
