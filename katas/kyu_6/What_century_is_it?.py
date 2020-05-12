# https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python

'''
Instructions :

Return the inputted numerical year in century format. The input will always be a 4 digit string. So there is no need for year string validation.

Examples:

  "1999" --> "20th"
  "2011" --> "21st"
  "2154" --> "22nd"
  "2259" --> "23rd"
  "1124" --> "12th"
  "2000" --> "20th"
  
'''


import math

def what_century(year):
    year = int(year)
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])
    if year <= 100:
        return '1st'
  
    elif year % 100 == 0:
        return ordinal(int(year/100))
        
    else:
        return ordinal(int(year/ 100) + 1)
