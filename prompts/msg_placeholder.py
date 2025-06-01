from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful assistant.'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}')
])

chat_history = []

with open("chat_history.txt", "r") as file:
    chat_history.extend(file.readlines())



prompt = chat_template.invoke({
    "query": "where is my refund?",
    "chat_history": chat_history
})

print(prompt)