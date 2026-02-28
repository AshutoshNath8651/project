import requests

def ask_ai(question):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": question,
                "stream": False
            }
        )
        return response.json()["response"]
    except Exception as e:
        print("Ollama Error:", e)
        return "AI error occurred."