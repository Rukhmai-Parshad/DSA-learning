def sumofdigits(n):
    sum = 0
    while n != 0:
        last = n % 10
        sum += last
        n //= 10
    return sum

n = 12345
print(sumofdigits(n))    