numbers = []
# end_loop = 8

def while_loop_exercise(i, end_loop, scale): 
    # i = 0
    for i in range(i, end_loop, scale):
        print(f"At the top i is {i}")
        numbers.append(i) #appending = fancy word of saying adding

        #i = i + scale  

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

while_loop_exercise(6, 20, 3)

print("The numbers: ")

for num in numbers: 
    print(num)