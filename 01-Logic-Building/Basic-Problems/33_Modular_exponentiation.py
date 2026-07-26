# Given three integers x, n, and M, compute (xn) % M 
# (remainder when x raised to the power n is divided by M).

# (a * b) % m = ((a % m) * (b % m)) % m

def mod_power(a, b, m):

    result = 1

    while b > 0:

        if b % 2 == 1:
            result = (result * a) % m

        a = (a * a) % m

        b //= 2

    return result


print(mod_power(2, 10, 1000))