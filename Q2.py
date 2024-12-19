import math

# Input: An integer to check for primality
n = int(input("Enter a number: "))

# Checking if n is prime
is_prime = n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# Result
print("Prime" if is_prime else "Not Prime")

