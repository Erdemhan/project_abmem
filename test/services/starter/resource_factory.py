import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.models import Resource
from django_model.db.models.enums import *
from decimal import Decimal

def create(name: str, energyType: EnergyType, fuelCost: Decimal, emission = Decimal) -> (Resource,bool):
    resource = Resource.objects.filter(name= name).first()

    if resource:
        resource = None
    else:
        if energyType == EnergyType.RENEWABLE:
            fuelCost ,emission = 0,0
        resource = Resource(name=name, energyType=EnergyType[energyType], fuelCost=fuelCost, emission=emission)
        resource.save()
        
    return resource