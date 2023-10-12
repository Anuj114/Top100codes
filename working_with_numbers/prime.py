def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return "%s is NOT prime"%num
    return "%s is prime"%num

print(is_prime(7))
print(is_prime(9)) 
print(is_prime(11))          