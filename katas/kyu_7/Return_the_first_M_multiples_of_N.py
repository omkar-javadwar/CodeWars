# https://www.codewars.com/kata/593c9175933500f33400003e/train/python

'''
Instructions:

Implement a function, multiples(m, n), which returns an array of the first m multiples of the real number n. Assume that m is a positive integer.

Ex.

multiples(3, 5.0)
should return

[5.0, 10.0, 15.0]
'''


def multiples(m, n):
    return [n*i for i in range(1,m+1)]
