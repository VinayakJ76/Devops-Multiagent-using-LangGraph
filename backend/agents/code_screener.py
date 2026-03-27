from agents.base_agent import BaseAgent
from tools.security_tool import run_security_scan

class CodeScreenerAgent(BaseAgent):

    def __init__(self):
        super().__init__("Code-Screener")

    def execute(self, state: dict) -> dict:

        query = state["query"]
        plan = state.get("plan", [])

        result = {
            "agent": self.name,
            "steps_executed": [],
            "findings": []
        }

        # Step 1: Security scan
        scan_result = run_security_scan(query)

        result["steps_executed"].append("security_scan")
        result["findings"].append(scan_result)

        return result