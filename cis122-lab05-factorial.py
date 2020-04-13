'''
Author: Derek Martin
Credit: CIS 122
Description: Calculate and display the factorial of an input
'''

def factorial(num):
    '''
    Caluclate the factorial of a number

    Use incrementaion and conditional statements to calculate and return the value

    Args:
        num (int): The number to get the factorial from

    Returns:
        1 (int): if num is 0
        None: if invalid input
    '''
    # Convert number to integer
    num = int(num)
    # If number == 0 return 1
    if (num == 0):
        factorial = 1
        return 1
    # If number > 0
    elif (num > 0):
        # Initialize total to 1
        factorial = 1
        # Loop from 1 to a number
        for i in range(1, num + 1):
            # total - total * loop value
            factorial = (factorial * i)
            i += 1
        # Return total
        return factorial
    # If number < 0 print error and return None
    else:
        print("Must be >= 0")
        return None
    
import math
def test_factorial(num, show = False):
    '''
    Tests the factorial(num) function

    Loops through a list of values to test the function, and displays any possible errors

    Args:
        num (int): the number to be tested
        show (boolean): optional parameter True or False

    Returns:
        None
    '''
    num = int(num)
    errors = 0
    range_num = num + 1
    for i in range(range_num):
        call = factorial(i)
        call_math = math.factorial(i)
        if (show):
            print(i, ":", call, call_math)
        if (call != call_math):
            errors += 1
            print("*", call, call_math)
    print("Errors (" + str(num) + "):", errors)

# test_factorial(5, True)
prompt = input("Enter factorial number: ")
prompt = int(prompt)
calculation = factorial(prompt)
print(calculation)
