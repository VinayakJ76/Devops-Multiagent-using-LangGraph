from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from knowledge.embeddings import get_embeddings

def ingest_documents(docs, persist_dir="data/chroma_store"):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    db = Chroma(
        persist_directory=persist_dir,
        embedding_function=get_embeddings()
    )

    db.add_documents(chunks)
    db.persist()

    return f"{len(chunks)} chunks ingested"