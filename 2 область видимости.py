counter = 0
def increment_counter():
    global counter
    counter+=1
    return counter
print(increment_counter())
print(increment_counter())

