a=int(input())
c=[]
for i in range(a):
    b=int(input())
    c.append(b)
print(c)
for j in range(a-1):
    for i in range(a-1-j):
        if c[i]<c[i+1]:
            temp=c[i]
            c[i]=c[i+1]
            c[i+1]=temp
print(c)

