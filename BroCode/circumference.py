import math

def getCircumference(radius):
    return 2 * math.pi * radius

# Example usage without rounding the input radius
radius = 4
circumference = getCircumference(radius)

# Print the circumference rounded to 2 decimal places
print(round(circumference, 2))
