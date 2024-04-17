from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import sys
import pandas as pd

sys.path.append("scripts")
from scripts.prompt_gen import generate_prompt
from qa_config import llama_system_qa_prompt, system_qa_prompt
from scripts.translate_summary_json import translate_summary

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = 'true'

# prompt_dict = generate_prompt(df, q_df, return_prompt_string=False)
# full_note_and_questions = prompt_dict['prompt']
# translated_summary = translate_summary(prompt_dict["summary"])

df = pd.read_csv("outputs/eval.csv")
output_parser = StrOutputParser()

def get_pred_dict():
    return {
        "idx": 0,
        "section_1" : "",
        "section_2" : "",
        "section_1_ground_truth_summary" : "",
        "section_2_ground_truth_summary" : "",
        "ground_truth_summary" : "",
        "full_note_and_questions": "",
        "llama2_response": "",
        "gpt3_response": "",
        "ground_truth_response": "",
    }

llama_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", llama_system_qa_prompt),
        ("user", "{full_note_and_questions} [/INST]"),
    ]
)

gpt3_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_qa_prompt),
        ("user", "{full_note_and_questions}"),
    ]
)

llm_llama = Ollama(model="llama2", temperature=0.01, top_p=0.2)
chain_llama = llama_prompt | llm_llama | output_parser

llm_openai = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.01)
chain_chatgpt = gpt3_prompt | llm_openai | output_parser

pred_list = []
for row in df.iloc[:5].to_dict("records"):
    full_note_and_question = row["prompt"]

    llama_response = chain_llama.invoke({"full_note_and_questions": full_note_and_question})
    gpt_response = chain_chatgpt.invoke({"full_note_and_questions": full_note_and_question})

    print(llama_response)
    print(gpt_response)

    pred_dict = get_pred_dict()
    pred_dict["idx"] = row["idx"]
    pred_dict["ground_truth_summary_sections"] = row["ground_truth_summary_sections"]
    pred_dict["section_1"] = row["section_1"]
    pred_dict["section_2"] = row["section_2"]
    pred_dict["section_1_ground_truth_summary"] = row["section_1_ground_truth_summary"]
    pred_dict["section_2_ground_truth_summary"] = row["section_2_ground_truth_summary"]
    pred_dict["ground_truth_summary"] = row["ground_truth_summary"]
    pred_dict["full_note_and_questions"] = full_note_and_question
    pred_dict["llama2_response"] = llama_response
    pred_dict["gpt3_response"] = gpt_response
    pred_list.append(pred_dict)


# print(llama_response)
# print(gpt_response)

pd.DataFrame(pred_list).to_csv("outputs/preds.csv", index=True)
