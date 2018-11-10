def climbing_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbing_stairs(n-1) + climbing_stairs(n-2)

n = 3
print(climbing_stairs(n))
