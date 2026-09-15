from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=1024
    )

print("choose mode of your ai chatbot")
print("press 1 for angry teacher")
print("press 2 for depressed teacher")
print("press 3 for happy teacher")
print("press 4 for sad teacher")

choice = int(input("Enter your choice: "))

if choice == 1:
    mode = "you are an angry teacher. respond to the user in an angry tone."
elif choice == 2:
    mode = "you are a depressed teacher. respond to the user in a depressed tone."
elif choice == 3:
    mode = "you are a happy teacher. respond to the user in a happy tone."
elif choice == 4:
    mode = "you are a sad teacher. respond to the user in a sad tone."

messages = [
    SystemMessage(content=mode)
]

print("------------WELCOME TO CHATBOT -> PRESS 0 TO EXIT------------")
while True:
    
    prompt = input("You  :  ")
    messages.append(HumanMessage(content=prompt))

    if prompt == "0":
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot : ",response.content)

print(messages)






# from dotenv import load_dotenv
# load_dotenv()

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# from langchain_groq import ChatGroq
# from langchain_core.messages import (
#     AIMessage,
#     SystemMessage,
#     HumanMessage
# )

# app = FastAPI()

# # Allow React frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# model = ChatGroq(
#     model="openai/gpt-oss-20b",
#     temperature=0,
#     max_tokens=1024
# )

# messages = [
#     SystemMessage(
#         content="You are a depressed and a very sad teacher."
#     )
# ]


# class ChatRequest(BaseModel):
#     message: str


# @app.get("/")
# def home():
#     return {"message": "Chatbot API is running"}


# @app.post("/chat")
# def chat(request: ChatRequest):

#     user_message = request.message

#     messages.append(
#         HumanMessage(content=user_message)
#     )

#     response = model.invoke(messages)

#     messages.append(
#         AIMessage(content=response.content)
#     )

#     return {
#         "response": response.content
#     }
