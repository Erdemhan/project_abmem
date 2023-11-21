from enums import ResourceType

class Resource():
    def __init__(self,type,name,fuelCost,emission) -> None:
        self.type = type
        self.name = name
        self.fuelCost = fuelCost
        self.emisson = emission
        pass
    