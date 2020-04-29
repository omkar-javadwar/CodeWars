# https://www.codewars.com/kata/53368a47e38700bd8300030d/

'''
Instructions :

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

  namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
  # returns 'Bart, Lisa & Maggie'

  namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
  # returns 'Bart & Lisa'

  namelist([ {'name': 'Bart'} ])
  # returns 'Bart'

  namelist([])
  # returns ''
  
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
'''


def namelist(names):
    if len(names)>1:
        names = [ sub['name'] for sub in names ] 
        return ', '.join(names[:-1]) + ' & ' + names[-1]
    elif len(names) == 1:
        return [ sub['name'] for sub in names ][0]
    else:
        return ''
