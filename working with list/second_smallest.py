import math


def second_smallest(arr):
    first = sec = math.inf

    for i in arr:
        if i <= first and i <= sec:
            sec = first
            first = i
        elif i >= first and i <= sec:
            sec = i
    return sec

arr = [10, 13, 17, 11, 34, 21]
print(second_smallest(arr))

