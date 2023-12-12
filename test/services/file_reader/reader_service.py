import pandas as pd

DATAPATH = '../../data/'

def readFile(path: str) -> dict:
    return  pd.read_excel(DATAPATH+path, engine='openpyxl', sheet_name=None)

def readSimData(path: str) -> dict:
    return  pd.read_excel(DATAPATH+path, engine='openpyxl', sheet_name='simulation')

def readMarketData(path: str) -> dict:
    return  pd.read_excel(DATAPATH+path, engine='openpyxl', sheet_name='market')

def readAgentData(path: str) -> dict:
    return  pd.read_excel(DATAPATH+path, engine='openpyxl', sheet_name='agent')

