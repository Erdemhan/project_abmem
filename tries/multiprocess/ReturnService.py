import paralel
from agent import Agent
import multiprocessing
import ConnectionService


postgresConn,postgresCur = ConnectionService.connectPostgres()
sqliteConn,sqliteCur = ConnectionService.connectSqlite()

def run(agents: [Agent]):
    return returny(agents)

def returny(agents: [Agent]):
    with multiprocessing.Pool() as pool:
        results = pool.map(paralel.runWithReturn, agents)
    pool.close()
    pool.join()
    #DbMethod.updateReturny(results)
    return results



# Return Method
def updateReturny(result):
    agent = result[0]
    offer = result[1]
    postgresCur.execute('UPDATE agent SET state = %s, num = %s WHERE id = %s',[agent.state,agent.num,agent.id])
    postgresCur.execute('INSERT into offer(aid,price) VALUES (%s, %s) RETURNING id;',[agent.id,offer.price])
    postgresConn.commit()