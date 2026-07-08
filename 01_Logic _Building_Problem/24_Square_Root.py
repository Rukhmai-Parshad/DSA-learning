# Given a positive integer n, find its square root. 
# If n is not a perfect square, then return floor of √n.

def square_root(n):

    if n == 0:
        return 0

    for i in range(1, n + 1):
        if i * i == n:
            return i
            
        elif i * i > n:
            return i - 1           

n = 36
print(square_root(n))