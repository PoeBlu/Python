import math


def jump_search(arr, x):
    n = len(arr)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    return prev if arr[prev] == x else -1


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55
index = jump_search(arr, x)
print("\nNumber " + str(x) + " is at index " + str(index))
