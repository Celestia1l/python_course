class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Unknown sound")


class Dog(Animal):
    def speak(self):
        print("Bark")


class Cat(Animal):
    def speak(self):
        print("Meow")
