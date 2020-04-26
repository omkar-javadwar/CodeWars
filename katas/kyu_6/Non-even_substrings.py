# https://www.codewars.com/kata/59da47fa27ee00a8b90000b4/

'''
Instructions :

Given a string of integers, return the number of odd-numbered substrings that can be formed.

For example, in the case of "1341", they are 1, 1, 3, 13, 41, 341, 1341, a total of 7 numbers.

  solve("1341") = 7. See test cases for more examples.

'''


def solve(s):
    length = len(s) 
    count = 0
  
    for i in range(0,length,1): 
        temp = ord(s[i]) - ord('0') 
  
        # If current digit is even, add 
        # count of substrings ending with 
        # it. The count is (i+1) 
        if temp % 2: 
            count += (i + 1) 
  
    return count 
