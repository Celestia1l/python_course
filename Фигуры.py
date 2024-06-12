class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def area(self, a, b):
        return a * b


class Circle(Shape):
    def area(self, a):
        return 3,14 * a
