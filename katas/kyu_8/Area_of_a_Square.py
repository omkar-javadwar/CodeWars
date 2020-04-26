# https://www.codewars.com/kata/5748838ce2fab90b86001b1a/

'''
Instructions :

Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. Return the result rounded to two decimals.

http://i.imgur.com/nJrae8n.png

Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)
'''


import math
def square_area(A):
    return round(((2 * A / 3.141592653589793)**2),2)
