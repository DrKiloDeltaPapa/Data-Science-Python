# Case Match Function for Shapes


def determine_shape(sides):
    match sides:
        case 3:
            return "Triangle"
        case 4:
            return "Quadrilateral"
        case 5:
            return "Pentagon"
        case _:
            return f"Polygon with {sides} sides"


# Example usage:

shape = determine_shape(6)
print(shape)
