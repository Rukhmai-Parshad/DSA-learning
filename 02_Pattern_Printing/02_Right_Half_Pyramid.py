# Given an integer N, print a right half pyramid star pattern with N rows. 
# The first row has 1 star, the second row has 2 stars, and each next row has 
# one more star than the previous row. The Nth row has N stars, and all stars 
# are left aligned.

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()