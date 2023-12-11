# db/models.py
from typing import Any
from django.db import models
from django_enumfield import enum
from .enums import AgentState , AgentType
from .base import Base
from .market import Market
from .models import Offer
from services.agent import agent_service as AgentService


# AGENT
class Agent(Base):
    market = models.ForeignKey(Market,on_delete=models.CASCADE,null=False)
    state = enum.EnumField(AgentState,null=True,default=AgentState.CREATED)
    budget = models.DecimalField(decimal_places=2,max_digits=12,null=False,default=0)
    type = enum.EnumField(AgentState,null=True,default=AgentType.HYBRID)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.data = None

    def init(self) -> None:
        self.state = AgentState.WAITING
        self.data = AgentService.readData()
        # Create portfolio
        self.save()

        
    def relearn(self,results = AgentState.RUNNING) -> None:
        AgentService.relearn(self,results)

    def predict(self,results = AgentState.RUNNING) -> int:
        return AgentService.predict(self,results)
    
    # Decision in design
    def calculateOffers(self,prediction: int) -> [Offer]:
        return AgentService.calculateOffers(self,prediction)
    
    def giveOffers(self) -> None:
        return AgentService.saveOffers(self)


    def run(self) -> bool:
        if self.state == AgentState.CREATED:
            self.init()
        self.state = AgentState.RUNNING
        self.save()
        self.relearn()
        prediction = self.predict()
        offers = self.calculateOffers(prediction)
        self.giveOffers(offers)
        self.state = AgentState.WAITING
        self.save()
        return True

