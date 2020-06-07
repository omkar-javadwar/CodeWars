# https://www.codewars.com/kata/5970df092ef474680a0000c9/train/python

'''
Instructions:

The alphabetized kata
Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order. Whitespace and punctuation shall simply be removed!

The input is restricted to contain no numerals and only words containing the english alphabet letters.

Example:

alphabetized("The Holy Bible") # "BbeehHilloTy"
'''


def alphabetized(s):
    char = ['!','@','$','%','^','&','*','(',')','_','+','=','-','`',',','.',' ',"'"]
    for i in char:
        s = s.replace(i,'')
    return ''.join(sorted(list(s),key=str.lower))
