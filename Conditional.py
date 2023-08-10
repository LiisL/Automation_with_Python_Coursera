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

# Sets value of the "number" variable
number = 25

# The "number" variable will first be compared to 5. Since it is 
# False that "number" is not less than or equal to 5, the expression indented 
# under this line will be ignored. 
if number <= 5: 
   print("The number is 5 or smaller.")
 
# Next, the "number" variable will be compared to 33. Since it is 
# False that "number" is equal to 33, the expression indented under 
# this line will be ignored. 
elif number == 33:
   print("The number is 33.")
 
# Then, the "number" variable will be compared to 32 and 6. Since it 
# is True that 25 is less than 32 and greater than 6, the Python 
# interpreter will print "The number is less than 32 and/or greater
# than 6." Then, it will exit the if-elif-else statement and the remainder 
# of the if-elif-else statement will be ignored.
elif number < 32 and number >= 6:
   print("The number is less than 32 and greater than 6.")
 
else:
   print("The number is " + str(number))
 
# Expected output is: 
# The number is less than 32 and greater than 6.

# This function rounds a variable number up to the nearest 10x value
def round_up(number):
  x = 10
# The floor division operator will calculate the integer value of
# "number" divided by x: 35 // 10 will return the integer 3.
  whole_number = number // x
# The modulo operator will calculate the remainder value of "number"
# divided by x: 35 % 10 will return the remainder value 5.
  remainder = number % x
# If the remainder is greater than 0: 
  if remainder >= 5: 
# Return x multiplied by the (whole_number+1) to round up
    return x*(whole_number+1)
# Else, return x multiplied by the whole_number to round down
  return x*whole_number
 
# Calls the function with the parameter value of 35.
print(round_up(35)) # Should print 40
