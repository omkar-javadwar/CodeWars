# https://www.codewars.com/kata/5e824b35a05deb0028d0d52c/

'''
Instructions :

TASK:

Given the sidelengths of a triangle, return whether the triangle is equilateral, scalene, or isosceles(excluding equilateral) in a string --> all lowercase.

EXAMPLES:

type_triangle(2, 4, 5) returns "scalene"
type_triangle(3, 3, 3) returns "equilateral"
type_triangle(7, 7, 1) returns "isosceles"
type_triangle(1, 1, 9) returns None
NOTE: If the sides of the triangle is invalid, return None

'''


def type_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return None
    else:
        if a == b == c:
            return 'equilateral'
        elif a == b or a == c or b == c:
            return 'isosceles'
        else:
            return 'scalene'


# OR


def type_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return None
    else:
        if all([a==b, a==c]):
            return 'equilateral'
        elif any([
            all([a==c, a!=b]),
            all([a==b, a!=c]),
            all([c==b, c!=a]),
        ]):
            return 'isosceles'
        elif all([a!=c, c!=b, a!=b]):
            return 'scalene'
