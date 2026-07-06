# Given a number n, check whether it is even or odd. 
# Return true for even and false for odd.

def isEven(n):
    if (n % 2 == 0):
        return True
    else:   
        return False

n = int(input("Enter a number: "))
if isEven(n):
    print("True")
else:
    print("False")                