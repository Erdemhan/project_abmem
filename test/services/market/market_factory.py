import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.market import Market
from django_model.db.models.enums import MarketStrategy,MarketState


def create(sim, strategy: MarketStrategy,lowerBound: int, upperBound: int) -> Market:
    market = Market(strategy= MarketStrategy[strategy], state= MarketState.CREATED, lowerBidBound= lowerBound, upperBidBound= upperBound, simulation= sim)
    market.save()
    return market