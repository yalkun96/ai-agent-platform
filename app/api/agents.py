from http.client import HTTPException

from fastapi import APIRouter
from app.schemas.agent import *

router = APIRouter()

agents = []

@router.get("/", response_model=list[AgentResponse])
def get_agents():
    return agents
  
  
@router.post("/", response_model=AgentResponse, status_code=201)
def create_agent(agent: AgentCreate):
    id_calculator = len(agents) + 1
    agent_dict = {
     "id": id_calculator,
     "name": agent.name,
     "model": agent.model,
     "description": agent.description,
    }
    
    agents.append(agent_dict)
    
    return agent_dict
    
    
@router.get("/{agent_id}")
def get_agent(agent_id: int):
    return get_agent_by_id(agent_id)
    
    
@router.post("/test")
def create_test(agent: AgentCreate,):
    return {
        "message": "Agent created",
        "name": agent.name,
            }

@router.put("/{agent_id}")
def update_agent(agent_id: int, agent: AgentUpdate):
    find_agent = get_agent_by_id(agent_id)
    if agent.name is not None:
        find_agent["name"] = agent.name
    if agent.model is not None:
        find_agent["model"] = agent.model
    if agent.description is not None:
        find_agent["description"] = agent.description
    return find_agent
 
@router.delete("/{agent_id}")
def delete_agent(agent_id: int):   
    find_agent = get_agent_by_id(agent_id)
    if find_agent in agents: 
        agents.remove(find_agent)
        return find_agent
    

def get_agent_by_id(agent_id: int):
    find_agent = get_agent_by_id(agent_id)
    for agent in agents:
            if agent["id"] == agent_id:
                return agent
    if find_agent is None:       
        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )
        

    