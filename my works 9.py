c = []
x = int(input())
print()
while True:
    a = input()
    if c == "":
        break
    c.append(int(a))
for i in range(len(c)):
    if c[i] <= x:
        print(i + 1)
