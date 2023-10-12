def armstrong_num(num):
    original = num
    exp = len(str(num))

    #I am in main branch

    total = 0
    while num > 0:
        remainder = num % 10
        total = total + pow(remainder, exp)
        num = int(num/10)

    if original == total:
        return True
    return False         


def armstrong_num_in_range(first, last):
    for i in range(first, last+1):
        if armstrong_num(i):
            print(i)

armstrong_num_in_range(10, 1000)            
