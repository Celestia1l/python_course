a = int(input())
c = []
b = input()
for i in range(a):
    b = input()
    a.append(b)
d = input()
f = -1
for i, g in range(c):
    if g == d:
        f = i + 1
print(f)