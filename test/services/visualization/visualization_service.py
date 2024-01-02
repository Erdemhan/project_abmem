import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db import models
from django_model.db.models.enums import *

def visualizePeriod(period) -> None:
    test()
    pass


def visulizeSimulation(periods) -> None:
    pass


def test():
    simulation = models.Simulation(name='TEST',
                                mode=SimulationMode.ONLYRESULT,
                                state=SimulationState.STARTED,
                                periodType=PeriodType.HOUR,
                                periodNumber=10,
                                currentPeriod=0,
                                )


    market = models.Market(strategy=MarketStrategy.DAYAHEAD,
                              state=MarketState.BROADCASTING,
                              lowerBidBound=0,
                              upperBidBound=100,
                              simulation=simulation
                              )


    resource = models.Resource(energyType=EnergyType.FOSSIL,
                                  name='Coal',
                                  fuelCost=20.5,
                                  emission=0.5)
    
    print(market.simulation.mode)

test()