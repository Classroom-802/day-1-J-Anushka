def calculate_salary(stipend=0, base_salary=0, bonuses=0, incentives=0):
    if stipend:  # Intern
        return stipend
    elif base_salary and bonuses:  # Regular Employee
        return base_salary + bonuses
    elif base_salary and bonuses and incentives:  # Manager
        return base_salary + bonuses + incentives

# Input values
stipend = float(input("Enter the stipend for the Intern: "))
base_salary = float(input("Enter the base salary for the Regular Employee: "))
bonuses = float(input("Enter the bonuses for the Regular Employee: "))
incentives = float(input("Enter the performance incentives for the Manager: "))

# Output salaries
print(f"Salary of Intern: {calculate_salary(stipend=stipend)}")
print(f"Salary of Regular Employee: {calculate_salary(base_salary=base_salary, bonuses=bonuses)}")
print(f"Salary of Manager: {calculate_salary(base_salary=base_salary, bonuses=bonuses, incentives=incentives)}")
