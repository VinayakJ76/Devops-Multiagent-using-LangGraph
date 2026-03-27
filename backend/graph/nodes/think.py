from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

def think_node(state):

    prompt = f"""
    You are a Senior DevOps Engineer.

    Context:
    {state.get('context','')}

    Analyze request:
    {state['query']}
    """

    reasoning = llm.predict(prompt)

    return {**state, "reasoning": reasoning}