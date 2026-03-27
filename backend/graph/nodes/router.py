from config.llm import get_llm

llm = get_llm()

def router_node(state):

    query = state["query"]

    prompt = f"""
    Classify this DevOps request into one:
    - code
    - deploy
    - watchdog

    Request: {query}
    """

    agent = llm.predict(prompt).lower()

    if "deploy" in agent:
        agent_type = "deploy"
    elif "watchdog" in agent or "monitor" in agent:
        agent_type = "watchdog"
    else:
        agent_type = "code"

    return {**state, "agent_type": agent_type}