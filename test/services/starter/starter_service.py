import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from file_reader import reader_service as ReaderService
from simulation import simulation_factory as SimulationFactory
from simulation import simulation_service as SimulationService
from django_model.db.models import Simulation

def readData() -> dict:
    return ReaderService.readSimData()

def createSimulation(simData: dict) -> Simulation:
    return SimulationFactory.create(simData['name'],simData['mode'],simData['periodtype'],simData['periodnumber'])

def init(simulation: Simulation) -> None:
    SimulationService.init(simulation)
