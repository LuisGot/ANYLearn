import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
provider_url = os.getenv("PROVIDER_URL")
llm_model = os.getenv("LLM_MODEL")

def make_llm_request(prompt: str) -> str:
    """
    Make a request to the LLM API with the given prompt.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": llm_model,
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(provider_url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
