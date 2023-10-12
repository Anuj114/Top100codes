def sum_of_digits(num):
    total = 0
    while num > 0:
        remainder = num % 10
        total += remainder
        num = int(num/10)
    return total


print(sum_of_digits(123))