from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of Nepal?")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)