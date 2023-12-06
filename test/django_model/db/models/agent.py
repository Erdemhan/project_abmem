# db/models.py
from django.db import models
from django_enumfield import enum
from .enums import AgentState
from .base import Base
from .market import Market

# AGENT
class Agent(Base):
    market = models.ForeignKey(Market,on_delete=models.CASCADE,null=False)
    state = enum.EnumField(AgentState,null=True,default=AgentState.CREATED)
    budget = models.DecimalField(decimal_places=2,max_digits=12,null=False,default=0)
