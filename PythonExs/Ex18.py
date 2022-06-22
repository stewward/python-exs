def print_two(*args): # * means it can take any amount 
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
#lines 1-4 are pointless --> we can do" 
def print_two_again(arg1, arg2): #takes two parameters 
    print(f"arg1: {arg1}, arg2: {arg2}")
    
#Takes in one argument: 
def print_one(arg1): 
    print(f"arg1: {arg1}")
    
#Doesn't take any arguments: 
def print_none(): 
    print("I got nothin!")
    
print_two("Coco", "Tan") 
print_two_again("Coco", "Ten")
print_one("Yupyup!")
print_none()
