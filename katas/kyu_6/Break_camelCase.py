# https://www.codewars.com/kata/5208f99aee097e6552000148/

'''
Instructions :

Complete the solution so that the function will break up camel casing, using a space between words.

Example
  solution("camelCasing")  ==  "camel Casing"

'''


def solution(str):
    words = [[str[0]]] 

    for c in str[1:]: 
        if words[-1][-1].islower() and c.isupper(): 
            words.append(list(c)) 
        else: 
            words[-1].append(c) 

    return ' '.join([''.join(word) for word in words]) 
