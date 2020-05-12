# https://www.codewars.com/kata/5666bd1011beb6f768000073/train/python

'''
Instructions :

If I give you a date, can you tell me what day that date is? For example, december 8th, 2015 is a tuesday.

Your job is to write the function day(d) which takes a string representation of a date as input, in the format YYYYMMDD. The example would be "20151208". The function needs to output the string representation of the day, so in this case "Tuesday".

Your function should be able to handle dates ranging from January first, 1582 (the year the Gregorian Calendar was introduced) to December 31st, 9999. You will not be given invalid dates. Remember to take leap years into account.
'''


import datetime 

def day(date):
    date = date[-2:]+' '+date[4:6]+' '+date[:4]
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'][day] 
