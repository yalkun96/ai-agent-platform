from http.client import HTTPException

from fastapi import APIRouter, Depends
from app.schemas.agent import *
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter()


@router.get("/", response_model=list[AgentResponse])
def get_agents(db: Session = Depends(get_db)):
    return db.query(Agent).all()


@router.post("/", response_model=AgentResponse, status_code=201)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    new_agent = Agent(
        name=agent.name,
        model=agent.model,
        description=agent.description)
    
    db.add(new_agent)
    db.commit()
    db.refresh(new_agent)
    return new_agent
    
    
    
@router.get("/{agent_id}", response_model=AgentResponse)
def get_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.get(Agent, agent_id)
    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )
    return agent



@router.put("/{agent_id}", response_model=AgentResponse)
def update_agent(agent_id: int, agent: AgentUpdate, 
                 db: Session = Depends(get_db)):
    agent_to_update = db.get(Agent, agent_id)
    if agent_to_update is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )
    if agent.name is not None:
        agent_to_update.name = agent.name

    if agent.model is not None:
        agent_to_update.model = agent.model

    if agent.description is not None:
        agent_to_update.description = agent.description
        
    db.commit()
    db.refresh(agent_to_update)
    return agent_to_update
        
    
 
@router.delete("/{agent_id}")
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    agent_to_delete = db.get(Agent, agent_id)
    if agent_to_delete is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )
    db.delete(agent_to_delete)
    db.commit() 
    return {"message": "Agent deleted successfully"}
    
        

    