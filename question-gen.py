import pandas as pd
import os
import json

FILE_NAME = "Quiz 34 - Question Bank - LO4F - specific.csv"
LO = 'LO4F-SPECIFIC'

# Assuming csv file contains columns: ['Usage', 'Question Prompt', 'Correct Answer', 'D0', ..., 'Dn', 'Notes']

df = pd.read_csv(FILE_NAME)
df = df.drop(columns = ['Usage', 'Notes'])

# Need to manually drop empty rows here
df = df.drop(index = [0], axis = 0)

def run():
    # Create main folder
    main_folder_name = LO
    if not os.path.exists(main_folder_name):
        os.makedirs(main_folder_name)
            
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

        # Create sub folder
        sub_folder_name = LO + f'-0{i+1}'
        sub_folder_path = os.path.join(main_folder_name, sub_folder_name)
        if not os.path.exists(sub_folder_path):
            os.makedirs(sub_folder_path)

        # Write question to MD file
        md_file_path = os.path.join(sub_folder_path, "prompt.md")
        with open(md_file_path, "w") as md_file:
            md_file.write(question)

        # Write answers to JSON file
        json_file_path = os.path.join(sub_folder_path, "question.json")
        with open(json_file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

run()
