# https://www.codewars.com/kata/5d50e3914861a500121e1958/train/python

'''
Instructions :

Your task is to add up letters to one letter.

The function will be given a variable amount of arguments, each one being a letter to add.

Notes:
Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
If no letters are given, the function should return 'z'
Examples:
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'
Confused? Roll your mouse/tap over here
'''


def add_letters(*letters):
    l_index = 0
    alphabet = ['zero trolls', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in letters :
        l_index += alphabet.index(i)
    
    if(len(letters) > 0) :
        while (l_index > 26) :
            l_index -= 26
        return alphabet[l_index]
    
    return 'z'
