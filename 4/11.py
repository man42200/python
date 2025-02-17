import math

def calculate_sin(x_degrees):

    x_radians = x_degrees * (math.pi / 180)

    sin_x = math.sin(x_radians)
    return sin_x

x_degrees = float(input("Enter x in degrees: "))
result = calculate_sin(x_degrees)
print(f"sin({x_degrees} degrees) = {result}")