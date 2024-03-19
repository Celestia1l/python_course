a=int(input())
c=[]
for i in range(a):
    b=int(input())
    c.append(b)
d=int(input())
l=-1
for i in range(len(c)):
    if d==c[i]:
        l=i
if l==-1:
    print('no')
else:
    print(l)