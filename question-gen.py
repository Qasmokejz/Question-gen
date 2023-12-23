import pandas as pd
import os
import json
import sys, getopt

# Assuming csv file is formatted as: ['Usage', 'Prompt', 'Solution', 'D0', ..., 'Dn', 'Type', 'Notes']
# The column names do not need to be exact, this is position based

def run(FILE_NAME, PATH):
    df = pd.read_csv(FILE_NAME)
    # drop usage, type, and notes columns
    df = df.drop(columns = [df.columns[0], df.columns[len(df.columns)-1]])

    # Create main folder
    if (PATH.rfind("/") > 0):
        LO = PATH[PATH.rfind("/")+1:]
    else:
        LO = PATH
    if not os.path.exists(PATH):
        os.makedirs(PATH)
            
    for i in range(len(df)):
        curr = df.iloc[i].dropna()

        try:
            # Sample data
            question = curr[0]
            answers = curr[1:-1]
            type = curr[-1].lower()
            type_function = None  # function pointer

            # Visuals
            print(f'\n===== Question {i+1}, len {len(curr)} =====')
            print(curr)

            # Manually checking question type
            if type[0:16] == "multiple choice":
                type_function = mcq
            elif type[0:10] == "true/false":
                type_function = tf
            else:
                print(f'question type {type} currently not supported')
                continue
        except IndexError:
            # Black bar should cause index error
            print("Transcription Complete")
            break

        # Create the structured dictionary
        data = type_function(answers)

        # Create sub folder
        sub_folder_name = LO + f'-0{i+1}'
        print(sub_folder_name)
        sub_folder_path = os.path.join(PATH, sub_folder_name)
        print(PATH, sub_folder_path)
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

# helper functions
def mcq(answers):
    data = {
        "type" : "multiple_choice_question",
        "answers" : [{"correct": True,  "text": answers[0]}]
    }
    for ans in answers[1:]:
        data["answers"].append({"correct": False, "text": ans})
    return data

def tf(answers):
    data = {
        "type" : "true_false_question"
    }
    if answers[0].lower() == "true":
        data["answers"] = True
    else:
        data["answers"] = False
    return data

if __name__ == "__main__":
    help = """
\nQUESTION GENERATOR supplimental to QUIZGEN
    -i: path to input CSV, ensure that CSV is formatted correctly
    -p: path to output directory (to be created)
    -h, --help: this page
\n"""
    FILE_NAME = None
    PATH = "qgen"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:p:", ["help"])
    except getopt.GetoptError as err:
        # print help information and exit
        print(err)  # will print something like "option -a not recognized"
        print(help)
        sys.exit(2)
    for o, a in opts:
        if o in ["-h", "--help"]:
            print(help)
            sys.exit(1)
        elif o in ["-i"]:
            FILE_NAME = a
        elif o in ["-p"]:
            PATH = a
        else:
            print(help)
            sys.exit(2)
    if FILE_NAME is None or PATH is None:
        print("Please specify a input csv file.")
        print(help)
        sys.exit(2) 
    run(FILE_NAME, PATH)
