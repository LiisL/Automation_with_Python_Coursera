#Loops
# While loop
x = 0
while x < 5:
     print("Not there yet, x = " + str(x))
     x = x + 1
     
print( "x = " + str(x)) 

#More examples of a while loop

def attempts(n):
    x = 1
    while x <= n:
        print(" Attempt "+ str(x))
        x+=1
    print("Done")    
    
attempts(9)    

#For loops

for x in range(5):
    print(x)
    
friends = ['Elias', 'Thomas', 'Manny', 'Andreas', 'Christie']    

for friend in friends:
    print(friend)
  
  
    
def to_celsius(x):
    return (x-32)*5/9
    
for x in range(0,101,10):
    print(x, to_celsius(x))
