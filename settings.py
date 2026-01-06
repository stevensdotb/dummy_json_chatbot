from streamlit import secrets


OLLAMA_API_KEY = secrets["OLLAMA_API_KEY"]
OLLAMA_HOST = secrets.get("OLLAMA_HOST", "https://ollama.com")
OLLAMA_MODEL = secrets.get("OLLAMA_MODEL", "llama3.2")
API_URL = secrets.get("API_URL", "https://dummyjson.com/users")
