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
import decimal
import timeit

def init(market: Market) -> None:
    market.state = MarketState.INITIALIZED
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

from collections import defaultdict

def marketClearing(market: Market, offers: [Offer], demand: int):
    market.state = MarketState.CALCULATING
    market.save()
    metDemand = demand
    ptf = 0
    
    # Fiyatlara göre teklifleri grupla
    offer_groups = defaultdict(list)
    for offer in offers:
        offer_groups[offer.offerPrice].append(offer)
    
    # Fiyat gruplarını fiyatlarına göre sırala
    sorted_groups = sorted(offer_groups.items(), key=lambda x: x[0])

    for _, group in sorted_groups:
        if demand > 0:
            total_amount = sum(offer.amount for offer in group)
            # Grubun toplam miktarı talebi karşılıyorsa
            if total_amount <= demand:
                for offer in group:
                    offer.acceptanceAmount = offer.amount
                    offer.acceptance = True
                    offer.acceptancePrice = offer.offerPrice
                    demand -= offer.acceptanceAmount
                    ptf = offer.acceptancePrice
            else:
                ptf = priceGroupCalculation(group,demand)
                break
        else:
            break
    
    return offers, metDemand - demand,ptf

def priceGroupCalculation(group: [Offer], demand: int):
    #RECURSIVE
    ptf = 0
    if len(group) <=0 or demand <=0:
        return 0
    gDemand = demand / len(group)
    for offer in group:
        if offer.amount <= gDemand:
            offer.acceptanceAmount = offer.amount
            offer.acceptance = True
            offer.acceptancePrice = offer.offerPrice
            demand -= offer.acceptanceAmount
            group.remove(offer)
            ptf = priceGroupCalculation(group=group, demand=demand)
            break
        else:
            offer.acceptanceAmount = gDemand
            demand -= offer.acceptanceAmount
            offer.acceptance = True
            offer.acceptancePrice = offer.offerPrice
            ptf = offer.offerPrice
    return ptf

def updatePeriod(period:Period) -> Period:
    period.save()
    return period

def saveOffers(market: Market, offers: [Offer], ptf: Decimal) -> None:
    market.state = MarketState.BROADCASTING
    for offer in offers:
        offer.save()
        agent = offer.agent
        agent.budget += budgetCalculation(offer)
        agent.save()

def budgetCalculation(offer: Offer):
    return  decimal.Decimal((offer.acceptanceAmount * offer.acceptancePrice)) - (offer.resource.fuelCost * decimal.Decimal(offer.acceptanceAmount))

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
    print("PTF: ", period.ptf)
    offers = period.offer_set.all()
    for offer in offers:
        print("Agent: ", offer.agent.id, "Resource: ",offer.resource.name,offer.amount,"MW/h        ",
               offer.offerPrice,"$      ", offer.acceptance," ", offer.acceptancePrice,"$   ",offer.acceptanceAmount,"/",offer.amount,"MW/h")
    VisualizationService.visualizePeriod(period)

def payasptf(offers: [Offer], ptf: int):
    for offer in offers:
        if offer.acceptance:
            offer.acceptancePrice = ptf
    return offers

def run(market: Market) -> bool:
    start = timeit.default_timer()
    
    if market.state == MarketState.CREATED:
        print("market inited in market service")
        init(market)

    period = createPeriod(market)
    demand = getDemand()
    offers = startPool(market)
    offers = np.concatenate(offers)

    offers,metDemand,ptf = marketClearing(market,offers,demand)
    if market.strategy == MarketStrategy.PAYASPTF:
        payasptf(offers,ptf)

    period.metDemand, period.ptf = metDemand, ptf
    period = updatePeriod(period=period)
    saveOffers(market,offers,ptf)
    print(" funcs called and period updated")

    market.state = MarketState.PERIODEND
    market.save()
    print("period details will be shown")
    showPeriodDetails(period)
    print(timeit.default_timer() - start)
    return True

def getDemand() -> int:
    return 1630