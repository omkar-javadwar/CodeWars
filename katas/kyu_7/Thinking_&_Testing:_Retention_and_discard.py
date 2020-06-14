# https://www.codewars.com/kata/56ee0448588cbb60740013b9/train/python

'''
Instructions:

Only by Thinking and Testing

Look at the results of the testcases, and guess the code!
'''


def mystery(n):
    return [i for i in range(1, n+1, 2) if n % i == 0]
