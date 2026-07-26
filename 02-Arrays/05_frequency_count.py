# Frequency Count.

arr = [1, 2, 2, 3, 1, 2]

freq = {}

for i in range(len(arr)):

    num = arr[i]

    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    print(key, "->", freq[key])