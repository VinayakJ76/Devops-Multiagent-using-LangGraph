import os
import json

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = "gpt-4o-mini"



CONFIG_PATH = "frontend/config/tools.config.json"

def load_tool_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)