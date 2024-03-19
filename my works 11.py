a=int(input())
c=[]
for i in range(a):
    b=int(input())
    c.append(b)
print(c)
k=int(input())
if c[k]>c[k+1]:
    temp = c[k]
    c[k] = c[k + 1]
    c[k + 1] = temp
print(c)