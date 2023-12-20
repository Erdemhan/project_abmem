
SIMULATION = 'simulation'
MARKET = 'market'
AGENTS = 'agents'
RESOURCES = 'resources'


def resourceCreatedString(name: str, id: int) -> str:
    return "Resource: " + name + " with id: " + str(id) + " created."

def resourcesCreationReportString(dataLenght: int, creationLength: int) -> str:
    return str(creationLength) + " Resources created " + str(dataLenght - creationLength) + " Resources already exists."