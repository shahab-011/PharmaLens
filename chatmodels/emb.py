from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

texts = [
    "GenAI is a technology that generates content.",
    "Machine learning allows computers to learn from data.",
    "RAG combines retrieval with generation."
]

response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts
)

vectors = [embedding.values for embedding in response.embeddings]

print("Number of vectors:", len(vectors))
print("Vector dimension:", len(vectors[0]))
print("First vector:", vectors[0])