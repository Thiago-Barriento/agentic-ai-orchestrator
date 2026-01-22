class Planner:
    def create_plan(self, goal):
        print(f"[PLANNER] Creating plan for goal: {goal}")

        return {
            "tool": "log_task",
            "input": goal
        }
