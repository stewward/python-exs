#"from" allows us to inport from different features/modules in python. 
from sys import argv #argv = arugment variable

#"script"another word for programming
script, first, second, third = argv #expecting 4 arugments 

print("The script is called: ", script)
print("Your first variable is called: ", first)
print("Your second variable is calle: ", second)
print("Your third variable is called: ", third)

#run in terminal and type: py (file name) and then the three variables 
#ex: py Ex13.py bloop bleep bop 