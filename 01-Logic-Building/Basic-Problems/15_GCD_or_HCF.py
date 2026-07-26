# Given two positive integers a and b, 
# the task is to find the GCD of the two numbers.

def gcd(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
    return gcd

a = 15
b = 25
print(gcd(a, b))