from django_model.db.models.models import Resource
from django_model.db.models.enums import EnergyType
from decimal import Decimal

def create(name: str, energyType: EnergyType, fuelCost: Decimal, emission = Decimal) -> (Resource,bool):
    created = False
    # if Resource.getResourceByName(plantData['name']) is not exist
    if energyType == EnergyType.RENEWABLE:
        fuelCost ,emission = 0,0
    resource = Resource(name=name, energyType=energyType, fuelCost=fuelCost, emission=emission)
    resource.save()
    created = True
    # else resource = getResourceByName(plantData['name'])
    return (resource.name,created)
    


def createFromData(resourcesData: dict) -> [Resource]:
    created = []
    for resource in resourcesData:
        resource,result = create(resource['name'],resource['energyType'],resource['fuelCost'],resource['emission'])
        if result:
            created.append(resource)
            print(resource.name , "with id:", resource.id, " Created")
    print(len(created), " Resources created", len(resourcesData)-len(created), " Resources already exists")
    return created
