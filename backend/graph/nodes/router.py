def router_node(state):
    q = state["query"].lower()

    if "deploy" in q or "kubernetes" in q:
        agent = "deploy"
    elif "monitor" in q or "cpu" in q:
        agent = "watchdog"
    else:
        agent = "code"

    return {**state, "agent_type": agent}