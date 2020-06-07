# https://www.codewars.com/kata/5b358a1e228d316283001892/train/python

'''
Instructions:

INTRODUCTION:

If I give you a name of a city as a string, I want you to return a string that shows how many times each letter shows up in the string by using an asterisk *

SEE TEST CASE!

As you can see for Chicago, in the return string, I only show the letter "c" once even though there are 2 "c" in Chicago (regardless of upper or lowercase).

I show 2 asteriks since there are 2 "c" in Chicago.

In the return string there are no spaces between the letters, asteriks, and commas.

"Chicago"  =>  "c:**,h:*,i:*,a:*,g:*,o:*"
Note that the return string contains the characters in order of first appearence in the original string.

HAVE FUN!! ;)
'''


def get_strings(city):
    lst = []
    city = city.lower().replace(" ", "")
    for i in city:
        if i not in lst:
            lst.append(i)
    return ','.join(['{}:{}'.format(i,city.count(i)*'*') for i in lst])
