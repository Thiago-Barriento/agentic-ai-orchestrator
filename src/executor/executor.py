class Executor:
    def __init__(self, tools):
        self.tools = {tool.name: tool for tool in tools}

    def execute(self, action):
        tool_name = action.get("tool")
        tool_input = action.get("input")

        if tool_name not in self.tools:
            print(f"[EXECUTOR] Tool '{tool_name}' not found.")
            return None

        print(f"[EXECUTOR] Using tool: {tool_name}")
        return self.tools[tool_name].execute(tool_input)
