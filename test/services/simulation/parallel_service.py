import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.enums import MarketState,MarketStrategy
from services.market import period_factory as PeriodFactory
from services.visualization import visualization_service as VisualizationService
from django_model.db.models import Market,Period,Offer,Agent
from decimal import Decimal
from services.agent import agent_service as AgentService
from services.agent import agent_factory as AgentFactory
from services.file_reader import reader_service as ReaderService
from constants import *
import multiprocessing
import os
import timeit


def startPool(agents: [Agent]) -> [Agent]:
    with multiprocessing.Pool() as pool:
        offers = pool.map(AgentService.run,agents)
    pool.join()
    pool.terminate()
    return offers
