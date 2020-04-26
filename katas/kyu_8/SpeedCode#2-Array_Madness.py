# https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1/

'''

SpeedCode #2 - Array Madness
Objective
Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.

E.g.

array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
Get your timer out. Are you ready? Ready, get set, GO!!!
'''


def array_madness(a,b):
    a = map(lambda x: x ** 2, a)
    b = map(lambda x: x ** 3, b)
    return True if (sum(a) > sum(b)) else False
