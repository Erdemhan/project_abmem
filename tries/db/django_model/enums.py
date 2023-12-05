from django_enumfield import enum

class EnergyType(enum.Enum):
    RENEWABLE = 0
    FOSSIL = 1
    NUCLEAR = 2

class PeriodType(enum.Enum):
    HOUR = 0
    DAY = 1
    WEEK = 2
    MONTH = 3
    YEAR = 4

class SimulationState(enum.Enum):
    STARTED = 8
    INITIALIZING = 0
    BIDDING = 1
    MARKETCLEARING = 2
    PERIODRESULT= 3
    RESULT= 4
    FINISHED = 5
    STOPPED = 6
    CANCELED = 7

class SimulationMode(enum.Enum):
    STEPBYSTEP = 0
    PERIODBYPERIOD = 1
    ONLYRESULT = 2


class MarketStrategy(enum.Enum):
    DAYAHEAD = 0


class MarketState(enum.Enum):
    WAITINGOFFERS = 0
    GETTINGOFFERS = 1
    MARKETCLEARING = 2
    BROADCASTING = 3

class AgentState(enum.Enum):
    NOTSTARTED = 0
    WAITING = 1
    RUNNING= 2
