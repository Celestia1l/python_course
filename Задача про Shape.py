import math
class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def area(self):
        return 0


class Rectangle(Shape):

    def area(self, a: float, b: float) -> float :
        return a * b

class Circle(Shape):
    def __init__(self, color):
        super().__init__(color)
    def area(self, a: float):
        s = a*a
        return s * math.pi


Rectangle_1 = Rectangle
print(Rectangle_1.area(5,5))
Circle_1 = Circle('red')
print(Circle_1.get_color())
print(Circle_1.area(5))

