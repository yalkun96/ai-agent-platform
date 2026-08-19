from sqlalchemy.orm import Session 
from app.models.agent import Agent, AgentUpdate
from fastapi import HTTPException



def get_agents(db: Session):
    return db.query(Agent).all(
        
    )
    
def get_agent_by_id(agent_id: int, db: Session):
    agent = db.get(Agent, agent_id)
    return agent

def save_agent(agent: Agent, db: Session):
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

def delete_agent(agent: Agent, db: Session):
    db.delete(agent)
    db.commit()