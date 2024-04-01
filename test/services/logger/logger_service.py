import logging
import logging.handlers
import os
from datetime import datetime
from services.logger import error_service
import sys , traceback

def setupFileLogger():
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    fileName = datetime.now().strftime("%d-%m-%Y--%H-%M.log")

    logs_path = os.path.join(os.getcwd()+'/test', 'logs')
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)
    path = os.path.join(logs_path,fileName)

    def exc_handler(exctype, value, tb):
        if exctype  != error_service.ResourceNotFoundError:
            print("Unexpected Exception! Please see "+ path + " for more.")
            logger.exception(''.join(traceback.format_exception(exctype, value, tb)))
    sys.excepthook = exc_handler

    handler = logging.FileHandler(path)
    handler.setFormatter(formatter)

    logger = logging.getLogger('FileLogger')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger