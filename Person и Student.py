class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is {name} and I am {age} years old.")

class Student(Person):

    def __init__(self, university, name, age):
        self.university = university
        super().__init__(name, age)

    def introduce(self):
        print("My name is {name} and I am {age} years old. I study at {university}.")