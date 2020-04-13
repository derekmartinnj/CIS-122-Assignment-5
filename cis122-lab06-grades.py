'''
Author: Derek Martin
Credit: CIS 122
Description: write a program that determines the lowest, highest, average, and total number of values (grades) given
'''

# Initialize variables
input_grades = True
count = 0
total = 0
lowest_score = 1000
highest_score = -1

# Input grades
while input_grades:
    # Add your input code, and code to check for input length,
    # with conditional expressions to change input_grades to False
    score = input("Enter score: ")
    if (len(score) > 0):
        # Something was entered, convert to integer
        score = int(score)
        # update variables
        if (score < lowest_score):
            lowest_score = score
        if (score > highest_score):
            highest_score = score
        count += 1
        total += score
        input_grades = True
    # Nothing entered, finish entering grades
    else:
        input_grades = False

# Output results
if (count > 0):   
    print("*** Results ***")
    print("Count:", count)
    # Calculate average score
    print("Average:", (total / count))
    print("Low score:", lowest_score)
    print("High score:", highest_score)
# Output "No scores entered" if on scores were entered
else:
    print("No scores entered")
