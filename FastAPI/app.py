from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn
import os

from dotenv import load_dotenv
import asyncio
import nest_asyncio

nest_asyncio.apply()

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

app = FastAPI(
    title="LangChainServer",
    version="1.0",
    description="API Server for LLMs"
)

# add_routes(
#     app,
#     ChatGoogleGenerativeAI(),
#     path="/route1"
# )

llm1 = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")

llm2 = Ollama(model="llama3")

prompt1 = ChatPromptTemplate.from_template("Give me a line of slogans about {topic} ")
prompt2 = ChatPromptTemplate.from_template("Give me 2 lines of poem about {topic} ")

add_routes(
    app,
    prompt1|llm1,
    path="/slogan"
)

add_routes(
    app,
    prompt2|llm2,
    path="/poem"
)

if __name__ =="__main__":
    uvicorn.run(app,host="localhost",port=8000)


# Swagger UI documentation at  http://localhost:8000/docs