# Given a number N, the task is to check whether the given number N is 
# a perfect cube or not. 

def is_perfect_cube(n):

    root = round(abs(n) ** (1/3))

    if root * root * root == abs(n):
        return True

    return False

n = 64
if is_perfect_cube(n):
    print("Perfect Cube")
else:
    print("Not a Perfect Cube")