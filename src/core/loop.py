class AgentLoop:
    def __init__(self, agent, planner, executor):
        self.agent = agent
        self.planner = planner
        self.executor = executor

    def run(self, goal: str):
        self.agent.observe(f"Goal received: {goal}")
        plan = self.planner.plan(goal)
        result = self.executor.execute(plan)
        self.agent.memory.add(result)
        return result
