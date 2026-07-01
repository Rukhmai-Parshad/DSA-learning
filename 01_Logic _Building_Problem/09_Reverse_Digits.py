# Given an Integer n, find the reverse of its digits.
def reversedigits(n):
    rev = 0
    while (n > 0):
        a = n % 10
        rev = rev * 10 + a
        n //= 10
    return rev

n = 12345678
print(reversedigits(n))        