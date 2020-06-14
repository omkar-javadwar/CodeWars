# https://www.codewars.com/kata/56d93f249c844788bc000002/train/python

'''
Instructions:

No Story

No Description

Only by Thinking and Testing

Look at result of testcase, guess the code!
'''


def testit(s):
    return ' '.join([i[:-1]+i[-1].upper() for i in s.split()])
