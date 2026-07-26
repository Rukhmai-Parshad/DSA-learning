# Given a number n, determine whether it is a perfect square. 
# Return true if it is a perfect square; otherwise, return false.

def is_perfect_square(n):
    if n < 0:
        return False

    root = int(n ** 0.5)

    return root * root == n

n = 49
if is_perfect_square(n):
    print("Perfect Square")       
else:
    print("Not a Perfect Square")     