from Shape import Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side ** 2, 2)

    def toString(self):
        return f"Square {self.side}"
