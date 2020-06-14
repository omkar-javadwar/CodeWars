# 

'''
Instructions:

https://www.codewars.com/kata/56d949281b5fdc7666000004/train/python

No Story

No Description

Only by Thinking and Testing

Look at result of testcase, guess the code!
'''


def testit(a, b):
    a = list(set(a))
    b = list(set(b))
    a.extend(b) # extend???
    a.sort()
    return a
