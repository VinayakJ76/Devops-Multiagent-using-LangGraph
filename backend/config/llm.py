from langchain.chat_models import ChatOpenAI
from config.settings import OPENAI_API_KEY, MODEL_NAME

def get_llm():
    return ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name=MODEL_NAME,
        temperature=0
    )