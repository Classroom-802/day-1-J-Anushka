import math

class Shape:
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def get_area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def get_area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def get_area(self):
        return 0.5 * self.base * self.height

shape_type = int(input("Enter Shape Type (1 for Rectangle, 2 for Circle, 3 for Triangle): "))

if shape_type == 1:
    length, breadth = map(int, input("Enter Length and Breadth of the Rectangle: ").split())
    shape = Rectangle(length, breadth)
elif shape_type == 2:
    radius = int(input("Enter Radius of the Circle: "))
    shape = Circle(radius)
elif shape_type == 3:
    base, height = map(int, input("Enter Base and Height of the Triangle: ").split())
    shape = Triangle(base, height)
else:
    print("Invalid Shape Type!")
    exit()

print(f"The area of the shape is: {shape.get_area():.3f}")
