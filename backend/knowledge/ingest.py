from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def ingest_documents(docs, persist_dir="data/chroma_store"):

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    db = Chroma.from_documents(
        chunks,
        OpenAIEmbeddings(),
        persist_directory=persist_dir
    )

    db.persist()
    return "ingested"