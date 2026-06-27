from langchain_openai import ChatOpenAI
#from dotenv import load_dotenv

import streamlit as st

#load_dotenv()

st.title("Ask Anything...")

with st.sidebar:
        st.title("Provide your API Key...")
        OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")

if not OPENAI_API_KEY:
      st.info("Enter OpenAI API Key to continue...")
      st.stop()

llm = ChatOpenAI(model = 'gpt-4.1-mini', api_key = OPENAI_API_KEY)

question = st.text_input("Enter a question: ")

if question:
    response = llm.invoke(question)
    st.write(response.content)