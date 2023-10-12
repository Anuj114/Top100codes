def reverse_num(num):
    res = 0
    while num != 0:
        remainder = num % 10
        res = res * 10 + remainder
        num = int(num/10) 
    return res

def reverse_num_recursion(num): 
    if len(str(num)) == 1:
        return num
    last_digit = num % 10
    remaining_num = int(num / 10)
    return last_digit * pow(10, len(str(remaining_num))) + reverse_num_recursion(remaining_num)

# print(reverse_num_recursion(123))
# print(reverse_num(2345))
      