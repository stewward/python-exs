the_count = [1, 2, 3, 4, 5] #ordinal (gives order to #) and Cardinal 
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This first kind of for-loop goes through a list 

for number in the_count: 
    print(f"This is count {number}")

#smae as above 
for fruits in fruits: 
    print(f"A fruit of type: {fruits}")

#also we can go through mixed lists too 
for i in change: 
    print(f"I got {i}")

#We can also build lists, first start with an empty one 
elements = []

#then use the range function to do 0 to 5 counts 
for i in range(0, 6): 
    print(f"Adding {i} to the list.")
    #append is a function that lists understand 
    elements.append(i) 

#now we can print them out too 
for i in elements:
    print(f"Elements was: {i}")