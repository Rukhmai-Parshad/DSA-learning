# Given a positive integer n, return all the divisors of n in the ascending order.

def divisors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result

n = 12
print(divisors(n))            