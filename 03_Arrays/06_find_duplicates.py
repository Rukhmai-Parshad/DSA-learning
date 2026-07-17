# Find duplicates.

arr = [1, 2, 2, 3, 1, 4]

freq = {}

for i in range(len(arr)):

    num = arr[i]

    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Duplicates:")

for key in freq:

    if freq[key] > 1:
        print(key)