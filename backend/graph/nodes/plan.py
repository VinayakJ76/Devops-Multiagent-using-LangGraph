from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

def plan_node(state):

    plan = llm.predict(
        f"Break into actionable DevOps steps:\n{state['query']}"
    )

    return {**state, "plan": plan.split("\n")}