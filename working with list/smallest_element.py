def smallest_element(arr):
    min_element = arr[0]
    for i in arr:
        if i < min_element:
            min_element = i
    return min_element

a = [10, 89, 9, 56, 4, 80, 8]
print(smallest_element(a))
