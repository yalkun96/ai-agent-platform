from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.enums.agent import AIProvider
from app.models.users import User


class Agent(Base):
    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str | None] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="agents")
    system_prompt: Mapped[str | None] = mapped_column()
    provider: Mapped[AIProvider] = mapped_column()
    model_name: Mapped[str] = mapped_column()
    temperature: Mapped[float] = mapped_column()
    max_tokens: Mapped[int] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True)
