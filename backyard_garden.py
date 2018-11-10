def backyard_garden(n):
    n = n % 21
    for i in range(3):
        if (n - i * 7) >= 0 and (n - i * 7) % 3 == 0:
            return True
    else:
        return False

print(backyard_garden(10))
print(backyard_garden(8))
