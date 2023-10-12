def is_pos_neg(num):
    if num >= 0:
        return f"{num} is positive"
    return f"{num} is negative"


print(is_pos_neg(5))
print(is_pos_neg(-5))
print(is_pos_neg(0))
