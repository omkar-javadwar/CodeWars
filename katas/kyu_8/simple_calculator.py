# https://www.codewars.com/kata/5810085c533d69f4980001cf/

'''
Instructions :

You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument will be numbers.
The third argument will represent a sign indicating the operation to perform on these two numbers.

Example:
calculator(1, 2, '+') => 3
if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.

Example:
calculator(1, 2, '$') # result will be "unknown value"
'''


def calculator(x,y,op):
    if isinstance(x, int) and isinstance(y, int):
        if op == '+':
            return x+y
        elif op == '-':
            return x-y
        elif op == '*':
            return x*y
        elif op == '/':
            return x/y
    return 'unknown value'
