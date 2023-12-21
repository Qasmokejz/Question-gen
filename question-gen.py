import pandas as pd
import os
import json

FILE_NAME = "Quiz 34 - Question Bank - LO4A-Ind.csv"
LO = 'LO4A-IND'

# Assuming csv file contains columns: ['Usage', 'Question Prompt', 'Correct Answer', 'D0', ..., 'Dn', 'Notes']

df = pd.read_csv(FILE_NAME)
df = df.drop(columns = ['Usage', 'Notes'])

# Need to manually drop empty rows here
df = df.drop(index = [1, 2, 3])

prompt = df['Question Prompt']
for i in range(len(df)):
    curr = df.iloc[i].dropna()
    print()
    print(f'===== Question {i+1}, len {len(curr)} =====')
    print(curr)

    # Sample data
    question = curr['Question Prompt']
    ca = curr['Correct Answer']
    answers = curr[2:]
    question_type = "multiple_choice_question"

    # Create the structured dictionary
    data = {
        "question_type": question_type,
        "answers": [
            {"correct": True,  "text": ca}
        ]
    }
    for ans in answers:
        data["answers"].append({"correct": False, "text": ans})
    
    # Create a folder
    folder_name = LO + f'-0{i+1}'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Write question to MD file
    md_file_path = os.path.join(folder_name, "prompt.md")
    with open(md_file_path, "w") as md_file:
        md_file.write(question)

    # Write answers to JSON file
    json_file_path = os.path.join(folder_name, "question.json")
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
