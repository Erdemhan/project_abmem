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
    def __init__(self,name,num) -> None:
        self.name=name
        self.num=num

    def __str__(self) -> str:
        return f"Teklif:  {self.name}   {self.num}"
    def __repr__(self) -> str:
        return f"Teklif:  {self.name}   {self.num}"

class Test():
    def __init__(self,name) -> None:
        self.name=name
    
    def __str__(self) -> str:
        return f"Test:  {self.name} "
    
    def __repr__(self) -> str:
        return f"Test:  {self.name} "
    
    def run(self,num):
        start = timeit.default_timer()
        self.name +=10
        teklif = Teklif(name=self.name,num=num)
        for i in range(500):
            array1=np.array([[1,2,3],[4,5,6],[7,8,9],[7,8,9],[7,8,9]],ndmin=5)  
            array2=np.array([[9,8,7],[6,5,4],[3,2,1],[7,8,9],[7,8,9]],ndmin=5)  
            result=np.multiply(array1,array2)  
        stop = timeit.default_timer()
        #print(f"Time for run : {stop-start}")
        
        return {'t':teklif,'ins':self}
    
    
def worker_function(test_instance, num):
    return test_instance.run(num)


def main():
    # İşlem havuzu oluşturma
    start = timeit.default_timer()
    with multiprocessing.Pool() as pool:
        agents=[]
        teklifler=[]
            # Birden çok işlem sürecinde worker_function fonksiyonunu çalıştırma
        for i in range(100):
            agents.append(Test(name=i))

        for i in range(240):
            results = pool.starmap(worker_function,[(agent,i) for agent,i in zip(agents,[i for i in range(0,100)])])
            for i in range(100):
               agents[i] = results[i]['ins']
        pool.terminate()
    stop = timeit.default_timer()
    print(f"Time for parallel: {stop-start}")



def main_async():
    # İşlem havuzu oluşturma
    start = timeit.default_timer()
    with multiprocessing.Pool() as pool:
        agents=[]
        teklifler=[]
            # Birden çok işlem sürecinde worker_function fonksiyonunu çalıştırma
        for i in range(5):
            agents.append(Test(name=i))

        for i in range(1):
            results_as = pool.starmap_async(worker_function,[(agent,i) for agent,i in zip(agents,[i for i in range(0,5)])])
            results = results_as.get()
            for i in range(5):
               agents[i] = results[i]['ins']
        pool.terminate()
    stop = timeit.default_timer()
    print(f"Time for parallel async: {stop-start}")



def main_sing():
    start = timeit.default_timer()
    agents=[]
    teklifler=[]
    nums=[]
    for i in range(100):
        agents.append(Test(name=i))
        nums.append(i)

    for i in range(240):
        for a in range(100):
            result = agents[a].run(nums[a])

    stop = timeit.default_timer()
    print(f"Time for queue: {stop-start}")

if __name__ == "__main__":
    main()
    #main_async()
    main_sing()