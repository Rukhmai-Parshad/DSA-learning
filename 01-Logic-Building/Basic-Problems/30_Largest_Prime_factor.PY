# Given a positive integer n ( 1 <= n <= 1015). 
# Find the largest prime factor of a number. 

def isprime(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

def unique_prime_factors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            if isprime(i):
                result.append(i)
    return max(result)

n = 12
print(unique_prime_factors(n)) 