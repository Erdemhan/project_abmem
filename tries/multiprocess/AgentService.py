from agent import Agent
import DbMethod


def createAgent():
    agent = Agent()
    DbMethod.postgresCur.execute('INSERT into agent (state) VALUES (%s) RETURNING id;',[agent.state])
    agent.id =  DbMethod.postgresCur.fetchone()[0]
    DbMethod.postgresConn.commit()
    return agent


def createAgentList(num:int) -> [Agent]:
    agents = []
    for i in range(num):
        agents.append(createAgent())
    return agents

