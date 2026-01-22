from src.agent import Agent
from src.planner import Planner
from src.executor import Executor
from src.memory import Memory
from src.tools import get_default_tools



def main():
    memory = Memory()
    planner = Planner()
    tools = get_default_tools()
    executor = Executor(tools)

    agent = Agent(planner, executor, memory)

    agent.run("Organize tasks autonomously")
    memory.show()


if __name__ == "__main__":
    main()
