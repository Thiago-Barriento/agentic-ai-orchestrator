class Agent:
    def __init__(self, name: str, memory):
        self.name = name
        self.memory = memory

    def observe(self, observation: str):
        self.memory.add(f"OBSERVE: {observation}")
