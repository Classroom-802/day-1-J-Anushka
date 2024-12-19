class Employee:
    def __init__(self, emp_id, name, salary):
        # Private attributes
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    # Setter methods
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    # Getter methods
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    # Method to display all details
    def display_details(self):
        print(f"Employee ID: {self.get_emp_id()}")
        print(f"Employee Name: {self.get_name()}")
        print(f"Employee Salary: {self.get_salary()}")

# Input
emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
salary = float(input("Enter Employee Salary: "))

# Create Employee object and display details
employee = Employee(emp_id, name, salary)
employee.display_details()
