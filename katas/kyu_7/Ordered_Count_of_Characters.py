# https://www.codewars.com/kata/57a6633153ba33189e000074/

'''
Instructions :

Count the number of occurrences of each character and return it as a list of tuples in order of appearance.

Example:

ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
'''


def ordered_count(inp):
    lst = []
    for i in inp:
        if i not in lst:
            lst.append(i)
    return [(i,inp.count(i)) for i in lst]
