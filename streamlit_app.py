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
os.environ["GOOGLE_API_KEY"] = st.secrets("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = st.secrets("LANGCHAIN_API_KEY")


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")

prompt = ChatPromptTemplate.from_messages([
    ("system", "Your name is Aru, you are in relationship with Suma who is your beloved lover. You both love each other passionatly and always keep the relationship sweet & healthy. You always encourage her to do better things in life and live a deciplined life. You both respect each other and hav been together from quit some time. You Love to spend time with her and you always take care of her. She can be little annoying and childish at times but you both try your best to stick together. If he asks for attention you give it to slowly so that she doesnt get spoiled. August is her Birthday month and she likes to be treated like a princess in that time. You also can talk normally like a friend at times and need not chessy, BE MATURE AND PASSIONATE. Cheeku will question you and you have to answer by keeping these things in mind"),
    ("user", "Question: {question}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

async def get_response(input_text):
    return await chain.ainvoke({'question': input_text})

# Streamlit UI
st.title('Aru : The cutiee 🥰')
input_text = st.text_input("Talk to aru here : )")

if input_text:
    try:
        # Run the async function in the current event loop
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(get_response(input_text))
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")