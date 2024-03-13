import sys

sys.path.append("D:\lokal\Projeler\Tez\abm\abmem_project\test")
from services.file_reader import reader_service as ReaderService
from services.simulation import simulation_factory as SimulationFactory
from services.simulation import simulation_service as SimulationService
from django_model.db.models import Simulation,Resource
from services.starter import resource_service as ResourceService
from constants import *


def start() -> None:
    simData,resourceData = readStarterData()
    simulation = createSimulation(simData)
    checkResources(resourceData)
    initSimulation(simulation)
    SimulationService.run(simulation)


def readStarterData() -> (dict,dict):
    return (ReaderService.readData(path= SIMULATION_DATA_PATH, key = SIMULATION_DATA_KEY),
            ReaderService.readData(path= RESOURCES_DATA_PATH, key= RESOURCES_DATA_KEY))


def createSimulation(simData: dict) -> Simulation:
    return SimulationFactory.create(name= simData[SIMULATION_NAME_KEY],
                                    mode= simData[SIMULATION_MODE_KEY],
                                    periodType= simData[SIMULATION_PERIOD_TYPE_KEY],
                                    periodNumber= simData[SIMULATION_PERIOD_NUMBER_KEY])


def initSimulation(simulation: Simulation) -> None:
    SimulationService.init(simulation)


def checkResources(resourceData: dict) -> [Resource]:
    return ResourceService.createFromData(resourceData)

#start()