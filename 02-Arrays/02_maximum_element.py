# Find maximum element.

def largest(arr):
    largest = arr[0]

    for i in range(len(arr)):

        if arr[i] > largest:
            largest = arr[i]

    return largest

arr = [10, 20, 30, 40, 50]
print(largest(arr))            