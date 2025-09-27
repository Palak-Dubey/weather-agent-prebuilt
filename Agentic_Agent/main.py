import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/models"
headers = {"Authorization": f"Bearer {API_KEY}"}

try:
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        print("✅ API Key is working!")
        print("Available models:", [m['id'] for m in response.json()["data"]])
    else:
        print("❌ Error:", response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print("⚠️ Connection error:", e)
