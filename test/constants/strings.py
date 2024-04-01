
SIMULATION = 'simulation'
MARKET = 'market'
AGENTS = 'agents'
RESOURCES = 'resources'
SYSPATH = 'D:\lokal\Projeler\Tez\abm\abmem_project\test'


def resourceCreatedString(name: str, id: int) -> str:
    return "Resource: " + name + " with id: " + str(id) + " created."

def resourcesCreationReportString(dataLenght: int, creationLength: int) -> str:
    return str(creationLength) + " Resources created " + str(dataLenght - creationLength) + " Resources already exists."

def resourceNotFoundString(resourceName: str):
    return "ResourceNotFoundError: Resource '" + resourceName + "' in agents.yml not found. Make sure it is included in resources.yml"
