import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.enums import AgentState
from django_model.db.models import Agent,Offer,Portfolio
from services.file_reader import reader_service as ReaderService
from services.agent import portfolio_factory as PortfolioFactory

def init(agent: Agent, portfolioData: dict):
    agent.state = AgentState.INITIALIZED
    createPortfolio(agent,portfolioData)
    agent.save()

def relearn(agent: Agent, results) -> None:
    agent.state = AgentState.LEARNING
    agent.save()
    # Learning Module
    pass

def predict(agent: Agent, results) -> int:
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

def saveOffers(agent: Agent, offers: [Offer]) -> None:
    agent.state = AgentState.OFFERING
    agent.save()
    for offer in offers:
        offer.save()


def createPortfolio(agent: Agent, plantsData: dict) -> Portfolio:
    return PortfolioFactory.create(agent,plantsData)


def run(agent: Agent) -> bool:
    if agent.state == AgentState.CREATED:
        agent.__init__()
    agent.state = AgentState.RUNNING
    agent.save()
    relearn()
    prediction = predict()
    offers = calculateOffers(prediction)
    saveOffers(offers)
    agent.state = AgentState.WAITING
    agent.save()
    return True