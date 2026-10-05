from app.models.agent import Agent
from app.schemas.agent import AgentUpdate, AgentCreate, AgentResponse
from sqlalchemy.orm import Session 
from fastapi import Depends, HTTPException
from app.repositories.agent import *
from app.models.users import User

def get_agents_service(user: User, db: Session):
    all_agents = get_agents(user, db)
    return all_agents
    
def create_agent_service(agent: AgentCreate, db: Session, user: User):
    new_agent = Agent(
            name=agent.name,
            model=agent.model,
            description=agent.description,
            user_id=user.id)
    send_new_agent = save_agent(new_agent, db)
    return send_new_agent
    

def get_agent_service(agent_id: int, db: Session, user: User):
    found_agent = get_agent_by_id(agent_id, db, user)
    if found_agent is None:
                raise HTTPException(
                        status_code=404,
                        detail="Agent not found"
                    )
    return found_agent


def update_agent_service(agent_id: int, agent:AgentUpdate, 
                   db: Session, user: User):

    updated_agent = get_agent_by_id(agent_id, db, user)

    
    if updated_agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )
        
    for key, value in agent.model_dump(exclude_unset=True).items():
        setattr(updated_agent, key, value)
    save_agent(updated_agent, db)
    return updated_agent


def delete_agent_service(agent_id: int, db: Session, user: User):
    deleted_agent = get_agent_by_id(agent_id, db, user)
    if deleted_agent is None:
            raise HTTPException(
                status_code=404,
                detail="Agent not found"
            )
    delete_agent(deleted_agent, db)


