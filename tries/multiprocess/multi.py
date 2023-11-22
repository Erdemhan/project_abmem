import time
import multiprocessing
from agent import Agent


def worker(agent, shared_dict):
    agent.agent_process(shared_dict)

def main():
    agents = []
    shared_data_dict = multiprocessing.Manager().dict()

    # Her Agent için ayrı SharedAgentData oluştur
    for i in range(5):
        agents.append(Agent(name=i,id=i))

    # Her bir Agent'ı ayrı bir süreçte çalıştır
    for i in range(3):
        processes = [multiprocessing.Process(target=worker, args=(agent, shared_data_dict)) for agent in agents]

        for p in processes:
            p.start()

        for p in processes:
            p.join()
            p.terminate()

    final_result = dict(shared_data_dict)
    print("Final Result:", final_result)

if __name__ == "__main__":
    main()
