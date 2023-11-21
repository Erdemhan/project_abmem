from enum import Enum

class ResourceType(Enum):
    FOSSIL = 0
    RENEWABLE = 1
    NUCLEAR = 2

class PortfolioType(Enum):
    FOSSIL = 0
    RENEWABLE = 1
    NUCLEAR = 2
    HYBRID = 3
