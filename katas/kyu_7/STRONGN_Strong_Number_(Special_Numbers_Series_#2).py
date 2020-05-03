# https://www.codewars.com/kata/5a4d303f880385399b000001/

'''
Instructions :

Definition
Strong number is the number that the sum of the factorial of its digits is equal to number itself.

For example: 145, since
1! + 4! + 5! = 1 + 24 + 120 = 145
So, 145 is a Strong number.

Task
  Given a number, Find if it is Strong or not.
'''

import math 

def strong_num(number):
    sum = 0
    temp = number
    while(number):
        i = 1
        fact = 1
        r = number%10
        while(i<=r):
            fact *= i
            i += 1
        sum += fact
        number = number//10
    return "STRONG!!!!" if sum == temp else "Not Strong !!"
