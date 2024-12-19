# Input: An integer n
n = int(input("Enter a number: "))

# Initializing the largest digit variable
largest_digit = 0

# Loop through each digit and find the largest
while n > 0:
    digit = n % 10
    largest_digit = max(largest_digit, digit)
    n //= 10

# Output the result
print(largest_digit)
