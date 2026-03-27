from typing import TypedDict, List

class AgentState(TypedDict):
    query: str
    agent_type: str
    context: str
    reasoning: str
    plan: List[str]
    result: str