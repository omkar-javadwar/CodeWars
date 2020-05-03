# https://www.codewars.com/kata/55ed875819ae85ca8b00005c/

'''

Instructions :

Your task is to write a function, which takes two arguments and returns a sequence. First argument is a sequence of values, second is multiplier. The function should filter all non-numeric values and multiply the rest by given multiplier.

'''


def multiply_and_filter(seq, multiplier): 
    return [i*multiplier for i in seq if ((isinstance(i,int) or isinstance(i,float)) and not isinstance(i,bool))]
