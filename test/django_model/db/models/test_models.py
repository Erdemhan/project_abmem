from django_model.db.models.enums import *


class Market():

    def __init__(self,strategy:MarketStrategy,state:MarketState,lowerBound:int,upperBound:int) -> None:
        self.strategy=strategy
        self.state = state
        self.lowerBound = lowerBound
        self.upperBound =upperBound


def market():
    return Market(strategy=MarketStrategy.DAYAHEAD,state=MarketState.CREATED,lowerBound=0,upperBound=100)

def main():
    market = market()