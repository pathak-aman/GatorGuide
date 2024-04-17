import numpy as np
import pandas as pd

import sys
sys.path.append('../scripts')

from scripts.translate_summary_json import translate_summary


def get_question_list(q_df):
    questions = {section: [] for section in q_df["Section Header"].unique()}
    for row in q_df.to_dict("records"):
        section = row["Section Header"]
        q_theme = row["Question Theme"]
        question = row["Question"]

        # question_with_theme = "{q_theme} : {question}".format(q_theme=q_theme, question=question)
        question_with_theme = "{question}".format(question=question)
        questions[section].append(question_with_theme)
    return questions


def random_questions_old(question_dict):
    random_questions_dict = {}
    selected_keys = np.random.choice(list(question_dict.keys()), size=2,
                                     replace=False)  # Select 2 unique keys (no replacement)
    for key in selected_keys:
        random_questions_dict[key] = list(np.random.choice(question_dict[key], size=len(question_dict[key]),
                                                      replace=False))  # Select 2 random elements from chosen keys
    return random_questions_dict


def random_questions(question_dict, translated_summaries):
      random_questions_dict = {}
      info_sections = [section for section, summary in translated_summaries.items() if not ": No information" in summary]

      if len(info_sections) < 2:
          print("No information section found!")
          return random_questions_dict

      selected_keys = np.random.choice(info_sections, size=2, replace=False)

      for key in selected_keys:
          random_questions_dict[key] = list(np.random.choice(question_dict[key], size=len(question_dict[key]), replace=False))

      return random_questions_dict




def random_full_note(df, size = 1):
    return df.sample(size).reset_index(drop=True)


def generate_prompt(df, q_df, return_prompt_string = True):

    sample_note_row = random_full_note(df)
    full_note = sample_note_row["full_note"]
    summary = sample_note_row["summary_eval"].iloc[0]
    translated_summary = translate_summary(summary)[1]

    # print(translated_summary)

    random_questions_dict = random_questions(get_question_list(q_df),translated_summary)

    prompt_string = f'[Start Full note:]\n{full_note[0]}\n[End Full note]\n\n[Start Random questions]\n'
    for section, questions in random_questions_dict.items():
        prompt_string += f"\n* {section}: Generate a short paragraph and STRICTLY OMIT any information that was not found in the note: \n"
        for question in questions:
            prompt_string += f"{question}\n"
    prompt_string += '[End Random questions]'

    if return_prompt_string:
        return prompt_string
    else:
        prompt_dict = {
            "idx": sample_note_row["idx"].iloc[0],
            "prompt": prompt_string,
            "full_note": full_note,
            "summary": sample_note_row["summary_eval"].iloc[0],
            "sections": list(random_questions_dict.keys()),
            "questions": list(random_questions_dict.values()),
            "translated_summary" : translated_summary,
        }
        return prompt_dict

if __name__ == '__main__':
    df = pd.read_csv("../outputs/cleaned_augmented_clinical_notes.csv")
    q_df = pd.read_csv("../outputs/questions.csv")
    x = generate_prompt(df, q_df, return_prompt_string=True)
    print(x)