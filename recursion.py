# Recursion 


def factorial(n):
    print("Factorial called with" + str(n))
    if n < 2:
        print("returning 1")
        return 1
    result =  n* factorial(n-1)    
    print(f"Returning {result} for factorial of {n}")
    return result

factorial(5)


def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


#A recursive function must include a recursive case and base case. 
#The recursive case calls the function again, with a different value. T
#he base case returns a value without calling the same function.

#A recursive function will usually have this structure:
#def recursive_function(parameters):
    #if base_case_condition(parameters):
        #return base_case_value
    #recursive_function(modified_parameters)
# Practice Quiz
#Fill in the blanks to make the is_power_of function return wheter the number is a power of the given base.
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  elif(number/base)==1:
    return True  

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


# Practice Quiz
def count_users(group):
    count = 0
    for member in get_members(group):
    #count += 1
        if is_group(member):
            count += count_users(member)
        else:
            count+=1
    return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


# Practice Quiz
def sum_positive_numbers(n):
  if n<1:
    return n
  return n + sum_positive_numbers(n-1)
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
