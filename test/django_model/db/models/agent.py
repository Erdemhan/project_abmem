# db/models.py
from typing import Any
from django.db import models
from django_enumfield import enum
from .enums import AgentState , AgentType
from .base import Base
from .market import Market
from services.agent import agent_service as AgentService
import time

# AGENT
class Agent(Base):
    market = models.ForeignKey(Market,on_delete=models.CASCADE,null=False)
    state = enum.EnumField(AgentState,null=True,default=AgentState.CREATED)
    budget = models.DecimalField(decimal_places=2,max_digits=12,null=False,default=0)
    type = enum.EnumField(AgentState,null=True,default=AgentType.HYBRID)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.data = None

    def init(self):
        self.state = AgentState.WAITING
        self.data = AgentService.readData()
        self.save()
        time.sleep(5)
        
    def relearn(self,results = AgentState.RUNNING):
        self = AgentService.relearn(self,results)
        self.save()
        time.sleep(5)

    def predict(self,results = AgentState.RUNNING):
        return AgentService.predict(self,results)
    
    # Decision in design
    def calculateOffers(self,prediction):
        return AgentService.calculateOffers(self,prediction)
    
    def giveOffers(self):
        return AgentService.saveOffers(self)


    def run(self):
        if self.state == AgentState.CREATED:
            self.init()
            
        self.relearn()
        prediction = self.predict()
        self.state = AgentState.WAITING
        time.sleep(5)
        self.save()
        return self.calculateOffers(prediction)

