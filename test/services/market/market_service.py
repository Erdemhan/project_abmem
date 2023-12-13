import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.enums import MarketState,MarketStrategy,SimulationMode
from . import period_factory as PeriodFactory
from decimal import Decimal


def startPool(market, lower: int, upper: int, periodNum: int):
    market.state = MarketState.WAITINGAGENTS
    agents = market.agent_set.all()
    # ParallelService.startPool(agents)
    market.save()
    pass

def marketAlgorithm(market, offers) :
    market.state = MarketState.CALCULATING
    # Market Algorithm / Calculate PTF
    market.save()
    pass

def marketClearing(market,offers, ptf: Decimal):
    market.state = MarketState.MARKETCLEARING
    # Market Clearing
    market.save()
    pass

def saveToDb(market,offers, ptf: Decimal) -> None:
    market.state = MarketState.BROADCASTING
    # for offer in offers save() / market.period.save()
    market.save()
    pass

def createPeriod(markett):
    PeriodFactory.create()
    pass

def readData() -> dict:
    # ReaderService.readMarketData()
    pass

def createAgents(market,agentData):
    from ..agent import agent_factory as AgentFactory
    agents = []
    for agent in agentData:
        agents.append(AgentFactory.create(market,agent.budget,agent.type))
    return agents


def initAgents(agents) -> None:
    for agent in agents:
        agent.init()



