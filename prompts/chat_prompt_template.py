from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant which is expert in {domain}.'),
        ('human', 'Explain in simple terms, what is {topic}.')
        
    ]
)

prompt = chat_template.format_prompt(topic="Quantum Computing", domain="Quantum Physics")
print(prompt)