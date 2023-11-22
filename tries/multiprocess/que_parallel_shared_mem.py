from copy import copy
import multiprocessing
import time
import timeit
import random
import numpy as np

#50 agent 2000 run için MATRIX Carpimi for1 ken 7.72 vs 0.6 // for10 ken 9.00 vs 4.78 // for50 ken 10.96 vs 23.49 // for100 ken 18.24 vs 51.17
#10 agent 24 run için eğer tek bir işlemin run süresi paralel için 3ms ise eşit çalışıyorlar 3ms üzeri paralel daha hızlı altı que hızlı, süre matris çarpımı ile oluşturuldu
#10 agent 24 run 40ms ile 2.28 paralel 5.64 que
#100 agent 240 run için 5ms ile paralel 18sn queue 63sn // 1.5ms ile paralel 9.41 que 29.61 sn
#100 agent 24 run için 5ms(paralel) ile paralel 16.43sn (2.5ms) queue 55.89sn
#10 agent 240 run için 5ms(paralel) ile paralel 18.81sn (2.5ms) queue 55.63sn
# 50k matrix çarpımı için 10 paralel 0.37sn queue 0.24sn 1run (10x24 18.7sn vs 57sn)
# 5k matrix çarpımı için  10 paralel 5ms queue 2.5ms 1 run 

class Teklif():
    def __init__(self, name, num) -> None:
        self.name = name
        self.num = num

    def __str__(self) -> str:
        return f"Teklif:  {self.name}   {self.num}"

    def __repr__(self) -> str:
        return f"Teklif:  {self.name}   {self.num}"

class Test():
    def __init__(self,id, name, agents) -> None:
        self.id = id
        self.name = name
        self.shared = agents

    def __str__(self) -> str:
        return f"Test:  {self.name} "

    def __repr__(self) -> str:
        return f"Test:  {self.name} "

    def run(self, num):
        start = timeit.default_timer()
        self.name += 10
        teklif = Teklif(name=self.name, num=num)
        for i in range(500):
            array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9], [7, 8, 9]], ndmin=5)
            array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1], [7, 8, 9], [7, 8, 9]], ndmin=5)
            result = np.multiply(array1, array2)
        stop = timeit.default_timer()

        # Teklif nesnesini güncelleyerek paylaşılan sözlüğe ekleyin
        self.shared[self.id] = self
        #print(f"Time for one parallel run: {stop-start}")
        return {'t': teklif}
    
class TestSingle():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Test:  {self.name} "

    def __repr__(self) -> str:
        return f"Test:  {self.name} "

    def run(self, num):
        start = timeit.default_timer()
        self.name += 10
        teklif = Teklif(name=self.name, num=num)
        for i in range(500):
            array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9], [7, 8, 9]], ndmin=5)
            array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1], [7, 8, 9], [7, 8, 9]], ndmin=5)
            result = np.multiply(array1, array2)
        stop = timeit.default_timer()

        #print(f"Time for one single run: {stop-start}")
        return {'t': teklif}





def worker_function(test_instance, num):
    return test_instance.run(num)

def main_parallel_shared():
    # İşlem havuzu oluşturma
    start = timeit.default_timer()

    with multiprocessing.Manager() as manager:
        shared_agents= manager.list()
        shared_agents.extend([Test(id=i,name=i, agents=shared_agents) for i in range(100)])

        with multiprocessing.Pool() as pool:
            for t in range(240):
                results = pool.starmap(worker_function,[(agent,i) for agent,i in zip(shared_agents,[i for i in range(0,100)])])
                pass


    stop = timeit.default_timer()

    print(f"Time for parallel: {stop-start}")



def main_sing():
    start = timeit.default_timer()
    agents=[]
    teklifler=[]
    nums=[]
    for i in range(100):
        agents.append(TestSingle(name=i))
        nums.append(i)

    for i in range(240):
        for a in range(100):
            result = agents[a].run(nums[a])

    stop = timeit.default_timer()
    print(f"Time for queue: {stop-start}")

if __name__ == "__main__":
    main_parallel_shared()
    main_sing()