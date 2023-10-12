def prim_number_range(first, last):
    flag = True
    for i in range(first, last+1):
        
        for j in range(2,i):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i)
        flag = True         

prim_number_range(11, 50)