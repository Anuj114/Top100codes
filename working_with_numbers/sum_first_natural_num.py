def sum_of_first_natural_num(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

def sfnn_recursive(num):
    if num == 0:
        return 0
    sum = sfnn_recursive(num-1)
    return sum + num


print(sum_of_first_natural_num(10))   
print(sfnn_recursive(10))     