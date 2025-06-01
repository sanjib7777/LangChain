from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

st.header("Research Tool")
user_input = st.text_input("Enter your research question here:")
if st.button("Submit"):
    response = model.invoke(user_input)
    st.write("Response from the model:")
    st.write(response.content)