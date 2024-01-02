
import timeit
import AgentService
import ReturnService
import DbMethod
import multiprocessing
import time

def main(period: int,N: int):

    agents = AgentService.createAgentList(N)
    dbs = timeit.default_timer()
    for i in range(period):  
        agents = DbMethod.run(agents)

    dbf = timeit.default_timer()
    dbt = dbf-dbs
    print("DB: ",dbt)

    agents = AgentService.createAgentList(N)
    rs = timeit.default_timer() 
    for i in range(period):
        results = ReturnService.returny(agents)
        agents = [result[0] for result in results]
        pool = multiprocessing.Pool()
        ress = pool.map_async(ReturnService.updateReturny, results)

    ress.wait()
    rf = timeit.default_timer()
    rt = rf-rs
    print("R: ",rt)
    print("DB - R : ", dbt - rt)




if __name__ == "__main__":
    period=500
    N=120
    print("Period: " , period , "  N: " , N)
    main(period,N)