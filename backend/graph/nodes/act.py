from tools.security_tool import run_security_scan
from tools.kubernetes_tool import deploy_to_k8s
from tools.monitoring_tool import check_metrics
from tools.terraform_tool import run_terraform

def act_node(state):

    agent = state["agent_type"]
    query = state["query"]

    if agent == "code":
        result = run_security_scan(query)

    elif agent == "deploy":
        result = deploy_to_k8s(query)

    elif agent == "watchdog":
        result = check_metrics(query)

    else:
        result = "Unknown"

    return {**state, "result": result}