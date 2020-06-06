# https://www.codewars.com/kata/5ec970f05864da001853b55b/train/python

'''
Instructions:

You have to find factorial of a factorial.
Example:
n = 4, then,
fof(4) = 4! * 3! * 2! * 1! = 288
Write a funtion fof(n), which takes n as input and returns the factorial of factorial.
'''


import math 

def fof(n):
    return 1 if n<2 else fof(n-1)*math.factorial(n)
