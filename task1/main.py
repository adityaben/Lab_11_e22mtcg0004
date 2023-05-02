from Circle import Circle
from ShapeCollection import ShapeCollection
from Square import Square
from Rectangle import Rectangle



def calculate_area(input_file_path, result_file_path, roll_no):
    valid_shape_types = ["circle", "square", "rectangle"]
    error_messages = {
        "value_error": "Invalid value(s) for shape dimensions",
        "unknown_shape_type": "Unknown shape type",
        "missing_shape_dimensions": "Missing shape dimensions"
    }

    try:
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()

        with open(result_file_path, 'w') as result_file:
            result_file.write(str(roll_no) + "\n")
            result_file.write("Name: Aditya Jhankal\n\n")

            for line in lines:
                line = line.strip()
                if not line:
                    continue
                values = line.split()

                if len(values) < 2:
                    result_file.write(f"{line}/ {error_messages['missing_shape_dimensions']}\n")
                    continue

                shape_type = values[0].lower()
                if shape_type not in valid_shape_types:
                    result_file.write(f"{line}/ {error_messages['unknown_shape_type']}\n")
                    continue

                try:
                    dimensions = [float(dimension) for dimension in values[1:]]
                except ValueError:
                    result_file.write(f"{line}/ {error_messages['value_error']}\n")
                    continue

                if shape_type == "circle":
                    if len(dimensions) != 1:
                        result_file.write(f"{line}/ {error_messages['missing_shape_dimensions']}\n")
                        continue
                    radius = dimensions[0]
                    area = Circle(radius).area()
                elif shape_type == "square":
                    if len(dimensions) != 1:
                        result_file.write(f"{line}/ {error_messages['missing_shape_dimensions']}\n")
                        continue
                    side = dimensions[0]
                    area = Square(side).area()
                else:
                    if len(dimensions) != 2:
                        result_file.write(f"{line}/ {error_messages['missing_shape_dimensions']}\n")
                        continue
                    length, width = dimensions
                    area = Rectangle(length, width).area()

                result_file.write(f"{line} {area:.2f}\n")
    except Exception as e:
        with open(result_file_path, 'w') as result_file:
            result_file.write(f"{roll_no}\n")
            result_file.write("Name: John Doe\n\n")
            result_file.write(f"Error: {str(e)}")




input_file_path = 'input.txt'
result_file_path = 'result_e22mtcg0004.txt'
roll_no = 'e22mtcg0004'
calculate_area(input_file_path, result_file_path, roll_no)
