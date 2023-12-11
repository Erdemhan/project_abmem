from django_model.db.models.models import Period
from django_model.db.models.market import Market

def create(market: Market, num: int, demand: int) -> Period:
    period = Period(market=market,periodNumber=num,demand=demand)
    period.save()
    return period