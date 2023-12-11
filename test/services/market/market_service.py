from django_model.db.models.models import Offer,Market,Period
from django_model.db.models.enums import MarketState,MarketStrategy,SimulationMode
from decimal import Decimal


def startPool(market: Market, lower: int, upper: int, periodNum: int) -> [Offer]:
    market.state = MarketState.WAITINGAGENTS
    agents = market.agent_set.all()
    # ParallelService.startPool()
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
    # PeriodFactory.Create()
    pass

def readData() -> dict:
    # ReaderService.readMarketData()
    pass



