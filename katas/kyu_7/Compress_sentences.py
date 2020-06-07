# https://www.codewars.com/kata/59de469cfc3c492da80000c5/train/python

'''
Instructions:

Your task is to make a program takes in a sentence (without puncuation), adds all words to a list and returns the sentence as a string which is the positions of the word in the list. Casing should not matter too.

Example
"Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"

becomes

"01234567802856734"

Another example
"the one bumble bee one bumble the bee"

becomes

"01231203"
'''


def compress(sentence):
    lst = []
    for i in sentence.lower().split():
        if i not in lst:
            lst.append(i)
    return ''.join([str(lst.index(i)) for i in sentence.lower().split()])
