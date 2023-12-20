import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.models import Resource
from services.starter import resource_factory as ResourceFactory
from constants import *


def createFromData(resourcesData: dict) -> [Resource]:
    created = []
    for resource in resourcesData:
        resource = ResourceFactory.create(name= resource[RESOURCES_NAME_KEY],
                                                 energyType= resource[RESOURCES_ENERGY_TYPE_KEY],
                                                 fuelCost= resource[RESOURCES_FUELCOST_KEY],
                                                 emission= resource[RESOURCES_EMISSION_KEY])
        if resource:
            created.append(resource)
            print(resourceCreatedString(name=resource.name, id=resource.id))
    print(resourcesCreationReportString(dataLenght= len(resourcesData), creationLength= len(created)))
    return created
