from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY"),
    http_options=types.HttpOptions(timeout=30000),
)

response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="Say hello in one sentence.",
)

print(response.text)