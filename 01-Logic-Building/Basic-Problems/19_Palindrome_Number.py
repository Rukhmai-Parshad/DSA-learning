# Given an integer n, determine whether it is a palindrome number or not.
# A number is called a palindrome if it reads the same from forward and backward.

def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev == original

n = 87898
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not a Palindrome")