from sys import exit 

def gold_room(): 
    print("You wonder for a long time in the desert hungry and thirsty...")
    print("Do you find water or food first?")

    choice = input("> ")
    if "food" in choice:
         dead("Water is more essential for your body idiot.")
    elif "water" in choice:
        print("Good choice")
        exit(0)
    else: 
        dead("You didn't want food or water...")
    

def mysterious_figure(): 
    print("You go to the left path")
    print("You walk by a pond and see something faint in the distance")
    print("Do you want to go closer to the mysterious figure or run away? (1 or 2)")
    person_moved = True 

    while True:
        choice = input("> ")

        if choice == "2":
            dead("As you try to runaway you trip over a stone and fall into the pond and drown!")
        elif choice == "1" and person_moved:
            print("The mysterious figure turns out to be your mom, quick run away!")
            print("You run away from your mom and enter a different scenery called the desert")
            gold_room()
        else: 
             dead("As you stand outside pondering what choice to make, the weather temperature drops drastically and you die of hypothermia!")


def dead_body(): 
    print("You stumble upon a dead body.")
    print("There is letter in her hand.")
    print("Do you read the letter or not? (yes or no)")

    choice = input("> ")

    if "yes" in choice: 
        print(""" 
    The letter reads:
        If you have found this letter, then I am already dead. 
        I have the location attached to this letter where you can find money that I hid,
        However my only wish from you is to get rid of the evidence of my body. 
        """)
    elif "no" in choice: 
        mysterious_figure()
    else: 
        print("Try again")
        choice = input("> ") 

    print("""Now that you've read the letter, you have two choices: 
    1. Do as the letter is told and get the money 
    2. Call the police 
    (1 or 2)
    """)
    while True:
        choice = input("> ")

        if choice == "1": 
            print("It was a social experiment and you end up finding a cop standing at the location of the money")
            exit(0)
        elif choice == "2": 
            print("Good job! You passed the social experiment")
            exit(0)
        else: 
            print("Pick a choice (1 or 2)")
            

def dead(why): 
    print(why, "Good job!")
    exit(0) 

def start(): 
    print("You start an exploration through an unknown land.")
    print("What direction do you go in?")
    print("> Right or left")

    choice = input("> ")

    if choice == "left": 
        mysterious_figure()
    elif choice == "right": 
        dead_body()
    else: 
        dead("You're deciding for too long, and end up dying from dehydration")

start() 
