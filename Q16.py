import math

# Base class: Shape
class Shape:
    def area(self):
        pass

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius * self.radius

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth

# Derived class: Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height

# Input reading
radius, length, breadth, base, height = map(float, input().split())

# Creating shape objects
shapes = [Circle(radius), Rectangle(length, breadth), Triangle(base, height)]

# Displaying areas
for shape in shapes:
    print(f"{shape.area():.2f}")
