a=int(input())
c=[]
for i in range(a):
    b=int(input())
    c.append(b)
min=99999999999999999999999999999999999999999999999999999999999999999999999
for i in range(len(c)):
    if c[i]<min:
        min=c[i]
print(c.index(min))