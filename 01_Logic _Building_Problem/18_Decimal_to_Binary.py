# Given a non negative number n, the task is to convert 
# the given number into an equivalent binary representation.

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        digit = n % 2
        binary = str(digit) + binary
        n //= 2
    return binary

n = 13
print(decimal_to_binary(n)) 