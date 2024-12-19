# Input: An integer n
n = int(input("Enter a number: "))

# Calculating the sum of odd numbers from 1 to n
sum_of_odds = sum(i for i in range(1, n + 1, 2))

# Output the result
print(sum_of_odds)
