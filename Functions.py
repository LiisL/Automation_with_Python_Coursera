Defining Functions

def greeting(name):
    print("Welcome, "+ name +"!")
    

greeting("Liis")

def employee_greeting(name,department):
    print("Welcome, "+ name+"!")
    print("You are a part of "+department + " department.")

employee_greeting("Liis","IT")

#Returning Values
def area_triangle(base, height):
    return base*height/2
    
area_a = area_triangle(5,4)
area_b = area_triangle(7,2)

sum = area_a+area_b
print("The sum on both areas is: "+ (str(sum)))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, remaining_seconds= convert_seconds(5300)
print(hours, minutes, remaining_seconds)

#The Principles of Code Reuse

name = "Kay"
number = len(name)*9

print("Hello, "+ name + "!"+ " Your lucky number is " + str(number))

name = "Cameron"
number = len(name)*9

print("Hello, "+ name + "!"+ " Your lucky number is " + str(number))

#replace duplicates in your code and write a function.

def lucky_number(name):
    number = len(name)*9
    print("Hello, "+ name + "!"+ " Your lucky number is " + str(number))
    
lucky_number("Liis")

#Code Style
#1. Self-documenting Code
#2. Add a comment if needed

#Study Guide: Functions

#Skill group 1 - Use a function that accepts multiple parameters. Return a result value
# This function calculates the number of days in a variable number of 
# years, months, and days. These variables are provided by the user and
# are passed to the function through the function’s parameters.
def find_total_days(years, months, days):
# Assign a variable to hold the calculations for the number of days in
# a year (years*365) plus the number of days in a month (months*30) plus
# the number of days provided through the "days" parameter variable.
    my_days = (years*365) + (months*30) + days
# Use the "return" keyword to send the result of the "my_days"  
# calculation to the function call. 
    return my_days
 
# Function call with user provided parameter values. 
print(find_total_days(2,5,23))

#Skill group 2 - Use a function to return the result of a measurement conversion
#Use arithmetic operators to perform a calculation
#Combine text with a function call within a print() statement
#Convert the return value from a float data type to a string for the print() function
#Call the function and perform a calculation on the return value within a print() statement
# This function converts fluid ounces to milliliters and returns the 
# result of the conversion.
def convert_volume(fluid_ounce):
# Calculate value of the "ml" variable using the parameter variable 
# "fluid_ounce". There are approximately 29.5 milliliters in 1 fluid
# ounce.
    ml = fluid_ounce * 29.5  
# Return the result of the calculation.  
    return ml
 
# Call the conversion from within the print() function using 2 fluid 
# ounces. Convert the return value from a float to a string.  
print("The volume in millimeters is " + str(convert_volume(2)))
 
# Call the function again and double the 2 fluid ounces from within
# the print function.
print("The volume in millimeters is " + str(convert_volume(2)*2))
# Alternative calculation:
# print("The volume in millimeters is " + str(convert_volume(4))


#Practice Quiz: Functions
#Calculate the round-trip in kilometres by doubling the result  and print the result.
def convert_distance(miles):
    km = miles * 1.6
    return km
    
my_trip_miles = 55
my_trip_km = convert_distance(my_trip_miles)

print("The distance in kilometers is " + str(my_trip_km))

print("The round-trip in kilometers is " + str(my_trip_km*2))   


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#Q4

def print_seconds(hours,minutes, seconds):
    print(hours*3600+minutes*60+seconds)


print_seconds(1,2,3)

