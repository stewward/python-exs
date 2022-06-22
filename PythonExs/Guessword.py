import random
guess_limit = 10

word_list = ["whale", 'unicorn', 'tiger', 'lion']
#stores word
secret_word = random.choice(word_list)

#Repeatedly asks the user for a guess until they enter a valid response. Returns the guess. 
def get_user_guess(): 
    while True: 
        user_guess = input("What's your guess?")
        if len(user_guess) != 1: 
            print("Your guess must have one letter character")
        elif not user_guess.islower(): 
            print("Your guess must have a lower-case letter")
        else: 
            return user_guess #makes it assesible to other functions

#This function takes the word, the current state of dashes, and the user's last guess. 
#It returns a version of dashes with all instances of the guess exposed 
def make_dashes(word, dashes, guess):
    for i in range(len(word)): #length of word
        if word[i] == guess: 
            dashes = dashes[:i] + guess + dashes[i + 1:] 
    return dashes

#store dashes
dashes = "-" * len(secret_word)

#Repeatdely ask for guesses and then take the guess_limit into account 
while guess_limit > 0 and dashes != secret_word:
    print(dashes)
    print(str(guess_limit) + " guesses remaining")
    user_guess = get_user_guess() #makes it assesible to other functions
    dashes = make_dashes(secret_word, dashes, user_guess)
    if user_guess in secret_word:
        print("You got one letter of the secret word!")
    else: 
        print("Try again -- that letter isn't in the secret word :( ")
        guess_limit = guess_limit - 1 

#step 7 
if guess_limit == 0:
    print("Failed to guess secret word") 
else:
    print("Congrats! Secret word found")
    print(f"The secret word is {secret_word}!")