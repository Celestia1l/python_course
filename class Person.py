class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello {self.name}!')


person_1 = Person('Max', 14)
person_1.greet()
print(person_1.age)