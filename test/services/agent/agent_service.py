import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.enums import AgentState
from django_model.db.models import Agent,Offer,Portfolio,Resource
from services.file_reader import reader_service as ReaderService
from services.agent import portfolio_factory as PortfolioFactory
from services.agent import offer_factory as OfferFactory
import random

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
    return random.randint(10,1000)

def calculateOffers(agent: Agent, prediction: int) -> [Offer]:
    agent.state = AgentState.CALCULATING
    agent.save()
    offers = []

    for plant in agent.portfolio.plant_set.all():
        lowerBound = plant.resource.fuelCost
        offer = OfferFactory.create(agent=agent, resource=plant.resource, amount=plant.capacity, offerPrice=random.randint(lowerBound,250))
        offers.append(offer)
    # Offer Module
    return offers

def saveOffers(offers: [Offer]) -> None:
    for offer in offers:
        offer.save()


def createPortfolio(agent: Agent, plantsData: dict) -> Portfolio:
    return PortfolioFactory.create(agent,plantsData)


def run(agent: Agent) -> bool:
    if agent.state == AgentState.CREATED:
        print("entered to agent init in run")
        agent.__init__()
    print(agent.id, " entered to agent run. Budget: ", agent.budget)
    agent.state = AgentState.RUNNING
    agent.save()
    relearn(agent,results=0)
    prediction = predict(agent,results=0)
    offers = calculateOffers(agent,prediction)
    saveOffers(offers)
    agent.state = AgentState.WAITING
    agent.save()
    return offers