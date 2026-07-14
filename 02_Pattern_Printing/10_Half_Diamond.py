# Half Diamond pattern.

n = 5

# Upper Half
for i in range(1, n + 1):

    for j in range(i):
        print("*", end=" ")

    print()

# Lower Half
for i in range(1, n):

    for j in range(n - i):
        print("*", end=" ")

    print()
    print()