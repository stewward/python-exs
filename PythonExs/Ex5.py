name = 'Coco Tan' 
age = 17 #years           #no " " because it's a string/integer 
height = 65 #inches
eyes = 'Brown'
hair = 'Black'
in_to_cm = 2.54 #converting inch to cm

print(f'My name is {name}') #f = format 
print(f'I am {height} inches tall. ')
print(f'I am {age} years old. ')
print(f'I have {eyes} eyes and {hair} hair.')

#another/different way to insert variables, using {}, if you don't have tthe f' 
#you would use commas etc and () instead. 
total = age + height*in_to_cm #adding two integers
print(f'If I add my age {age} and {height*in_to_cm}, I get {total}.')
