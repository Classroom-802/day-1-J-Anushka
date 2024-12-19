import cmath

class Complex:
    def __init__(self, real=0, imaginary=0):
        self.num = complex(real, imaginary)

    # Add two complex numbers
    def __add__(self, other):
        return Complex(self.num.real + other.num.real, self.num.imag + other.num.imag)

    # Multiply two complex numbers
    def __mul__(self, other):
        result = self.num * other.num
        return Complex(result.real, result.imag)

    # Calculate magnitude of the complex number
    def magnitude(self):
        return abs(self.num)

    # Display the complex number
    def display(self):
        return f"{self.num.real} + {self.num.imag}i" if self.num.imag >= 0 else f"{self.num.real} - {-self.num.imag}i"

# Main logic
operation = int(input("Select Operation: (1) Addition (2) Multiplication (3) Magnitude: "))

if operation == 1 or operation == 2:
    real1, imaginary1 = map(int, input("Enter first complex number (real imaginary): ").split())
    real2, imaginary2 = map(int, input("Enter second complex number (real imaginary): ").split())
    
    c1 = Complex(real1, imaginary1)
    c2 = Complex(real2, imaginary2)

    if operation == 1:
        result = c1 + c2
        print("Sum:", result.display())
    elif operation == 2:
        result = c1 * c2
        print("Product:", result.display())

elif operation == 3:
    real, imaginary = map(int, input("Enter complex number (real imaginary): ").split())
    c = Complex(real, imaginary)
    print("Magnitude:", c.magnitude())

else:
    print("Invalid operation")
