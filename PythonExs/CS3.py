
import math
from sys import argv

# This is a list of command line arguments that's passed to a python script 
# (in this case file 1 and file 2 are hamlet and pride_and_prejudice txt)
script, input_file_1, input_file_2 = argv

#
# -----
# This function takes 

def get_score(mystery_value_6, counts):
    denominator = float(1 + counts["_total"])
    if mystery_value_6 in counts:
        return math.log((1 + counts[mystery_value_6]) / denominator)
    else:
        return math.log(1 / denominator)

# 
# -----
# This function takes 
def normalize(mystery_value_6):
    return "".join(mystery_value_7 for mystery_value_7 in mystery_value_6 if mystery_value_7.isalpha()).lower()

# get_counts
# -----
# This function takes a filename and generates a 
def get_counts(filename):
    mystery_value_5 = {}
    total = 0
    file_to_read = open(filename)

    # Read 
    for line in file_to_read:
        # Get 
        for mystery_value_6 in line.strip().split():
            word = normalize(mystery_value_6)
            if mystery_value_6 == "":
                continue
            if mystery_value_6 in mystery_value_5:
                mystery_value_5[mystery_value_6] += 1
            else:
                mystery_value_5[mystery_value_6] = 1
            total += 1

    file_to_read.close()
    mystery_value_5["_total"] = total
    return mystery_value_5
    
# 
# -----
# This function takes 
def predict(mystery_input, txt_one, txt_two):
    pride_and_prejudice_txt, hamlet_txt = 0.0, 0.0
    for word in mystery_input.split():
        word = normalize(word)
        if word == "":
            continue

        pride_and_prejudice_txt += get_score(word, txt_one)
        hamlet_txt += get_score(word, txt_two)

    if pride_and_prejudice_txt > hamlet_txt:
        print("I think that was written by Jane Austen.")
    else:
        print("I think that was written by William Shakesphere.")

# Get the the text and return the total count of a given element in a list 
txt_one = get_counts(input_file_1)
txt_two = get_counts(input_file_2)

# Get the user input (text from pride_and_prejudice.txt or hamlet.txt) and then enables us to predict
# the labels of the data values 
user_input = input("Text sample: ")
predict(user_input, txt_one, txt_two)