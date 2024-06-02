name=100
def print_name():
    name=0
    def print_name2():
        global name
        print(name)
    print_name2()
    print(name)
print(print_name())