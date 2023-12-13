import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.agent import Agent
from django_model.db.models.enums import AgentState,AgentType

def create(market, budget: int,type):
    agent = Agent(market=market, state=AgentState.CREATED, budget=budget, type=type)
    agent.save()
    return  agent