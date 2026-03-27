from agents.code_screener import CodeScreenerAgent
from agents.deploy_buddy import DeployBuddyAgent
from agents.watchdog import WatchDogAgent

def act_node(state):

    agent_type = state["agent_type"]

    if agent_type == "code":
        agent = CodeScreenerAgent()

    elif agent_type == "deploy":
        agent = DeployBuddyAgent()

    elif agent_type == "watchdog":
        agent = WatchDogAgent()

    else:
        return {**state, "result": "Unknown agent"}

    result = agent.execute(state)

    return {**state, "result": result}