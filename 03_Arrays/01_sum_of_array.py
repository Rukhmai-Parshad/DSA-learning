# Find sum of array.

def total(arr):

    total = 0
    for i in range(len(arr)):
        total += arr[i]

    return total

arr = [10, 20, 30, 40, 50]
print(total(arr))        