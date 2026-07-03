# Given two integer arrays a[] and b[] containing two integers each 
# representing the numerator and denominator of a fraction respectively. 
# The task is to find the sum of the two fractions 
# and return the numerator and denominator of the result.

def add_fraction(a, b):

    n1, d1 = a
    n2, d2 = b

    new_numerator = (n1 * d2) + (n2 * d1)

    new_denominator = (d1 * d2)

    for i in range(1, min(new_numerator, new_denominator) + 1):
        if (new_numerator % i == 0 and new_denominator % i == 0):
            gcd = i

    numerator = new_numerator // gcd
    denominator = new_denominator // gcd
    return [numerator, denominator]

a = [2, 5]
b = [3, 10]
print(add_fraction(a, b))    