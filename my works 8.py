a = int(input()
c = []
for i in range(a):
    b = input()
    c.append(b)
d = input()
c = [b for b in c if b != d]
print(c)
