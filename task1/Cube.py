from Shape import Shape
class Cube(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(6 * self.side ** 2, 2)

    def toString(self):
        return f"Cube {self.side}"
