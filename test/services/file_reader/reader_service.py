import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
import pandas as pd
from django_model.db.models.enums import *
import yaml
from constants.paths import DATAPATH,SIMULATION_DATA_PATH
import logging

# TODO: yaml scheme validator / checkers (IO operations, consistency agent portfolio resources already saved?) / ErrorService / 
logger = logging.getLogger('FileLogger')


def openFile(path: str):
    try:
        with open(DATAPATH + path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError as error:
        print(path,"could not find in folder data")
        logger.error(error)
        sys.exit(1)

        
def readData(path: str, key: str) -> dict:
    try:
        data = openFile(path)
        return data[key]
    except KeyError as error:
        print("Key: '" , key , "' could not find in " , path)
        logger.error(error)
        sys.exit(1)
        