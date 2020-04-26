# https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124/

'''
Instructions :

Definition (Primorial Of a Number)
Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied, only prime numbers are multiplied to calculate the primorial of a number. It's denoted with P#.

Task
Given a number N , calculate its primorial. !alt !alt

Notes
Only positive numbers will be passed (N > 0) .
Input >> Output Examples:
1- numPrimorial (3) ==> return (30)

Explanation:
Since the passed number is (3) ,Then the primorial should obtained by multiplying 2 * 3 * 5 = 30 .

Mathematically written as , P3# = 30 .
2- numPrimorial (5) ==> return (2310)

Explanation:
Since the passed number is (5) ,Then the primorial should obtained by multiplying 2 * 3 * 5 * 7 * 11 = 2310 .

Mathematically written as , P5# = 2310 .
3- numPrimorial (6) ==> return (30030)

Explanation:
Since the passed number is (6) ,Then the primorial should obtained by multiplying 2 * 3 * 5 * 7 * 11 * 13 = 30030 .

Mathematically written as , P6# = 30030 .
'''


import math 
MAX = 1000000;  
primes=[];  

def Prime(): 
    marked=[False]*(int(MAX/2)+1);  

    for i in range(1,int((math.sqrt(MAX)-1)/2)+1):  
        for j in range(((i*(i+1))<<1),(int(MAX/2)+1),(2*i+1)):  
            marked[j] = True;  

    primes.append(2);  
  
    for i in range(1,int(MAX/2)):  
        if (marked[i] == False):  
            primes.append(2*i + 1);  

def num_primorial(n):  
    # Multiply first n primes  
    result = 1;  
    for i in range(n): 
        result = result * primes[i];  
    return result;  
  
Prime(); 
