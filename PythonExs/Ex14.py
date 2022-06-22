from sys import argv #argv = arugment variable 

script, user_name = argv 
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)
print(f"What kind of computer are you using?")
computer = input(prompt)

print(f'''
Alright, so you said {likes} about liking me
You live in {lives}. 
And you're using a {computer} computer. Nice! 
 ''')
    
    
    