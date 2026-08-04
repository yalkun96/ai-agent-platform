from fastapi import APIRouter
from app.schemas.agent import *

router = APIRouter()

agents = []

@router.get("/")
def get_agents():
    return {
        "agents": []
    }
  
  
@router.post("/")
def create_agent(agent: AgentCreate):
    id_calculator = len(agents) + 1
    agent_dict = {
     "id": id_calculator,
     "name": agent.name,
     "model": agent.model,
     "description": agent.description   
    }
    
    agents.append(agent_dict)
    
    return agent_dict
    
    
@router.get("/{agent_id}")
def get_agent(agent_id: int):
    return {
        "agent_id": agent_id
    }
    
@router.post("/test")
def create_test(agent: AgentCreate):
    return {
        "message": "Agent created",
        "name": agent.name,
            }


