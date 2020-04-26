# https://www.codewars.com/kata/529872bdd0f550a06b00026e/

'''

Instructions : 

Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits in the given string of digits.

For example:

greatestProduct("123834539327238239583") // should return 3240
The input string always has more than five digits.

Adapted from Project Euler.

'''


def product(n):
    p = 1
    for i in n:
        p *= int(i)
    return p
    
def greatest_product(n):
    res = []
    mul = 1
    digit = 5
    while len(n)>= digit:
        res.append(product(n[:digit]))
        n = n[1:]
        print(res)
        print(n)
    return(max(res))
