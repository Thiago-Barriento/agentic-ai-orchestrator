from tools.base import Tool

class LoggerTool(Tool):
    name = "logger"

    def run(self, input_data: str) -> str:
        return f"[LOG]: {input_data}"
