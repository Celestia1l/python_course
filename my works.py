c = []
while True:
    a = input()
    if a == "exit":
        break
c.append(a)
b = input()
d = 0
for a in c:
    if a == b:
        d += 1
print(d)
