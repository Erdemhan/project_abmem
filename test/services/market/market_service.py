import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.enums import MarketState,MarketStrategy
from services.market import period_factory as PeriodFactory
from services.visualization import visualization_service as VisualizationService
from django_model.db.models import Market,Period,Offer,Agent
from decimal import Decimal
from services.agent import agent_service as AgentService
from services.agent import agent_factory as AgentFactory
from services.simulation import parallel_service as ParallelService
from services.file_reader import reader_service as ReaderService
from constants import *
import numpy as np

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

def startPool(market: Market) -> None:
    market.state = MarketState.WAITINGAGENTS
    market.save()
    agents = market.agent_set.all()
    return ParallelService.startPool(agents)

def marketClearing(market: Market, offers: [Offer], demand: int) :
    market.state = MarketState.CALCULATING
    market.save()
    metDemand = demand
    offers = sorted(offers, key=lambda x: x.offerPrice)
    for i in range(len(offers)):
        offer = offers[i]
        offer.acceptance = False
        if demand > 0:
            if offer.amount < demand:
                offer.acceptanceAmount = offer.amount
                offer.acceptance = True
                offer.acceptancePrice = offer.offerPrice
                demand -= offer.acceptanceAmount
            else:
                offer.acceptanceAmount = demand
                offer.acceptance = True
                demand -= offer.acceptanceAmount # must be 0
        else:
            break
        i += 1
    return offers,metDemand-demand

def ptfCalculation(market: Market, offers: [Offer], demand):
    market.state = MarketState.MARKETCLEARING
    # Market Clearing
    market.save()
    pass
    return 1,2

def updatePeriod(period:Period, ptf: Decimal) -> Period:
    period.save()
    return period

def saveOffers(market: Market, offers: [Offer], ptf: Decimal) -> None:
    market.state = MarketState.BROADCASTING
    for offer in offers:
        offer.save()
    pass

def createPeriod(market: Market) -> Period:
    return PeriodFactory.create(market= market, num= market.simulation.currentPeriod, demand= getDemand())

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
        print("market inited in market service")
        init(market)

    period = createPeriod(market)
    demand = getDemand()
    offers = startPool(market)
    offers = np.concatenate(offers)

    ptf = ptfCalculation(market,offers,demand)
    offers,metDemand = marketClearing(market,offers,demand)

    period.metDemand = metDemand
    period = updatePeriod(period=period, ptf=ptf)
    saveOffers(market,offers,ptf)
    print(" funcs called and period updated")

    market.state = MarketState.PERIODEND
    market.save()
    print("period details will be shown")
    showPeriodDetails(period)
    return True

def getDemand() -> int:
    return 1630