def freq_of_element(arr):
    res = {}
    for i in arr:
        if i in res.keys():
            res[i] += 1
        else:
            res[i] = 1
    return res

arr = [5, 8, 5, 7, 8, 10]
print(freq_of_element(arr))
