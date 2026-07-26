# Given a positive integer n, we have to find the sum of squares of 
# first n natural numbers. 

def summation(n):
    return sum(i**2 for i in range(1, n + 1))

n = 2
print(summation(n))