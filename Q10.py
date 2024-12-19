# Input: An integer n
n = int(input("Enter a number: "))

# Initialize the sum of digits
sum_of_digits = 0

# Extracting and sum the digits
while n > 0:
    sum_of_digits += n % 10
    n //= 10

# Output the result
print(sum_of_digits)
