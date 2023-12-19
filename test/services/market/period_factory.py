import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")

def create(market, num: int, demand: int):
    from django_model.db.models.models import Period
    period = Period(market=market,periodNumber=num,demand=demand)
    period.save()
    return period