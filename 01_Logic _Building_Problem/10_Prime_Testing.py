# Given a number n, check whether it is a prime number or not.
def isprime(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

n = int(input("Enter n number: "))
if (isprime(n)):
    print("True")
else:
    print("False")    