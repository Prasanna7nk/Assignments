"""
Given a number, check whether the given number is an
Armstrong number or not. A positive integer is called an
Armstrong number of order n if:

abcd... = an + bn + cn + dn + ...

Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

153 is an Armstrong number of order 3.

Inputs from the user will be number and order n
"""

number = input("Enter the number to check for Armstrong: ")
order = int(input("Enter the order: "))

number_list = list(map(int, number.strip()))

armstrong_sum = 0

for numbers in number_list:
    armstrong_sum += numbers ** order

if armstrong_sum == int(number):
    print(True)
else:
    print(False)
