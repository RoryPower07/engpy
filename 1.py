# calculate the area of a cone
import math

def cone_area(radius, height):
    slant_height = math.hypot(radius, height)
    return math.pi * radius * (radius + slant_height)

radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

area = cone_area(radius, height)
print(f"The area of the cone is: {area:.2f}")