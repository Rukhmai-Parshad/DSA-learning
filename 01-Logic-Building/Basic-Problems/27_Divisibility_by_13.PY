# Given a number s represented as a string, determine whether the integer it 
# represents is divisible by 13 or not.

def divisible_by_13(s):
    remainder = 0

    for digit in s:
        remainder = (remainder * 10 + int(digit)) % 13

    return remainder == 0


s = "2912"

if divisible_by_13(s):
    print("Divisible by 13")
else:
    print("Not Divisible by 13")