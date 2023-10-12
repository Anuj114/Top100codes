def greatest_of_three(first, second, third):
    if first >= second and first >= third:
        return first
    elif second >= first and second >= third:
        return second    
    return third



print(greatest_of_three(20, 30, 10))
print(greatest_of_three(20, 20, 10))
print(greatest_of_three(30, 20, 10))    