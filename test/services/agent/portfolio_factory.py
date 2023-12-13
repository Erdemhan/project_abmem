
from django_model.db.models.models import Portfolio,Plant
from django_model.db.models.enums import *

def create(agent, plantsData: dict):
    portfolio = Portfolio(agent=agent)
    portfolio.save()
    for plant in plantsData():
        createPlant(portfolio,plant)
    return portfolio


def createPlant(portfolio,plantData: dict):
    resource = None # TODO: Resource.getResourceByName(plantData['name'])
    plant = Plant(portfolio = portfolio, resource = resource, capacity=plantData['capacity'])
    plant.save()
    return plant
