def sum_in_range(first, last):
    total_sum = 0
    for i in range(first, last+1):
        total_sum += i
    return total_sum

print(sum_in_range(2, 5))        