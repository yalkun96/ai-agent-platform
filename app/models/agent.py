from sqlalchemy import  Enum, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.enums.agent import AIModel
from app.models.users import User

class Agent(Base):
    __tablename__ = "agents"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    model: Mapped[AIModel] = mapped_column(Enum(AIModel))
    description: Mapped[str | None] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="agents")
