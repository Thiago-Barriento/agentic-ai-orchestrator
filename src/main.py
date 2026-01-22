from agent.agent import Agent
from agent.planner import Planner
from agent.executor import Executor
from memory.memory import Memory
from core.loop import AgentLoop
from tools.logger import LoggerTool

def main():
    memory = Memory()
    agent = Agent("OrchestratorAgent", memory)
    planner = Planner()

    tools = {
        "logger": LoggerTool()
    }

    executor = Executor(tools)
    loop = AgentLoop(agent, planner, executor)

    result = loop.run("Organize tasks autonomously")

    print(result)
    print("\nMemory:")
    for event in memory.get_all():
        print("-", event)

if __name__ == "__main__":
    main()
