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
    CREATED = 0
    STARTED = 1
    INITIALIZING = 2
    BIDDING = 3
    MARKETCLEARING = 4
    PERIODRESULT= 5
    RESULT= 6
    FINISHED = 7
    STOPPED = 8
    CANCELED = 9

class SimulationMode(enum.Enum):
    STEPBYSTEP = 0
    PERIODBYPERIOD = 1
    ONLYRESULT = 2


class MarketStrategy(enum.Enum):
    DAYAHEAD = 0


class MarketState(enum.Enum):
    CREATED = 0
    WAITINGOFFERS = 1
    GETTINGOFFERS = 2
    MARKETCLEARING = 3
    BROADCASTING = 4

class AgentState(enum.Enum):
    CREATED = 0
    WAITING = 1
    RUNNING= 2
