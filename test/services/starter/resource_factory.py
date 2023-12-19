import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.agent import Agent
from django_model.db.models.models import Resource,Portfolio,Plant
from django_model.db.models.enums import *
from decimal import Decimal

def create(energyType: EnergyType, name: str, fuelCost: Decimal, emission: Decimal) -> Resource:
    resource = Resource(energyType=energyType, name=name, fuelCost=fuelCost, emission=emission)
    resource.save()
    return resource