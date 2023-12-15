import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
import pandas as pd
from django_model.db.models.enums import *

DATAPATH = 'test/data/'

def readFile(path: str) -> dict:
    return  pd.read_excel(DATAPATH + path, engine='openpyxl', sheet_name=None).to_dict(orient='records')[0]

def readSimData(path: str = 'simulation.xlsx') -> dict:
    return  pd.read_excel(DATAPATH + path, engine='openpyxl', sheet_name='simulation').to_dict(orient='records')[0]

def readMarketData(path: str= 'market.xlsx') -> dict:
    return  pd.read_excel(DATAPATH + path, engine='openpyxl', sheet_name='market').to_dict(orient='records')[0]

def readAgentData(path: str= 'agent.xlsx') -> dict:
    return  pd.read_excel(DATAPATH + path, engine='openpyxl', sheet_name='agent').to_dict(orient='records')[0]

def readResourceData(path: str= 'resource.xlsx') -> dict:
    return  pd.read_excel(DATAPATH + path, engine='openpyxl', sheet_name='agent').to_dict(orient='records')[0]

