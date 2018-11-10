def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        pt_n_1 = pascal_triangle(n-1)
        layer = pt_n_1[-1]
        new_layer = [0] * n
        new_layer[0] = 1
        new_layer[-1] = 1
        for i in range(1, n-1):
            new_layer[i] = layer[i-1] + layer[i]
        return pt_n_1 + [new_layer]

print(pascal_triangle(4))
