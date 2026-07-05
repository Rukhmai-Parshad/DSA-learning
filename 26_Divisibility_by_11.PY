# Given a number in the form of string s, Check if the number is divisible by 11 
# or not. The input number may be large and it may not be possible to store it 
# even if we use long long int.

def divisible_by_11(s):
    odd_sum = 0
    even_sum = 0

    for i in range(len(s)):
        digit = int(s[i])
        if i % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    difference = abs(odd_sum - even_sum)
    return difference % 11 == 0

s = "121"
if divisible_by_11(s):
    print("Divisible by 11")
else:
    print("Not divisible by 11")             


