def ugly_number(n):
    print(n)
    if n == 1:
        return True
    if n % 2 == 0:
        return ugly_number(n / 2)
    if n % 3 == 0:
        return ugly_number(n / 3)
    if n % 5 == 0:
        return ugly_number(n / 5)
    return False

n = 8
print(ugly_number(n))
