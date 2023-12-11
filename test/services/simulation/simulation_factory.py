from django_model.db.models.simulation import Simulation
from django_model.db.models.enums import SimulationMode,SimulationState,PeriodType

def create(name: str, mode: SimulationMode, periodType: PeriodType, periodNumber: int) -> Simulation:
    sim = Simulation(name = name,mode = mode, periodType = periodType, periodNumber = periodNumber, currentPeriod = -1)
    sim.save()
    return sim