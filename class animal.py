class Animal:
    print('В классе Animal')

    def __init__(self, color, weight):
        print('В конструкторе класса Animal')
        self.color = color
        self.weight = weight

    def print(self):
        print(f'цвет = {self.color}, вес = {self.weight}')

class Cat(Animal):
    print('В классе Cat')

    def __init__(self, breed, color, weight):
        print('В конструкторе класса Cat')
        self.breed = breed
        super().__init__(color, weight)

class Lion(Animal):
    print('В классе Lion')

    def __init__(self, color, weight, mane_size):
        print('В конструкторе класса Lion')
        super().__init__(color, weight)
        self.mane_size = mane_size

class Tiger(Animal):
    print('В классе Tiger')

    def __init__(self, color, weight, pattern):
        print('В конструкторе класса Tiger')
        super().__init__(color, weight)
        self.stripe_pattern = pattern

class Elephant(Animal):
    print('В классе Elephant')

    def __init__(self, color, weight, tusk_size):
        print('В конструкторе класса Elephant')
        super().__init__(color, weight)
        self.tusk_size = tusk_size

class Shark(Animal):
    print('В классе Shark')

    def __init__(self, color, weight, fin_size):
        print('В конструкторе класса Shark')
        super().__init__(color, weight)
        self.fin_size = fin_size


cat2 = Cat('Британская короткошёрстная', 'Серый', 10)
print(cat2.breed, cat2.color, cat2.weight)
cat2.print()

lion1 = Lion('Золотистый', 250, 50)
print(lion1.color, lion1.weight, lion1.mane_size)
lion1.print()

tiger1 = Tiger('Оранжевый', 300, 'полосатый')
print(tiger1.color, tiger1.weight, tiger1.pattern)
tiger1.print()

elephant1 = Elephant('Серый', 5000, 120)
print(elephant1.color, elephant1.weight, elephant1.tusk_size)
elephant1.print()

shark1 = Shark('Серый', 500, 30)
print(shark1.color, shark1.weight, shark1.fin_size)
shark1.print()
