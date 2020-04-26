# https://www.codewars.com/kata/52597aa56021e91c93000cb0/

'''

Instructions :

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

'''


def move_zeros(array):
    arr = []
    count = 0
    for i in array:
        if ( i !=0 ) or (type(i) == bool) :
            arr.append(i)
        else :
            count = count + 1
    for i in range(count):
        arr.append(0)
    return arr
