from constants import *
import logging

import logging

logger = logging.getLogger('FileLogger')

class ResourceNotFoundError(Exception):
 
    # Constructor or Initializer
    def __init__(self,resourceName):
        self.__traceback__ = None
        self.value = resourceNotFoundString(resourceName)
        print(self.value)
        logger.error(self)
 
    # __str__ is to print() the value
    def __str__(self):
        return self.value
 
