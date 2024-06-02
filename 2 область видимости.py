counter = 0
print(counter)
def increment_counter():
    global counter
    counter+=1
    return counter
print(increment_counter())
print(increment_counter())

