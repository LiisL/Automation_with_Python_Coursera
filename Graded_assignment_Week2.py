Week 2 Graded Assessment
#Q4

def exam_grade(score):
    if score > 95:
        grade = "Top score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Failed"
    return grade  
        
print(exam_grade(15))
print(exam_grade(60))
print(exam_grade(94))
print(exam_grade(100))

#Q6

def letter_translator(letter):
    if letter == "a":
        position = 1
    elif letter == "b":
        position = 2
    elif letter == "c":
        position = 3
    else:
        position = None
        print("Unknown letter")
    return position
    
    
print("The position of a letter is: ",letter_translator("r"))

#Q9

def safe_division(numerator, denominator):
    if denominator == 0:
        result = 0
    else:
        result = numerator/denominator
        
    return result
    
    
print(safe_division(10,2)) 
print(safe_division(10,0))
