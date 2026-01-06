from ollama import Client

from settings import OLLAMA_API_KEY, OLLAMA_HOST, OLLAMA_MODEL


client = Client(
    host=OLLAMA_HOST,
    headers={'Authorization': f'Bearer {OLLAMA_API_KEY}'}
)

def open_stream(messages: list[dict[str, str]], tools=[]):
    return client.chat(
        model=OLLAMA_MODEL,
        messages=messages,
        tools=tools,
        stream=True
    )
