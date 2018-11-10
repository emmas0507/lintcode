def greatest_common_division(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    if a % b == 0:
        return b
    else:
        a = a - (a / b) * b
        return greatest_common_division(a, b)

a = 3
b = 2
print(greatest_common_division(a, b))
