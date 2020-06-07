# https://www.codewars.com/kata/5bd00c99dbc73908bb00057a/train/python

'''
Instructions:

In this kata you will be given a random string of letters and tasked with returning them as a string of comma-separated sequences sorted alphabetcally, with each sequence starting with an uppercase character followed by n-1 lowercase characters, where n is the letter's alphabet position 1-26.

Example
alpha_seq("ZpglnRxqenU") -> "Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Xxxxxxxxxxxxxxxxxxxxxxxx,Zzzzzzzzzzzzzzzzzzzzzzzzzz"
Technical Details
The string will include only letters.
The first letter of each sequence is uppercase followed by n-1 lowercase.
Each sequence is seperated with a comma.
Return value needs to be a string.
'''


def alpha_seq(string):
    alphabet_order = {'a' : 'A', 'b' : 'Bb', 'c' : 'Ccc', 'd' : 'Dddd', 'e' : 'Eeeee',
                    'f' : 'Ffffff', 'g' : 'Ggggggg', 'h' : 'Hhhhhhhh', 'i' : 'Iiiiiiiii', 'j' : 'Jjjjjjjjjj',
                    'k' : 'Kkkkkkkkkkk', 'l':'Llllllllllll', 'm':'Mmmmmmmmmmmmm', 'n':'Nnnnnnnnnnnnnn',
                    'o':'Ooooooooooooooo', 'p':'Pppppppppppppppp', 'q':'Qqqqqqqqqqqqqqqqq',
                    'r':'Rrrrrrrrrrrrrrrrrr', 's':'Sssssssssssssssssss', 't':'Tttttttttttttttttttt',
                    'u':'Uuuuuuuuuuuuuuuuuuuuu', 'v':'Vvvvvvvvvvvvvvvvvvvvvv', 'w':'Wwwwwwwwwwwwwwwwwwwwwww', 
                    'x':'Xxxxxxxxxxxxxxxxxxxxxxxx', 'y':'Yyyyyyyyyyyyyyyyyyyyyyyyy', 'z':'Zzzzzzzzzzzzzzzzzzzzzzzzzz'}
    return ','.join([alphabet_order[i] for i in sorted(list(string.lower()))])
