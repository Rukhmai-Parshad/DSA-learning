# Given a non-negative integers n, compute the factorial of the given number. 
# Factorial of n is defined as n * (n -1) * (n - 2) * ... * 1.
# For n = 0, the factorial is defined as 1.

def factorial(n):
    fact = 1
    i = 2
    while (i <= n):
         fact *= i
         i += 1
    return fact     

n =5 
print(factorial(n))
