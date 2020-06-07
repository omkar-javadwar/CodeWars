# https://www.codewars.com/kata/5714041e8807940ff3001140/train/python

'''
Instructions:

* Nova polynomial subtract*

This kata is from a series on polynomial handling. ( #1 #2 #3 #4)

Consider a polynomial in a list where each element in the list element corresponds to the factors. The factor order is the position in the list. The first element is the zero order factor (the constant).

p = [a0, a1, a2, a3] signifies the polynomial a0 + a1x + a2x^2 + a3*x^3

In this kata subtract two polynomials:

poly_subtract([1, 2], [1] ) = [0, 2]
poly_subtract([2, 4], [4, 5] ) = [-2, -1]
The first and second katas of this series are preloaded in the code and can be used:

'''


def poly_subtract(p1, p2):
    if p1 and p2:
        if len(p1)>len(p2):
            p2 = p2 + [0 for i in range(len(p1)-len(p2))]
            return list(map(int.__sub__, p1, p2))
        else:
            p1 = p1 + [0 for i in range(len(p2)-len(p1))]
            return list(map(int.__sub__, p1, p2))
    elif not p1:
        return [-i for i in p2]
    elif not p2:
        return p1
