# https://www.codewars.com/kata/59e19a747905df23cb000024/

'''
Instructions :

Take a string str and return a string that is made up of the number of occurances of each english letter in str, followed by that letter. The string shouldn't contain zeros; leave them out.

An empty string, or one with no letters, should return an empty string.

Notes
  Ignore all case
  str will never be null
  
Examples
  "This is a test sentence."  =>  "1a1c4e1h2i2n4s4t"
  ""  =>  ""
  "555"  =>  ""

'''


def string_letter_count(s):
    s = s.lower()
    return ''.join([str(s.count(l)) + l for l in sorted(set(s)) if l.isalpha()])
