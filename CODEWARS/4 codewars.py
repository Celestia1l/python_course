def flick_switch(lst: list) -> list:
    r = []
    value = True
    for i in lst:
        if i == 'flick':
            value = not value
        a.append(value)
    return a


print(flick_switch(['flick', 'chocolate', 'flick', 'adventure', 'sunshine']))
