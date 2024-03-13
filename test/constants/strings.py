
SIMULATION = 'simulation'
MARKET = 'market'
AGENTS = 'agents'
RESOURCES = 'resources'
SYSPATH = 'D:\lokal\Projeler\Tez\abm\abmem_project\test'


def resourceCreatedString(name: str, id: int) -> str:
    return "Resource: " + name + " with id: " + str(id) + " created."

def resourcesCreationReportString(dataLenght: int, creationLength: int) -> str:
    return str(creationLength) + " Resources created " + str(dataLenght - creationLength) + " Resources already exists."