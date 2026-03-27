from agents.base_agent import BaseAgent
from tools.kubernetes_tool import deploy_to_k8s
from tools.terraform_tool import run_terraform

class DeployBuddyAgent(BaseAgent):

    def __init__(self):
        super().__init__("Deploy-Buddy")

    def execute(self, state: dict) -> dict:

        query = state["query"]

        result = {
            "agent": self.name,
            "steps_executed": [],
            "logs": []
        }

        # Terraform step (if mentioned)
        if "terraform" in query.lower():
            tf_result = run_terraform("terraform apply -auto-approve")
            result["steps_executed"].append("terraform_apply")
            result["logs"].append(tf_result)

        # Kubernetes deploy
        k8s_result = deploy_to_k8s(query)

        result["steps_executed"].append("k8s_deploy")
        result["logs"].append(k8s_result)

        return result