# Given a number n, find the digital root of n. Digital Root of a number is 
# the recursive sum of its digits until we get a single digit number.
def digital_root(n):
    while n >= 10:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit
            n //= 10
        n = total

    return n

n = 999999
print(digital_root(n))    