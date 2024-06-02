number=1

def increase_by_5():
    global number
    number+=5
    return number

def multiply_by_2():
    global number
    number*=2
    return number

print(number)
print(increase_by_5())
print(multiply_by_2())