from langchain.embeddings import OpenAIEmbeddings
from config.settings import OPENAI_API_KEY

def get_embeddings():
    return OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)