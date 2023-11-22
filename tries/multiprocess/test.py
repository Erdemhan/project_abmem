from copy import copy
import multiprocessing
import time
import timeit
import random
import numpy as np

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
        self.name +=10
        teklif = Teklif(name=self.name,num=num)
        for i in range(50):
            array1=np.array([[1,2,3],[4,5,6],[7,8,9],[7,8,9],[7,8,9]],ndmin=5)  
            array2=np.array([[9,8,7],[6,5,4],[3,2,1],[7,8,9],[7,8,9]],ndmin=5)  
            result=np.multiply(array1,array2)  
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
        for i in range(50):
            agents.append(Test(name=i))

        for i in range(2000):
            results = pool.starmap(worker_function,[(agent,i) for agent,i in zip(agents,[i for i in range(0,50)])])
            for i in range(50):
               agents[i] = results[i]['ins']
        pool.terminate()
    stop = timeit.default_timer()
    print(f"Time for parallel: {stop-start}")

def main_sing():
    start = timeit.default_timer()
    agents=[]
    teklifler=[]
    nums=[]
    for i in range(50):
        agents.append(Test(name=i))
        nums.append(i)

    for i in range(2000):
        for a in range(50):
            result = agents[a].run(nums[a])

    stop = timeit.default_timer()
    print(f"Time for queue: {stop-start}")

if __name__ == "__main__":
    main()
    main_sing()