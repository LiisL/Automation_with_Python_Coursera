#Data types
#In Python, text in between quotes -- either single or double quotes -- is a string data type. 
#An integer is a whole number, without a fraction, while a float is a real number that can contain a fractional part. 
#For example, 1, 7, 342 are all integers, while 5.3, 3.14159 and 6.0 are all floats. When attempting to mix incompatible data types, you may encounter a TypeError. 
#You can always check the data type of something using the type() function.
print(type("I am a string"))
print(type(8))
print(type(2.5))

#Variables
#ariables are names that we give to certain values in our programs. Those values can be of any data type; numbers, strings or even the results of operations. 

#calculate the area of a rectangle
lenght = 10
height = 2
area = lenght*height

print(area)

#calculate the area of a triangle
base =5
height = 3
area = 5*3/2

print(area)

#Expressions, Numbers, and Type Conversions
#Implicit Conversions-the interpreter automatically converts one data type into another.
print(7+8.5)

#Adding strings
print("This"+" "+"is"+" "+"pretty"+" "+"neat!")

#Explicit Conversions
base =6
height = 3
area = 5*3/2
print("The area of a triangle is:" + " "+ str(area))

#"Practice writing some expressions and conversions yourself.

#In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. 
#Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the 
#files variable to the number of files. Finally, output a message saying "The average size is: " followed by the resulting number. 
#Remember to use the str() function to convert the number into a string. "
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is:" + str(average))

#Skill group 1 - Use the assignment operator =  to assign values to variables.Use basic arithmetic operators with variables to create expressions.Use explicit conversion to change a data type from float to string

#Study Guide: Expressions and Variables
# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests 
 
# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type

#Skill group 2 - Output multiple string variables on a single line to form a sentence.Use the plus (+) connector or a comma to connect strings in a print() function. Create spaces between variables in  a print() function


# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.

#Skill group 3 - Resolve TypeError caused by a data type mismatch issue. Use an explicit conversion function


print("5 * 3 = " + str(5*3)) 
 
# Resolution: 
# print("5 * 3 = " + str(5*3))
#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string.  


#Skill group 4 -Resolve a ZeroDivisionError caused by an attempt to divide by 0
numerator = 7
denominator = 1   # Possible resolution: Change the denominator value 
result = numerator / denominator
print(result)
 
# One possible assumption for a number divided by zero error might
# include the issue of a null value as a denominator (could happen when
# using a loop to iterate over values in a database). In such cases, the
# desired outcome may be to leave the numerator value intact. The
# numerator value can be preserved by reassigning the denominator with 
# the integer value of 1. The result would then equal the numerator.

