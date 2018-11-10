def spiral_array(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1,2], [4,3]]
    else:
        add_on = (n-1) * 4
        mat = spiral_array(n-2)
        new_mat = [range(1,n+1)]
        for i in range(len(mat)):
            new_m_ = [mm_ + add_on for mm_ in mat[i]]

            new_mat = new_mat + [[4*(n-1)-i] + new_m_ + [n+1+i]]
        new_mat = new_mat + [range(3*n-2, 2*n-2, -1)]
    return new_mat

print(spiral_array(5))
