from langgraph.graph import StateGraph
from graph.state import AgentState

from graph.nodes.router import router_node
from graph.nodes.retrieve import retrieve_node
from graph.nodes.think import think_node
from graph.nodes.plan import plan_node
from graph.nodes.act import act_node
from graph.nodes.memory import memory_node

def build_graph():

    g = StateGraph(AgentState)

    g.add_node("router", router_node)
    g.add_node("retrieve", retrieve_node)
    g.add_node("think", think_node)
    g.add_node("plan", plan_node)
    g.add_node("act", act_node)
    g.add_node("memory", memory_node)

    g.set_entry_point("router")

    g.add_edge("router", "retrieve")
    g.add_edge("retrieve", "think")
    g.add_edge("think", "plan")
    g.add_edge("plan", "act")
    g.add_edge("act", "memory")

    g.set_finish_point("memory")

    return g.compile()