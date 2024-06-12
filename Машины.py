class Vehicle:

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def move(self):
        pass

class Car(Vehicle):

    def __init__(self, brand, color, speed):
        self.brand = brand
        super().__init__(color, speed)

    def honk(self):
        print('Гудок')