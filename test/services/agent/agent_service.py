from django_model.db.models.models import Offer,Period
from django_model.db.models.agent import Agent
from django_model.db.models.enums import AgentState

def readData() -> dict:
    # ReaderService.read()
    pass

def relearn(agent: Agent, results: Period) -> None:
    agent.state = AgentState.LEARNING
    agent.save()
    # Learning Module
    pass

def predict(agent: Agent, results: Period) -> int:
    agent.state = AgentState.PREDICTING
    agent.save()
    # Prediction Module
    ptf = 10
    return ptf

def calculateOffers(agent: Agent, ptf: int) -> [Offer]:
    agent.state = AgentState.CALCULATING
    agent.save()
    # Offer Module
    return [1,2,3]

def saveOffers(agent: Agent,offers: [Offer]) -> None:
    agent.state = AgentState.OFFERING
    agent.save()
    # Prediction Module
    # for offer in offers save()
    pass