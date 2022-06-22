def add(a, b): 
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b): 
    print(f"SUBTRACTING {a} - {b}")
    return a - b 

def multiply(a, b): 
    print(f"MULTIPLYING {a} * {b}")
    return a*b 
    
def divide(a,b): 
    print(f"DIVIDING {a} / {b}")
    return a/b 


print("Let's do some math with just functions!")
age = add(5, 11)
height = subtract(78, 4)
weight = multiply(70, 2)
iq = divide(49, 50)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
      
