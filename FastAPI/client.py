# Web app that will interact with the API

import requests
import streamlit as st 

def get_gemini_response(inp_text):
    response = requests.post("http://localhost:8000/slogan/invoke",
                             json={'input':{'topic':inp_text}})
    
    return response.json()['output']['content']

def get_ollama_response(inp_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input':{'topic':inp_text}})
    
    return response.json()['output']

st.title("LLMs as API with Langchain & FastAPI")
inptext1 = st.text_input("Write a slogan on")
inptext2 = st.text_input("Write a poem on")

if inptext1:
    st.subheader("Gemini 1.5 Pro Response on Slogan")
    st.write(get_gemini_response(inptext1))

if inptext2:
    st.subheader("Llama 3-7B Response on Poem")
    st.write(get_ollama_response(inptext2))

