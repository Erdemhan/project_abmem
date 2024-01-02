from agent import Agent
from offer import Offer
import ConnectionService
import numpy as np

conn,cur = ConnectionService.connectPostgres()


def runWithReturn(agent: Agent) -> (Agent,bool):
    agent.state = "returned"
    agent.num += 1
    offer = Offer(aid=agent.id,price=100)
    #matrixMul()
    return (agent,offer)



def runWithPostgres(agent: Agent) -> None:
    agent.state = "post"
    agent.num += 1
    offer = Offer(aid=agent.id,price=100)
    cur.execute('UPDATE agent SET state = %s, num = %s WHERE id = %s',[agent.state,agent.num,agent.id])
    cur.execute('INSERT into offer(aid,price) VALUES (%s, %s)',[agent.id,offer.price])
    conn.commit()
    #matrixMul()

def runWithSqlite(agent: Agent) -> None:
    matrixMul()
    pass



def matrixMul() -> None:
    for i in range(500):
            array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9], [7, 8, 9]], ndmin=5)
            array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1], [7, 8, 9], [7, 8, 9]], ndmin=5)
            np.multiply(array1, array2)