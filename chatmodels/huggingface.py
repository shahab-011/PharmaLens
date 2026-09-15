from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)

model = ChatHuggingFace(llm=llm)

res = model.invoke("Who are you? What is your purpose? Explain in one paragraph.")
print(res.content)