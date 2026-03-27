from knowledge.retriever import get_retriever

retriever = get_retriever()

def retrieve_node(state):
    docs = retriever.get_relevant_documents(state["query"])
    context = "\n".join([d.page_content for d in docs])
    return {**state, "context": context}