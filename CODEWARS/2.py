#https://www.codewars.com/kata/5966e33c4e686b508700002d
#Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string
def sum_str(a: str, b: str) -> str:
    a = int(a) if a != '' else 0
    b = int(a) if a != '' else 0
    s=int(a)+int(b)
    return str(s)