from app.models.agent import Agent
from app.scehemas.agent import AgentUpdate, AgentCreate, AgentResponse
from sqlalchemy.orm import Session 
from fastapi import Depends, HTTPException
from app.repositories.agent import *



def get_agents_service(db: Session):
    all_agents = get_agents(db)
    return all_agents
    
def create_agent_service(agent: AgentCreate, db: Session):
    new_agent = Agent(
            name=agent.name,
            model=agent.model,
            description=agent.description)
    send_new_agent = save_agent(new_agent, db)
    return send_new_agent
    

def get_agent_service(agent_id: int, db: Session):
    found_agent = get_agent_by_id(agent_id, db)
    if found_agent is None:
                raise HTTPException(
                        status_code=404,
                        detail="Agent not found"
                    )
    return found_agent


def update_agent_service(agent_id: int, agent:AgentUpdate, 
                   db: Session):

    updated_agent = get_agent_by_id(agent_id, db)

    
    if updated_agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )
        
    for key, value in agent.model_dump(exclude_unset=True).items():
        setattr(updated_agent, key, value)
    save_agent(updated_agent, db)
    return updated_agent


def delete_agent_service(agent_id: int, db: Session):
    deleted_agent = get_agent_by_id(agent_id, db)
    if deleted_agent is None:
            raise HTTPException(
                status_code=404,
                detail="Agent not found"
            )
    delete_agent(deleted_agent, db)


