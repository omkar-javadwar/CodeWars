# https://www.codewars.com/kata/57729a09914da60e17000329/train/python

'''
Instructions :

Given a time in AM/PM format as a string, convert it to military (24-hour) time as a string.

Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock

Sample Input: 07:05:45PM Sample Output: 19:05:45

Try not to use built in DateTime libraries.

For more information on military time, check the wiki https://en.wikipedia.org/wiki/24-hour_clock#Military_time
'''


def get_military_time(time):
    if time[-2:] == "AM" and time[:2] == "12": 
        return "00" + time[2:-2] 
          
    elif time[-2:] == "AM": 
        return time[:-2] 
      
    elif time[-2:] == "PM" and time[:2] == "12": 
        return time[:-2] 
          
    else: 
        return str(int(time[:2]) + 12) + time[2:8]
