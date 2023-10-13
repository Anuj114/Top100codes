def arr_reverse(arr):
    first = 0
    last = len(arr) - 1
    while(first <= last):
        temp = arr[first]
        arr[first] = arr[last]
        arr[last] = temp

        first += 1
        last -= 1
    return arr
A = [10, 20, 30, 40, 50, 60]

res = arr_reverse(A)
print(res)