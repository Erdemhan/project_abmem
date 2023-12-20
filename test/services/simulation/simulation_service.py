import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models import Simulation
from django_model.db.models.enums import *
from services.file_reader import reader_service as ReaderService
from services.market import market_factory as MarketFactory
from services.market import market_service as MarketService
from services.visualization import visualization_service as VisualizationService
from constants import *


def init(simulation: Simulation):
    simulation.state = SimulationState.INITIALIZED
    simulation.currentPeriod = -1
    if simulation.mode == SimulationMode.ONLYRESULT:
        # Placeholder for future development
        pass
    elif simulation.mode == SimulationMode.PERIODBYPERIOD:
            # Placeholder for future development
        pass
    marketData = readMarketData()
    market = MarketFactory.create(sim= simulation,
                                  strategy= marketData[MARKET_STRATEGY_KEY],
                                  lowerBound= marketData[MARKET_LOWERBOUND_KEY],
                                  upperBound= marketData[MARKET_UPPERBOUND_KEY])
    MarketService.init(market)
    simulation.save()


def readMarketData() -> dict:
    return ReaderService.readData(path= MARKET_DATA_PATH, key= MARKET_DATA_KEY)
 

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


