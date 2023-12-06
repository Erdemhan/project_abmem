import db.models as models
from db.models import enums
def main():
    simulation = models.simulation.Simulation(name='TEST',
                                mode=enums.SimulationMode.STEPBYSTEP,
                                state=enums.SimulationState.STARTED,
                                periodType=enums.PeriodType.HOUR,
                                periodNumber=10,
                                currentPeriod=0,
                                )
    simulation.save()

    market = models.market.Market(strategy=enums.MarketStrategy.DAYAHEAD,
                              state=enums.MarketState.BROADCASTING,
                              lowerBidBound=0,
                              upperBidBound=100,
                              simulation=simulation
                              )
    market.save()

    


    resource = models.models.Resource(energyType=enums.EnergyType.FOSSIL,
                                  name='Coal',
                                  fuelCost=20.5,
                                  emission=0.5)
    resource.save()
    
    agent = models.agent.Agent(market=market,
                            budget=100)
    agent.save()
    
    portfolio=models.models.Portfolio(agent=agent)
    portfolio.save()

    plant = models.models.Plant(portfolio=portfolio,
                            resource=resource,
                            capacity=100)
    plant.save()



    print(agent.budget)



main()