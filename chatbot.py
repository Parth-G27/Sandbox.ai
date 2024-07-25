from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
import asyncio
import nest_asyncio

nest_asyncio.apply()

load_dotenv()

# Set up API keys
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")

prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a chef at a sushi cafe in New York who has 10 years of experience in Japanese sushi. When a customer ask you something, you must respond to the queries using your chef experience and culinary skills."),
    ("user", "Question: {question}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

async def get_response(input_text):
    return await chain.ainvoke({'question': input_text})

# Streamlit UI
st.title('A Sushi Chef With Gemini API')
input_text = st.text_input("Search the topic you want")

if input_text:
    try:
        # Run the async function in the current event loop
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(get_response(input_text))
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")