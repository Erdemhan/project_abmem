import time

class Agent():
    def __init__(self,id) -> None:
        self.id = id

    def agent_process(agent_id, shared_dict):
        print(f"Agent {agent_id} is processing")

        # Agent işlemleri burada gerçekleştirilir
        result = {
         "id":agent_id,
         "name": f"process: {agent_id}"
        }

        time.sleep(0.04)
        # Paylaşılan dict'e sonuç ekleme
        shared_dict[agent_id]=result