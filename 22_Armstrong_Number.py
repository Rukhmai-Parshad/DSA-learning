# Given a number x, determine whether the given number is Armstrong's number or not. 
# A positive integer of n digits is called an Armstrong number of order n 
# (order is the number of digits) if
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
# Here a, b, c and d are digits of input number abcd.....

def is_armstrong(n):
    original = n
    count = 0
    total = 0
    # Count digits
    while n > 0:
        n //= 10
        count += 1
    n = original
    # Calculate sum of powers
    while n > 0:
        digit = n % 10
        total += digit ** count
        n //= 10
    return total == original

n = 15
if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")        