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
