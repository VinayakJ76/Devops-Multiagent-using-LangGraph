class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def execute(self, state: dict) -> dict:
        raise NotImplementedError("Each agent must implement execute()")