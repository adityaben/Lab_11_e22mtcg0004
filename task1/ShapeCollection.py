
class ShapeCollection:
    def __init__(self, shapes):
        self.shapes = shapes

    def displayShapes(self):
        for shape in self.shapes:
            print(shape.toString(), shape.area())

    @staticmethod
    def main(args):
        shapes = []
        for i in range(1, len(args)):
            shape_type, *dimensions = args[i].split()
            if shape_type.lower() == 'circle':
                radius = float(dimensions[0])
                circle = Circle(radius)
                shapes.append(circle)
            elif shape_type.lower() == 'square':
                side = float(dimensions[0])
                square = Square(side)
                shapes.append(square)
            elif shape_type.lower() == 'rectangle':
                length = float(dimensions[0])
                width = float(dimensions[1])
                rectangle = Rectangle(length, width)
                shapes.append(rectangle)
            elif shape_type.lower() == 'cube':
                side = float(dimensions[0])
                cube = Cube(side)
                shapes.append(cube)
            else:
                raise ValueError(f"Unknown shape type '{shape_type}'")

        collection = ShapeCollection(shapes)
        collection.displayShapes()