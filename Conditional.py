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
