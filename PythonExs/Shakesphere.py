#The purpose of this code is to identify authors from a sample text
import math
from sys import argv


# The files are listed as a argument (in this case file 1 and file 2 are hamlet and pride_and_prejudice txt)
# The user must assign the files in a specific order in the terminal so it can later spit out the proper author assigned
script, input_file_1, input_file_2 = argv

#
# -----
# This function takes "word" and dictionary in word counts
# Forms a score that comes close to a word that's somehow connected to the document where the word counts generated
# The higher the word score determines how connected/relevant a word is to the text, 
# Counts the number of words in the file and then return 

def get_score(word, counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)

# 
# -----
# This function takes word and determines/checks if the letters are in the alphabet 
# then converts the letters to all lowercases while also removing all non-letters
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# get_counts
# -----
# This function takes a filename creates and empty dictionary 
# initialize total to equal zero 
def get_counts(filename):
    word_index = {}
    total = 0
    file_to_read = open(filename)

    # Read the inputted text file line by line 
    for line in file_to_read:
        # Gets each word
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
    
# This function is a prediction algorithm
# -----
# It takes a variable user_text_input, author_1_counts, author_2_counts, which would assign a score (that's initialized to 0.0) to the author 
# then takes the total of author 1 and author 2 score and compares the score to each other which would determine what to print 
def predict(user_text_input, author_1_counts, author_2_counts):
    author_1_score, author_2_score = 0.0, 0.0
    for word in user_text_input.split():
        word = normalize(word)
        if word == "":
            continue

        author_1_score += get_score(word, author_1_counts)
        author_2_score += get_score(word, author_2_counts)

    if author_1_score > author_2_score:
        print("I think that was written by William Shakesphere.")
    else:
        print("I think that was written by Jane Austen.")

# Gets the counts of the common words in each text file 
# Then assigns them to the author_1_counts, author_2_counts variable
author_1_counts = get_counts(input_file_1)
author_2_counts = get_counts(input_file_2)

# Get the user input (text from pride_and_prejudice.txt or hamlet.txt) and then allows python to predict (using the predict function)
# the author assigned to the given sample
user_text_input = input("Text sample: ")
predict(user_text_input, author_1_counts, author_2_counts)


#Extra notes:
#Takes both text 1 and 2 files, counts the words as a dictionary so when put into sample text it cross references how many reference words there are
#(Comparing each word) How many similar words in the file.txt are in the dictionary. To determine/identify which text sample is who's author
