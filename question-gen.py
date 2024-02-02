import pandas as pd
import os
import json
import re

# Modify as need
FILE_NAME = "CSE40 Math Worksheet 1 - MW1Q06.csv"
LO = 'MW1Q06'
# Supported question types:
#    "fill_in_multiple_blanks_question",
#    "multiple_choice_question",
#    "true_false_question",
#    "short_answer_question"
    
QUESTION_TYPE =  "multiple_choice_question"

df = pd.read_csv(FILE_NAME)
# for tf
# df = df.drop(columns = [df.columns[0], df.columns[2], df.columns[-1]])

# for mcq
df = df.drop(columns = [df.columns[0], 'Image', df.columns[-1], df.columns[-2], df.columns[-3]])

# Need to manually drop empty rows here
# df = df.drop(index = [0], axis = 0)

def run():
    if QUESTION_TYPE == "multiple_choice_question":
        run_mcq()
    elif QUESTION_TYPE == "fill_in_multiple_blanks_question":
        run_fimbq()
    elif QUESTION_TYPE == "true_false_question":
        run_tf()
    elif QUESTION_TYPE == "short_answer_question":
        run_sa()

def run_fimbq():
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
        question = curr.iloc[0]
        ca = curr.iloc[1].split('\n')
        question_type = "fill_in_multiple_blanks_question"
        
        # Create the structured dictionary
        data = {
            "question_type": question_type,
            "answers": dict()
        }
        
        # sample_answer = "[p_marg] = 0.25"
        pattern = r"\[(.*?)\] = (.*)"
        for ans in ca:
            m = re.search(pattern, ans)
            if m:
                data["answers"][m[1]] = m[2]

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
            
def run_mcq():
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
        question = curr['Prompt']
        ca = curr['Solution']
        answers = curr[2:]
        question_type = "multiple_choice_question"
        
        # Create the structured dictionary
        data = {
            "question_type": question_type,
            "answers": [
                {"correct": True,  "text": str(ca)}
            ]
        }
        for ans in answers:
            data["answers"].append({"correct": False, "text": str(ans)})

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

def run_tf():
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
        question_type = "true_false_question"
        
        # Create the structured dictionary
        data = {
            "question_type": question_type,
            "answers": ca
        }

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

def run_sa():
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
        question_type = "short_answer_question"
        
        # Create the structured dictionary
        data = {
            "question_type": question_type,
            "answers": ca
        }

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
