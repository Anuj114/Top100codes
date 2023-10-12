def fibonacci_series(num):
    a = 0
    b = 1
    # print(a, end=" ")
    # print(b, end=" ")

    for i in range(num-2):
        c = a+b
        a = b
        b = c
    return c    

print(fibonacci_series(10))
