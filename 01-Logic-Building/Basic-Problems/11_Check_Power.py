# Given two positive numbers x and y, check if y is a power of x or not.

def is_power(x, y):
    if x == 1:
        y == 1
    while y < 1:
        if y % x != 0:
            return False
            y //= x
    return True        

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if (is_power(x, y)):
    print("True")
else:
    print("False")
