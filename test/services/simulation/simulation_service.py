import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models import Simulation,Market,Resource
from django_model.db.models.enums import *
from file_reader import reader_service as ReaderService
from starter import resource_service as ResourceService
from market import market_factory as MarketFactory
from market import market_service as MarketService
from visualization import visualization_service as VisualizationService


def checkResources(resourceData: dict) -> [Resource]:
    return ResourceService.createFromData(resourceData)

def init(simulation: Simulation):
    simulation.state = SimulationState.INITIALIZED
    simulation.currentPeriod = -1
    if simulation.mode == SimulationMode.ONLYRESULT:
        # Placeholder for future development
        pass
    elif simulation.mode == SimulationMode.PERIODBYPERIOD:
            # Placeholder for future development
        pass
    resourceData,marketData = readData()
    checkResources(resourceData)
    market = MarketFactory.create(simulation,marketData['strategy'])
    MarketService.init(market)
    simulation.save()


def readData(simulation: Simulation) -> dict:
    return ReaderService.readResourceData(), ReaderService.readMarketData()
 

def run(simulation: Simulation) -> bool:
    isOk = True
    if simulation.market.state == MarketState.CREATED:
        simulation.market.init()
    while simulation.currentPeriod > simulation.periodNumber:
        simulation.market.run()
        simulation.currentPeriod += 1
        simulation.save()
        if simulation.mode == SimulationMode.ONLYRESULT:
            pass
        elif simulation.mode == SimulationMode.PERIODBYPERIOD:
            #wait for action
            key = input("Enter any key to continue")
            pass
    VisualizationService.visulizeSimulation(simulation.market.period_set.all())
    return isOk


