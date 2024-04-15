from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import os
from dotenv import load_dotenv

from qa_config import *

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = 'true'

prompt = ChatPromptTemplate.from_messages(
    [
        # ("system", system_prompt),
        ("system", llama_system_qa_prompt),
        ("user", "{full_note_and_questions} [/INST]"),

    ]
)

# print(prompt)

# streamlit
st.title("QA Demo with LLAMA2")
input_text = st.text_area("Enter your prompt")



llm = Ollama(model="llama2", temperature=0)



output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"full_note_and_questions": input_text}))
