import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_enumfield import enum
from typing import Any
from django_model.db.models.enums import *
from django_model.db.models.simulation import Simulation
from django_model.db.models.base import Base
from django.db import models


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


    