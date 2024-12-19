# Function to calculate area of a circle
def area(radius=None, length=None, breadth=None, base=None, height=None):
    pi = 3.14159
    
    # Checks for circle area
    if radius is not None:
        return pi * radius * radius
    
    # Checks for rectangle area
    elif length is not None and breadth is not None:
        return length * breadth
    
    # Checks for triangle area
    elif base is not None and height is not None:
        return 0.5 * base * height

# Input: Circle radius, rectangle dimensions, triangle base and height
radius = float(input("Enter the radius of the circle: "))
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Output the areas of all shapes
print(f"Area of the circle: {area(radius=radius)}")
print(f"Area of the rectangle: {area(length=length, breadth=breadth)}")
print(f"Area of the triangle: {area(base=base, height=height)}")
