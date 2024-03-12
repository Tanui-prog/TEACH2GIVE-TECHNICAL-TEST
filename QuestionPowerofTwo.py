
# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.

# Examples:
# 8=> returns true
# 6=> returns false

n = int(input())  # Taking input from the user

# Checking if n is a power of 2 and printing the result
print(n & (n - 1) == 0 and n != 0)
