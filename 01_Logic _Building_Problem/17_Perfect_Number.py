# A number is a perfect number if it is equal to the sum of its proper divisors, 
# that is, the sum of its positive divisors excluding the number itself. 
# Find whether a given positive integer n is perfect or not.

def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if (n % i == 0):
            sum += i
    return sum == n

n = 28
if (perfect_number(n)):
    print("Perfect number")
else:
    print("Not a perfect number")                