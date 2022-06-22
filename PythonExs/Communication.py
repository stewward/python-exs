import math
from sys import argv

# This is a list of command line arguments that's passed to a python script 
# (in this case file 1 and file 2 are hamlet and pride_and_prejudice txt)
script, input_file_1, input_file_2 = argv

#
# -----
# This function takes 

def get_score(words, counts):
    denominator = float(1 + counts["_total"])
    if words in counts:
        return math.log((1 + counts[words]) / denominator)
    else:
        return math.log(1 / denominator)

# 
# -----
# This function takes 
def normalize(words):
    return "".join(letter for letter in words if letter.isalpha()).lower()

# get_counts
# -----
# This function takes a filename and generates a 
def get_counts(filename):
    word_index = {}
    total = 0
    file_to_read = open(filename)

    # Read the inputted text file line by line 
    for line in file_to_read:
        # Get 
        for word in line.strip().split():
            word = normalize(word)
            if word == "":
                continue
            if word in word_index:
                word_index[word] += 1
            else:
                word_index[word] = 1
            total += 1

    file_to_read.close()
    word_index["_total"] = total
    return word_index
    
# 
# -----
# This function takes 
def predict(user_text_sample, author_1_count, author_2_count):
    author_1_score, author_2_score = 0.0, 0.0
    for word in user_text_sample.split():
        word = normalize(word)
        if word == "":
            continue

        author_1_score += get_score(word, author_1_count)
        author_2_score += get_score(word, author_2_count)

    if author_1_score > author_2_score:
        print("I think that was written by William Shakesphere.")
    else:
        print("I think that was written by Jane Austen.")

# Get 
author_1_count = get_counts(input_file_1)
author_2_count = get_counts(input_file_2)

# Get 
user_text_sample = input("Text sample: ")
predict(user_text_sample, author_1_count, author_2_count)