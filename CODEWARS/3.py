# https://www.codewars.com/kata/57f222ce69e09c3630000212
# For every good kata idea there seem to be quite a few bad ones!
# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'.
# If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'.
# If there are no good ideas, as is often the case, return 'Fail!'.

def search_str_in_list(f: str, x: list) -> int:
    a = 0
    for i in x:
        if i == f:
            a += 1
    return a


def get_result_by_counter(k: int) -> str:
    if k == 1 or k == 2:
        return 'Publish!'
    elif k > 2:
        return 'I smell a series!'
    return 'Fail!'


def well(x: list) -> str:
    counter = search_str_in_list('good', x)
    return get_result_by_counter(counter)


print(well(['good', 'good', 'asd']))
