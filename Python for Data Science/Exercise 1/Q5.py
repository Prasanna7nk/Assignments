"""
Given a number n, write a function to print all prime factors of
n. 

For example, if the input number is 12, then output should be
“2 2 3”
"""

def PrimeFactors(n: int):
    prime_factors = []
    i = 2

    for x in range(2, i):
        if n % i == 0:
            prime_factors.append(i)
            for y in range(2, i + 1):
                if x % y == 0:
                    break
    
    print(prime_factors)

PrimeFactors(12)

# def PrimeFactors(n: int):
#     prime_factors = []
#     i = 2
#     while True:
#         if n % i == 0:
#             n = n // i
#             for x in range(2, i):
#                 if n % i == 0:
#                     break
            
#             else:
#                 prime_factors.append(i)
#         i += 1

#         if n == 1:
#             break

#     print(prime_factors)

# n = 12
# PrimeFactors(n)