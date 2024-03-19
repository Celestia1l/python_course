k = 0
n = 0
a = int(input())
while a == 4 or a == 5:
    if a == 4:
        k = k + 1
    else:
        n = n + 1
    a = int(input())
if k > n:
    print('4 больше')
elif n > k:
    print('5 больше')
else:
    print('5 и 4 одинаковое количество')
