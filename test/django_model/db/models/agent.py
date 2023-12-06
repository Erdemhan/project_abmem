# db/models.py
from django.db import models
from django_enumfield import enum
from .enums import AgentState
from .base import Base
from .market import Market
from services.agent import agent_service as AgentService
import time

# AGENT
class Agent(Base):
    market = models.ForeignKey(Market,on_delete=models.CASCADE,null=False)
    state = enum.EnumField(AgentState,null=True,default=AgentState.CREATED)
    budget = models.DecimalField(decimal_places=2,max_digits=12,null=False,default=0)

    def init(self):
        self.state = AgentState.WAITING
        self.save()
        time.sleep(5)
        
    def relearn(self,results = AgentState.RUNNING):
        self = AgentService.relearn(self,results)
        self.save()
        time.sleep(5)

    def predict(self,results = AgentState.RUNNING):
        return AgentService.predict(self,results)
    

    def calculate_offers(self,prediction):
        return AgentService.calculate_offers(self,prediction)

    def run(self):
        self.relearn()
        prediction = self.predict()
        self.state = AgentState.WAITING
        time.sleep(5)
        self.save()
        return self.calculate_offers(prediction)

