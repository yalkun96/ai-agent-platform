

from fastapi import APIRouter, HTTPException
from app.schemas.agent import *
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.agent import Agent
from app.services.agent import *

router = APIRouter()


@router.get("/", response_model=list[AgentResponse])
def get_agents(db: Session = Depends(get_db)):
    found_agents = get_agents_service(db)
    return found_agents


@router.post("/", response_model=AgentResponse, status_code=201)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    new_agent = create_agent_service(agent, db)
    return new_agent
    
    
    
@router.get("/{agent_id}", response_model=AgentResponse)
def get_agent(agent_id: int, db: Session = Depends(get_db)):
    found_agent = get_agent_service(agent_id, db)
    return found_agent



@router.put("/{agent_id}", response_model=AgentResponse)
def update_agent(agent_id: int, agent: AgentUpdate, 
                 db: Session = Depends(get_db)):
    
    updated_agent = update_agent_service(agent_id, agent, db)
    return updated_agent
        
    
 
@router.delete("/{agent_id}")
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    delete_agent_service(agent_id, db)
    return {"message": "Agent deleted successfully"}
    
        

    