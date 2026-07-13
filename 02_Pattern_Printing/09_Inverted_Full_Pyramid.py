# Given an integer N, the task is to print a pattern of N rows representing 
# an inverted full pyramid. In this pattern, the first row has (2 * N - 1) stars, 
# the second row has (2 * N - 3) stars, and so on until the Nth row, which has 
# only 1 star. All stars are center-aligned.

n = 5

for i in range(n):

    # Print spaces
    for j in range(i):
        print(" ", end=" ")

    # Print stars
    for k in range(2 * (n - i) - 1):
        print("*", end=" ")

    print()