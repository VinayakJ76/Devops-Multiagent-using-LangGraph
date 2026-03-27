from config.llm import get_llm

llm = get_llm()

def think_node(state):

    prompt = f"""
    You are a Senior DevOps Engineer AI.

    Context:
    {state.get('context','')}

    User Request:
    {state['query']}

    Analyze deeply:
    - What is the problem?
    - What system is involved?
    - What risks exist?
    """

    reasoning = llm.predict(prompt)

    return {**state, "reasoning": reasoning}