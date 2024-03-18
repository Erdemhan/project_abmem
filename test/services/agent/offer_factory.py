import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django_model.db.models.agent import Agent
from django_model.db.models.market import Market
from django_model.db.models.models import Period,Resource,Offer
from django_model.db.models.enums import AgentState,AgentType
from decimal import Decimal

def create(agent: Agent, resource: Resource, amount: int, offerPrice: Decimal):
    period = agent.market.period_set.order_by('periodNumber').last()
    offer = Offer(period=period, agent=agent, resource=resource, amount=amount, offerPrice=offerPrice, acceptance=False, acceptancePrice = 0, acceptanceAmount=0)
    offer.save()
    return  offer

