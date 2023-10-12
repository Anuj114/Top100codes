def is_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        remainder = num % 10
        rev = rev * 10 + remainder
        num = int(num/10)

    if rev == original:
        return f'{original} is palindrome'
    return f'{original} is NOT palindrome' 

print(is_palindrome(12221))