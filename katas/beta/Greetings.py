# https://www.codewars.com/kata/5901c9d463bf406d7c000107/train/python

'''
Instructions :

Greet someone by the given time of day and their name. If no time or name is given, return "Hey dude greet someone"

Example
  greetings("morning", "John") = "Good morning John"
'''


def greetings(time, name):
    return 'Good ' + time + ' ' + name if isinstance((time and name),str) else "Hey dude greet someone"
