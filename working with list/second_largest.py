import math


def second_largest(arr):
    first = sec = arr[0]

    for i in arr:
        if i > first and i > sec:
            sec = first
            first = i
        if i < first and i > sec:
            sec = i
    return sec

arr = [10, 13, 17, 11, 34, 21]
print(second_largest(arr))

