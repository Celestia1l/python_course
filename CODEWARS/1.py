#https://www.codewars.com/kata/515e271a311df0350d00000f
#Complete the square sum function so that it squares each number passed into it and then sums the results together.
def square_sum(numbers):
    s=0
    for i in numbers:
        s=s+i**2
    return s
