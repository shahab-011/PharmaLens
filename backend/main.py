# from dotenv import load_dotenv

# load_dotenv()

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# from langchain_groq import ChatGroq
# from langchain_core.messages import (
#     AIMessage,
#     SystemMessage,
#     HumanMessage,
# )


# # =====================================================
# # FASTAPI
# # =====================================================

# app = FastAPI()


# # =====================================================
# # CORS
# # =====================================================

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# # =====================================================
# # GROQ MODEL
# # =====================================================

# model = ChatGroq(
#     model="openai/gpt-oss-20b",
#     temperature=0,
#     max_tokens=1024,
# )


# # =====================================================
# # TEACHER MODES
# # =====================================================

# MODES = {
#     "angry": "You are an angry teacher. Respond to the user in an angry tone.",
    
#     "depressed": "You are a depressed teacher. Respond to the user in a depressed tone.",
    
#     "happy": "You are a happy teacher. Respond to the user in a happy tone.",
    
#     "sad": "You are a sad teacher. Respond to the user in a sad tone.",
# }


# # =====================================================
# # CONVERSATION
# # =====================================================

# messages = []

# current_mode = None


# # =====================================================
# # REQUEST MODEL
# # =====================================================

# class ChatRequest(BaseModel):
#     message: str
#     mode: str


# # =====================================================
# # HOME
# # =====================================================

# @app.get("/")
# def home():
#     return {
#         "message": "Teacher AI API is running"
#     }


# # =====================================================
# # CHAT
# # =====================================================

# @app.post("/chat")
# def chat(request: ChatRequest):

#     global messages
#     global current_mode

#     # Validate mode
#     if request.mode not in MODES:
#         return {
#             "response": "Invalid teacher mode."
#         }


#     # If user changes teacher mode,
#     # start a new conversation.
#     if current_mode != request.mode:

#         current_mode = request.mode

#         messages = [
#             SystemMessage(
#                 content=MODES[request.mode]
#             )
#         ]


#     # Add user message

#     messages.append(
#         HumanMessage(
#             content=request.message
#         )
#     )


#     # Get AI response

#     response = model.invoke(messages)


#     # Store AI response

#     messages.append(
#         AIMessage(
#             content=response.content
#         )
#     )


#     return {
#         "response": response.content
#     }
