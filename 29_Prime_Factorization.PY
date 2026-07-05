# Given a number n. Find its unique prime factors in increasing order.

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
    return result

n = 12
print(unique_prime_factors(n)) 