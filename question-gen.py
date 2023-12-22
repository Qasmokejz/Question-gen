import pandas as pd
import os
import json

# Modify as need
FILE_NAME = "Quiz 12 - Question Bank - LO1A.csv"
LO = 'LO1A'

# Assuming csv file is formatted as: ['Usage', 'Prompt', 'Solution', 'D0', ..., 'Dn', 'Type', 'Notes']
# The column names do not need to be exact, this is position based

df = pd.read_csv(FILE_NAME)
# get the type of question
type = (df[df.columns[len(df.columns)-2]][1]).lower()
# drop usage, type, and notes columns
df = df.drop(columns = [df.columns[0], df.columns[len(df.columns)-2], df.columns[len(df.columns)-1]])

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

        try:
            # Sample data
            question = curr[0]
            ca = curr[1]
            answers = curr[2:]
        except IndexError:
            # black bar should cause index error
            print("Transcription Complete")
            break

        # Create the structured dictionary
        data = {
            "question_type": type,
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
