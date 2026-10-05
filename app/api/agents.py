

from fastapi import APIRouter, HTTPException
from app.schemas.agent import *
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.agent import Agent
from app.services.agents import *
from app.core.security import get_current_user

router = APIRouter()


@router.get("/", response_model=list[AgentResponse])
def get_agents(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    found_agents = get_agents_service(user, db)
    return found_agents


@router.post("/", response_model=AgentResponse, status_code=201)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db), 
                 user: User = Depends(get_current_user)):
    
    new_agent = create_agent_service(agent, db, user)
    
    return new_agent
    
    
    
@router.get("/{agent_id}", response_model=AgentResponse)
def get_agent(agent_id: int, db: Session = Depends(get_db),
               user: User = Depends(get_current_user)):
    found_agent = get_agent_service(agent_id, db, user)
    return found_agent



@router.put("/{agent_id}", response_model=AgentResponse)
def update_agent(agent_id: int, agent: AgentUpdate, db: Session = Depends(get_db),
                 user: User = Depends(get_current_user)):
    
    updated_agent = update_agent_service(agent_id, agent, db, user)
    return updated_agent
        
    
 
@router.delete("/{agent_id}")
def delete_agent(agent_id: int, db: Session = Depends(get_db),
                  user: User = Depends(get_current_user)):
    delete_agent_service(agent_id, db, user)
    return {"message": "Agent deleted successfully"}
    
        

    