a = "12  43    24  53"
a = a.split() #Разбиваем по пробелам
print(a)
l = list(map(int, a)) #Применяем к каждому элементу списка а функцию int
print(l)
# Считываем строку, разбиваем по пробелам и делаем каждый элемент числом
m = list(map(int, input().split()))
print(m)