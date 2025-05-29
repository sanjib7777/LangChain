from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # Ensure your .env file contains HUGGINGFACEHUB_API_TOKEN    

llm = HuggingFaceEndpoint(
    model="deepseek-ai/DeepSeek-R1",  # You can change this to another supported model
    task="text-generation",
    temperature=1
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is MATLAB?")
print(response.content)