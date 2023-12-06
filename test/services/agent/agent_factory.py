from django_model.db.models.agent import Agent
from django_model.db.models.enums import AgentState

def createAgent(market,budget):
    agent = Agent(market=market, state=AgentState.CREATED, budget=budget)
    agent.save()
    return  agent