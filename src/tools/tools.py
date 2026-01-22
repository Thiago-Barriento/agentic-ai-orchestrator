class Tool:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func

    def execute(self, input_data=None):
        return self.func(input_data)


def log_task(task):
    print(f"[TOOL] Executing task: {task}")
    return f"Task '{task}' executed successfully"


def list_tasks(_):
    print("[TOOL] Listing tasks (mock)")
    return ["Task A", "Task B", "Task C"]


def get_default_tools():
    return [
        Tool(
            name="log_task",
            description="Logs and executes a task",
            func=log_task
        ),
        Tool(
            name="list_tasks",
            description="Lists existing tasks",
            func=list_tasks
        )
    ]
