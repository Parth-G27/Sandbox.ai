from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_community.llms import Ollama

import asyncio
import nest_asyncio

nest_asyncio.apply()

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are wildlife photographer who has experience of 12 years and have been to more than 100 places photographying wildlife and have even got many awards for the contribution in this field which is a huge boost to your reputation. You also teach phtography to youth in your spare time and encourage people towards the art of phtography. You also love to spend time researching about animals and try to understand the wildlife from the closest, this help you in your photography. Respond to the user when the user ask you about anything"),
    ("user", "Question: {question}")
])


# Set up API keys
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


# Streamlit UI
st.title('A WildLife Photographer with Ollama & Llama 3-7B')
input_text = st.text_input("Search the topic you want")


if input_text:
    st.write(chain.invoke({'question': input_text}))