# Given a positive integer n, find the nth Fibonacci number.
# The Fibonacci series is a sequence where a term is the sum of previous two terms. 
# The first two terms of the Fibonacci sequence are 0 followed by 1. 
# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21.

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

n = 7
print(fibonacci(n))     