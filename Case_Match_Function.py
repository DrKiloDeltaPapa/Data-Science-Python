## Case Match Conditional for Shapes


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


## Example usage:

shape = determine_shape(6)
print(shape)


## Another Example of the  Match Case or Case Match  Condtional

# value = "four"
# match value:
#     case "one":
#         result = 1
#     case "two":
#         result = 2
#     case "three":
#         result = 3
#     case "four" | "five":
#         result = (4, 5)
#     case _:
#         result = -1

# print(result)
