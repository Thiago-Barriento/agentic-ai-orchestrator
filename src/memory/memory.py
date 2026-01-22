class Memory:
    def __init__(self):
        self.logs = []

    def add(self, entry):
        self.logs.append(entry)

    def show(self):
        print("\n[MEMORY]")
        for log in self.logs:
            print("-", log)
