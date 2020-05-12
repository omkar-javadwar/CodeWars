# https://www.codewars.com/kata/58a6e75d934f82c94f0000ce/train/python

'''
Instructions :

Description:

In this Kata we are passing a number (n) into a function.

Your code will determine if the number passed is integer (or not).

The function needs to return either a true or false.

Numbers may be positive or negative, string or null.

Example
  isInt(3) = true ;
  isInt(3.1) = false ;
'''


def isInt(n):
    return isinstance(n, int)
