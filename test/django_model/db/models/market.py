# db/models.py
from typing import Any
from django.db import models
from django_enumfield import enum
from .enums import MarketState,MarketStrategy,SimulationMode
from .base import Base
from .simulation import Simulation
from models import Period
from services.market import market_service as MarketService
from services.visualization import visualization_service as VisualizationService
import time

# MARKET
class Market(Base):
    strategy = enum.EnumField(MarketStrategy,null=False)
    state = enum.EnumField(MarketState,null=False,default=MarketState.CREATED)
    lowerBidBound = models.IntegerField()
    upperBidBound = models.IntegerField()
    simulation = models.OneToOneField(Simulation,on_delete=models.CASCADE,null=False)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.data = None
        self.currentPeriod = -1


    def init(self):
        self.state = MarketState.INITIALIZING
        if self.strategy == MarketStrategy.DAYAHEAD:
            pass
        self.data = self.readData()
        self.save()
        time.sleep(5)
        
    def readData(self):
        self.data = MarketService.readData()

    def startPeriod(self):
        self.currentPeriod += 1
        return MarketService.createPeriod(self)

    def startAgents(self):
        return MarketService.startPool(self.lowerBidBound,self.upperBidBound,self.currentPeriod)

    def calculateOffers(self,offers):
        return MarketService.marketAlgorithm(self,offers)
    
    def marketClearing(self,offers,ptf):
        return MarketService.marketClearing(self,offers,ptf)
    
    def broadCast(self,offers,ptf):
        MarketService.saveToDb(self,offers,ptf)

    def showPeriodDetails(self):
        VisualizationService.visualize(self.period)




    def run(self):
        if self.state == MarketState.CREATED:
            self.init()
        period = self.startPeriod()
        offers = self.startAgents()
        offers,ptf = self.calculateOffers(offers)
        offers = self.marketClearing(offers,ptf)
        self.broadCast(offers,ptf)
        self.state = MarketState.PERIODEND
        self.showPeriodDetails()
        self.save()