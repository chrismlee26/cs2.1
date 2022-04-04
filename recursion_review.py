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
        # because n == 0 returns 1, n-1 as this is where it stops recursion.
        return b * power(b, n-1)

# print(power(2,3))


# Q2
def double(n):
    if n == 0:
        return 1
    else:
        return double(n - 1) + double(n - 1)

# print(double(17), "2^n")

# 2.1 What is the value returned when calling double(3)? 8

# 2.2 What does this function do? 

# 2.3 Can you modify the definition of double so that it computes the same result with a single recursive call?
def double2(n):
    if n == 0:
        return 1
    else:
        return 2* double2(n - 1)

# print(double2(17), "~~")

# Q3
# 3.1 Can you find the greatest common denominator of two integers using recursion? Paste your working algorithm below:

def gcd(a, b):
    x = a % b
    if (x == 0):
        return b
    else: 
        return gcd(b, x)



# 3.2 Use your algorithm to find gcd(15, 9). Enter the value below: 3
# print(gcd(15, 9))

# 3.3 Now find gcd(13, 8). Enter the value below: 1
# print(gcd(13, 8))

# Q4
def m(a, b):
    if a < b:
        return a
    else:
        return m(a - b, b)

# Find m(3, 5).
print(m(3, 5))
# Find m(7, 5). 
print(m(7, 5))
# Find m(14, 5). 
print(m(14, 5))
# Try some more!
# Question: What does m do? It performs a modulus function on a % b

print (3%5, "~~~~")
print (4%5, "~~~~")
print (5%5, "~~~~")
print (6%5, "~~~~")