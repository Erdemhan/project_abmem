import time

class Agent():
    def __init__(self,id=-1) -> None:
        self.id = id
        self.state = "created"
        self.num = 0