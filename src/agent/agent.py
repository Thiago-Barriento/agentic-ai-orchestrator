class Agent:
    def __init__(self, planner, executor, memory):
        self.planner = planner
        self.executor = executor
        self.memory = memory

    def run(self, goal):
        self.memory.add(f"OBSERVE: Goal received -> {goal}")

        action = self.planner.create_plan(goal)
        self.memory.add(f"PLAN: {action}")

        result = self.executor.execute(action)
        self.memory.add(f"RESULT: {result}")

        return result
