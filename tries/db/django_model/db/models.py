# db/models.py
from django.db import models
from manage import init_django
from django_enumfield import enum
from enums import EnergyType,SimulationMode,SimulationState,AgentState,MarketState,MarketStrategy,PeriodType

init_django()

class Base(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




# define models here
class Resource(Base):
    energyType = enum.EnumField(EnergyType)
    name = models.CharField(max_length=20)
    fuelCost = models.DecimalField(decimal_places=1,max_digits=5)
    emission = models.DecimalField(decimal_places=1,max_digits=5)


class Market(Base):
    strategy = enum.EnumField(MarketStrategy)
    state = enum.EnumField(MarketState)
    lowerBidBound = models.IntegerField()
    upperBidBound = models.IntegerField()


class Simulation(Base):
    name = models.CharField(max_length=20)
    mode = enum.EnumField(SimulationMode)
    state = enum.EnumField(SimulationState)
    periodType = enum.EnumField(PeriodType)
    periodNumber = models.IntegerField()
    currentPeriod = models.IntegerField()
    market = models.OneToOneField(Market,on_delete=models.CASCADE)


class Agent(Base):
    simulation = models.ForeignKey(Simulation,on_delete=models.CASCADE)
    state = enum.EnumField(AgentState)
    budget = models.DecimalField(decimal_places=2,max_digits=12)


class Portfolio(Base):
    agent = models.OneToOneField(Agent,on_delete=models.CASCADE)


class Plant(Base):
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE)
    capacity = models.IntegerField()



class Period(Base):
    market = models.ForeignKey(Market,on_delete=models.CASCADE)
    periodNumber = models.IntegerField()
    demand = models.IntegerField()
    metDemand = models.IntegerField()
    marketVolume = models.IntegerField()
    ptf = models.IntegerField()


class Offer(Base):
    period = models.ForeignKey(Period,on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE)
    amount = models.IntegerField()
    offerPrice = models.DecimalField(decimal_places=2,max_digits=7)
    acceptance = models.BooleanField()
    acceptancePrice = models.DecimalField(decimal_places=2,max_digits=7)
    acceptanceAmount = models.IntegerField()

