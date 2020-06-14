# https://www.codewars.com/kata/53697be005f803751e0015aa/train/python

'''
Instructions :

Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
'''


def encode(st):
    return ''.join([i if i not in 'aeiouAEIOU' else str('aeiou'.index(i)+1) for i in st])
    
def decode(st):
    return ''.join([i if i not in '12345' else str('aeiou'[int(i)-1]) for i in st])