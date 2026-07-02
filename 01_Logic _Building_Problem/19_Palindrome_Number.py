# Given an integer n, determine whether it is a palindrome number or not.
# A number is called a palindrome if it reads the same from forward and backward.

def is_palindrome(n):
    rev  = 0
    while (n > 0):
        a = n % 10
        rev = rev * 10 + a
        n //= 10
    return rev    

n = 87898
if (is_palindrome(n) == n):
    print("palindrome")
else:
    print("not a palindrome")        