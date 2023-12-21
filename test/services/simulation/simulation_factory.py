import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.simulation import Simulation
from django_model.db.models.enums import SimulationMode,SimulationState,PeriodType

def create(name: str, mode: SimulationMode, periodType: PeriodType, periodNumber: int) -> Simulation:
    pass
    sim = Simulation(name = name,mode = SimulationMode[mode], periodType = PeriodType[periodType], periodNumber = periodNumber, currentPeriod = -1)
    sim.save()
    return sim