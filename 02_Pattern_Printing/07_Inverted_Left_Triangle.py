# Inverted Left Triangle Printing.

n = 4

for i in range(1, n + 1):

    for j in range(i - 1):          # Print spaces
        print("  ", end="")

    for j in range(n - i + 1):      # Print stars
        print("* ", end="")

    print()