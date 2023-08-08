#Comparing Things
print(10>1)
print("cat" == "dog")
print(1 != 2)
print ("Yellow"< "Brown"and "Blue" > "Green")
print(25 < 50 or 1 != 2)

#Calculate exponents with Python
import math

print(2**5)
print(pow(2,3))
print(math.pow(2,3))



#Exponentiate with list comprehension 
#List of values
values = [8, 5, 23, 12, 10, 0.4, -25]
# Raise each number to the power 3
exponents = [pow(value, 3) for value in values]

print(values)
print(exponents)
#comparison Operators with Strings
print("a string" == "a string")
print("4 + 5" == 4 + 5)
print("rabbit"!= "frog")
event_city = "Shanghai"
print(event_city != "Shanghai")
print("three" == 3

#Logical Operators

print((6*3 >= 18) and (9+9 <= 36/2))
print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")
# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))


# False or True returns True
country = None
city = None
print(country == "New York City" or city == "New York City")


# True or False returns True
print(16 <= 4**2 or 9**(0.5) != 3)


# False or False returns False
print("B_name" > "C_name" or "B_name" < "A_name")


#Branching with if Statements
def hint_username(username):
    if len(username) < 3:
        print("Ivalid username! Username must be atleast 3 characters long. ")
        
hint_username("Li")

#else Statements
def hint_username(username):
    if len(username) < 3:
        print("Ivalid username! Username must be atleast 3 characters long. ")
    else:
        print("valid username!")
        
hint_username("Lii")        
def is_positive(number):
  if number > 0:
    return True
  else:
    return False
    
print(is_positive(5) )   
    
    
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
        
print(is_even(10))        
    

#elif Statements
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Username must be atleast 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Username can be at most 15 characters long.")
    else:
        print("Valid username")
        
hint_username("Lyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
#Study Guide: Conditionals

def translate_error_code(error_code):
    if error_code == "401 Unauthorized":
        translation = "Server received an unauthenticated request"
    elif error_code == "404 Not Found":    
        translation = "Requested web page not found on server"
    elif error_code == "408 Request Timeout":
        translation = "Server request to close unused connection"
    else:
        translation = "Unknown error code"
    return translation
        
print(translate_error_code("404 Not Found"))


def your_stage_name(name):
    if name.startswith("A"):
        stage_name ="Anna"
    elif name.startswith("B"):
        stage_name = "Banana"
    else:
        stage_name = name
    return stage_name
    
print(your_stage_name("Angelina"))
print(your_stage_name("Brianne")) 
print(your_stage_name("Lovely"))       

