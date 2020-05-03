# https://www.codewars.com/kata/563d59dd8e47a5ed220000ba/

'''
Instructions :

Debug   function getSumOfDigits that takes positive integer to calculate sum of it's digits. Assume that argument is an integer.

Example
  123  => 6
  223  => 7
  1337 => 15

'''


def get_sum_of_digits(num):
    sum = 0
    digits = list(str(num))
    for x in digits:
        sum += int(x)
    return sum
