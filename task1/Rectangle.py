from Shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def toString(self):
        return "Rectangle"

    def area(self):
        return self.length * self.width
