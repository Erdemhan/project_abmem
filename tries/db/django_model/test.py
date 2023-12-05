import db.models as entitites
import enums
def main():
    market = entitites.Market(strategy=enums.MarketStrategy.DAYAHEAD,
                              state=enums.MarketState.BROADCASTING,
                              lowerBidBound=0,
                              upperBidBound=100
                              )
    market.save()
    simulation = entitites.Simulation(name='TEST',
                                      mode=enums.SimulationMode.STEPBYSTEP,
                                      state=enums.SimulationState.STARTED,
                                      periodType=enums.PeriodType.HOUR,
                                      periodNumber=10,
                                      currentPeriod=0,
                                      market=market
                                      )
    
    simulation.save()

    print(market.simulation.name)



main()