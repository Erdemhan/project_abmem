# db/models.py
from django.db import models
from django_enumfield import enum
from enums import MarketState,MarketStrategy
from .base import Base
from .simulation import Simulation

# MARKET
class Market(Base):
    strategy = enum.EnumField(MarketStrategy,null=False)
    state = enum.EnumField(MarketState,null=False,default=MarketState.CREATED)
    lowerBidBound = models.IntegerField()
    upperBidBound = models.IntegerField()
    simulation = models.OneToOneField(Simulation,on_delete=models.CASCADE,null=False)