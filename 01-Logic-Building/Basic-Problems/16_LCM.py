# Given two positive integers a and b. Find the Least Common Multiple (LCM) of a and b.
# LCM of two numbers is the smallest number which can be divided by both numbers. 

def lcm(a, b):
    candidate = max(a, b)
    while True:
        if candidate % a == 0 and candidate % b == 0:
            return candidate
        candidate += 1

a = 4
b = 6
print(lcm(a, b))