import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.agent import Agent
from django_model.db.models.market import Market
from django_model.db.models.models import Period,Resource,Offer
from django_model.db.models.enums import AgentState,AgentType
from decimal import Decimal

def create(agent: Agent, resource: Resource, amount: int, offerPrice: Decimal):
    period = agent.market.period_set.order_by('periodNumber').last()
    offer = Offer(period=period, agent=agent, amount=amount, offerPrice=offerPrice)
    offer.save()
    return  offer

'''
# OFFER
class Offer(Base):
    period = models.ForeignKey(Period, on_delete=models.CASCADE, null=False)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=False)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=False)
    amount = models.IntegerField()
    offerPrice = models.DecimalField(decimal_places=2, max_digits=7)
    acceptance = models.BooleanField()
    acceptancePrice = models.DecimalField(decimal_places=2, max_digits=7)
    acceptanceAmount = models.IntegerField()

'''