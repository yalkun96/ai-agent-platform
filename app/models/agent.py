from sqlalchemy import  Enum
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from app.enums.agent import AIModel


class Agent(Base):
    __tablename__ = "agents"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    model: Mapped[AIModel] = mapped_column(Enum(AIModel))
    description: Mapped[str | None] = mapped_column()
    
    