import django_model.db.models as models
from django_model.db.models.enums import *
from services.agent.agent_factory import *

def main():
    simulation = models.simulation.Simulation(name='TEST',
                                mode=SimulationMode.ONLYRESULT,
                                state=SimulationState.STARTED,
                                periodType=PeriodType.HOUR,
                                periodNumber=10,
                                currentPeriod=0,
                                )
    simulation.save()

    market = models.market.Market(strategy=MarketStrategy.DAYAHEAD,
                              state=MarketState.BROADCASTING,
                              lowerBidBound=0,
                              upperBidBound=100,
                              simulation=simulation
                              )
    market.save()


    resource = models.models.Resource(energyType=EnergyType.FOSSIL,
                                  name='Coal',
                                  fuelCost=20.5,
                                  emission=0.5)
    resource.save()
    



main()