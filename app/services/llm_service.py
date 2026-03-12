import requests
# OLLAMA_URL = "http://localhost:11434/api/generate" # for Local
OLLAMA_URL = "http://host.docker.internal:11434/api/generate" # for docker

MODEL_NAME = "llama3"   # you can change if you installed another model

def  generate_insights(prompt:str)-> str:
    payload={
        "model":MODEL_NAME,
        "prompt":prompt,
        "stream":False

    }

    response=requests.post(OLLAMA_URL,json=payload)
    if response.status_code!=200:
            raise Exception("Ollama request Failed")
    result = response.json()

    return result["response"]                       