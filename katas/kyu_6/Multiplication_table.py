# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python

'''

Instructions :

Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
'''

from itertools import islice 

def multiplication_table(n):
    lst = [i*j for i in list(range(1,n+1)) for j in list(range(1,n+1))]
    Input = iter(lst) 
    return [list(islice(Input, n)) for i in range(n)]
