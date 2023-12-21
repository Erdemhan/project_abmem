import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models import Period

def create(market, num: int, demand: int) -> Period:
    period = Period(market= market, periodNumber= num, demand= demand)
    period.save()
    return period