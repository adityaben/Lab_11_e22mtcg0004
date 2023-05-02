from Shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def toString(self):
        return "Circle"

    def area(self):
        return 3.14 * self.radius * self.radius