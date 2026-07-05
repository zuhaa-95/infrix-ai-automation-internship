import requests
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def query_model(prompt):
    try:
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 300
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()
        if 'choices' in result:
            return result['choices'][0]['message']['content']
        else:
            return str(result)
    except Exception as e:
        return f"Error: {str(e)}"