from langchain_openai import ChatOpenAI
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
        ("system", system_qa_prompt),
        ("user", "[Start:] {full_note_and_questions} [End]"),

    ]
)

# print(prompt)

# streamlit
st.title("QA Demo with ChatGPT")
input_text = st.text_area("Enter your prompt")



llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)



output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"full_note_and_questions": input_text}))
