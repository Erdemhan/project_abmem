import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
import pandas as pd
from django_model.db.models.enums import *
import yaml
from constants.paths import DATAPATH,SIMULATION_DATA_PATH

# TODO: yaml scheme validator / checkers (IO operations, consistency agent portfolio resources already saved?) / ErrorService / 


def openFile(path: str):
    try:
        with open(DATAPATH + path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(path,"could not find in folder data")
        sys.exit(1)

        
def readData(path: str, key: str) -> dict:
    try:
        data = openFile(path)
        return data[key]
    except KeyError:
        print("Key: '" , key , "' could not find in " , path)
        sys.exit(1)
        