# https://www.codewars.com/kata/570ac43a1618ef634000087f/train/python

'''
Instructions:

Nova polynomial add
This kata is from a series on polynomial handling. ( #1 #2 #3 #4 )

Consider a polynomial in a list where each element in the list element corresponds to a factor. The factor order is the position in the list. The first element is the zero order factor (the constant).

p = [a0, a1, a2, a3] signifies the polynomial a0 + a1x + a2x^2 + a3*x^3

In this kata add two polynomials:

poly_add ( [1, 2], [1] ) = [2, 2]
'''


def poly_add(p1, p2):
    if p1 and p2:
        if len(p1)>len(p2):
            p2 = p2 + [0 for i in range(len(p1)-len(p2))]
            return list(map(int.__add__, p1, p2))
        else:
            p1 = p1 + [0 for i in range(len(p2)-len(p1))]
            return list(map(int.__add__, p1, p2))
    elif not p1:
        return p2
    elif not p2:
        return p1
