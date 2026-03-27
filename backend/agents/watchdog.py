from agents.base_agent import BaseAgent
from tools.monitoring_tool import check_metrics

class WatchDogAgent(BaseAgent):

    def __init__(self):
        super().__init__("Watch-Dog")

    def execute(self, state: dict) -> dict:

        query = state["query"]

        result = {
            "agent": self.name,
            "analysis": "",
            "action_taken": []
        }

        metrics = check_metrics(query)

        result["analysis"] = metrics

        # Simple remediation logic (expand later)
        if "high cpu" in query.lower():
            result["action_taken"].append("scale_up")

        return result