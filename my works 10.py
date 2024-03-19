a=int(input())
c=[]
for i in range(a):
    b = input()
    c.append(b)
z=input()
p = c.count(z)
for i in range(p):
    c.remove(z)
print(c)
