#https://www.codewars.com/kata/5966e33c4e686b508700002d
#Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string
def sum_str(a, b):
    if len(a) == 0 and len(b) == 0:
        return '0'
    elif len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    s=int(a)+int(b)
    return str(s)