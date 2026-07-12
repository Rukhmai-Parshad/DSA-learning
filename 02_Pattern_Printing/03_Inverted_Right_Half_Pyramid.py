# Given an integer N, create an inverted left half pyramid pattern with N rows. 
# In this pattern, the first row contains N stars, the second row contains N - 1 stars,
# and each following row has one star less than the previous row, until the last row contains 
# only 1 star. All stars are right-aligned.

n = 5

for i in range(n, 0, -1):

    for j in range(i):

        print("*", end=" ")

    print()