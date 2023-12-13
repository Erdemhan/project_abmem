# db/models.py
from typing import Any
from django.db import models
from django_enumfield import enum
from .enums import MarketState,MarketStrategy
from .base import Base
from services.market import market_service as MarketService
from services.visualization import visualization_service as VisualizationService
from decimal import Decimal

# MARKET
class Market(Base):
    strategy = enum.EnumField(MarketStrategy,null=False)
    state = enum.EnumField(MarketState,null=False,default=MarketState.CREATED)
    lowerBidBound = models.IntegerField()
    upperBidBound = models.IntegerField()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.data = self.readData()
        self.currentPeriod = -1

    def init(self):
        self.state = MarketState.INITIALIZING
        if self.strategy == MarketStrategy.DAYAHEAD:
            # Placeholder for future development
            pass
        self.data = self.readData()
        self.agents = self.createAgents()
        self.initAgents(self.agents)
        self.save()
        
    def readData(self):
        return MarketService.readData()

    def startPeriod(self):
        self.currentPeriod += 1
        return MarketService.createPeriod(self)

    def startAgents(self, period) :
        return MarketService.startPool(self.lowerBidBound,self.upperBidBound,period)

    def calculateOffers(self, offers):
        return MarketService.marketAlgorithm(self,offers)
    
    def marketClearing(self, offers,ptf: Decimal):
        return MarketService.marketClearing(self,offers,ptf)
    
    def broadCast(self,offers,ptf: Decimal) -> None:
        MarketService.saveToDb(self,offers,ptf)

    def showPeriodDetails(self) -> None:
        VisualizationService.visualizePeriod(self.period)

    def createAgents(self,agentData):
        return MarketService.createAgents(self,agentData)
    
    def initAgents(self):
        return MarketService.initAgents(self.agents)




    def run(self) -> bool:
        if self.state == MarketState.CREATED:
            self.init()

        period = self.startPeriod()
        offers = self.startAgents(period)
        offers,ptf = self.calculateOffers(offers)
        offers = self.marketClearing(offers,ptf)
        
        self.broadCast(offers,ptf)
        self.state = MarketState.PERIODEND
        self.save()
        self.showPeriodDetails()
        return True