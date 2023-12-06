# db/models.py
from django.db import models
from django_enumfield import enum
from enums import EnergyType
from .market import Market
from .agent import Agent
from .base import Base



# -------------------- MODELS ---------------------

# RESOURCE
class Resource(Base):
    energyType = enum.EnumField(EnergyType,null=False)
    name = models.CharField(max_length=20,null=False)
    fuelCost = models.DecimalField(decimal_places=1,max_digits=5,null=False,default=0)
    emission = models.DecimalField(decimal_places=1,max_digits=5,null=False,default=0)


# PORTFOLIO
class Portfolio(Base):
    agent = models.OneToOneField(Agent,on_delete=models.CASCADE,null=False)


# PLANT
class Plant(Base):
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE,null=False)
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE,null=False)
    capacity = models.IntegerField(default=0,null=False)


# PERIOD
class Period(Base):
    market = models.ForeignKey(Market,on_delete=models.CASCADE,null=False)
    periodNumber = models.IntegerField(null=False)
    demand = models.IntegerField()
    metDemand = models.IntegerField()
    marketVolume = models.IntegerField()
    ptf = models.IntegerField()


# OFFER
class Offer(Base):
    period = models.ForeignKey(Period,on_delete=models.CASCADE,null=False)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,null=False)
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE,null=False)
    amount = models.IntegerField()
    offerPrice = models.DecimalField(decimal_places=2,max_digits=7)
    acceptance = models.BooleanField()
    acceptancePrice = models.DecimalField(decimal_places=2,max_digits=7)
    acceptanceAmount = models.IntegerField()

