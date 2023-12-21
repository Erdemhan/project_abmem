import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")

# TO USE DJANGO ORM
from manage import init_django
init_django()

from django_model.db.models.simulation import Simulation
from django_model.db.models.market import Market
from django_model.db.models.agent import Agent
from django_model.db.models.models import *