from django_model.db.models.agent import Agent
from django_model.db.models.enums import AgentState,AgentType
from django_model.db.models.market import Market

def create(market: Market, budget: int,type: AgentType):
    agent = Agent(market=market, state=AgentState.CREATED, budget=budget, type=type)
    agent.save()
    return  agent