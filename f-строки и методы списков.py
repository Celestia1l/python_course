c=['компьютер','мышка','стол','лампа','коврик для мыши']
for i in range(len(c)):
    print(f"№ {i+1} {c[i]}") #Мы можем встроить любой код в f-строку {...}

c.insert(2, "Новый предмет") #Вставка по индексу 2(Толкает следующие элементы)
print(c)
print(c.index("стол")) #Находит индекс элемента
print(c.count("стол")) #Получаем скалько раз встречается элемент
c.pop(2) # Удаляет элемент по индексу
print(c)
c.remove("стол") # Удаляет элемент по значению
print(c)
