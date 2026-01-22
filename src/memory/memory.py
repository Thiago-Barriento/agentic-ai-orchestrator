class Memory:
    def __init__(self):
        self.events = []

    def add(self, event: str):
        self.events.append(event)

    def get_all(self):
        return self.events
