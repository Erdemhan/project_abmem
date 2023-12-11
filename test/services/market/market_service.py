from django_model.db.models.models import Offer,Market,Period,Agent
from django_model.db.models.enums import MarketState,MarketStrategy,SimulationMode
from agent import agent_factory as AgentFactory
import period_factory as PeriodFactory
from decimal import Decimal


def startPool(market: Market, lower: int, upper: int, periodNum: int) -> [Offer]:
    market.state = MarketState.WAITINGAGENTS
    agents = market.agent_set.all()
    # ParallelService.startPool(agents)
    market.save()
    pass

def marketAlgorithm(market: Market, offers: [Offer]) -> ([Offer],Decimal):
    market.state = MarketState.CALCULATING
    # Market Algorithm / Calculate PTF
    market.save()
    pass

def marketClearing(market: Market,offers: [Offer], ptf: Decimal) -> [Offer]:
    market.state = MarketState.MARKETCLEARING
    # Market Clearing
    market.save()
    pass

def saveToDb(market: Market,offers: [Offer], ptf: Decimal) -> None:
    market.state = MarketState.BROADCASTING
    # for offer in offers save() / market.period.save()
    market.save()
    pass

def createPeriod(market: Market) -> Period:
    PeriodFactory.create()
    pass

def readData() -> dict:
    # ReaderService.readMarketData()
    pass

def createAgents(market: Market,agentData) -> [Agent]:
    agents = []
    for agent in agentData:
        agents.append(AgentFactory.create(market,agent.budget,agent.type))
    return agents


def initAgents(agents: [Agent]) -> None:
    for agent in agents:
        agent.init()



