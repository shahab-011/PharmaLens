# #for avtivate ve -> .venv\Scripts\Activate.ps1


# from dotenv import load_dotenv
# from pathlib import Path
# import os

# # Find the .env file in the GenAI root folder
# env_path = Path(__file__).resolve().parent.parent / ".env"


# load_dotenv()
# from langchain.chat_models import init_chat_model

# model = init_chat_model("google_genai:gemini-3.7-flash")

# response = model.invoke("What is GenAI ?")

# print(response.content)

from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=50
    )

response = model.invoke(
    "What is GenAI? Explain it in simple words and in one paragraph."
)

print(response.content)