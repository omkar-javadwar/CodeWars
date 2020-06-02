# https://www.codewars.com/kata/5635e7cb49adc7b54500001c/solutions/python/

'''
Instructions:

There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.

You are given money in nominal value of n with 1<=n<=1500.

Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.

Good Luck!!!
'''


def solve(n):
    count = 0
    while(n>=500):
        count += 1  
        n-=500
    while(n>=200):
        count += 1  
        n-=200
    while(n>=100):
        count += 1  
        n-=100
    while(n>=50):
        count += 1  
        n-=50
    while(n>=20):
        count += 1  
        n-=20
    while(n>=10):
        count += 1  
        n-=10
    return count if n ==0 else -1
