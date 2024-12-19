import math

# Base class: Shape
class Shape:
    def area(self):
        pass  # Virtual method to be overridden by derived classes

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)

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

# Input
radius = float(input("Enter radius of the circle: "))
length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))

# Create objects for each shape
circle = Circle(radius)
rectangle = Rectangle(length, breadth)
triangle = Triangle(base, height)

# Calculate and print the area for each shape
print(f"Circle Area: {circle.area():.2f}")
print(f"Rectangle Area: {rectangle.area():.2f}")
print(f"Triangle Area: {triangle.area():.2f}")
