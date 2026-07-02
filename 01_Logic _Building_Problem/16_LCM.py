# Given two positive integers a and b. Find the Least Common Multiple (LCM) of a and b.
# LCM of two numbers is the smallest number which can be divided by both numbers. 

def lcm(a, b):
    lcm = max(a, b)
    while True:
        if ((a % lcm == 0) and (b % lcm == 0)):
            return lcm 
            lcm +=1

a = 4
b = 6
print(lcm(a, b))