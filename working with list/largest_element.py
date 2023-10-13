
def largest_element(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


a = [10, 89, 9, 56, 4, 80, 8]
print(largest_element(a))