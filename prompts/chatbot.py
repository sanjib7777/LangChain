from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
chat_history = [
    SystemMessage(content="You are a helpful chatbot that engages in conversation with users."),
    
]   


while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("Chatbot:", response.content)

print("Chat history:", chat_history)  
