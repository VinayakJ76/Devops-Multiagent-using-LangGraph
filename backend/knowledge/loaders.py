from langchain.document_loaders import PyPDFLoader, WebBaseLoader

def load_pdf(path):
    return PyPDFLoader(path).load()

def load_url(url):
    return WebBaseLoader(url).load()