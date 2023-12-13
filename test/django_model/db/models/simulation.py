# db/models.py
from django.db import models
from django_model.db.models.market import Market
from django_enumfield import enum
from .enums import SimulationMode,SimulationState,PeriodType,MarketState,MarketStrategy
from services.simulation import simulation_service as SimulationService
from services.market import market_factory as MarketFactory
from services.visualization import visualization_service as VisualizationService
from .base import Base
from typing import Any


# SIMULATION
class Simulation(Base):
    name = models.CharField(max_length=20,null=False)
    mode = enum.EnumField(SimulationMode,null=False)
    state = enum.EnumField(SimulationState,null=False,default=SimulationState.CREATED)
    periodType = enum.EnumField(PeriodType,null=False)
    periodNumber = models.IntegerField(null=False)
    currentPeriod = models.IntegerField(null=False)
    market =  models.OneToOneField(Market,on_delete=models.CASCADE,null=False)


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


    def init(self):
        self.state = SimulationState.INITIALIZED
        if self.mode == SimulationMode.ONLYRESULT:
            # Placeholder for future development
            pass
        elif self.mode == SimulationMode.PERIODBYPERIOD:
             # Placeholder for future development
            pass
        self.data = self.readData()
        self.checkResources(self.data['resources'])
        self.market = MarketFactory.create(self,self.data.market['strategy'])

    def readData(self):
        return None # Reader.read

    def checkResources(self,resourceData: dict) -> None:
         SimulationService.checkResources(resourceData)
        

        

    def run(self):
        if self.market.state == MarketState.CREATED:
            self.market.init()
        while self.currentPeriod > self.periodNumber:
            self.market.run()
            self.currentPeriod += 1
            self.save()
            if self.mode == SimulationMode.ONLYRESULT:
                pass
            elif self.mode == SimulationMode.PERIODBYPERIOD:
                #wait for action
                key = input("Enter any key to continue")
                pass
        VisualizationService.visulizeSimulation(self.market.period_set.all())


  