types_of_people = 10 
x = f'There are {types_of_people} types of people.'#f' = f-string, providing formatting to a string
binary = 'binary'
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False #Binary either true or false
joke_evaluation = "Isn't that joke so funny?! {}" #false because nothing in the {}
print(joke_evaluation.format(hilarious)) # .format() syntax: how  we print out a string that already happened

w = "This is the left side of ..."
e = " a string with a ride side."
print(w+e)