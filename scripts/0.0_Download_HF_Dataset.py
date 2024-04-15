from datasets import load_dataset
import pandas as pd
from ftfy import fix_text

dataset = "AGBonnet/augmented-clinical-notes"
datasets = load_dataset(dataset)


datasets.set_format("pandas")
df = datasets["train"][:]

full_note_fixed = fix_text(df["full_note"])
summary_fixed = fix_text(df["summary"])


# df.to_csv("../datasets/augmented_clinical_notes/augmented_clinical_notes.csv", index=False)


print(df.loc[0])