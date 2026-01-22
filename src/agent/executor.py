class Executor:
    def __init__(self, tools: dict):
        self.tools = tools

    def execute(self, plan: str):
        tool = self.tools.get("logger")
        if not tool:
            raise ValueError("Logger tool not available")
        return tool.run(plan)
