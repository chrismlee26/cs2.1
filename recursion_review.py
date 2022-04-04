# Q1 
# The function power should compute the value of b^n, where n is any non-negative integer. 
# Fill in the blanks below, so that power behaves correctly.
# Hint: How does knowing the value of 39 help you find the value of 310?

# def power(b, n):
#     if n == __________:
#         return __________
#     else:
#         return __________ * power(__________, __________)


def power(b, n):
    # base condition
    if n == 0:
        return 1
    # run b*b, n-1 times
    else:
        # because return b * recursive power, use n-1 
        return b * power(b, n-1)

print(power(2,3))


# Q2
# def double(n):
#      if n == 0:
#           return 1
#      else:
#           return double(n - 1) + double(n - 1)

# 2.1 What is the value returned when calling double(3)?

# 2.2 What does this function do?

# 2.3 Can you modify the definition of double so that it computes the same result with a single recursive call?

# Q3
# 3.1 Can you find the greatest common denominator of two integers using recursion? Paste your working algorithm below:

# 3.2 Use your algorithm to find gcd(15, 9). Enter the value below:

# 3.3 Now find gcd(13, 8). Enter the value below:

# Q4
# def m(a, b):
#    if a < b:
#      return a
#    else:
#      return m(a - b, b)

# Find m(3, 5). 
# Find m(7, 5). 
# Find m(14, 5). 
# Try some more!
# Question: What does m do?