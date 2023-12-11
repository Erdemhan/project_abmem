from django_model.db.models.agent import Agent
from django_model.db.models.models import Resource,Portfolio,Plant
from django_model.db.models.enums import *

def create(agent: Agent, plantsData: dict) -> Portfolio:
    portfolio = Portfolio(agent=agent)
    portfolio.save()
    for plant in plantsData():
        createPlant(portfolio,plant)
    return portfolio


def createPlant(portfolio: Portfolio ,plantData: dict) -> Plant:
    resource = None # TODO: Resource.getResourceByName(plantData['name'])
    plant = Plant(portfolio = portfolio, resource = resource, capacity=plantData['capacity'])
    plant.save()
    return plant
