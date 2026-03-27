from config.llm import get_llm

llm = get_llm()

def plan_node(state):

    prompt = f"""
    Break this DevOps task into clear actionable steps.
    Return as numbered list.

    Task:
    {state['query']}
    """

    response = llm.predict(prompt)

    steps = [s.strip() for s in response.split("\n") if s.strip()]

    return {**state, "plan": steps}