from sqlalchemy.orm import Session

from app.models.agent import Agent
from app.models.users import User


def get_agents(user: User, db: Session):
    user_agents = db.query(Agent).filter(Agent.user_id == user.id).all()
    return user_agents


def get_agent_by_id(agent_id: int, db: Session, user: User):
    user_agent = (
        db.query(Agent).filter(Agent.user_id == user.id, Agent.id == agent_id).first()
    )
    return user_agent


def save_agent(agent: Agent, db: Session):
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent


def delete_agent(agent: Agent, db: Session):
    db.delete(agent)
    db.commit()
