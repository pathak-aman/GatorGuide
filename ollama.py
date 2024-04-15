from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import os
from dotenv import load_dotenv

from config import *

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = 'true'

prompt = ChatPromptTemplate.from_messages(
    [
        # ("system", system_prompt),
        ("system", system_prompt_with_example),
        ("user", "[Start Note:] {full_note} [End Note]")

    ]
)

# print(prompt)

# streamlit
st.title("Information Extraction Demo with ChatGPT")
input_text = st.text_area("Enter your prompt")



llm = Ollama(model="meditron", temperature=0)



output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"full_note": input_text}))
