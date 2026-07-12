# Given an integer N, the task is to print a full pyramid pattern with N rows. 
# In this pattern, each row contains an odd number of stars, ranging from 1 star in
# the first row to (2 * N - 1) stars in the Nth row. All the stars are center-aligned.

n = 5

for i in range(n):

    # Print spaces
    for j in range(n - i - 1):
        print(" ", end=" ")

    # Print stars
    for k in range(2 * i + 1):
        print("*", end=" ")

    print()