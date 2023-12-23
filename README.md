# Question-gen
Short python script that semi-automatically handles converting questions from csv format to a folder with prompt.md and question.json.

Types currently supported (to be put into the type column, see below. captialization does not matter):
- Multiple Choice
- True/False
- Fill in Multiple Blanks

Under construction, currently only handles plain text, no mathematic expressions etc.

<img width="733" alt="Picture depicting folder system" src="https://github.com/Qasmokejz/Question-gen/assets/71815990/241534e5-446a-4912-ac28-787bfebf1954">

# Usage

The python script is ran on command-line using two arguments:
`python3 question-gen.py -i path/to/input/file.csv -p path/to/output/directory`

The input CSV must have the column format as: `['Anything', 'Prompt', 'Solution', 'D0', ..., 'Dn', 'Type', 'Anything']`
- Anything can be any sort of column, it can be notes. It will not be considered during the generation.
- Columns are called by index, names do not matter.
- Solution and `D0-Dn` specifications:
    - MCQ: `D0-Dn` will be any other non-solution options for MCQ
    - T/F: Put True or False in solution and leave `D0-Dn` empty for TF
    - FIMBQ: List the correct answers in `'Solution'` in corresponding order to the blanks, separate them with a `;`
- Each question should be on a new row
    - Generation will terminate when hitting a completely empty row or end of file

The path to directory can be anything, with the last folder as the name of the folder to be created. For example: `folder1/folder2/folder3` will find the directory `folder1/folder2`, create a directory called `folder3` and place all the generated questions there. to If no input is given, it will create a directory called `qgen` in the currect directory and put all the converted questions in there.
