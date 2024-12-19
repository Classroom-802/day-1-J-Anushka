# Input: An integer n
n = int(input("Enter a number: "))

# Reversing the number
reversed_number = 0
while n > 0:
    reversed_number = reversed_number * 10 + n % 10
    n //= 10

# Output the result
print(reversed_number)
