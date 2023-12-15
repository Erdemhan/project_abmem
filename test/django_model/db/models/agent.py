import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")

from typing import Any
from django_enumfield import enum
from enums import AgentState , AgentType
from base import Base
from market import Market
from django.db import models


# AGENT
class Agent(Base):
    market = models.ForeignKey(Market,on_delete=models.CASCADE,null=False)
    state = enum.EnumField(AgentState,null=True,default=AgentState.CREATED)
    budget = models.DecimalField(decimal_places=2,max_digits=12,null=False,default=0)
    type = enum.EnumField(AgentState,null=True,default=AgentType.HYBRID)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.state = AgentState.INITIALIZED
        self.save()
     
    

