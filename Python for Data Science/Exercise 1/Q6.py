"""
Given two numbers n and r, find the value of nCr (binomial
coefficient: nCr = (n!) / (r! * (n-r)!))
"""

n = int(input("Enter the n value: "))
r = int(input("Enter the r value: "))


# Recursive Method
def factorial_recursive(number: int):
    if number == 0 or number == 1:
        return 1
    elif number < 0:
        return 0
    else:
        return number * factorial_recursive(number - 1)


ncr_recursive = int(factorial_recursive(n) / (factorial_recursive(r) * factorial_recursive(n - r)))
print(ncr_recursive)


# Normal Method
def factorial(number: int):
    if number == 0 or number == 1:
        return 1
    elif number < 0:
        return 0
    else:
        factorial_num = 1
        for i in range(number, 1, -1):
            factorial_num *= i

    return factorial_num


ncr = int(factorial(n) / (factorial(r) * factorial(n - r)))
print(ncr)
