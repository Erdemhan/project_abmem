import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.enums import MarketState,MarketStrategy
from services.market import period_factory as PeriodFactory
from services.visualization import visualization_service as VisualizationService
from django_model.db.models import Market,Period,Offer
from decimal import Decimal
from services.agent import agent_service as AgentService
from services.agent import agent_factory as AgentFactory
from services.file_reader import reader_service as ReaderService
from constants import *


def init(market: Market) -> None:
    market.state = MarketState.INITIALIZED
    if market.strategy == MarketStrategy.DAYAHEAD:
        # Placeholder for future development
        pass
    agentData = readAgentData()
    agents = createAgents(market,agentData)
    for agentData,agent in zip(agentData,agents):
        AgentService.init(agent= agent,portfolioData= agentData[AGENTS_PORTFOLIO_KEY])
    market.save()

def startPool(market: Market, lower: int, upper: int, periodNum: int) -> None:
    market.state = MarketState.WAITINGAGENTS
    agents = market.agent_set.all()
    # ParallelService.startPool(agents)
    market.save()
    pass

def marketAlgorithm(market: Market, offers: [Offer]) :
    market.state = MarketState.CALCULATING
    # Market Algorithm / Calculate PTF
    market.save()
    pass

def marketClearing(market: Market, offers: [Offer], ptf: Decimal):
    market.state = MarketState.MARKETCLEARING
    # Market Clearing
    market.save()
    pass

def saveToDb(market: Market, offers: [Offer], ptf: Decimal) -> None:
    market.state = MarketState.BROADCASTING
    # for offer in offers save() / market.period.save()
    market.save()
    pass

def createPeriod(market: Market):
    PeriodFactory.create()
    pass

def readAgentData() -> dict:
    return ReaderService.readData(path= AGENT_DATA_PATH, key= AGENTS_DATA_KEY)

def createAgents(market: Market, agentData: dict):    
    agents = []
    for agent in agentData:
        agents.append(AgentFactory.create(market= market,
                                          budget= agent[AGENTS_BUDGET_KEY],
                                          type= agent[AGENTS_TYPE_KEY]))
    return agents

def showPeriodDetails(period: Period) -> None:
    VisualizationService.visualizePeriod(period)

def run(market: Market) -> bool:
    if market.state == MarketState.CREATED:
        market.init()

    period = createPeriod(market)
    offers = startPool(period)
    offers,ptf = marketAlgorithm(offers)
    offers = marketClearing(offers,ptf)
    
    saveToDb(offers,ptf)
    market.state = MarketState.PERIODEND
    market.save()
    showPeriodDetails(period)
    return True