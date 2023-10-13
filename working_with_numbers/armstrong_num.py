def armstrong_num(num):
    original = num
    exp = len(str(num))
<<<<<<< HEAD


    #I am in main branch

    #I am in feature branch



=======
    #added comment
    #added 2nd comment
    #I am in feature1 branch
>>>>>>> f78a887123afa4f71d1c5ed67db5deec78cb8575
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
