# https://www.codewars.com/kata/53907ac3cd51b69f790006c5/

'''

Instructions :

In this kata, you should calculate type of triangle with three given sides a, b and c (given in any order).

If all angles are less than 90°, this triangle is acute and function should return 1.

If one angle is strictly 90°, this triangle is right and function should return 2.

If one angle more than 90°, this triangle is obtuse and function should return 3.

If three sides cannot form triangle, or one angle is 180° (which turns triangle into segment) - function should return 0.

Input parameters are sides of given triangle. All input values are non-negative floating point or integer numbers (or both).
  1. Acute
  2. Right
  3. Obtuse

Examples:
  triangle_type(2, 4, 6) # return 0 (Not triangle)
  triangle_type(8, 5, 7) # return 1 (Acute, angles are approx. 82°, 38° and 60°)
  triangle_type(3, 4, 5) # return 2 (Right, angles are approx. 37°, 53° and exactly 90°)
  triangle_type(7, 12, 8) # return 3 (Obtuse, angles are approx. 34°, 106° and 40°)

If you stuck, this can help you: http://en.wikipedia.org/wiki/Law_of_cosines. But you can solve this kata even without angle calculation.

There is very small chance of random test to fail due to round-off error, in such case resubmit your solution.
'''


# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle


def triangle_type(a, b, c):
    c,b,a = sorted((a,b,c))
    if a >= b+c:
        return 0
    elif a*a < b*b + c*c: 
        return 1
    elif a*a == b*b + c*c:
        return 2
    elif a*a > b*b + c*c :  
        return 3


# OR


def triangle_type(a, b, c):
    print(a, b, c)
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 0
    elif any([
    all([a>c, a>b, (a**2) < ((c**2) + (b**2))]),
    all([b>c, b>a, (b**2) < ((c**2) + (a**2))]),
    all([c>a, c>b, (c**2) < ((a**2) + (b**2))])
    ]):
        return 1
    elif any([
    all([a>c, a>b, (a**2) == ((c**2) + (b**2))]),
    all([b>c, b>a, (b**2) == ((c**2) + (a**2))]),
    all([c>a, c>b, (c**2) == ((a**2) + (b**2))])
    ]):
        return 2
    elif any([
    all([a>c, a>b, (a**2) > ((c**2) + (b**2))]),
    all([b>c, b>a, (b**2) > ((c**2) + (a**2))]),
    all([c>a, c>b, (c**2) > ((a**2) + (b**2))])
    ]):
        return 3
    else:
        return 1
