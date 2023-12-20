import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.models import Portfolio,Plant,Resource,Agent
from django_model.db.models.enums import *
from constants import *

def create(agent: Agent, plantsData: dict):
    portfolio = Portfolio(agent=agent)
    portfolio.save()
    for plant in plantsData:
        createPlant(portfolio,plant)
    return portfolio


def createPlant(portfolio: Portfolio, plantData: dict):
    resource = Resource.objects.filter(name= plantData[PLANT_RESOURCE_KEY]).first()
    plant = Plant(portfolio= portfolio, resource= resource, capacity= plantData[PLANT_CAPACITY_KEY]) 
    plant.save()
    return plant
