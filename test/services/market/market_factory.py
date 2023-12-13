from django_model.db.models.market import Market
from django_model.db.models.enums import MarketStrategy,MarketState

def create(sim, strategy: MarketStrategy, state: MarketState,lowerBound: int, upperBound: int) -> Market:
    market = Market(strategy =strategy, state =state, lowerBidBound= lowerBound, upperBidBound=upperBound, sim=sim)
    market.save()
    return market

def create(sim, strategy: MarketStrategy) -> Market:
    market = Market(strategy =strategy, sim=sim)
    market.save()
    return market