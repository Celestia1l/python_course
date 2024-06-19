import math


class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def area(self):
        return 0


class Rectangle(Shape):

    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        super().__init__(color)

    def area(self) -> float:
        return self.a * self.b


class Circle(Shape):
    def __init__(self, a, color):
        self.a = a
        super().__init__(color)

    def area(self):
        s = self.a * self.a
        return s * math.pi


Rectangle_1 = Rectangle(5,3,'red')
print(Rectangle_1.area())
Circle_1 = Circle(6, 'red')
print(Circle_1.get_color())
print(Circle_1.area())