# Base class: Student
class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name

    def display_student_details(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")

# Derived class: Result
class Result(Student):
    def __init__(self, roll_number, name, marks1, marks2, marks3):
        # Initialize base class attributes
        super().__init__(roll_number, name)
        # Additional attributes for Result class
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def calculate_total(self):
        return self.marks1 + self.marks2 + self.marks3

    def calculate_percentage(self):
        total_marks = self.calculate_total()
        return (total_marks / 300) * 100  # Out of 300 for three subjects

    def display_result(self):
        self.display_student_details()
        print(f"Marks in Subject 1: {self.marks1}")
        print(f"Marks in Subject 2: {self.marks2}")
        print(f"Marks in Subject 3: {self.marks3}")
        total = self.calculate_total()
        print(f"Total Marks: {total}")
        percentage = self.calculate_percentage()
        print(f"Percentage: {percentage:.2f}%")

# Input
roll_number = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
marks1 = int(input("Enter Marks for Subject 1: "))
marks2 = int(input("Enter Marks for Subject 2: "))
marks3 = int(input("Enter Marks for Subject 3: "))

# Create Result object and display details
result = Result(roll_number, name, marks1, marks2, marks3)
result.display_result()
