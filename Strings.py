#Strings
#What is a String

name = "Sasha"
name = 'Sasha'

place = "Cambridge"

print("Name is:"+ name +". " "Favourite place is :"+ place)

print(len(name))



#The parts of a String
name = "Jaylen"
#First index starts with 0
print(name[0])

#Last index is one less than the lenght of a String

print(name[5])
print(name[-1])

#Accessing a slice of a String
color = "Orange"
print(color[1:4])
print(color[:4])
print(color[4:0])

#Creating new Strings
#Strings in Python are immutable
message = "A kong String with a silly typo."
new_message = message[0:2] + "l" + message[3:]
print(new_message)

#We can assign a new value to a String
message = " A message"
print(message)
message = " Another message"
print(message)
