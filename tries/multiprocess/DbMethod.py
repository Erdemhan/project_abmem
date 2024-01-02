import paralel
import ConnectionService
from agent import Agent
import multiprocessing

postgresConn,postgresCur = ConnectionService.connectPostgres()
sqliteConn,sqliteCur = ConnectionService.connectSqlite()

#DB Method

def run(agents: [Agent]):
    res = dbMethodPostgres(agents=agents)
    return res


def dbMethodPostgres(agents: [Agent]) -> [Agent]:
    with multiprocessing.Pool() as pool:
        pool.map(paralel.runWithPostgres, agents)
    pool.close()
    pool.join()
    res = dbMethodUpdatePostgres(agents)
    return res


def dbMethodUpdatePostgres(agents: [Agent]) -> [Agent]:
    for agent in agents:
        postgresCur.execute('SELECT * from agent WHERE id= %s',[agent.id])
        agentData = postgresCur.fetchone()
        agent.id,agent.state,agent.num = agentData[0],agentData[1],agentData[2]
    return agents


def dbMethodSqlite(agents: [Agent]) -> [Agent]:
    with multiprocessing.Pool() as pool:
        pool.map(paralel.runWithPostgres, agents)
    pool.close()
    pool.join()

    return dbMethodUpdateSqlite(agents)


def dbMethodUpdateSqlite(agents: [Agent]) -> [Agent]:
    for agent in agents:
        sqliteCur.execute('SELECT * from agent WHERE id= %s',[agent.id])
        agentData = sqliteCur.fetchone()
        agent.id,agent.state = agentData[0],agentData[1]
    return agents
