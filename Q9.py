# Input: An integer n
n = int(input("Enter a number: "))

# Storing the original number for comparison
original_number = n

# Reversing the number
reversed_number = 0
while n > 0:
    reversed_number = reversed_number * 10 + n % 10
    n //= 10

# Checks if the original number is the same as the reversed number
if original_number == reversed_number:
    print("Palindrome")
else:
    print("Not Palindrome")
