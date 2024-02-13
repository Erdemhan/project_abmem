from django_model.db.models import *
from django_model.db.models import enums
from services.agent import agent_factory as AgentFactory

def main():
    simulation = Simulation(name='TEST',
                                mode=enums.SimulationMode.ONLYRESULT,
                                state=enums.SimulationState.STARTED,
                                periodType=enums.PeriodType.HOUR,
                                periodNumber=10,
                                currentPeriod=0,
                                )
    simulation.save()

    market = Market(strategy=enums.MarketStrategy.DAYAHEAD,
                              state=enums.MarketState.BROADCASTING,
                              lowerBidBound=0,
                              upperBidBound=100,
                              simulation=simulation
                              )
    market.save()




    resource = Resource(energyType=enums.EnergyType.FOSSIL,
                                  name='Coalala',
                                  fuelCost=20.5,
                                  emission=0.5)
    
    resource.save()

    agent = AgentFactory.create(market=market,budget=100,type=enums.AgentType.NUCLEAR)

    portfolio=Portfolio(agent=agent)
    portfolio.save()

    plant = Plant(portfolio=portfolio,
                            resource=resource,
                            capacity=100)

    
    plant.save()


    print(agent.budget)



main()