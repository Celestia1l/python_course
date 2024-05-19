def flick_switch(lst):
    a = []
    value = True
    for i in lst:
        if i == 'flick':
            if value == True:
                value = False
            else:
                value = True
        a.append(value)
    return a


print(flick_switch(['flick', 'chocolate', 'flick', 'adventure', 'sunshine']))
