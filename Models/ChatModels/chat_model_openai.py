from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
# Load environment variables
load_dotenv()  # Ensure your .env file contains HUGGINGFACEHUB_API_TOKEN
# Initialize the Hugging Face LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",  # You can change this to another supported model
    temperature=0.7
)
# Generate a response
response = llm.invoke("What is MATLAB?")
print(response.content)
