import math

def circle_calculator(radius):
    pi = math.pi
    perimeter = 2*pi*radius
    area = pi*(radius**2)
    return perimeter, area