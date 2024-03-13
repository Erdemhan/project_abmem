from django_model.db.models import *
from django_model.db.models import enums
from services.agent import agent_factory as AgentFactory
from services.starter import starter_service

def main():
    starter_service.start()

if __name__ == "__main__":
    main()