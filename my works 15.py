a=int(input())
c=[]
for i in range(a):
    b=int(input())
    c.append(b)
print(c)
for i in range(len(c) - 1):
    n = i
    for j in range(i, len(c)):
        if c[j] < c[n]:
            n = j
    temp = c[i]
    c[i] = c[n]
    c[n] = temp
print(c)