from langchain.vectorstores import Chroma
from knowledge.embeddings import get_embeddings

def get_retriever(persist_dir="data/chroma_store"):

    db = Chroma(
        persist_directory=persist_dir,
        embedding_function=get_embeddings()
    )

    return db.as_retriever(search_kwargs={"k": 4})