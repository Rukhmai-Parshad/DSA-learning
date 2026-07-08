# Given two integers n and m (m != 0). 
# Find the number closest to n and divisible by m. 
# If there is more than one such number, then output the one having 
# maximum absolute value.

def closest_number(n, m):
    lower = (n // m) * m
    upper = lower + m
    distance1 = n - lower
    distance2 = upper - n
    
    if distance1 < distance2:
        return lower
    elif distance2 < distance1:
        return upper
    else:
        if abs(lower) > abs(upper):
            return lower 
        else:
            return upper

n = 29
m = 6
print(closest_number(n, m))                     