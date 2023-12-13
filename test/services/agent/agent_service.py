from django_model.db.models.enums import AgentState


def readData() -> dict:
    # ReaderService.read()
    pass

def relearn(agent, results) -> None:
    agent.state = AgentState.LEARNING
    agent.save()
    # Learning Module
    pass

def predict(agent, results) -> int:
    agent.state = AgentState.PREDICTING
    agent.save()
    # Prediction Module
    ptf = 10
    return ptf

def calculateOffers(agent, ptf: int):
    agent.state = AgentState.CALCULATING
    agent.save()
    # Offer Module
    return [1,2,3]

def saveOffers(agent,offers) -> None:
    agent.state = AgentState.OFFERING
    agent.save()
    # Prediction Module
    # for offer in offers save()
    pass


def createPortfolio(agent, plantsData: dict):
    from . import portfolio_factory as PortfolioFactory
    return PortfolioFactory.create(agent,plantsData)
