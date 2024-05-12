# https://www.codewars.com/kata/5966e33c4e686b508700002d
# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string

def str_to_int(s: str) -> int:
    return int(s) if s.isdigit() else 0


def sum_str(a: str, b: str) -> str:
    return str_to_int(a) + str_to_int(b)


print(sum_str('x', '123'))
