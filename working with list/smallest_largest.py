def small_large(arr):
    min_element = arr[0]
    max_element = arr[0]
    for i in arr:
        if i < min_element:
            min_element = i
        if i > max_element:
            max_element = i
    return min_element, max_element

a = [10, 89, 9, 56, 4, 80, 8]
min_res, max_res = small_large(a)
print(min_res, max_res)