# Question 5: Reverse Integer
# Write a program that takes an integer as input and returns an integer with reversed digit
# ordering.
# Examples:

# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.


def reverse_integer(n):
    # Initialize result
    reversed_num = 0
    
    # Check if the number is negative
    negative = False
    if n < 0:
        negative = True
        n = -n
    
    # Reverse the digits
    while n != 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n //= 10
    
    # If the original number was negative, make the reversed number negative
    if negative:
        reversed_num = -reversed_num
    
    return reversed_num

# Test cases
print(reverse_integer(500))  # Output: 5
print(reverse_integer(-56))  # Output: -65
print(reverse_integer(-90))  # Output: -9
print(reverse_integer(91))   # Output: 19
