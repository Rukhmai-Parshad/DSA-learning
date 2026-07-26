# Given a positive integer n, find the sum of the first n natural numbers.

def findSum(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        i += 1
    return sum

n = 4
print(findSum(n))