import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_enumfield import enum
from typing import Any
from enums import *
from base import Base
from django.db import models
from simulation import Simulation

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


    