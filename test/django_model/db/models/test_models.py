from django_model.db.models.enums import *


class Market():

    def __init__(self,strategy:MarketStrategy,state:MarketState,lowerBound:int,upperBound:int) -> None:
        self.strategy=strategy
        self.state = state
        self.lowerBound = lowerBound
        self.upperBound =upperBound



