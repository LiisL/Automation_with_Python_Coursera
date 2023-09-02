
def factorial(n):
    print("Factorial called with" + str(n))
    if n < 2:
        print("returning 1")
        return 1
    result =  n* factorial(n-1)    
    print(f"Returning {result} for factorial of {n}")
    return result

factorial(5)