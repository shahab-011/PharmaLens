from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

texts = [
    "GenAI is a cutting-edge technology that leverages artificial intelligence to generate content, answer questions, and assist in various tasks. It can understand and process natural language, making it a powerful tool for communication and information retrieval.",
    "GenAI is a revolutionary technology that uses advanced algorithms to create content, provide insights, and enhance user experiences. It can generate text, images, and other forms of media, making it a versatile solution for businesses and individuals alike.",
    "GenAI is an innovative platform that combines machine learning and natural language processing to deliver intelligent"
]

vector = embeddings.embed_documents(texts)

print(vector)