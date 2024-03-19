a=input()
c=[]
z = 0
while a!='exit':
    c.append(int(a))
    a = input()
print(c)
for i in range(len(c) - 1):
    n = i
    for j in range(i, len(c)):
        if c[j] < c[n]:
            n = j
            temp = c[i]
            c[i] = c[n]
            c[n] = temp
            z+=1
print(c)
print(z)


