import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models import Simulation
from django_model.db.models.enums import *
from services.file_reader import reader_service as ReaderService
from services.market import market_factory as MarketFactory
from services.market import market_service as MarketService
from services.visualization import visualization_service as VisualizationService
from constants import *
import timeit


def init(simulation: Simulation):
    simulation.state = SimulationState.INITIALIZED
    simulation.currentPeriod = 1
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
    start = timeit.default_timer()
    if simulation.market.state == MarketState.CREATED:
        simulation.market.init()
        print("market inited")
    while simulation.currentPeriod < simulation.periodNumber:
        print("market run start")
        MarketService.run(simulation.market)
        simulation.currentPeriod += 1
        simulation.state = SimulationState.STARTED
        simulation.save()
        if simulation.mode == SimulationMode.ONLYRESULT:
            print("mode onlyresult" , simulation.mode)
            pass
        elif simulation.mode == SimulationMode.PERIODBYPERIOD:
            #wait for action
            key = input("Press enter to continue")
            pass
    print("sim viz")
    VisualizationService.visulaizeSimulation(simulation.market.period_set.all())
    #print("T: " , timeit.default_timer() - start)
    return isOk


