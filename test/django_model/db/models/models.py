# db/models.py
from django.db import models
from django_enumfield import enum
from django_model.db.models.enums import EnergyType
from django_model.db.models.market import Market
from django_model.db.models.agent import Agent
from django_model.db.models.base import Base



# -------------------- MODELS ---------------------

# RESOURCE
class Resource(Base):
    energyType = enum.EnumField(EnergyType, null=False)
    name = models.CharField(max_length=20, null=False, unique=True)
    fuelCost = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=0)
    emission = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=0)


# PORTFOLIO
class Portfolio(Base):
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE, null=False)


# PLANT
class Plant(Base):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=False)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=False)
    capacity = models.IntegerField(default=0, null=False)


# PERIOD
class Period(Base):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, null=False)
    periodNumber = models.IntegerField(null=False)
    demand = models.IntegerField()
    metDemand = models.IntegerField()
    marketVolume = models.IntegerField()
    ptf = models.IntegerField()


# OFFER
class Offer(Base):
    period = models.ForeignKey(Period, on_delete=models.CASCADE, null=False)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=False)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=False)
    amount = models.IntegerField(null=False)
    offerPrice = models.DecimalField(decimal_places=2, max_digits=7, null=False)
    acceptance = models.BooleanField(null=True)
    acceptancePrice = models.DecimalField(decimal_places=2, max_digits=7, null=True)
    acceptanceAmount = models.IntegerField(null=True)
