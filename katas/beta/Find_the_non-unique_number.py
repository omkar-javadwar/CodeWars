# https://www.codewars.com/kata/5b62031b97568072da0003db/

'''

Instructions :

Given a list of numbers, a number that appears only once is considered unique. The number that appears more than once is considered non-unique.

In this kata find the non-unique number and return a list consisting of two elements: [number, # of occurrences of the non-unique number]

If all the numbers in the list are unique, return the string 'unique'. If the list is empty, return the empty list [].

#Examples

  ['1', '2', '3.0', '3'] -> [3, 2]
  ['0', '0.0', '0'] -> 'unique'
  [] -> []
  
  '''
  
  
  def non_unique(lst):
    x = []
    lst = [float(i) for i in lst]
    if lst:
        for i in lst:
            if i.is_integer():
                x.append(int(i))
            else:
                x.append(i)
        arr = [i for i in x if x.count(i) > 1]
        return [arr[0],arr.count(arr[0])] if arr else 'unique'
    else:
        return []
